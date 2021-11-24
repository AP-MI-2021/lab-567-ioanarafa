from tests.testCRUD import testAdaugareRezervare, testStergereRezervare, testModificaRezervare
from tests.testDomeniu import testRezervare
from tests.testFunctionalitati import testTrecereaClasaSuperioaraDupaNume, testIeftinirePretRezervariDupaCheckin, \
    testOrdoneazaRezervarileDescrescDupaPret, testSumaPreturiPerNume


def runAllTests():
    testRezervare()
    testAdaugareRezervare()
    testStergereRezervare()
    testModificaRezervare()
    testTrecereaClasaSuperioaraDupaNume()
    testIeftinirePretRezervariDupaCheckin()
    testOrdoneazaRezervarileDescrescDupaPret()
    testSumaPreturiPerNume()
