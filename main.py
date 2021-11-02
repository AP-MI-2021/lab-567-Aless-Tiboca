from Logic.CRUD import adaugaVanzare
from Tests.testAll import runAllTests
from UserInterface.command_line_console import runLine
from UserInterface.console import runMenu

def main():
    runAllTests()
    lista = []
    lista = adaugaVanzare("1", "Pirati din Caraibe", "Explorare", 45.0, "gold", lista)
    lista = adaugaVanzare("2", "Alba ca zapada", "Basm", 25.0, "silver", lista)
    while True:
        print("Alegeti tipul de interfata ")
        print("1. Citirea printr-un meniu ")
        print("2. Citirea unei liste de comenzi ")
        optiune = input("Dati optiunea aleasa: ")
        if optiune == "1":
            lista = runMenu(lista)
        elif optiune == "2":
            lista = runLine(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune invalida! Reincercati!")    
    

main()
