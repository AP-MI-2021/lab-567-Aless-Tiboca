from Domain.librarie import getGen, getId, getPret, getTip, getTitlu
from Logic.CRUD import adaugaVanzare, getbyID, modificareVanzare, stergereVanzare


def testAdaugaComanda():
    l = []
    l = adaugaVanzare("1", "Piratii din Caraibe", "Explorare", 45, "gold", l)
    assert getId(getbyID("1",l)) =="1"
    assert getTitlu(getbyID("1",l)) == "Piratii din Caraibe"
    assert getGen(getbyID("1",l)) == "Explorare"
    assert getPret(getbyID("1",l)) == 45
    assert getTip(getbyID("1",l)) == "gold"

def testSterge():
    l = []
    l = adaugaVanzare("1", "Pirati din Caraibe", "Explorare", 45, "gold", l)
    l = adaugaVanzare("2", "Alba ca zapada", "Basm", 25, "silver", l)
    l = adaugaVanzare("3", "Cenusareasa", "Basm", 30, "none", l)
    l = stergereVanzare("2",l)
    assert getbyID("1",l) is not None
    assert getbyID("2",l) is None
    assert getbyID("3",l) is not None

def testModifComanda():
    l = []
    l = adaugaVanzare("1", "Pirati din Caraibe", "Explorare", 45, "gold", l)
    l = adaugaVanzare("2", "Alba ca zapada", "Basm", 25, "silver", l)
    l = modificareVanzare("2","Alba ca zapada","Nuvela",10,"gold", l)
    assert getId(getbyID("2", l)) == "2"
    assert getTitlu(getbyID("2", l)) == "Alba ca zapada"
    assert getGen(getbyID("2", l)) == "Nuvela"
    assert getPret(getbyID("2", l)) == 10
    assert getTip(getbyID("2", l)) == "gold"

def testGetById():
    l = []
    l = adaugaVanzare("1", "Pirati din Caraibe", "Explorare", 45, "gold", l)
    l = adaugaVanzare("2", "Alba ca zapada", "Basm", 25, "silver", l)
    l = adaugaVanzare("3", "Cenusareasa", "Basm", 30, "none", l)
    assert getbyID("1",l) == ["1", "Pirati din Caraibe", "Explorare", 45, "gold"]
    assert getbyID("2",l) == ["2", "Alba ca zapada", "Basm", 25, "silver"]
    assert getbyID("3",l) == ["3", "Cenusareasa", "Basm", 30, "none"]


def testCrud():
    testGetById()
    testModifComanda()
    testSterge()
    testAdaugaComanda()