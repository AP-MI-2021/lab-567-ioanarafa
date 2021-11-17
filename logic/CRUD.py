from Domain.rezervare import getId, creeazaRezervare


def adaugaRezervare (id, nume, clasa, pret, checkin, lista):
    '''

    :param id:
    :param nume:
    :param clasa:
    :param pret:
    :param checkin:
    :param lista:
    :return:
    '''

    rezervare = creeazaRezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]


def stergereRezervare(id, lista):
    '''
    sterge rezervarea dupa id-ul din lista
    :param id: id-ul rezervarii de sters, str
    :param lista:lista de rezervari
    :return: o lista continand rezervarile cu id-ul direrit de id
    '''

    return [rezervare for rezervare in lista if getId(rezervare) != id]


def modificaRezervare(id, nume, clasa, pret, checkin, lista):
    '''

    :param id:
    :param nume:
    :param clasa:
    :param pret:
    :param checkin:
    :param lista:
    :return:
    '''

    listaNoua = []
    for rezervare in lista:
        if getId(rezervare) == id:
            rezervareNoua = creeazaRezervare(id, nume, clasa, pret, checkin)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua


def getById(id, lista):
    '''

    :param id:
    :param lista:
    :return:
    '''

    for rezervare in lista:
        if getId(rezervare) == id:
            return rezervare
    return None