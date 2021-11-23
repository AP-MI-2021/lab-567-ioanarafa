from Domain.rezervare import toString
from logic.CRUD import adaugaRezervare, stergereRezervare, modificaRezervare
from logic.functionalitati import trecereaClasaSuperioaraDupaNume, ieftinirePretRezervariDupaCheckin, \
    pretMaximRezervare, ordoneazaRezervarileDescrescDupaPret, sunaPreturiPerNume


def printMenu():
    print("1. Adauga rezervare")
    print("2. Sterge rezervare")
    print("3. Modifica rezervarea")
    print("4. Trece toate rezervările făcute pe un nume citit la o clasă superioară.")
    print("5. Ieftineste toate rezervările la care s-a făcut checkin cu un procentaj citit.")
    print("6. Determina prețul maxim pentru fiecare clasă.")
    print("7. Ordoneaza rezervările descrescător după preț.")
    print("8. Afișaza sumele prețurilor pentru fiecare nume")
    print("a. Afiseaza toate rezervariile")
    print("x. Iesire")


def uiAdaugaRezervare(lista):
    try:
        id= input("Dati id-ul: ")
        nume= input("Dati numele: ")
        clasa= input("Dati clasa (`economy`, `economy plus`, `business`): ")
        pret= float(input("Dati pret-ul: "))
        checkin= input("Dati checkin-ul făcut (`da` / `nu`): ")
        return adaugaRezervare( id, nume, clasa, pret, checkin, lista)
    except ValueError as ve :
        print("Eroarea: ",ve)
        return lista


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

def uiIeftinirePretRezervariDupaCheckin(lista):
    procentaj = int(input("Dati procentajul:"))
    return ieftinirePretRezervariDupaCheckin (procentaj, lista)

def uiPretMaximRezervare(lista):
    rezultat = pretMaximRezervare(lista)
    return rezultat

def uiOrdoneazaRezervarileDescrescDupaPret(lista):
    rezultat = ordoneazaRezervarileDescrescDupaPret(lista)
    showAll(rezultat)

def uiSunaPreturiPerNume(lista):
    rezultat = sunaPreturiPerNume(lista)
    for nume in rezultat:
        print("Pentru numele {} suma preturilor este: {}".format(nume, rezultat[nume]))

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
        elif optiune == "5":
            lista = uiIeftinirePretRezervariDupaCheckin(lista)
        elif optiune == "6":
            uiPretMaximRezervare(lista)
        elif optiune == "7":
            uiOrdoneazaRezervarileDescrescDupaPret(lista)
        elif optiune == "8":
            uiSunaPreturiPerNume(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati")


