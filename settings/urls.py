from django.urls import path
from . import views

app_name = 'settings'

urlpatterns = [
    path('', views.show_settings, name='settings'),
    path('update/', views.update_settings, name='settings_update'),
    path('health/', views.site_health, name='site_health'),
]