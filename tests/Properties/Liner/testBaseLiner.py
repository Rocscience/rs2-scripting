import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestBaseLiner(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
    def tearDown(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)
    def testBaseLinerProperty(self):
        liner = self.liner
        liner.setLinerName("VYJpH")
        liner.setLinerColor(31891)
        liner.setLinerType(LinerTypes.REINFORCED_CONCRETE)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.getLinerName(), "VYJpH")
        self.assertEqual(liner.getLinerColor(), 31891)
        self.assertEqual(liner.getLinerType(), LinerTypes.REINFORCED_CONCRETE)
