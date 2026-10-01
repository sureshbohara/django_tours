from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import PromoCode
from .forms import PromoCodeForm
from datetime import date

@login_required
def promo_list(request):
    items = PromoCode.objects.all()
    search = request.GET.get('search')
    status = request.GET.get('status')
    
    if search:
        items = items.filter(code__icontains=search)
    if status in ['0', '1']:
        items = items.filter(status=bool(int(status)))
        
    return render(request, 'admin/promos/index.html', {'items': items, 'filters': request.GET})

@login_required
def promo_create(request):
    if request.method == 'POST':
        form = PromoCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Promo code created successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/promos/form.html', {'form': PromoCodeForm()})

@login_required
def promo_update(request, pk):
    item = get_object_or_404(PromoCode, pk=pk)
    if request.method == 'POST':
        form = PromoCodeForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Promo code updated successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/promos/form.html', {'form': PromoCodeForm(instance=item), 'item': item})

@login_required
def promo_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(PromoCode, pk=pk).delete()
    return redirect('promos:promo_list')

@login_required
def promo_toggle_status(request):
    if request.method == 'POST':
        item = get_object_or_404(PromoCode, pk=request.POST.get('status_id'))
        item.status = not item.status
        item.save()
        return JsonResponse({'success': True, 'message': 'Status updated!'})
    return JsonResponse({'success': False}, status=400)