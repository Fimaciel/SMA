from django.urls import path
from .views import registrar_rfid

urlpatterns = [
    path("api/rfid/", registrar_rfid),
]
