import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.RS2Interpreter import RS2Interpreter
from rs2.PropertyEnums import*
import time

parentDirectoryHelper.addParentDirectoryToPath()

class TestModelerWithChanges(unittest.TestCase):
    pathToModelerExecutable = ""

    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        RS2Modeler.startApplication(60040, overridePathToExecutable=TestModelerWithChanges.pathToModelerExecutable)
        self.modeler = RS2Modeler(port=60040)
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
    def tearDown(self):
        self.model.close()
        self.modeler.closeProgram(False)
        self.model._client.closeConnection()
        time.sleep(5)
        os.remove(self.copiedModelPath)

    @unittest.skipIf(not pathToModelerExecutable, "requires path to debug build of RS2 Modeler")  
    def testModelerWithChangesSaved(self):
        bolt = self.bolt
        bolt.setBoltName("VYJpH")
        bolt.setBoltColor(31891)
        bolt.setBoltType(BoltTypes.FULLY_BONDED)
        self.modeler.closeProgram(True)
        self.model._client.closeConnection()
        time.sleep(5)
        RS2Modeler.startApplication(60040, overridePathToExecutable=TestModelerWithChanges.pathToModelerExecutable)
        self.modeler = RS2Modeler(port=60040)
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.getBoltName(), "VYJpH")
        self.assertEqual(bolt.getBoltColor(), 31891)
        self.assertEqual(bolt.getBoltType(), BoltTypes.FULLY_BONDED)

    @unittest.skipIf(not pathToModelerExecutable, "requires path to debug build of RS2 Modeler")  
    def testModelerWithChangesNotSaved(self):
        bolt = self.bolt
        bolt.setBoltType(BoltTypes.FULLY_BONDED)
        self.modeler.closeProgram(False)
        self.model._client.closeConnection()
        time.sleep(5)
        RS2Modeler.startApplication(60040, overridePathToExecutable=TestModelerWithChanges.pathToModelerExecutable)
        self.modeler = RS2Modeler(port=60040)
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertNotEqual(bolt.getBoltType(), BoltTypes.FULLY_BONDED)