from django.urls import path
from . import views

urlpatterns = [
    path('dash', views.dashboard, name="dashboard"),
    path('canvas', views.canvas, name="canvas"),
]
