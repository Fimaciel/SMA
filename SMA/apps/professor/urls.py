from django.urls import path
from .views import ProfessorListView, ProfessorCreateView, ProfessorUpdateView, ProfessorDeleteView

app_name = 'professor'

urlpatterns = [
    path('', ProfessorListView.as_view(), name='professor_list'),
    path('add/', ProfessorCreateView.as_view(), name='professor_add'),
    path('<int:pk>/edit/', ProfessorUpdateView.as_view(), name='professor_edit'),
    path('<int:pk>/delete/', ProfessorDeleteView.as_view(), name='professor_delete'),
]
