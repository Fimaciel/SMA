from django.urls import path
from . import views

urlpatterns = [
    path('', views.horarios_list, name='horarios_list'),
    path('novo/', views.horarios_create, name='horarios_create'),
    path('<int:horario_id>/editar/', views.horarios_edit, name='horarios_edit'),
    path('<int:horario_id>/excluir/', views.horarios_delete, name='horarios_delete'),
]
