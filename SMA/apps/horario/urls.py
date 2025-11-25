from django.urls import path
from .views import HorarioListView, HorarioCreateView, HorarioUpdateView, HorarioDeleteView

app_name = 'horario'

urlpatterns = [
    path('', HorarioListView.as_view(), name='horario_list'),
    path('add/', HorarioCreateView.as_view(), name='horario_add'),
    path('<int:pk>/edit/', HorarioUpdateView.as_view(), name='horario_edit'),
    path('<int:pk>/delete/', HorarioDeleteView.as_view(), name='horario_delete'),
]
