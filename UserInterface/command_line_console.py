from Domain.librarie import toString
from Logic.CRUD import adaugaVanzare, stergereVanzare


def printDescriere():
    print("Lista de comenzi va fi separat prin ; ")
    print("Comenzile pot fi: add, showall, delete, exit ")
    print("Parametri dintr-o comanda vor fi separati prin ,")

def runLine(lista):
    while True:
        printDescriere()
        listaInput = []
        listaComenzi = []
        listaInput = input("Dati lista de comenzi: ")
        listaComenzi = listaInput.split(";")
        for x in listaComenzi:
            listaExecut = []
            listaExecut = x.split(",")
            l = []
            for y in listaExecut:
                l.append(y.lstrip())
            listaExecut = l[:]
            if listaExecut[0] == "add":
                try:
                    if listaExecut[5] != "none" and listaExecut[5] != "silver" and listaExecut[5] != "gold":
                        raise ValueError("Tipul de reducere introdus este gresit")
                    lista = adaugaVanzare(listaExecut[1], listaExecut[2], listaExecut[3], listaExecut[4], listaExecut[5], lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif listaExecut[0] == "showall":
                for comanda in lista:
                    print(toString(comanda))
            elif listaExecut[0] == "delete":
                try:
                    id = listaExecut[1]
                    lista = stergereVanzare(id, lista)
                except ValueError as ve:
                    print("Eroare: {}".format(ve))
            elif listaExecut[0] == "exit":
                return lista
            else:
                print("Comanda este gresita ")


    