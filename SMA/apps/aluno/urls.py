from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='alunos_index'),
    path('create/', views.create, name='alunos_create'),
    path('editar/<int:aluno_id>/', views.edit, name='alunos_edit'),
    path('deletar/<int:aluno_id>/', views.destroy, name='alunos_destroy'),
]
