from django.urls import path

from . import views

urlpatterns = [
    path('categorias/', views.categorias, name="categorias"),
    path('categorias/add', views.categorias_add, name="categorias_add")
]