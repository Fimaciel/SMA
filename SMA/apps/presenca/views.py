from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from apps.aluno.models import Aluno
from apps.presenca.models import Presencas, PresencaAluno
import json

@csrf_exempt
def     registrar_presenca(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método não permitido"}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8"))
        uid = data.get("uid")

        if not uid:
            return JsonResponse({"error": "UID não informado"}, status=400)

        try:
            aluno = Aluno.objects.get(uid=uid)
        except Aluno.DoesNotExist:
            return JsonResponse({"error": "Aluno não encontrado"}, status=404)

        # Verifica se o aluno já tem presença hoje
        hoje = timezone.localdate()
        presenca = Presencas.objects.filter(data=hoje).first()

        if not presenca:
            # Cria a presença do dia se ainda não existir
            presenca = Presencas.objects.create(
                data=hoje,
                horario_entrada=timezone.now().time(),
                horario_saida=None
            )

        # Verifica se o aluno já marcou entrada hoje
        relacao = PresencaAluno.objects.filter(presenca=presenca, aluno=aluno).first()

        if not relacao:
            # Marca entrada
            PresencaAluno.objects.create(presenca=presenca, aluno=aluno)
            status = "ENTRADA"
        else:
            # Marca saída (atualiza horário_saida)
            presenca.horario_saida = timezone.now().time()
            presenca.save()
            status = "SAÍDA"

        return JsonResponse({
            "aluno": aluno.nome,
            "uid": uid,
            "status": status,
            "data": str(hoje),
            "hora": timezone.now().strftime("%H:%M:%S")
        })

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
