from django.urls import path
from . import views

urlpatterns = [
    path('', views.disciplina_list, name='disciplina_list'),
    path('create/', views.disciplina_create, name='disciplina_create'),
    path('edit/<int:disciplina_id>/', views.disciplina_edit, name='disciplina_edit'),
    path('delete/<int:disciplina_id>/', views.disciplina_delete, name='disciplina_delete'),
]
