from Tests.testDomain import testVanzare
from Tests.testCRUD import testAdaugaComanda, testGetById, testModifComanda, testSterge
from Tests.testFunct import testFunct

def runAllTests():
    testVanzare()
    testAdaugaComanda()
    testModifComanda()
    testSterge()
    testGetById()
    testFunct()