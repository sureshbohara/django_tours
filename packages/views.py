import os
import uuid
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Package, FixedDeparture
from .forms import PackageForm, FixedDepartureForm
from categories.models import Category

@login_required
def package_list(request):
    items = Package.objects.prefetch_related('categories').all()
    
    search = request.GET.get('search')
    status = request.GET.get('status')
    display_on = request.GET.get('display_on')  
    
    if search: 
        items = items.filter(name__icontains=search)
    if status in ['0', '1']: 
        items = items.filter(status=bool(int(status)))
    if display_on:  # ✅ Display On filter लागू गर्ने
        items = items.filter(display_on=display_on)
    
    return render(request, 'admin/packages/index.html', {
        'items': items, 
        'filters': request.GET
    })

@login_required
def package_create(request):
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES)
        if form.is_valid():
            package = form.save(commit=False)
            package.highlight_key = [h for h in request.POST.getlist('highlight_key[]') if h.strip()]
            package.activities = request.POST.getlist('activities[]')
            package.save()
            package.categories.set(request.POST.getlist('categories'))
            
            gallery_files = request.FILES.getlist('gallery')
            if gallery_files:
                gallery_paths = []
                for f in gallery_files:
                    ext = os.path.splitext(f.name)[1]
                    filename = f"{uuid.uuid4().hex}{ext}"
                    file_path = f"packages/gallery/{filename}"
                    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
                    os.makedirs(os.path.dirname(full_path), exist_ok=True)
                    with open(full_path, 'wb+') as dest:
                        for chunk in f.chunks():
                            dest.write(chunk)
                    gallery_paths.append(file_path)
                package.gallery = gallery_paths
                package.save()
            
            return JsonResponse({'success': True, 'message': 'Package created successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    
    categories = Category.objects.filter(parent__isnull=True).prefetch_related('children').order_by('order_level')
    return render(request, 'admin/packages/form.html', {
        'form': PackageForm(), 
        'categories': categories,
        'activities': settings.TRAVEL_ACTIVITIES  
    })

@login_required
def package_update(request, pk):
    package = get_object_or_404(Package, pk=pk)
    if request.method == 'POST':
        form = PackageForm(request.POST, request.FILES, instance=package)
        if form.is_valid():
            package = form.save(commit=False)
            package.highlight_key = [h for h in request.POST.getlist('highlight_key[]') if h.strip()]
            package.activities = request.POST.getlist('activities[]')
            package.save()
            package.categories.set(request.POST.getlist('categories'))
            
            gallery_files = request.FILES.getlist('gallery')
            if gallery_files:
                gallery_paths = package.gallery or []
                for f in gallery_files:
                    ext = os.path.splitext(f.name)[1]
                    filename = f"{uuid.uuid4().hex}{ext}"
                    file_path = f"packages/gallery/{filename}"
                    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
                    os.makedirs(os.path.dirname(full_path), exist_ok=True)
                    with open(full_path, 'wb+') as dest:
                        for chunk in f.chunks():
                            dest.write(chunk)
                    gallery_paths.append(file_path)
                package.gallery = gallery_paths
                package.save()
            
            return JsonResponse({'success': True, 'message': 'Package updated successfully!'})
        return JsonResponse({'success': False, 'errors': form.errors}, status=422)
    
    categories = Category.objects.filter(parent__isnull=True).prefetch_related('children').order_by('order_level')
    return render(request, 'admin/packages/form.html', {
        'form': PackageForm(instance=package), 
        'item': package, 
        'categories': categories,
        'activities': settings.TRAVEL_ACTIVITIES  # ✅ Activities यहाँबाट आउँछ
    })

@login_required
def package_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(Package, pk=pk).delete()
    return redirect('packages:package_list')

@login_required
def package_toggle_status(request):
    if request.method == 'POST':
        item = get_object_or_404(Package, pk=request.POST.get('status_id'))
        item.status = not item.status
        item.save()
        return JsonResponse({'success': True, 'message': 'Status updated!'})
    return JsonResponse({'success': False}, status=400)

@login_required
def package_update_order(request):
    if request.method == 'POST':
        item = get_object_or_404(Package, pk=request.POST.get('id'))
        item.order_level = int(request.POST.get('order_level'))
        item.save()
        return JsonResponse({'success': True, 'message': 'Order updated!'})
    return JsonResponse({'success': False}, status=400)

@login_required
def package_inc_exc(request, pk):
    package = get_object_or_404(Package, pk=pk)
    if request.method == 'POST':
        package.included_data = [{'content': val} for val in request.POST.getlist('included_content[]') if val.strip()]
        package.excluded_data = [{'content': val} for val in request.POST.getlist('excluded_content[]') if val.strip()]
        package.save()
        return JsonResponse({'success': True, 'message': 'Inclusions/Exclusions updated!'})
    return render(request, 'admin/packages/inc_exc.html', {'item': package})

@login_required
def package_itinerary(request, pk):
    package = get_object_or_404(Package, pk=pk)
    if request.method == 'POST':
        titles = request.POST.getlist('title[]')
        contents = request.POST.getlist('content[]')
        max_elevations = request.POST.getlist('max_elevation[]')
        durations = request.POST.getlist('duration[]')
        distances = request.POST.getlist('distance[]')
        meals_list = request.POST.getlist('meals[]')
        accommodations = request.POST.getlist('accommodation[]')
        
        itinerary = []
        for i in range(len(titles)):
            if titles[i].strip():
                itinerary.append({
                    'name': titles[i], 'content': contents[i] if i < len(contents) else '',
                    'max_elevation': max_elevations[i] if i < len(max_elevations) else '',
                    'duration': durations[i] if i < len(durations) else '',
                    'distance': distances[i] if i < len(distances) else '',
                    'meals': meals_list[i] if i < len(meals_list) else '',
                    'accommodation': accommodations[i] if i < len(accommodations) else ''
                })
        package.itinerary_data = itinerary
        package.save()
        return JsonResponse({'success': True, 'message': 'Itinerary updated!'})
    return render(request, 'admin/packages/itinerary.html', {'item': package}) # ✅ Typo fixed

@login_required
def package_equipment(request, pk):
    package = get_object_or_404(Package, pk=pk)
    if request.method == 'POST':
        package.general = [{'content': val} for val in request.POST.getlist('equipment1[]') if val.strip()]
        package.lower_body = [{'content': val} for val in request.POST.getlist('equipment2[]') if val.strip()]
        package.upper_body = [{'content': val} for val in request.POST.getlist('equipment3[]') if val.strip()]
        package.footwear = [{'content': val} for val in request.POST.getlist('equipment4[]') if val.strip()]
        package.accessories = [{'content': val} for val in request.POST.getlist('equipment5[]') if val.strip()]
        package.save()
        return JsonResponse({'success': True, 'message': 'Equipment updated!'})
    return render(request, 'admin/packages/equipment.html', {'item': package})

@login_required
def package_prices(request):
    items = Package.objects.order_by('order_level')
    return render(request, 'admin/packages/prices.html', {'items': items})

@login_required
def package_update_prices(request):
    if request.method == 'POST':
        pk = request.POST.get('id')
        package = get_object_or_404(Package, pk=pk)
        package.trip_previous_price = request.POST.get('trip_previous_price') or None
        package.trip_price = request.POST.get('trip_price') or None
        package.save()
        return JsonResponse({'success': True, 'message': 'Prices updated!'})
    return JsonResponse({'success': False}, status=400)

@login_required
def package_delete_gallery_image(request):
    if request.method == 'POST':
        pk = request.POST.get('id')
        image_name = request.POST.get('image')
        package = get_object_or_404(Package, pk=pk)
        if package.gallery and image_name in package.gallery:
            package.gallery.remove(image_name)
            package.save()
        return JsonResponse({'status': 200, 'msg': 'Image deleted.'})
    return JsonResponse({'status': 400, 'msg': 'Invalid request'}, status=400)

@login_required
def fixed_departure_list(request):
    items = FixedDeparture.objects.select_related('package').all()
    return render(request, 'admin/packages/fixed_departures.html', {'items': items})

@login_required
def fixed_departure_add(request):
    if request.method == 'POST':
        form = FixedDepartureForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 200, 'msg': 'Departure added.'})
        return JsonResponse({'status': 400, 'errors': form.errors}, status=400)
    return render(request, 'admin/packages/fixed_departure_form.html', {'form': FixedDepartureForm()})

@login_required
def fixed_departure_delete(request, pk):
    if request.method == 'POST':
        get_object_or_404(FixedDeparture, pk=pk).delete()
    return redirect('packages:fixed_departure_list')

@login_required
def fixed_departure_status(request):
    if request.method == 'POST':
        item = get_object_or_404(FixedDeparture, pk=request.POST.get('id'))
        item.status = request.POST.get('status')
        item.save()
        return JsonResponse({'status': 200, 'msg': 'Status updated.'})
    return JsonResponse({'status': 400}, status=400)