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
            for i in range(len(listaExecut)):
                listaExecut[i].strip() 
            if listaExecut[0] == "add":
                try:
                    lista = adaugaVanzare(listaExecut[1], listaExecut[2], listaExecut[3], listaExecut[4], listaExecut[5],lista)
                except ValueError as e:
                    print("Eroare: {}".format(e))
            elif listaExecut[0] == "showall":
                for comanda in lista:
                    print(toString(comanda))
            elif listaExecut[0] == "delete":
                try:
                    id = listaExecut[1]
                    lista = stergereVanzare(id, lista)
                except ValueError as e:
                    print("Eroare: {}".format(e))
            elif listaExecut[0] == "exit":
                return lista
            else:
                print("Comanda este gresita ")


    