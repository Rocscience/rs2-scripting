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
        self.linerList = self.model.getAllLinerProperties()

    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    
    def testLinerListSize(self):
        linerList = self.linerList
        self.assertEqual(len(linerList), 5)

    def testLinerListContents(self):
        linerList = self.linerList
        linerID = 1
        for liner in linerList:
            self.assertEqual(liner.getLinerName(), f"Liner {linerID}")
            linerID+=1    

    def testGetSetLinerProperties(self):
		#These will change once liner architecture is finalized
        linerList = self.linerList
        liner = linerList[0]
        
        liner.setThickness(50)
        self.assertEqual(liner.getThickness(), 50)
        
        liner.setLinerType(liner.LinerTypes.P2_LINER_STANDARD_BEAM)
        self.assertEqual(liner.getLinerType(), liner.LinerTypes.P2_LINER_STANDARD_BEAM)


if __name__ == '__main__':
    unittest.main()