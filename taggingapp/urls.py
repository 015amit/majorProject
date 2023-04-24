from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('openfile/', views.openfile, name='annoatate'),
    path('find_and_replace/', views.find_and_replace, name='find_and_replace'),
]