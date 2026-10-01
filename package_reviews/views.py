from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from packages.models import Package
from .models import PackageReview  

@require_POST
def submit_review(request, package_id):
    try:
        package = get_object_or_404(Package, id=package_id, status=True)
        
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        rating = request.POST.get('rating')
        comment = request.POST.get('review', '').strip()

        if not all([name, email, rating, comment]):
            return JsonResponse({'success': False, 'message': 'All fields are required.'}, status=400)
        
        if not (1 <= int(rating) <= 5):
            return JsonResponse({'success': False, 'message': 'Rating must be between 1 and 5.'}, status=400)


        PackageReview.objects.create(
            package=package,
            name=name,
            email=email,
            rating=int(rating),
            comment=comment,
            status=False
        )

        return JsonResponse({
            'success': True, 
            'message': 'Thank you! Your review has been submitted and is pending admin approval.'
        })
    
    except ValueError:
        return JsonResponse({'success': False, 'message': 'Invalid rating value.'}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Error: {str(e)}'}, status=500)