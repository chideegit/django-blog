from django.urls import path 
from .views import * 

urlpatterns = [
    path('', website, name='website'),
    path('dashboard/', dashboard, name='dashboard')
]