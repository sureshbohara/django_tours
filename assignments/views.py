from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Assignment
from .forms import AssignmentForm

@login_required
def assignment_list(request):
    items = Assignment.objects.select_related('package', 'staff').all()
    return render(request, 'admin/assignments/index.html', {'items': items})

@login_required
def assignment_create(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Assignment created successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/assignments/form.html', {'form': AssignmentForm()})

@login_required
def assignment_update(request, pk):
    item = get_object_or_404(Assignment, pk=pk)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Assignment updated successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    return render(request, 'admin/assignments/form.html', {'form': AssignmentForm(instance=item), 'item': item})

@login_required
def assignment_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(Assignment, pk=pk).delete()
    return redirect('assignments:assignment_list')