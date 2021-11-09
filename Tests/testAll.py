from Tests.testDomain import testVanzare
from Tests.testCRUD import testCrud
from Tests.testFunct import testFunct

def runAllTests():
    testVanzare()
    testFunct()
    testCrud()