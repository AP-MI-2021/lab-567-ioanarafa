from Domain.rezervare import toString
from logic.CRUD import adaugaRezervare, stergereRezervare, modificaRezervare
from logic.functionalitati import trecereaClasaSuperioaraDupaNume


def printMenu():
    print("1. Adauga rezervare")
    print("2. Sterge rezervare")
    print("3. Modifica rezervarea")
    print("4. Trece toate rezervările făcute pe un nume citit la o clasă superioară.")
    print("a. Afiseaza toate rezervariile")
    print("x. Iesire")


def uiAdaugaRezervare(lista):
    id= input("Dati id-ul: ")
    nume= input("Dati numele: ")
    clasa= input("Dati clasa (`economy`, `economy plus`, `business`): ")
    pret= float(input("Dati pret-ul: "))
    checkin= input("Dati checkin-ul făcut (`da` / `nu`): ")
    return adaugaRezervare( id, nume, clasa, pret, checkin, lista)


def uiStergereRezervare(lista):
    id= input("Dati id-ul rezervarii de sters: ")
    return stergereRezervare(id, lista)


def uiModificaRezervare(lista):

    id = input("Dati id-ul rezervarii de moduficat: ")
    nume= input("Dati noul numele: ")
    clasa = input("Dati noua clasa (`economy`, `economy plus`, `business`): ")
    pret = float(input("Dati noul pret: "))
    checkin = input("Dati noul checkin făcut (`da` / `nu`): ")
    return modificaRezervare(id, nume, clasa, pret, checkin, lista)

def uiTrecereaClasaSuperioaraDupaNume(lista):
    nume = input("Dati numele: ")
    return trecereaClasaSuperioaraDupaNume(nume, lista)


def showAll(lista):
    for rezervare in lista:
        print (toString(rezervare))


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
           lista = uiAdaugaRezervare(lista)
        elif optiune == "2":
            lista = uiStergereRezervare(lista)
        elif optiune == "3":
            lista = uiModificaRezervare(lista)
        elif optiune == "4":
            lista = uiTrecereaClasaSuperioaraDupaNume(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati")


