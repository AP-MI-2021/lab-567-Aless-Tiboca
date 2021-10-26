def creazaVanzare(id, titlu, gen, pret, tip):
    """Creaza un dictionar ce reprezinta o vanzare

    Args:
        id ([int]): [id-ul carti]
        titlu ([string]): [titlul cartii]
        gen ([string]): [genul cartii]
        pret ([float]): [pretul cartii]
        tip ([string]): [tipul de reducere (`none`, `silver`, `gold`)]

    Returns:
        un dictionar ce reprezinta o vanzare a unei carti
    """
    return [id, titlu, gen, float(pret), tip]

def getId(comanda):
    return comanda[0]

def getTitlu(comanda):
    return comanda[1]

def getGen(comanda):
    return comanda[2]

def getPret(comanda):
    return comanda[3]

def getTip(comanda):
    return comanda[4]

def toString(comanda):
    return "Id: {}, Titlu: {}, Gen: {}, Pret: {}, Tip Reducere: {}".format(
    getId(comanda),
    getTitlu(comanda),
    getGen(comanda),
    getPret(comanda),
    getTip(comanda)
    )