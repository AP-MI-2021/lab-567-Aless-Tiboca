from Domain.librarie import toString
from Logic.CRUD import adaugaVanzare, modificareVanzare, stergereVanzare
from Logic.functionalitati import determinaMinimPreturi, discount, modificareGenDupaTitlu, ordonareDupaPret, titluriDistinctePentruGen

def printmenu():
    print("1. Adaugare comanda ")
    print("2. Stergere comanda ")
    print("3. Modifica comanda ")
    print("4. Fa discount in functie de tipul reduceri ")
    print("5. Modifica genul unei vanzari dupa un titlu dat ")
    print("6. Determina prețului minim pentru fiecare gen")
    print("8. Ordonarea vânzărilor crescător după preț")
    print("9. Afișarea numărului de titluri distincte pentru fiecare gen")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare comenzi ")
    print("x. Iesire din interfata meniu")

def addComanda(lista, undoList, redoList):
    try:
        id = input("Dati ID: ")
        titlu = input("Titlu: ")
        gen = input("Genul: ")
        pret = float(input("Pret: "))
        reducere = input("Reducere (none/silver/gold): ")
        if reducere != "none" and reducere != "silver" and reducere != "gold":
            raise ValueError("Tipul de reducere introdus este gresit")
        return adaugaVanzare(id,titlu,gen,pret,reducere,lista)
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista

def stergComanda(lista):
    id = input("Dati id ul unei comenzi: ")
    return stergereVanzare(id,lista)


def modifGenDupaTitlu(lista):
    titlu = input("Dati titlu pentru care doriti sa modificati genul: ")
    gen = input("Genul nou: ")
    
    return modificareGenDupaTitlu(titlu, gen, lista)


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


def ordonarePret(lista):
    return ordonareDupaPret(lista)


def determinaMin(lista):
    listaPreturi = determinaMinimPreturi(lista)
    for pret in listaPreturi:
        print(pret)
        


def runMenu(lista):
    undoList = []
    redoList = []

    while True:
        printmenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = addComanda(lista, undoList, redoList)
        elif optiune =="2":
            lista = stergComanda(lista)
        elif optiune =="3":
            lista = modifComanda(lista)
        elif optiune =="4":
            lista = aplicDiscount(lista)
        elif optiune =="5":
            lista = modifGenDupaTitlu(lista)    
        elif optiune == "6":
            lista = determinaMin(lista)   
        elif optiune == "8":
            lista = ordonarePret(lista) 
        elif optiune == "9":
            titluriDistinctePentruGen(lista)
        elif optiune =="u":
            if len(undoList)>0:
                redoList.append(lista)
                lista = undoList.pop()
                print(lista)
            else:
                print("Nu se poate face undo!")
        elif optiune =="r":
            if len(redoList)>0:
                undoList.append(lista)
                lista = redoList.pop()
                print(lista)
            else:
                print("Nu se poate face redo!")
        elif optiune =="a":
            arata(lista)
        elif optiune =="x":
            return lista
        else:
            print("Optiune incorecta! Reincercati: ")

