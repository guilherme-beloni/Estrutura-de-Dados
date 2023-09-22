def busca(lista, elemento):
    for valor in lista:
        if valor == elemento:
            return True
    return False


lista = [2, "5", 5.8, 0, "python", 4]
#lista.append('Guilherme')
#lista.clear()
#lista_copia = lista.copy()
#contagem = lista.count(0) #número de ocorrências de um elemento
#posicao = lista.index(0) #posição da primeira ocorrência de um elemento
#inserir = lista.insert() #insere um elemento numa posição especificada
#remover = lista.remove() #remove a primeira ocorrência de um elemento
elemento = 0
#print(contagem)

achou = busca(lista, elemento)
print(achou)