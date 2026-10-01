import os
import sys
import platform
import shutil
import json
import importlib
import django
from django.db import connection
from django.conf import settings as django_settings
from django.core.cache import cache
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta

from .models import SiteSetting, DiskUsageLog
from .forms import SettingForm

@login_required
def show_settings(request):
    setting = SiteSetting.get_instance()
    form = SettingForm(instance=setting)
    return render(request, 'admin/site_settings/index.html', {'form': form, 'setting': setting})

@login_required
def update_settings(request):
    if request.method == 'POST':
        setting = SiteSetting.get_instance()
        form = SettingForm(request.POST, request.FILES, instance=setting)
        
        if form.is_valid():
            form.save()
            
            def parse_json_field(prefix):
                items = []
                i = 0
                while f'{prefix}[{i}][icon]' in request.POST:
                    items.append({
                        'icon': request.POST.get(f'{prefix}[{i}][icon]'),
                        'title': request.POST.get(f'{prefix}[{i}][title]'),
                        'subtitle': request.POST.get(f'{prefix}[{i}][subtitle]'),
                        'content': request.POST.get(f'{prefix}[{i}][content]'),
                    })
                    i += 1
                return items

            setting.process_item = parse_json_field('process_item')
            setting.work_item = parse_json_field('work_item')
            setting.counter_item = parse_json_field('counter_item')
            setting.save() 
            
            return JsonResponse({'success': True, 'message': 'Settings updated successfully!'})
        
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)


# ==========================================
#  New Site Health Logic & Views
# ==========================================
def get_server_info():
    try:
        with connection.cursor() as cursor:
            if 'sqlite' in django_settings.DATABASES['default']['ENGINE']:
                cursor.execute("SELECT sqlite_version();")
            elif 'mysql' in django_settings.DATABASES['default']['ENGINE']:
                cursor.execute("SELECT VERSION();")
            elif 'postgresql' in django_settings.DATABASES['default']['ENGINE']:
                cursor.execute("SELECT version();")
            else:
                db_version = 'Unknown'
            
            if 'db_version' not in locals():
                db_version = cursor.fetchone()[0]
    except Exception:
        db_version = 'Unknown'

    return {
        'Python Version': sys.version.split()[0],
        'Django Version': django.get_version(),
        'Server Architecture': platform.machine(),
        'Operating System': f"{platform.system()} {platform.release()}",
        'Database Engine': django_settings.DATABASES['default']['ENGINE'].split('.')[-1],
        'Database Version': db_version,
        'Debug Mode': 'Yes' if django_settings.DEBUG else 'No',
        'Timezone': django_settings.TIME_ZONE,
        'Current Server Time': timezone.now().strftime('%Y-%m-%d %H:%M:%S'),
        'Site URL': django_settings.ALLOWED_HOSTS[0] if django_settings.ALLOWED_HOSTS else 'localhost',
    }

def get_directory_sizes():
    def get_size(start_path='.'):
        total_size = 0
        for dirpath, _, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if not os.path.islink(fp):
                    try:
                        total_size += os.path.getsize(fp)
                    except OSError:
                        pass
        return total_size

    def format_bytes(size):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return f"{size:.2f} {unit}"
            size /= 1024.0
        return f"{size:.2f} PB"

    dirs_to_check = {
        'Media Root': getattr(django_settings, 'MEDIA_ROOT', 'Not configured'),
        'Static Root': getattr(django_settings, 'STATIC_ROOT', 'Not configured'),
        'Base Directory': str(django_settings.BASE_DIR),
    }
    
    sizes = {}
    for name, path in dirs_to_check.items():
        if path and path != 'Not configured' and os.path.exists(path):
            sizes[name] = format_bytes(get_size(path))
        else:
            sizes[name] = 'N/A'
    return sizes

def get_site_health_status():
    cache_status = 'No'
    try:
        cache.set('health_check_test', 'ok', 10)
        if cache.get('health_check_test') == 'ok':
            cache_status = 'Yes'
        cache.delete('health_check_test')
    except Exception:
        cache_status = 'Error'

    db_status = 'Failed'
    try:
        connection.ensure_connection()
        db_status = 'Connected'
    except Exception:
        pass

    try:
        usage = shutil.disk_usage(django_settings.BASE_DIR)
        disk_space = f"{usage.used / (1024**3):.2f} GB / {usage.total / (1024**3):.2f} GB"
    except Exception:
        disk_space = 'Error calculating'

    required_packages = ['Pillow', 'requests']
    missing = [pkg for pkg in required_packages if not importlib.util.find_spec(pkg.lower())]
    pkg_status = 'All installed' if not missing else f"Missing: {', '.join(missing)}"

    return {
        'Site is online': 'Yes',
        'Cache Working': cache_status,
        'Database Connection': db_status,
        'Disk Space Usage': disk_space,
        'Required Python Packages': pkg_status,
        'Error Logging': 'Enabled' if django_settings.DEBUG else 'Disabled (Production)',
    }

def get_disk_chart_data():
    logs = DiskUsageLog.objects.order_by('log_date')[:7]
    labels = [log.log_date.strftime('%b %d') for log in logs]
    data = [log.used_bytes for log in logs]
    
    if not labels:
        today = timezone.now().date()
        labels = [(today - timedelta(days=i)).strftime('%b %d') for i in range(6, -1, -1)]
        data = [0] * 7
        
    return {'labels': json.dumps(labels), 'data': json.dumps(data)}

@login_required
def site_health(request):
    today = timezone.now().date()
    if not DiskUsageLog.objects.filter(log_date=today).exists():
        try:
            usage = shutil.disk_usage(django_settings.BASE_DIR)
            DiskUsageLog.objects.create(log_date=today, used_bytes=usage.used, free_bytes=usage.free)
        except Exception:
            pass

    return render(request, 'admin/site_settings/site_health.html', {
        'server_info': get_server_info(),
        'directories': get_directory_sizes(),
        'site_health_status': get_site_health_status(),
        'disk_chart_data': get_disk_chart_data(),
    })