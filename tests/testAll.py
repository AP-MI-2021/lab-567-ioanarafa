from tests.testCRUD import testAdaugareRezervare, testStergereRezervare, testModificaRezervare
from tests.testDomeniu import testRezervare


def runAllTests():
    testRezervare()
    testAdaugareRezervare()
    testStergereRezervare()
    testModificaRezervare()