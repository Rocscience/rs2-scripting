import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper

parentDirectoryHelper.addParentDirectoryToPath()

from rs2.modeler.RS2Modeler import RS2Modeler
class TestGetAllBoltProperties(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.boltList = self.model.getAllBoltProperties()

    def tearDown(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)
    
    def testBoltListSize(self):
        boltList = self.boltList
        self.assertEqual(len(boltList), 5)

    def testBoltListOrder(self):
        boltList = self.boltList
        for boltID, bolt in enumerate(boltList, start=1):
            self.assertEqual(bolt.getBoltName(), f"Bolt {boltID}") 