from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('dashboard/', include('core.urls')),
    path('settings/', include('settings.urls')),
    path('categories/', include('categories.urls')),
    path('banners/', include('banners.urls')),
    path('galleries/', include('galleries.urls')),
    path('faqs/', include('faqs.urls')),
    path('reviews/', include('reviews.urls')),
    path('teams/', include('teams.urls')),
    path('services/', include('services.urls')),
    path('pages/', include('pages.urls')),
    path('blogs/', include('blogs.urls')),
    path('packages/', include('packages.urls')),
    path('promos/', include('promos.urls')),
    path('assignments/', include('assignments.urls')),
    path('login-activities/', include('login_activities.urls')),
    path('newsletters/', include('newsletters.urls')),

    path('', include('front.urls')),
    path('reviews/', include('package_reviews.urls', namespace='package_reviews')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)