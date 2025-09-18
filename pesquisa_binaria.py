#   Algoritmo para pesquisa binária
#   Requer que a lista esteja ordenada
def pesquisa_binaria(lista, item):
    # Posicao inicial
    baixo = 0
    # Posicao final
    alto = len(lista)-1
    # Enquanto a posicao inicial for menor ou igual a posicao final
    while baixo <= alto:
        meio = (baixo+alto)/2
        chute=lista[meio]
        if chute==item:
            return meio
        if chute > item:
            alto = meio -1
        else:
            baixo = meio +1
    return None 
# Testando o algoritmo
minha_lista = [1, 3, 5, 7, 9]
print pesquisa_binaria(minha_lista, 3)
print pesquisa_binaria(minha_lista, -1)