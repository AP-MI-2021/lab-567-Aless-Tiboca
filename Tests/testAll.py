from Tests.testDomain import testVanzare
from Tests.testCRUD import testAdaugaComanda, testGetById, testModifComanda, testSterge

def runAllTests():
    testVanzare()
    testAdaugaComanda()
    testModifComanda()
    testSterge()
    testGetById()