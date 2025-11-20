from django.urls import path
from .views import registrar_presenca

urlpatterns = [
    path('rfid/', registrar_presenca, name='registrar_presenca'),
]
