from Logic.CRUD import adaugaVanzare, getbyID
from UserInterface.console import redo, undo


def testUndoRedo():
    # 1
    lista = []
    undo_list = []
    redo_list = []
    # 2
    undo_list.append(lista)
    redo_list.clear()
    lista = adaugaVanzare("1", "Harap Alb", "fantastica", 300.0, "silver", lista)

    # 3
    undo_list.append(lista)
    redo_list.clear() 
    lista = adaugaVanzare("2", "Fat Frumos din lacrima", "fantastica", 150.0, "gold", lista)

    # 4
    undo_list.append(lista)
    redo_list.clear()
    lista = adaugaVanzare("3", "Povestea micii sirene", "apa", 280.0, "none", lista)

    assert len(lista) == 3

    # 5

    lista = undo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getbyID('1', lista) is not None
    assert getbyID('2', lista) is not None
    assert getbyID('3', lista) is None

    # 6
    lista = undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert getbyID('1', lista) is not None
    assert getbyID('2', lista) is None
    assert getbyID('3', lista) is None

    # 7
    lista = undo(lista, undo_list, redo_list)
    assert len(lista) == 0
    assert getbyID('1', lista) is None
    assert getbyID('2', lista) is None
    assert getbyID('3', lista) is None

    # 8

    assert len(lista) == 0
    assert getbyID('1', lista) is None
    assert getbyID('2', lista) is None
    assert getbyID('3', lista) is None

    # 9
    undo_list.append(lista)
    redo_list.clear()
    lista = adaugaVanzare("1", "Harap Alb", "fantastica", 300.0, "silver", lista)

    undo_list.append(lista)  
    redo_list.clear() 
    lista = adaugaVanzare("2", "Fat Frumos din lacrima", "fantastica", 150.0, "gold", lista)

    undo_list.append(lista)
    redo_list.clear()
    lista = adaugaVanzare("3", "Povestea micii sirene", "apa", 280.0, "none", lista)

    # 10
    lista = redo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert getbyID('1', lista) is not None
    assert getbyID('2', lista) is not None
    assert getbyID('3', lista) is not None

    # 11
    lista = undo(lista, undo_list, redo_list)
    lista = undo(lista, undo_list, redo_list)

    assert len(lista) == 1
    assert getbyID('1', lista) is not None
    assert getbyID('2', lista) is None
    assert getbyID('3', lista) is None

    # 12

    lista = redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getbyID('1', lista) is not None
    assert getbyID('2', lista) is not None
    assert getbyID('3', lista) is None

    # 13

    lista = redo(lista, undo_list, redo_list)
    assert len(lista) == 3
    assert getbyID('1', lista) is not None
    assert getbyID('2', lista) is not None
    assert getbyID('3', lista) is not None

    # 14

    lista = undo(lista, undo_list, redo_list)
    lista = undo(lista, undo_list, redo_list)

    assert len(lista) == 1
    assert getbyID('1', lista) is not None
    assert getbyID('2', lista) is None
    assert getbyID('3', lista) is None

    # 15
    undo_list.append(lista)
    redo_list.clear()
    lista = adaugaVanzare("4", "Povestea micii sirene", "apa", 240.5, "silver", lista)

    assert len(lista) == 2
    assert getbyID('1', lista) is not None
    assert getbyID('2', lista) is None
    assert getbyID('3', lista) is None
    assert getbyID('4', lista) is not None

    # 16
    lista = redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getbyID('1', lista) is not None
    assert getbyID('2', lista) is None
    assert getbyID('3', lista) is None
    assert getbyID('4', lista) is not None

    # 17
    lista = undo(lista, undo_list, redo_list)
    assert len(lista) == 1
    assert getbyID('1', lista) is not None
    assert getbyID('2', lista) is None
    assert getbyID('3', lista) is None
    assert getbyID('4', lista) is None

    # 18
    lista = undo(lista, undo_list, redo_list)
    assert len(lista) == 0
    assert getbyID('1', lista) is None
    assert getbyID('2', lista) is None
    assert getbyID('3', lista) is None
    assert getbyID('4', lista) is None

    # 19
    lista = redo(lista, undo_list, redo_list)
    lista = redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getbyID('1', lista) is not None
    assert getbyID('2', lista) is None
    assert getbyID('3', lista) is None
    assert getbyID('4', lista) is not None

    # 20
    lista = redo(lista, undo_list, redo_list)
    assert len(lista) == 2
    assert getbyID('1', lista) is not None
    assert getbyID('2', lista) is None
    assert getbyID('3', lista) is None
    assert getbyID('4', lista) is not None