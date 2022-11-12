from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='jewelleryhouse/home'),
    path('index/', views.index, name='jewelleryhouse/index'),

]