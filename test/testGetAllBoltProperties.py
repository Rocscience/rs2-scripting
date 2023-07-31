import unittest
import os, sys, inspect
import shutil

#add parent directory to path
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from src.rs2.RS2Modeler import RS2Modeler
class TestGetAllBoltProperties(unittest.TestCase):
    def setUp(self):
        blankModelPath = f"{currentdir}/resources/blankProject.fez"
        self.copiedModelPath = f"{currentdir}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.boltList = self.model.getAllBoltProperties()

    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    
    def testBoltListSize(self):
        boltList = self.boltList
        self.assertEqual(len(boltList), 5)

    def testBoltListContents(self):
        boltList = self.boltList
        boltID = 1
        for bolt in boltList:
            self.assertEqual(bolt.getBoltName(), f"Bolt {boltID}")
            boltID+=1    

    def testGetSetBoltProperties(self):
        #These will change once bolt architecture is finalized
        boltList = self.boltList
        bolt = boltList[0]

        bolt.setBoltDiameter(22)
        self.assertEqual(bolt.getBoltDiameter(), 22)

        bolt.setBoltType(bolt.BoltTypes.END_ANCHORED)
        self.assertEqual(bolt.getBoltType(), bolt.BoltTypes.END_ANCHORED)


if __name__ == '__main__':
    unittest.main()