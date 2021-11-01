from Domain.librarie import creazaVanzare, getGen, getId, getPret, getTip, getTitlu


def testVanzare():
    comanda = creazaVanzare("1", "Alba ca Zapada", "Basm", 12.5, "none")

    assert getId(comanda) == "1"
    assert getTitlu(comanda) == "Alba ca Zapada"
    assert getPret(comanda) == 12.5
    assert getGen(comanda) == "Basm"
    assert getTip(comanda) == "none" 

