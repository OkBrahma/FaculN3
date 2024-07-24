dicionario = {1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}}
print("Dicionário inicial:", dicionario)

dicionario.update({2: {'nome': 'João', 'idade': 30, 'nacionalidade': 'português'}})
dicionario.update({3: {'nome': 'Ana', 'idade': 22, 'nacionalidade': 'brasileira'}})
print("Dicionário atualizado:", dicionario)

dicionario_copia = dicionario.copy()
print("Cópia do dicionário:", dicionario_copia)

removido = dicionario.pop(2)
print("Elemento removido com pop:", removido)
print("Dicionário após pop:", dicionario)

ultimo_removido = dicionario.popitem()
print("Último elemento removido com popitem:", ultimo_removido)
print("Dicionário após popitem:", dicionario)

dicionario.clear()
dicionario_copia.clear()
print("Dicionário após clear:", dicionario)
print("Cópia do dicionário após clear:", dicionario_copia)

novas_chaves = ['a', 'b', 'c']
novo_dicionario = dict.fromkeys(novas_chaves, 'valor_comum')
print("Novo dicionário criado com fromKeys:", novo_dicionario)

print("Itens do novo dicionário:", novo_dicionario.items())
print("Chaves do novo dicionário:", novo_dicionario.keys())
print("Valores do novo dicionário:", novo_dicionario.values())
