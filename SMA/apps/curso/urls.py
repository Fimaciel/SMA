from django.urls import path
from .views import CursoListView, CursoCreateView, CursoUpdateView, CursoDeleteView

app_name = 'curso'

urlpatterns = [
    path('', CursoListView.as_view(), name='curso_list'),
    path('add/', CursoCreateView.as_view(), name='curso_add'),
    path('<int:pk>/edit/', CursoUpdateView.as_view(), name='curso_edit'),
    path('<int:pk>/delete/', CursoDeleteView.as_view(), name='curso_delete'),
]