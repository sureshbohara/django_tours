from django.urls import path
from . import views

app_name = 'promos'

urlpatterns = [
    path('', views.promo_list, name='promo_list'),
    path('create/', views.promo_create, name='promo_create'),
    path('<int:pk>/update/', views.promo_update, name='promo_update'),
    path('<int:pk>/delete/', views.promo_delete, name='promo_delete'),
    path('toggle-status/', views.promo_toggle_status, name='promo_toggle_status'),
]