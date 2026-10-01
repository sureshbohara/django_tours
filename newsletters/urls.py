from django.urls import path
from . import views

app_name = 'newsletters'

urlpatterns = [
    path('', views.subscriber_list, name='subscriber_list'),
    path('send/', views.send_newsletter, name='send_newsletter'),
    path('<int:pk>/delete/', views.subscriber_delete, name='subscriber_delete'),
]