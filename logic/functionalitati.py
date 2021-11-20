from Domain.rezervare import getNume, getClasa, getId, creeazaRezervare, getPret, getCheckin


def trecereaClasaSuperioaraDupaNume(nume, lista):
    """
    Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.
    :param nume: numele citit
    :param lista: lista finala dupa schimbarea clasei
    :return:
    """
    listaNoua = []
    for rezervare in lista:
        if nume == getNume(rezervare) and getClasa(rezervare) == "economy":
            modificaRezervare = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                "economy plus",
                getPret(rezervare),
                getCheckin(rezervare)
            )
            listaNoua.append(modificaRezervare)
        elif nume == getNume(rezervare) and getClasa(rezervare) == "economy plus":
            modificaRezervare = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                "business",
                getPret(rezervare),
                getCheckin(rezervare)
            )
            listaNoua.append(modificaRezervare)
        else:
            listaNoua.append(rezervare)
    return listaNoua


def getByName(nume, lista):
    '''
    gaseste o rezervare cu numele dat intr-o lista
    :param nume: numele dat
    :param lista: lista de rezervari
    :return: rezervarea cu numele dat din lista sau None, daca aceasta nu exista
    '''
    for rezervare in lista:
        if getNume(rezervare) == nume:
            return rezervare
    return None


def ieftinirePretRezervariDupaCheckin(procentaj, lista):
    '''
    Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit.
    :param procentaj: procentajul scazut, int
    :param lista: lista initiala
    :return: lista finala dupa scaderea de procentaj
    '''
    listaNoua = []
    for rezervare in lista:
        if getCheckin(rezervare) == "Da":
            modificaRezervare = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                getClasa(rezervare),
                calculProcentajRedus(procentaj, getPret(rezervare)),
                getCheckin(rezervare)
            )
            listaNoua.append(modificaRezervare)
        else:
            listaNoua.append(rezervare)
    return listaNoua


def calculProcentajRedus(procentaj, pret):
    '''
    calculeaza ieftinirea  pretulul cu un procentaj dat
    :param procentaj: procentajul dat, int
    :param pret: pretul rezervarii
    :return: returneaza calculul ieftinirii pretului cu un procentaj dat
    '''
    return pret - (pret * (procentaj / 100))


def getByCheckin(lista):
    '''
     gaseste o rezervare dupa checkin in lista
    :param lista:lista de rezervari
    :return: rezervarea cu checkin-ul "Da" dintr-o lista
    '''

    for rezervare in lista:
        if getCheckin(rezervare) == "Da":
            return rezervare
    return None

def pretMaximRezervare(lista):
    '''
    Determinarea prețului maxim pentru fiecare clasă.
    :param lista: lista de rezervari
    :return: preturile maxime de la clase
    '''
    maxEconomy = -1
    maxEconomyPlus = -1
    maxBusiness = -1
    for rezervare in lista:
        if getClasa(rezervare) == "economy" and getPret(rezervare) >= maxEconomy:
            maxEconomy = getPret(rezervare)
        elif getClasa(rezervare) == "economy plus" and getPret(rezervare) >= maxEconomyPlus:
            maxEconomyPlus = getPret(rezervare)
        elif getClasa(rezervare) == "business" and getPret(rezervare) >= maxBusiness:
            maxBusiness = getPret(rezervare)

    if maxEconomy > -1:
        print("Pretul maxim la clasa economy este: " + str(maxEconomy))
    else:
        print("Nu sunt rezervari la clasa economy")
    if maxEconomyPlus > -1:
        print("Pretul maxim la clasa economy plus este: " + str(maxEconomyPlus))
    else:
        print("Nu sunt rezervari la clasa economy plus!")
    if maxBusiness > -1:
        print("Pretul maxim la clasa business este: " + str(maxBusiness))
    else:
        print("Nu sunt rezervari la clasa economy plus")

