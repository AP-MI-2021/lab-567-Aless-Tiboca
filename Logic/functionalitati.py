from Domain.librarie import creazaVanzare, getGen, getId, getPret, getTip, getTitlu


def discount(lista):
    listaNoua = []
    for comanda in lista:
        if getTip(comanda) == "silver":
            comandaNoua = creazaVanzare(
                getId(comanda),
                getTitlu(comanda),
                getGen(comanda),
                getPret(comanda) * 0.9,
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
