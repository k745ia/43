from django.urls import path
from .views import index_2

urlpatterns = [
    path('', index_2)
]