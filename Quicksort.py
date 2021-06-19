#Quicksort 
def quick_sort(lista):
    lista2 = " ".join(lista)
    lista2 = lista2.split(":")
    lista2 = " ".join(lista2)
    puntajes = [int(temp)for temp in lista2.split() if temp.isdigit()]
    jugadores = [str(temp+":")for temp in lista2.split() if temp.isidentifier()]
    largo = len(puntajes)
    if largo <= 1:
        return lista
    else:
        pivote = puntajes.pop()
        pivote2 = jugadores.pop()

    mayores = []
    menores = []


    for i in range(0,len(puntajes)):
        f = jugadores[i]
        j = puntajes[i]
        if j <= pivote:
            mayores += [f+str(j)]
        else:
            menores += [f+str(j)]


    return quick_sort(menores) + [pivote2+str(pivote)] + quick_sort(mayores)



def quick_sort_record(lista):
    lista2 = " ".join(lista)
    lista2 = lista2.split(":")
    lista2 = " ".join(lista2)
    puntajes = [int(temp)for temp in lista2.split() if temp.isdigit()]
    largo = len(puntajes)
    if largo <= 1:
        return lista
    else:
        pivote = puntajes.pop()

    mayores = []
    menores = []


    for i in range(0,len(puntajes)):
        j = puntajes[i]
        if j < pivote:
            mayores += [j]
        else:
            menores += [j]


    return quick_sort_record_aux(menores) + [pivote] + quick_sort_record_aux(mayores)

def quick_sort_record_aux(lista):
    largo = len(lista)
    if largo <= 1:
        return lista
    else:
        pivote = lista.pop()

    mayores = []
    menores = []


    for i in range(0,len(lista)):
        j = lista[i]
        if j < pivote:
            mayores += [j]
        else:
            menores += [j]


    return quick_sort_record_aux(menores) + [pivote] + quick_sort_record_aux(mayores)