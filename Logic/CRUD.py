from Domain.librarie import creazaVanzare, getId


def adaugaVanzare(id, titlu, gen, pret, tip, lista):
    """Functia adauga o vanzare la lista

    Args:
        id ([int]): [id-ul carti]
        titlu ([string]): [titlul cartii]
        gen ([string]): [genul cartii]
        pret ([string]): [pretul cartii]
        tip ([string]): [tipul de reducere (`none`, `silver`, `gold`)]
        lista ([list]): [lista cu vanzarile precedente]

    Returns:
        [list]: [returneaza lista continand atat elementele vechi cat si cele noi]
    """
    comanda = creazaVanzare(id, titlu, gen, pret, tip)
    return lista+[comanda]


def stergereVanzare(id, lista):
    """Functia sterge o vanzare dupa id-ul dat

    Args:
        id ([int]): [id-ul carti]
        lista ([list]): [lista cu vanzarile precedente]

    Returns:
        [list]: [returneaza lista fara elmentele care au id-ul echivalent cu cel dat]
    """
    return [comanda for comanda in lista if getId(comanda) != id]


def modificareVanzare(id, titlu, gen, pret, tip, lista):
    """Functia modifica o vanzare dupa id-ul dat

    Args:
        id ([int]): [id-ul carti]
        titlu ([string]): [titlul cartii]
        gen ([string]): [genul cartii]
        pret ([string]): [pretul cartii]
        tip ([string]): [tipul de reducere (`none`, `silver`, `gold`)]
        lista ([list]): [lista cu vanzarile precedente]
    
    Returns:
        listaNoua[list]: [returneaza lista continand atat elementele vechi cat si cele modificate]   

    """
    listaNoua = []
    for comanda in lista:
        if getId(comanda) == id:
            comandaModificata = creazaVanzare(id, titlu, gen, pret, tip)
            listaNoua.append(comandaModificata)
        else:
            listaNoua.append(comanda)

    return listaNoua  


def getbyID(id,lista):
    for comanda in lista:
        if getId(comanda) == id:
            return comanda
    return None
     