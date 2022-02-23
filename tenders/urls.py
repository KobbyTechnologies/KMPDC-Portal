from django.urls import path

from . import views

urlpatterns = [
    path('openTenders', views.open_tenders, name="open"),
    path('restrictedTenders', views.Restricted_tenders, name='restricted'),
    path('Odetails/<str:pk>', views.Open_Details, name="Odetails"),
    path('RES/<str:pk>', views.Restrict_Details, name="RES"),
    path('DocResponse/<str:pk>', views.DocResponse, name="DocResponse"),
]
