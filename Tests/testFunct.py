from Domain.librarie import getGen, getPret
from Logic.CRUD import adaugaVanzare, getbyID, modificareVanzare
from Logic.functionalitati import discount, modificareGenDupaTitlu


def testAplicReduceri():
    lista = []
    lista = adaugaVanzare("1", "Harap Alb", "fantastica", 100.0, "silver", lista)
    lista = adaugaVanzare("2", "Fat Frumos din lacrima", "fantastica", 100.0, "gold", lista)
    lista = adaugaVanzare("3", "Povestea micii sirene", "apa", 280.0, "none", lista)

    lista = discount(lista)

    assert getPret(getbyID("1", lista)) == 95.0
    assert getPret(getbyID("2", lista)) == 90.0
    assert getPret(getbyID("3", lista)) == 280.0



def testTitluriDist():
    l = []
    l = adaugaVanzare("1", "Piratii din Caraibe", "Explorare", 100, "gold", l)
    l = adaugaVanzare("2", "Alba ca zapada", "Basm", 34, "silver", l)
    l = adaugaVanzare("3", "Cenusareasa", "Basm", 10, "silver", l)
    newGen = []
    cntGen = []

    for comanda in l:
        ok = 1
        for gen in newGen:
            if getGen(comanda) == gen:
                ok = 0
        if ok == 1:
            newGen.append(getGen(comanda))

    for gen in newGen:
        c = 0
        for comanda in l:
            if getGen(comanda) == gen:
                c=c+1
        cntGen.append(c)

    assert cntGen[0] == 1
    assert cntGen[1] == 2


def testModificareGenDupaTitlu():
    lista = []
    lista = adaugaVanzare("1", "Harap Alb", "fantastica", 100.0, "silver", lista)
    lista = adaugaVanzare("2", "Fat Frumos din lacrima", "fantastica", 100.0, "gold", lista)
    lista = adaugaVanzare("3", "Povestea micii sirene", "apa", 280.0, "none", lista)

    titlu = "Harap Alb"
    genModificat = "poveste"
    lista = modificareGenDupaTitlu(titlu, genModificat, lista)

    assert getGen(getbyID("1", lista)) == genModificat
    assert getGen(getbyID("2", lista)) == "fantastica"

    titlu = "Povestea micii sirene"
    genModificat = "Poveste de dragoste"

    lista = modificareGenDupaTitlu(titlu, genModificat, lista)

    assert getGen(getbyID("3", lista)) == genModificat



def testFunct():
    testTitluriDist()
    testModificareGenDupaTitlu()
    testAplicReduceri()