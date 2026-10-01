from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Faq
from .forms import FaqForm

@login_required
def faq_list(request):
    items = Faq.objects.all()
    search = request.GET.get('search')
    status = request.GET.get('status')
    if search: items = items.filter(question__icontains=search)
    if status in ['0', '1']: items = items.filter(status=bool(int(status)))
    return render(request, 'admin/faqs/index.html', {'items': items, 'filters': request.GET})

@login_required
def faq_create(request):
    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'FAQ created successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/faqs/form.html', {'form': FaqForm()})

@login_required
def faq_update(request, pk):
    item = get_object_or_404(Faq, pk=pk)
    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'FAQ updated successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/faqs/form.html', {'form': FaqForm(instance=item), 'item': item})

@login_required
def faq_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(Faq, pk=pk).delete()
    return redirect('faqs:faq_list')

@login_required
def faq_toggle_status(request):
    if request.method == 'POST':
        item = get_object_or_404(Faq, pk=request.POST.get('status_id'))
        item.status = not item.status
        item.save()
        return JsonResponse({'success': True, 'message': 'Status updated!'})
    return JsonResponse({'success': False}, status=400)

@login_required
def faq_update_order(request):
    if request.method == 'POST':
        item = get_object_or_404(Faq, pk=request.POST.get('id'))
        item.order_level = int(request.POST.get('order_level'))
        item.save()
        return JsonResponse({'success': True, 'message': 'Order updated!'})
    return JsonResponse({'success': False}, status=400)