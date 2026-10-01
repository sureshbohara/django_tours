from django.urls import path
from . import views

app_name = 'package_reviews' 

urlpatterns = [
    path('submit/<int:package_id>/', views.submit_review, name='submit_review'),
]