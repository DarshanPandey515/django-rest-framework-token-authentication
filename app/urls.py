from django.urls import path
from app.views import *


urlpatterns = [
    path('', index),
    path('data/', DataAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('get-books/', get_books),
    path('post-data/', post_data),
    path('update-data/<str:pk>/', updated_data),
    path('delete-data/<str:pk>/', delte_data),
]

