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

def determinaMinimPreturi(lista):
    listaNoua = listaGenuri(lista)
    listaPreturi = []
    for i in listaNoua:
        minim = None
        for comanda in lista:
            gen = getGen(comanda)
            pret = getPret(comanda)
            if gen == i:
                if minim == None:
                    minim = pret
                elif pret < minim:
                    minim = pret
        listaPreturi.append(minim)
    return listaPreturi


def swap(list, pos1, pos2):
     
    first = list.pop(pos1)  
    second = list.pop(pos2-1)
    list.insert(pos1, second) 
    list.insert(pos2, first) 
     
    return list


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
