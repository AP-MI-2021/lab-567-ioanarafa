from UI.console import runMenu
from logic.CRUD import adaugaRezervare
from tests.testAll import runAllTests


def main():
    runAllTests()
    lista = []
    lista = adaugaRezervare("1", "Luisa", "business", 200, "Nu", lista)
    lista = adaugaRezervare("2", "Ioana", "economy", 340, "Da", lista)
    runMenu(lista)


main()
