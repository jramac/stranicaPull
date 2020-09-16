from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='novosti-home'),
    path('novosti/', views.blog, name='novosti-novosti'),
    path('novosti/<int:id>/', views.detail, name='novosti-detail'),
    path('oprojektu/', views.oprojektu, name='novosti-oprojektu'),
    path('partneri/', views.partneri, name='novosti-partneri'),
    path('kontakt/', views.kontakt, name='novosti-kontakt')
]