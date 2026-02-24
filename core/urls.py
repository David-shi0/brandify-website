from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('team/', views.TeamView.as_view(), name='team'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]