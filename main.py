from Logic.CRUD import adaugaVanzare
from Tests.testAll import runAllTests
from UserInterface.console import runMenu

def main():
    runAllTests()
    lista = []
    lista = adaugaVanzare("1", "Pirati din Caraibe", "Explorare", 45.0, "gold", lista)
    lista = adaugaVanzare("2", "Alba ca zapada", "Basm", 25.0, "silver", lista)
    runMenu(lista)

main()