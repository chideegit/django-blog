from django.urls import path 
from .views import * 

urlpatterns = [
    path('create-category/', create_category, name='create-category'), 
    path('update-category/<str:title>/', update_category, name='update-category'), 
    path('create-post/', create_post, name='create-post'), 
    path('update-post/<slug:slug>/', update_post, name='update-post'), 
    path('all-categories/', all_categories, name='all-categories'), 
    path('all-posts/', all_posts, name='all-posts'), 
    path('post-details/<slug:slug>/', post_details, name='post-details'), 
]