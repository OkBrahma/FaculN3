lista_mesclada = [1, 2, 3, "Olá, Python", True, 12.6]
print("Conteúdo da lista inicial:")
print(lista_mesclada)
print()

lista_mesclada.append(["Lista aninhada"])
print("Lista após adicionar lista aninhada:")
print(lista_mesclada)
print()

lista_mesclada.insert(4, 5)
print("Lista após inserir o número 5:")
print(lista_mesclada)
print()

print("Tamanho atual da lista:", len(lista_mesclada))
print()


del lista_mesclada[1]
print("Lista após remover o item na posição 1:")
print(lista_mesclada)
print()

nova_lista_mesclada = lista_mesclada[:5]
print("Conteúdo da nova lista até a posição 4:")
print(nova_lista_mesclada)