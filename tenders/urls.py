from django.urls import path

from . import views

urlpatterns = [
    path('openTenders', views.open_tenders, name="open"),
]
