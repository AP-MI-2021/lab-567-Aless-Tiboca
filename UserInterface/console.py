from Domain.librarie import toString
from Logic.CRUD import adaugaVanzare, modificareVanzare, stergereVanzare
from Logic.functionalitati import discount, modificareGenDupaTitlu, ordonareDupaPret, pretMinimDupaGen, titluriDistinctePentruGen

def printmenu():
    print("1. Adaugare comanda ")
    print("2. Stergere comanda ")
    print("3. Modifica comanda dupa un id")
    print("4. Fa discount in functie de tipul reduceri ")
    print("5. Modifica genul unei vanzari dupa un titlu dat ")
    print("6. Determina prețului minim pentru fiecare gen")
    print("7. Ordonarea vânzărilor crescător după preț")
    print("8. Afișarea numărului de titluri distincte pentru fiecare gen")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare comenzi ")
    print("x. Iesire din interfata meniu")


def undo(lista, undo_list, redo_list):
    if len(undo_list) > 0:
        redo_list.append(lista)
        lista = undo_list.pop() 
    return lista


def redo(lista, undo_list, redo_list):
    if len(redo_list) > 0:
        undo_list.append(lista)
        lista = redo_list.pop()
    return lista


def addComanda(lista, undoList, redoList):
    try:
        id = input("Dati ID: ")        
        titlu = input("Titlu: ")
        gen = input("Genul: ")
        pret = float(input("Pret: "))
        reducere = input("Reducere (none/silver/gold): ")
        if reducere != "none" and reducere != "silver" and reducere != "gold":
            raise ValueError("Tipul de reducere introdus este gresit")
        undoList.append(lista)
        redoList.clear()
        return adaugaVanzare(id,titlu,gen,pret,reducere,lista)
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista

def stergComanda(lista, undoList, redoList):
    try:
        id = input("Dati id ul unei comenzi: ")
        undoList.append(lista)
        redoList.clear()
        return stergereVanzare(id,lista)
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista

def modifGenDupaTitlu(lista, undoList, redoList):
    try:
        titlu = input("Dati titlu pentru care doriti sa modificati genul: ")
        gen = input("Genul nou: ")
        undoList.append(lista)
        redoList.clear()
        return modificareGenDupaTitlu(titlu, gen, lista)
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista


def modifComanda(lista, undoList, redoList):
    try:
        id = input("Dati ID-ul: ")
        titlu = input("Titlu nou: ")
        gen = input("Genul nou: ")
        pret = input("Pret nou: ")
        reducere = input("Reducere noua (none/silver/gold): ")
        if reducere != "none" and reducere != "silver" and reducere != "gold":
            raise ValueError("Tipul de reducere introdus este gresit")
        undoList.append(lista)
        redoList.clear()
        return modificareVanzare(id,titlu,gen,pret,reducere,lista)
    except ValueError as ve:
        print("Eroare {}".format(ve))
        return lista

def arata(lista):
    for comanda in lista:
        print(toString(comanda))

def aplicDiscount(lista, undoList, redoList):
    undoList.append(lista)
    redoList.clear()
    return discount(lista)


def ordonarePret(lista, undoList, redoList):
    undoList.append(lista)
    redoList.clear()
    return ordonareDupaPret(lista)


def pretMinDupaGen(lista):
    rezultat = pretMinimDupaGen(lista)
    for gen in rezultat:
        print("Pretul minim pentru genul {} este {}".format(gen, rezultat[gen]))


def runMenu(lista):
    undoList = []
    redoList = []

    while True:
        printmenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = addComanda(lista, undoList, redoList)
        elif optiune =="2":
            lista = stergComanda(lista, undoList, redoList)
        elif optiune =="3":
            lista = modifComanda(lista, undoList, redoList)
        elif optiune =="4":
            lista = aplicDiscount(lista, undoList, redoList)
        elif optiune =="5":
            lista = modifGenDupaTitlu(lista, undoList, redoList)    
        elif optiune == "6":
            pretMinDupaGen(lista)   
        elif optiune == "7":
            lista = ordonarePret(lista, undoList, redoList) 
        elif optiune == "8":
            titluriDistinctePentruGen(lista)
        elif optiune =="u":
            if len(undoList)>0:
                redoList.append(lista)
                lista = undoList.pop()
                for comanda in lista:
                    print(toString(comanda))
            else:
                print("Nu se poate face undo!")
        elif optiune =="r":
            if len(redoList)>0:
                undoList.append(lista)
                lista = redoList.pop()
                for comanda in lista:
                    print(toString(comanda))
            else:
                print("Nu se poate face redo!")
        elif optiune =="a":
            arata(lista)
        elif optiune =="x":
            return lista
        else:
            print("Optiune incorecta! Reincercati: ")

