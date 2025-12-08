from django.shortcuts import render
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta
from apps.aluno.models import Aluno
from apps.disciplina.models import Aula, Disciplina
from apps.professor.models import Professor
from apps.curso.models import Curso
from apps.presenca.models import PresencaAluno, RegistroRFID


def dashboard(request):
    hoje = timezone.now().date()
    
    # KPIs principais
    total_alunos = Aluno.objects.count()
    total_professores = Professor.objects.count()
    total_disciplinas = Disciplina.objects.count()
    total_cursos = Curso.objects.count()
    
    # Aulas
    aulas_ativas = Aula.objects.filter(encerrada=False, data=hoje).count()
    total_aulas = Aula.objects.count()
    aulas_encerradas = Aula.objects.filter(encerrada=True).count()
    
    # Presenças hoje
    presencas_hoje = PresencaAluno.objects.filter(
        aula__data=hoje,
        presente=True
    ).count()
    
    # Taxa de presença geral
    total_presencas = PresencaAluno.objects.filter(presente=True).count()
    total_registros = PresencaAluno.objects.count()
    taxa_presenca = round((total_presencas / total_registros * 100) if total_registros > 0 else 0, 1)
    
    # RFIDs ativos
    rfids_ativos = Aluno.objects.filter(uid__isnull=False).exclude(uid='').count()
    
    # Últimas atividades (últimos 10 registros RFID)
    ultimas_atividades = RegistroRFID.objects.filter(
        uid__isnull=False
    ).exclude(uid='').order_by('-horario')[:10]
    
    # Adicionar informação do aluno para cada registro
    for atividade in ultimas_atividades:
        try:
            atividade.aluno = Aluno.objects.get(uid=atividade.uid)
        except Aluno.DoesNotExist:
            atividade.aluno = None
    
    # Aulas da semana
    inicio_semana = hoje - timedelta(days=hoje.weekday())
    fim_semana = inicio_semana + timedelta(days=6)
    aulas_semana = Aula.objects.filter(data__range=[inicio_semana, fim_semana]).order_by('data')
    
    # Próximas aulas
    proximas_aulas = Aula.objects.filter(
        data__gte=hoje,
        encerrada=False
    ).order_by('data', 'horario_inicio')[:5]
    
    context = {
        'total_alunos': total_alunos,
        'total_professores': total_professores,
        'total_disciplinas': total_disciplinas,
        'total_cursos': total_cursos,
        'aulas_ativas': aulas_ativas,
        'total_aulas': total_aulas,
        'aulas_encerradas': aulas_encerradas,
        'presencas_hoje': presencas_hoje,
        'taxa_presenca': taxa_presenca,
        'rfids_ativos': rfids_ativos,
        'ultimas_atividades': ultimas_atividades,
        'proximas_aulas': proximas_aulas,
        'aulas_semana': aulas_semana,
    }
    
    return render(request, 'dashboard.html', context)
