from django.urls import path
from django.views.generic import TemplateView

app_name = 'presenca'

urlpatterns = [

    path('controle/', TemplateView.as_view(template_name='presenca/aula_controle.html'), name='aula_controle'),

    path('historico/', TemplateView.as_view(template_name='presenca/historico.html'), name='historico'),

]
