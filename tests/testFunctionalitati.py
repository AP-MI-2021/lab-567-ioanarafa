from Domain.rezervare import getId, getNume, getClasa, getPret, getCheckin
from logic.CRUD import adaugaRezervare
from logic.functionalitati import trecereaClasaSuperioaraDupaNume, getByName, ieftinirePretRezervariDupaCheckin, \
    getByCheckin, ordoneazaRezervarileDescrescDupaPret, sumaPreturiPerNume


def testTrecereaClasaSuperioaraDupaNume():
    lista = []
    lista = adaugaRezervare("1", "Ana", "economy", 1400, "da", [])
    lista = adaugaRezervare("2", "Mara", "business", 360, "nu", lista)

    lista = trecereaClasaSuperioaraDupaNume("Ana", lista)
    rezervareUpdatata = getByName("Ana", lista)
    assert getId(rezervareUpdatata) == "1"
    assert getNume(rezervareUpdatata) == "Ana"
    assert getClasa(rezervareUpdatata) == "economy plus"
    assert getPret(rezervareUpdatata) == 1400
    assert getCheckin(rezervareUpdatata) == "da"


def testIeftinirePretRezervariDupaCheckin():
    lista = []
    lista = adaugaRezervare("1", "Ana", "economy", 1400, "da", [])
    lista = adaugaRezervare("2", "Mara", "business", 360, "nu", lista)

    lista = ieftinirePretRezervariDupaCheckin(42, lista)
    rezervareUpdatata = getByCheckin(lista)
    assert getId(rezervareUpdatata) == "1"
    assert getNume(rezervareUpdatata) == "Ana"
    assert getClasa(rezervareUpdatata) == "economy"
    assert getPret(rezervareUpdatata) == 812
    assert getCheckin(rezervareUpdatata) == "da"


def testOrdoneazaRezervarileDescrescDupaPret():
    lista = []
    lista = adaugaRezervare("1", "Ana", "economy", 140, "da", lista)
    lista = adaugaRezervare("2", "Mara", "business", 360, "nu", lista)
    lista = adaugaRezervare("3", "Ana", "economy", 1400, "da", lista)
    lista = adaugaRezervare("4", "Mara", "business", 90, "nu", lista)
    rezultat = ordoneazaRezervarileDescrescDupaPret(lista)
    assert getId(rezultat[0]) == "3"
    assert getId(rezultat[1]) == "2"
    assert getId(rezultat[2]) == "1"
    assert getId(rezultat[3]) == "4"


def testSumaPreturiPerNume():
    lista = []
    lista = adaugaRezervare("1", "Ana", "economy", 140, "da", lista)
    lista = adaugaRezervare("2", "Mara", "business", 360, "nu", lista)
    lista = adaugaRezervare("3", "Ana", "economy", 1400, "da", lista)
    rezultat = sumaPreturiPerNume(lista)
    assert len(rezultat) == 2
    assert rezultat["Ana"] == 1540
    assert rezultat["Mara"] == 360
