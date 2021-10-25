from Domain.librarie import toString
from Logic.CRUD import adaugaVanzare, modificareVanzare, stergereVanzare
from Logic.functionalitati import discount

def printmenu():
    print("1. Adaugare comanda ")
    print("2. Stergere comanda ")
    print("3. Modifica comanda ")
    print("4. Fa discount in functie de tipul reduceri ")
    print("a. Afisare comenzi ")
    print("x. Iesire")

def addComanda(lista):
    id = input("Dati ID: ")
    titlu = input("Titlu: ")
    gen = input("Genul: ")
    pret = input("Pret: ")
    reducere = input("Reducere (none/silver/gold): ")
    return adaugaVanzare(id,titlu,gen,pret,reducere,lista)

def stergComanda(lista):
    id = input("Dati id ul unei comenzi: ")
    return stergereVanzare(id,lista)

def modifComanda(lista):
    id = input("Dati noul ID: ")
    titlu = input("Titlu nou: ")
    gen = input("Genul nou: ")
    pret = input("Pret nou: ")
    reducere = input("Reducere noua (none/silver/gold): ")
    return modificareVanzare(id,titlu,gen,pret,reducere,lista)

def arata(lista):
    for comanda in lista:
        print(toString(comanda))

def aplicDiscount(lista):
    return discount(lista)

def runMenu(lista):
    while True:
        printmenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = addComanda(lista)
        elif optiune =="2":
            lista = stergComanda(lista)
        elif optiune =="3":
            lista = modifComanda(lista)
        elif optiune =="4":
            lista = aplicDiscount(lista)
        elif optiune =="a":
            arata(lista)
        elif optiune =="x":
            break
        else:
            print("Optiune incorecta! Reincercati: ")

