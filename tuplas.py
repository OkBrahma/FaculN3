primeira_tupla = (1, 2, 3, 4, "Olá, tupla")
print("Conteúdo da tupla inicial:")
print(primeira_tupla)
print()


indice_elemento_4 = primeira_tupla.index(4)
print("O índice do elemento 4 na tupla é:", indice_elemento_4)
print()

contem_elemento_3 = 3 in primeira_tupla
print("A tupla contém o elemento 3?", contem_elemento_3)
print()

contem_elemento_33 = 33 in primeira_tupla
print("A tupla contém o elemento 33?", contem_elemento_33)
