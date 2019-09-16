def find_outlier(list):
    list_len = len(list)
    lista_wartosci = []
    for i in range(0, list_len):
        lista_wartosci.append(list[i] % 2)

    if lista_wartosci.count(0) > lista_wartosci.count(1):
        indeks = lista_wartosci.index(1)
    else:
        indeks = lista_wartosci.index(0)

    return list[indeks]