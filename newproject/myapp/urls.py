from django.urls import path
from myapp import views

urlpatterns = [
    
    path('', views.form_view, name='form'),
    path('success/', views.success_view, name='success'),
]   