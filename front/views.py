from django.shortcuts import render, get_object_or_404
from django.db.models import Avg , Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from packages.models import Package, FixedDeparture
from categories.models import Category
from blogs.models import Post
from galleries.models import Gallery
from faqs.models import Faq
from teams.models import Team
from pages.models import Page
from banners.models import Banner
from reviews.models import Review 
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from newsletters.models import Subscriber 
from package_reviews.models import PackageReview 

def home(request):
    banners = Banner.objects.filter(status=True).order_by('order_level')
    regions = Category.objects.filter(
        parent__slug='trekking', 
        status=True
    ).only('id', 'name', 'slug', 'image', 'excerpt').order_by('order_level')

    recommended_packages = Package.objects.filter(status=True, display_on='recommended').order_by('order_level')[:6]
    popular_packages = Package.objects.filter(status=True, display_on='popular').order_by('order_level')[:6]
    fixed_departures = FixedDeparture.objects.filter(status='active').order_by('start_date')[:6]

    latest_blogs = Post.objects.filter(status=True).order_by('-created_at')[:4]
    featured_large_post = latest_blogs[0] if latest_blogs else None
    small_posts = latest_blogs[1:] if len(latest_blogs) > 1 else []

    latest_reviews = Review.objects.filter(status=True).order_by('-created_at')[:6]
    
    context = {
        'banners': banners, 'regions': regions, 'recommended_packages': recommended_packages,
        'popular_packages': popular_packages, 'fixed_departures': fixed_departures,
        'featured_large_post': featured_large_post, 'small_posts': small_posts, 'latest_reviews': latest_reviews,
    }
    return render(request, 'front/home.html', context)



def about(request):
    return render(request, 'front/about.html')


def contact(request):
    return render(request, 'front/contact.html')


def gallery(request):
    galleries = Gallery.objects.filter(status=True).order_by('-created_at')
    return render(request, 'front/gallery.html', {'galleries': galleries})


def faqs(request):
    faqs = Faq.objects.filter(status=True).order_by('order_level')
    return render(request, 'front/faqs.html', {'faqs': faqs})


def team(request):
    teams = Team.objects.filter(status=True).order_by('order_level')
    return render(request, 'front/team.html', {'teams': teams})


def cms_page(request, slug):
    page = get_object_or_404(Page, slug=slug, status=True)
    return render(request, 'front/cms_page.html', {'page': page})


@require_POST
def subscribe_newsletter(request):
    email = request.POST.get('email')
    if not email:
        return JsonResponse({'success': False, 'message': 'Email address is required.'}, status=400)
    if Subscriber.objects.filter(email=email).exists():
        return JsonResponse({'success': False, 'message': 'You are already subscribed!'}, status=400)
    
    Subscriber.objects.create(email=email, is_active=True)
    return JsonResponse({'success': True, 'message': 'Successfully subscribed! Welcome to the Himalayas.'})



def category_packages(request, slug):
 
    category = get_object_or_404(Category, slug=slug, status=True)
    

    sidebar_categories = Category.objects.filter(
        parent__isnull=True, 
        status=True
    ).prefetch_related('children').order_by('order_level', 'name')
    

    if category.parent is None: 
        packages = Package.objects.filter(
            Q(categories=category) | Q(categories__parent=category), 
            status=True
        ).distinct()
    else:  
        packages = Package.objects.filter(
            categories=category, 
            status=True
        ).distinct()
    

    sort_by = request.GET.get('sort', 'default')
    if sort_by == 'price_low':
        packages = packages.order_by('trip_price')
    elif sort_by == 'price_high':
        packages = packages.order_by('-trip_price')
    elif sort_by == 'duration':
        packages = packages.order_by('duration') 
    else:
        packages = packages.order_by('order_level', '-created_at')
    
  
    paginator = Paginator(packages, 9)
    page_number = request.GET.get('page')
    
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'front/category_packages.html', {
        'category': category,
        'packages': page_obj, 
        'sidebar_categories': sidebar_categories,
        'current_sort': sort_by,
    })



def package_detail(request, slug):
    package = get_object_or_404(Package, slug=slug, status=True)
    
    # Get only approved reviews
    reviews = PackageReview.objects.filter(package=package, status=True)
    
    # Calculate average rating
    avg_rating = reviews.aggregate(avg=Avg('rating'))['avg'] or 0
    review_count = reviews.count()
    
    return render(request, "front/package_detail.html", {  
        "package": package,
        "reviews": reviews,
        "avg_rating": round(avg_rating, 1),
        "review_count": review_count,
    })