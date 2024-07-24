set_inicial = {11, 12, 13, 14}
print("Conteúdo do set inicial:")
print(set_inicial)
print()

set_inicial.add(15)
print("Set após adicionar o elemento 15:")
print(set_inicial)
print()

set_inicial.update({1, 2, 3, 4, 5})
print("Set após atualização com novos elementos:")
print(set_inicial)
print()

set_inicial.discard(13)
print("Set após remover o elemento 13:")
print(set_inicial)
print()


novo_set = set([20, 21, 23, 1, 2])
print("Conteúdo do novo set:")
print(novo_set)
print()


uniao = set_inicial.union(novo_set)
print("Resultado da união entre os dois sets:")
print(uniao)
print()

intersecao = set_inicial.intersection(novo_set)
print("Resultado da interseção entre os dois sets:")
print(intersecao)
print()

diferenca = set_inicial.difference(novo_set)
print("Resultado da diferença entre os dois sets (set_inicial - novo_set):")
print(diferenca)
print()

dif_simetrica = set_inicial.symmetric_difference(novo_set)
print("Resultado da diferença simétrica entre os dois sets:")
print(dif_simetrica)