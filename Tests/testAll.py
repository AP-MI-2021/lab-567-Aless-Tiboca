from Tests.testDomain import testVanzare
from Tests.testCRUD import testCrud
from Tests.testFunct import testFunct
from Tests.testUndoRedo import testUndoRedo

def runAllTests():
    testVanzare()
    testFunct()
    testCrud()
    testUndoRedo()