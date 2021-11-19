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
    return


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
