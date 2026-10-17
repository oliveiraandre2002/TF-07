
def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]

    return quick_sort(menores) + iguais + quick_sort(maiores)


numeros = [8, 3, 7, 1, 4, 9, 3, 2]

resultado = quick_sort(numeros)

print("Lista original:", numeros)
print("Lista ordenada:", resultado)
