from django.contrib import admin
from django.urls import path
from .views import detail, index

urlpatterns = [
  path('', index, name='index'),
  path('<int:id>/', detail, name='detail'),
]
