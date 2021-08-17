from django.urls import path
from . import views

app_name = 'app_home'

urlpatterns = [
    path('', views.tax_home, name='tax_home'),
    path('tax/', views.tax, name='tax'),
    path('about/', views.about, name='about'),
]