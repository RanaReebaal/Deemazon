from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='fashionhouse/home'),
    path('index/', views.index, name='fashionhouse/index'),

]