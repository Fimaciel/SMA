from django.urls import path
from django.views.generic import TemplateView

app_name = 'presenca'

urlpatterns = [

    path('controle/', TemplateView.as_view(template_name='presenca/aula_controle.html'), name='aula_controle'),

    path('historico/', TemplateView.as_view(template_name='presenca/historico.html'), name='historico'),

from . import views

urlpatterns = [
    path('', views.presencas_list, name='presencas_list'),
    path('novo/', views.presencas_create, name='presencas_create'),
    path('<int:presenca_id>/editar/', views.presencas_edit, name='presencas_edit'),
    path('<int:presenca_id>/excluir/', views.presencas_delete, name='presencas_delete'),
]
