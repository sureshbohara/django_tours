from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Category
from .forms import CategoryForm

@login_required
def category_list(request):
    categories = Category.objects.select_related('parent').all()
    
    name = request.GET.get('name')
    parent_id = request.GET.get('parent_id')
    display_on = request.GET.get('display_on')
    status = request.GET.get('status')

    if name:
        categories = categories.filter(name__icontains=name)
    if parent_id:
        categories = categories.filter(parent_id=parent_id)
    if display_on:
        categories = categories.filter(display_on=display_on)
    if status in ['0', '1']:
        categories = categories.filter(status=bool(int(status)))

    parent_categories = Category.objects.filter(parent__isnull=True).order_by('name')
    
    return render(request, 'admin/categories/index.html', {
        'categories': categories,
        'parent_categories': parent_categories,
        'filters': request.GET
    })

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.updated_by = request.user
            category.save()
            return JsonResponse({'success': True, 'message': 'Category created successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    
    parent_categories = Category.objects.filter(parent__isnull=True).order_by('name')
    return render(request, 'admin/categories/form.html', {'form': CategoryForm(), 'parent_categories': parent_categories})

@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.updated_by = request.user
            category.save()
            return JsonResponse({'success': True, 'message': 'Category updated successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    
    parent_categories = Category.objects.filter(parent__isnull=True).exclude(pk=category.pk).order_by('name')
    return render(request, 'admin/categories/form.html', {'form': CategoryForm(instance=category), 'category': category, 'parent_categories': parent_categories})

@login_required
def category_delete(request, pk):
    if request.method == 'POST':
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return redirect('categories:category_list')
    return redirect('categories:category_list')

@login_required
def category_toggle_status(request):
    if request.method == 'POST':
        category_id = request.POST.get('status_id')
        category = get_object_or_404(Category, pk=category_id)
        category.status = not category.status
        category.save()
        return JsonResponse({'success': True, 'message': 'Status updated!', 'new_status': category.status})
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)

@login_required
def category_update_order(request):
    if request.method == 'POST':
        category_id = request.POST.get('id')
        order_level = request.POST.get('order_level')
        category = get_object_or_404(Category, pk=category_id)
        category.order_level = int(order_level)
        category.save()
        return JsonResponse({'success': True, 'message': 'Order updated!'})
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=400)