from django.urls import path
from . import views

urlpatterns = [
    path('', views.professor_list, name='professor_list'),
    path('novo/', views.professor_create, name='professor_create'),
    path('<int:professor_id>/editar/', views.professor_edit, name='professor_edit'),
    path('<int:professor_id>/excluir/', views.professor_delete, name='professor_delete'),
]
