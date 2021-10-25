from Tests.testDomain import testVanzare
from Tests.testCRUD import testAdaugaComanda, testModifComanda, testSterge

def runAllTests():
    testVanzare()
    testAdaugaComanda()
    testModifComanda()
    testSterge()