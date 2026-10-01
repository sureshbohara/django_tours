from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Banner
from .forms import BannerForm

@login_required
def banner_list(request):
    banners = Banner.objects.all()
    title = request.GET.get('title')
    status = request.GET.get('status')

    if title: banners = banners.filter(title__icontains=title)
    if status in ['0', '1']: banners = banners.filter(status=bool(int(status)))

    return render(request, 'admin/banners/index.html', {'banners': banners, 'filters': request.GET})

@login_required
def banner_create(request):
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Banner created successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/banners/form.html', {'form': BannerForm()})

@login_required
def banner_update(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Banner updated successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/banners/form.html', {'form': BannerForm(instance=banner), 'banner': banner})

@login_required
def banner_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(Banner, pk=pk).delete()
    return redirect('banners:banner_list')

@login_required
def banner_toggle_status(request):
    if request.method == 'POST':
        banner = get_object_or_404(Banner, pk=request.POST.get('status_id'))
        banner.status = not banner.status
        banner.save()
        return JsonResponse({'success': True, 'message': 'Status updated!'})
    return JsonResponse({'success': False}, status=400)

@login_required
def banner_update_order(request):
    if request.method == 'POST':
        banner = get_object_or_404(Banner, pk=request.POST.get('id'))
        banner.order_level = int(request.POST.get('order_level'))
        banner.save()
        return JsonResponse({'success': True, 'message': 'Order updated!'})
    return JsonResponse({'success': False}, status=400)