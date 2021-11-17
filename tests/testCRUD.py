from Domain.rezervare import getId, getNume, getClasa, getPret, getCheckin
from logic.CRUD import adaugaRezervare, getById, stergereRezervare, modificaRezervare


def testAdaugareRezervare():
    lista = []
    lista = adaugaRezervare("2", "Ana", "business", 300, "Nu", lista)
    assert len(lista) == 1
    assert getId(getById("2", lista)) == "2"
    assert getNume(getById("2", lista)) == "Ana"
    assert getClasa(getById("2", lista)) == "business"
    assert getPret(getById("2", lista)) == 300
    assert getCheckin(getById("2", lista)) == "Nu"



def testStergereRezervare():
    lista = []
    lista = adaugaRezervare("1", "Ana", "business", 300, "Nu", [])
    lista = adaugaRezervare("2", "Mara", "business", 360, "Nu", lista)

    lista= stergereRezervare("1", lista)
    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None


    lista = stergereRezervare("3", lista)
    assert len(lista) == 1
    assert getById("2", lista) is not None


def testModificaRezervare():
    lista = []
    lista = adaugaRezervare("1", "Ana", "business", 1400, "Da", lista)
    lista = adaugaRezervare("2", "Mara", "business", 800, "Nu", lista)

    lista = modificaRezervare("1", "Ana", "business", 1400, "Da", lista)

    rezervareUpdatata = getById("1", lista)
    assert getId(rezervareUpdatata) == "1"
    assert getNume(rezervareUpdatata) == "Ana"
    assert getClasa(rezervareUpdatata) == "business"
    assert getPret(rezervareUpdatata) == 1400
    assert getCheckin(rezervareUpdatata) == "Da"



    rezervareNeupdatata = getById("2", lista)
    assert getId(rezervareNeupdatata) == "2"
    assert getNume(rezervareNeupdatata) == "Mara"
    assert getClasa(rezervareNeupdatata) == "business"
    assert getPret(rezervareNeupdatata) == 800
    assert getCheckin(rezervareNeupdatata) == "Nu"


    lista = []
    lista = adaugaRezervare("1", "Ana", "business", 1400, "Da", lista)

    lista = modificaRezervare("3", "Mara", "business", 140, "Nu", lista)

    rezervareNeupdatata = getById("1", lista)
    assert getId(rezervareNeupdatata) == "1"
    assert getNume(rezervareNeupdatata) == "Ana"
    assert getClasa(rezervareNeupdatata) == "business"
    assert getPret(rezervareNeupdatata) == 1400
    assert getCheckin(rezervareNeupdatata) == "Da"
