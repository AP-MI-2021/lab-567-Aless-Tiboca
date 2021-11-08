from Logic.CRUD import adaugaVanzare


def testTitluriDist():
    l = []
    l = adaugaVanzare("1", "Piratii din Caraibe", 45, "Explorare", "Gold", l)
    l = adaugaVanzare("2", "Alba ca zapada", 25, "Basm", "Silver", l)
    l = adaugaVanzare("3", "Cenusareasa", 10, "Basm", "Silver", l)
    newgen1 = []
    contgen = []

    for i in l:
        ok = 1
        for gen in newgen1:
            if i[3] == gen:
                ok = 0
        if ok == 1:
            newgen1.append(i[3])

    for i in newgen1:
        c = 0
        for comanda in l:
            if comanda[3] == i:
                c = c + 1
        contgen.append(c)

    assert contgen[0] == 1
    assert contgen[1] == 2


def testFunct():
    testTitluriDist()