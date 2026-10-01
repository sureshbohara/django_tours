from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Service
from .forms import ServiceForm

def parse_process_items(request):
    items = []
    i = 0
    while f'process_item[{i}][title]' in request.POST:
        items.append({
            'title': request.POST.get(f'process_item[{i}][title]'),
            'content': request.POST.get(f'process_item[{i}][content]'),
        })
        i += 1
    return items

@login_required
def service_list(request):
    items = Service.objects.all()
    search = request.GET.get('search')
    status = request.GET.get('status')
    if search: items = items.filter(title__icontains=search)
    if status in ['0', '1']: items = items.filter(status=bool(int(status)))
    return render(request, 'admin/services/index.html', {'items': items, 'filters': request.GET})

@login_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save(commit=False)
            service.process_item = parse_process_items(request)
            service.highlight = {'sections': request.POST.getlist('highlight_sections[]')}
            service.save()
            return JsonResponse({'success': True, 'message': 'Service created successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/services/form.html', {'form': ServiceForm()})

@login_required
def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            service = form.save(commit=False)
            service.process_item = parse_process_items(request)
            service.highlight = {'sections': request.POST.getlist('highlight_sections[]')}
            service.save()
            return JsonResponse({'success': True, 'message': 'Service updated successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/services/form.html', {'form': ServiceForm(instance=service), 'item': service})

@login_required
def service_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(Service, pk=pk).delete()
    return redirect('services:service_list')

@login_required
def service_toggle_status(request):
    if request.method == 'POST':
        item = get_object_or_404(Service, pk=request.POST.get('status_id'))
        item.status = not item.status
        item.save()
        return JsonResponse({'success': True, 'message': 'Status updated!'})
    return JsonResponse({'success': False}, status=400)

@login_required
def service_update_order(request):
    if request.method == 'POST':
        item = get_object_or_404(Service, pk=request.POST.get('id'))
        item.order_level = int(request.POST.get('order_level'))
        item.save()
        return JsonResponse({'success': True, 'message': 'Order updated!'})
    return JsonResponse({'success': False}, status=400)