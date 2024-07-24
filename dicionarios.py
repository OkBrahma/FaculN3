meu_dicionario = {
    1: {'linguagem': 'Python'},
    2: {'linguagem': 'Java'},
    3: {'linguagem': 'PHP'}
}

print("Conteúdo do dicionário meu_dicionario:")
print(meu_dicionario)
print()

print("Tipo de dados do dicionário meu_dicionario:", type(meu_dicionario))
print()

print("Valor da chave 'linguagem' utilizando get:", meu_dicionario.get(1).get('linguagem'))
print()

print("Tamanho do dicionário meu_dicionario:", len(meu_dicionario))
print()


dicionario_frutas = dict()
dicionario_frutas = {
    1: {'nome': 'limão', 'tipo': 'ácida'},
    2: {'nome': 'laranja', 'tipo': 'ácida'},
    3: {'nome': 'manga', 'tipo': 'semiácida'},
    4: {'nome': 'maça', 'tipo': 'semiácida'},
    5: {'nome': 'banana', 'tipo': 'doce'},
    6: {'nome': 'mamão', 'tipo': 'doce'}
}


print("Valor das chaves 'nome' e 'tipo' da chave 1 em dicionario_frutas:")
print("Nome:", dicionario_frutas[1]['nome'])
print("Tipo:", dicionario_frutas[1]['tipo'])
print()

print("Valor das chaves 'nome' e 'tipo' da chave 2 em dicionario_frutas:")
print("Nome:", dicionario_frutas[2]['nome'])
print("Tipo:", dicionario_frutas[2]['tipo'])
print()

print("Valores de todas as chaves 'nome' e 'tipo' em dicionario_frutas:")
for chave, valor in dicionario_frutas.items():
    print(f"Chave {chave}: Nome = {valor['nome']}, Tipo = {valor['tipo']}")