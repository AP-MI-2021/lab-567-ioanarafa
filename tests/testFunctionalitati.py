from Domain.rezervare import getId, getNume, getClasa, getPret, getCheckin
from logic.CRUD import adaugaRezervare
from logic.functionalitati import trecereaClasaSuperioaraDupaNume, getByName


def testTrecereaClasaSuperioaraDupaNume():
    lista = []
    lista = adaugaRezervare("1", "Ana", "economy", 1400, "Da", [])
    lista = adaugaRezervare("2", "Mara", "business", 360, "Nu", lista)

    lista = trecereaClasaSuperioaraDupaNume("Ana", lista)
    rezervareUpdatata = getByName("Ana", lista)
    assert getId(rezervareUpdatata) == "1"
    assert getNume(rezervareUpdatata) == "Ana"
    assert getClasa(rezervareUpdatata) == "economy plus"
    assert getPret(rezervareUpdatata) == 1400
    assert getCheckin(rezervareUpdatata) == "Da"



