from django.urls import path
from . import views

urlpatterns = [
    path('', views.curso_list, name='curso_list'),
    path('create/', views.curso_create, name='curso_create'),
    path('edit/<int:curso_id>/', views.curso_edit, name='curso_edit'),
    path('delete/<int:curso_id>/', views.curso_delete, name='curso_delete'),
]
