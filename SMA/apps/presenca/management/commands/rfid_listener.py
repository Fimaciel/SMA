from django.core.management.base import BaseCommand
from apps.presenca.serial_listener import iniciar_leitor_serial

class Command(BaseCommand):
    help = "Inicia o leitor de RFID conectado via USB"

    def handle(self, *args, **options):
        porta = "/dev/ttyUSB0"  # ou /dev/ttyACM0
        iniciar_leitor_serial(porta)
