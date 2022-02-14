from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('call_demo/', views.call_demo, name='call_demo'),
]