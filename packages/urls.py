from django.urls import path
from . import views

app_name = 'packages'

urlpatterns = [
    path('', views.package_list, name='package_list'),
    path('create/', views.package_create, name='package_create'),
    path('<int:pk>/update/', views.package_update, name='package_update'),
    path('<int:pk>/delete/', views.package_delete, name='package_delete'),
    path('toggle-status/', views.package_toggle_status, name='package_toggle_status'),
    path('update-order/', views.package_update_order, name='package_update_order'),
    
    path('<int:pk>/inc-exc/', views.package_inc_exc, name='package_inc_exc'),
    path('<int:pk>/itinerary/', views.package_itinerary, name='package_itinerary'),
    path('<int:pk>/equipment/', views.package_equipment, name='package_equipment'),
    path('prices/', views.package_prices, name='package_prices'),
    path('update-prices/', views.package_update_prices, name='package_update_prices'),
    path('delete-gallery-image/', views.package_delete_gallery_image, name='package_delete_gallery_image'),
    
    path('fixed-departures/', views.fixed_departure_list, name='fixed_departure_list'),
    path('fixed-departures/add/', views.fixed_departure_add, name='fixed_departure_add'),
    path('fixed-departures/<int:pk>/delete/', views.fixed_departure_delete, name='fixed_departure_delete'),
    path('fixed-departures/status/', views.fixed_departure_status, name='fixed_departure_status'),
]