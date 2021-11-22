from Domain.rezervare import getId, getNume, getClasa, getPret, getCheckin
from logic.CRUD import adaugaRezervare
from logic.functionalitati import trecereaClasaSuperioaraDupaNume, getByName, ieftinirePretRezervariDupaCheckin, \
    getByCheckin, ordoneazaRezervarileDescrescDupaPret


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


def testIeftinirePretRezervariDupaCheckin():
    lista = []
    lista = adaugaRezervare("1", "Ana", "economy", 1400, "Da", [])
    lista = adaugaRezervare("2", "Mara", "business", 360, "Nu", lista)

    lista = ieftinirePretRezervariDupaCheckin(42, lista)
    rezervareUpdatata = getByCheckin(lista)
    assert getId(rezervareUpdatata) == "1"
    assert getNume(rezervareUpdatata) == "Ana"
    assert getClasa(rezervareUpdatata) == "economy"
    assert getPret(rezervareUpdatata) == 812
    assert getCheckin(rezervareUpdatata) == "Da"


def testOrdoneazaRezervarileDescrescDupaPret():
    lista = []
    lista = adaugaRezervare("1", "Ana", "economy", 140, "Da", lista)
    lista = adaugaRezervare("2", "Mara", "business", 360, "Nu", lista)
    lista = adaugaRezervare("3", "Ana", "economy", 1400, "Da", lista)
    lista = adaugaRezervare("4", "Mara", "business", 90, "Nu", lista)
    rezultat = ordoneazaRezervarileDescrescDupaPret(lista)
    assert getId(rezultat[0]) == "3"
    assert getId(rezultat[1]) == "2"
    assert getId(rezultat[2]) == "1"
    assert getId(rezultat[3]) == "4"
