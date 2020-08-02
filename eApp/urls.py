from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'eApp-home'),
    path('about/', views.about, name = 'eApp-about'),
    path('ncert-solutions/', views.ncertSol, name = 'eApp-ncert-solutions'),
]
