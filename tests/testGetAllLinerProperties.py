import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper

parentDirectoryHelper.addParentDirectoryToPath()

from src.rs2.RS2Modeler import RS2Modeler
class TestGetAllBoltProperties(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/blankProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
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

    def testLinerListOrder(self):
        linerList = self.linerList
        for linerID, liner in enumerate(linerList, start=1):
            self.assertEqual(liner.getLinerName(), f"Liner {linerID}") 

if __name__ == '__main__':
    unittest.main()