from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='parlourhouse/home'),
    path('index/', views.index, name='parlourhouse/index'),

]