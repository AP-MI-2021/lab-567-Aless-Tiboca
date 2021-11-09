from Domain.librarie import creazaVanzare, getGen, getId, getPret, getTip, getTitlu


def discount(lista):
    listaNoua = []
    for comanda in lista:
        if getTip(comanda) == "silver":
            comandaNoua = creazaVanzare(
                getId(comanda),
                getTitlu(comanda),
                getGen(comanda),
                getPret(comanda) * 0.95,
                getTip(comanda),

            )
            listaNoua.append(comandaNoua)
        elif getTip(comanda) == "gold":
            comandaNoua = creazaVanzare(
                getId(comanda),
                getTitlu(comanda),
                getGen(comanda),
                getPret(comanda) * 0.9,
                getTip(comanda),

            )
            listaNoua.append(comandaNoua)
        else:
            listaNoua.append(comanda)
    return listaNoua


def modificareGenDupaTitlu(titlu, gen, lista):
    listaNoua = []
    for comanda in lista:
        if getTitlu(comanda) == titlu:
            comandaModificata = creazaVanzare(getId(comanda), titlu, gen, getPret(comanda), getTip(comanda))
            listaNoua.append(comandaModificata)
        else:
            listaNoua.append(comanda)
    return listaNoua  


def listaGenuri(lista):
    listaNoua = []
    for comanda in lista:
        gen = getGen(comanda)
        if gen not in listaNoua:
            listaNoua.append(gen)
    return listaNoua


def pretMinimDupaGen(lista):
    """
    Functia creaza un dictionar cu fiecare gen si pretul minim corespunzator acesteia
    """
    rezultat = {}
    for vanzare in lista:
        gen = getGen(vanzare)
        pret = getPret(vanzare)
        if gen in rezultat:  # verifica daca e in dicitonar
            if pret < rezultat[gen]:
                rezultat[gen] = pret
        else:  # daca nu e in dictionar il pune
            rezultat[gen] = pret
    return rezultat


def ordonareDupaPret(lista):
    lista.sort(key = getPret)
    return lista


def titluriDistinctePentruGen(lista):
    newGen = []
    cntGen = []

    for comanda in lista:
        ok = 1
        for gen in newGen:
            if getGen(comanda) == gen:
                ok = 0
        if ok == 1:
            newGen.append(getGen(comanda))

    for gen in newGen:
        c = 0
        for comanda in lista:
            if getGen(comanda) == gen:
                c=c+1
        cntGen.append(c)

    for i in range(len(newGen)):
        print(newGen[i]," ",cntGen[i])
