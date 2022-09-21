from django.urls import path
from . import views

urlpatterns = [
    path('update_stats', views.update_stats),
]