# import time
# import serial  # use 'serial', não 'from serial import Serial'
# from django.utils import timezone
# from apps.aluno.models import Aluno
# from apps.presenca.models import Presencas, PresencaAluno

# def iniciar_leitor_serial(porta="/dev/ttyUSB0", baudrate=9600):
#     print(f"🔌 Iniciando leitura da porta {porta}...")
#     arduino = serial.Serial(porta, baudrate, timeout=1)
#     time.sleep(2)

#     while True:
#         if arduino.in_waiting > 0:
#             uid = arduino.readline().decode().strip()
#             if uid:
#                 print(f"UID lido: {uid}")
#                 registrar_presenca(uid)
#         time.sleep(1)


# def registrar_presenca(uid):
#     try:
#         aluno = Aluno.objects.get(uid=uid)
#     except Aluno.DoesNotExist:
#         print(f"❌ Aluno com UID {uid} não encontrado.")
#         return

#     print(aluno)
#     # hoje = timezone.localdate()
#     # agora = timezone.localtime()

#     # # Tenta pegar a presença do dia
#     # presenca, created = Presencas.objects.get_or_create(
#     #     data=hoje,
#     #     defaults={
    #         "horario_entrada": agora.time(),  # define horário de entrada se ainda não existir
    #         "horario_saida": None              # saída ainda não aconteceu
    #     }
    # )

    # # Checa se o aluno já está registrado nesse dia
    # relacao = PresencaAluno.objects.filter(presenca=presenca, aluno=aluno).first()

    # if not relacao:
    #     # Registra entrada do aluno
    #     PresencaAluno.objects.create(presenca=presenca, aluno=aluno)
    #     # Atualiza horario_entrada da Presencas se ainda estiver None
    #     if presenca.horario_entrada is None:
    #         presenca.horario_entrada = agora.time()
    #         presenca.save()
    #     print(f"✅ {aluno.nome} registrado: ENTRADA às {agora.strftime('%H:%M:%S')}")
    # else:
    #     # Registra saída do aluno
    #     presenca.horario_saida = agora.time()
    #     presenca.save()
    #     print(f"🚪 {aluno.nome} registrado: SAÍDA às {agora.strftime('%H:%M:%S')}")
