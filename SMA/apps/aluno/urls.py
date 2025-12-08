from django.urls import path
from .views import (
    AlunoListView,
    AlunoCreateView,
    AlunoUpdateView,
    AlunoDeleteView,
    toggle_rfid
)

app_name = 'aluno'

urlpatterns = [
    path('', AlunoListView.as_view(), name='aluno_list'),
    path('add/', AlunoCreateView.as_view(), name='aluno_add'),
    path('<int:pk>/edit/', AlunoUpdateView.as_view(), name='aluno_edit'),
    path('<int:pk>/delete/', AlunoDeleteView.as_view(), name='aluno_delete'),
    path('<int:pk>/toggle-rfid/', toggle_rfid, name='toggle_rfid'),
]
