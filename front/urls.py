from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    # Home Page
    path('', views.home, name='home'),
    # About Page
    path('about-us/', views.about, name='about'),
    # Contact Page
    path('contact/', views.contact, name='contact'),  
    # Gallery
    path('gallery/', views.gallery, name='gallery'),
    # FAQs
    path('faqs/', views.faqs, name='faqs'),
    # Team
    path('team/', views.team, name='team'),
    # CMS Pages (Dynamic)
    path('pages/<slug:slug>/', views.cms_page, name='cms_page'),


    path('subscribe-newsletter/', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('category/<slug:slug>/', views.category_packages, name='category_packages'),
    path("package/<slug:slug>/", views.package_detail, name="package_detail")
    

]