def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    return media < 6

def alunos_reprovados(dados_alunos, matriculas_reprovados):
    for aluno in dados_alunos:
        if aluno['matricula'] in matriculas_reprovados:
            print(f"Aluno Reprovado: {aluno['nome']} – Matrícula: {aluno['matricula']} – Média Final: {aluno['media']}")
