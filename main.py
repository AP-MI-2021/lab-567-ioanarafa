from UI.console import runMenu
from logic.CRUD import adaugaRezervare
from tests.testAll import runAllTests


def main():
    runAllTests()
    lista = []
    lista = adaugaRezervare("1", "Luisa", "business", 200, "Nu", lista)
    lista = adaugaRezervare("2", "Ioana", "economy", 1400, "Da", lista)
    lista = adaugaRezervare("3", "Luisa", "business", 100, "Nu", lista)
    lista = adaugaRezervare("4", "Mara", "economy", 1400, "Da", lista)
    lista = adaugaRezervare("5", "Carla", "business", 2300, "Nu", lista)
    lista = adaugaRezervare("6", "Ioana", "economy", 140, "Da", lista)
    runMenu(lista)

main()
