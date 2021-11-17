from Domain.rezervare import creeazaRezervare, getId, getNume, getClasa, getPret, getCheckin


def testRezervare():
    rezervare= creeazaRezervare("1", "Rafa", "economy plus", 400, "da")
    assert getId(rezervare) == "1"
    assert getNume(rezervare) == "Rafa"
    assert getClasa(rezervare) == "economy plus"
    assert getPret(rezervare) == 400
    assert getCheckin(rezervare) == "da"