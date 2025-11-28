from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import RegistroRFID


@api_view(["POST"])
def registrar_rfid(request):
    uid = request.data.get("uid")
    tipo = request.data.get("tipo")

    if not uid:
        return Response({"error": "RFID não enviado"}, status=400)

    RegistroRFID.objects.create(
        uid=uid,
        presenca=None,
        horario=timezone.now(),
        tipo=tipo  
    )

    return Response({"status": "ok", "uid": uid})

