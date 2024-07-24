from operacoes import calcular_media, verificar_reprovacao, alunos_reprovados

alunos = [
    {'nome': 'Maria', 'matricula': 26},
    {'nome': 'Ana', 'matricula': 101},
    {'nome': 'João', 'matricula': 13},
    {'nome': 'Ágatha', 'matricula': 37},
    {'nome': 'Joaquim', 'matricula': 72},
    {'nome': 'Félix', 'matricula': 5},
]


notas = {
    26: [8, 7, 5, 9],
    101: [9, 9, 8, 9],
    13: [6, 5, 5, 5],
    37: [8, 6, 7.5, 9],
    72: [6, 5.5, 5, 7],
    5: [10, 8, 8, 8],
}

matriculas_reprovados = []
for aluno in alunos:
    matricula = aluno['matricula']
    media = calcular_media(notas[matricula])
    aluno['media'] = media
    if verificar_reprovacao(media):
        matriculas_reprovados.append(matricula)

alunos_reprovados(alunos, matriculas_reprovados)