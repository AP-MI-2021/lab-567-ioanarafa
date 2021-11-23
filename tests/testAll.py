from tests.testCRUD import testAdaugareRezervare, testStergereRezervare, testModificaRezervare
from tests.testDomeniu import testRezervare
from tests.testFunctionalitati import testTrecereaClasaSuperioaraDupaNume, testIeftinirePretRezervariDupaCheckin, \
    testOrdoneazaRezervarileDescrescDupaPret, testSunaPreturiPerNume


def runAllTests():
    testRezervare()
    testAdaugareRezervare()
    testStergereRezervare()
    testModificaRezervare()
    testTrecereaClasaSuperioaraDupaNume()
    testIeftinirePretRezervariDupaCheckin()
    testOrdoneazaRezervarileDescrescDupaPret()
    testSunaPreturiPerNume()
