import serial
import json
import requests

# Porta serial do Arduino
PORTA = "/dev/ttyUSB0"
BAUD = 9600

ser = serial.Serial(PORTA, BAUD)

API_URL = "http://127.0.0.1:8000/presencas/api/rfid/"

while True:
    try:
        linha = ser.readline().decode().strip()

        if not linha.startswith("{"):
            continue

        dado = json.loads(linha)

        print("Lido:", dado)

        # Enviar para o Django
        requests.post(API_URL, json=dado)

    except Exception as e:
        print("Erro:", e)
