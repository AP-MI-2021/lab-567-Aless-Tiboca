def creazaVanzare(id, titlu, gen, pret, tip):
    """Creaza un dictionar ce reprezinta o vanzare

    Args:
        id ([int]): [id-ul carti]
        titlu ([string]): [titlul cartii]
        gen ([string]): [genul cartii]
        pret ([string]): [pretul cartii]
        tip ([string]): [tipul de reducere (`none`, `silver`, `gold`)]

    Returns:
        un dictionar ce reprezinta o vanzare a unei carti
    """
    return {
        "id": id,
        "titlu": titlu,
        "pret": pret,
        "gen": gen,
        "tip": tip
    }

def getId(comanda):
    return comanda["id"]

def getTitlu(comanda):
    return comanda["titlu"]

def getGen(comanda):
    return comanda["gen"]

def getPret(comanda):
    return comanda["pret"]

def getTip(comanda):
    return comanda["tip"]

def toString(comanda):
    return "Id: {}, Titlu: {}, Gen: {}, Pret: {}, Tip Reducere: {}".format(
    getId(comanda),
    getTitlu(comanda),
    getGen(comanda),
    getPret(comanda),
    getTip(comanda)
    )