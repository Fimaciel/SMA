from django.urls import path
from . import views

urlpatterns = [
    path('', views.presencas_list, name='presencas_list'),
    path('novo/', views.presencas_create, name='presencas_create'),
    path('<int:presenca_id>/editar/', views.presencas_edit, name='presencas_edit'),
    path('<int:presenca_id>/excluir/', views.presencas_delete, name='presencas_delete'),
]
