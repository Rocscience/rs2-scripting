import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestCloseProgram(unittest.TestCase):
    pathToModelerExecutable = ""
    modelerPortToUse = 60040

    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        RS2Modeler.startApplication(port=TestCloseProgram.modelerPortToUse, overridePathToExecutable=TestCloseProgram.pathToModelerExecutable)
        self.modeler = RS2Modeler(port=TestCloseProgram.modelerPortToUse)
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        
    def tearDown(self):
        os.remove(self.copiedModelPath)
        self.modeler.closeProgram(False)

    @unittest.skipIf(not pathToModelerExecutable, "requires path to debug build of RS2 Modeler")  
    def testCloseModelerWithChangesSaved(self):
        bolt = self.bolt
        bolt.setBoltName("VYJpH")
        bolt.setBoltColor(31891)
        bolt.setBoltType(BoltTypes.FULLY_BONDED)
        self.modeler.closeProgram(True)
        RS2Modeler.startApplication(port=TestCloseProgram.modelerPortToUse, overridePathToExecutable=TestCloseProgram.pathToModelerExecutable)
        self.modeler = RS2Modeler(port=TestCloseProgram.modelerPortToUse)
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.getBoltName(), "VYJpH")
        self.assertEqual(bolt.getBoltColor(), 31891)
        self.assertEqual(bolt.getBoltType(), BoltTypes.FULLY_BONDED)

    @unittest.skipIf(not pathToModelerExecutable, "requires path to debug build of RS2 Modeler")  
    def testCloseModelerWithChangesNotSaved(self):
        bolt = self.bolt
        bolt.setBoltType(BoltTypes.FULLY_BONDED)
        self.modeler.closeProgram(False)
        RS2Modeler.startApplication(port=TestCloseProgram.modelerPortToUse, overridePathToExecutable=TestCloseProgram.pathToModelerExecutable)
        self.modeler = RS2Modeler(port=TestCloseProgram.modelerPortToUse)
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertNotEqual(bolt.getBoltType(), BoltTypes.FULLY_BONDED)

    @unittest.skipIf(not pathToModelerExecutable, "requires path to debug build of RS2 Modeler")  
    def testPortAvailabilityAfterCloseModeler(self):
        self.modeler.closeProgram(False)
        RS2Modeler.startApplication(port=TestCloseProgram.modelerPortToUse, overridePathToExecutable=TestCloseProgram.pathToModelerExecutable)
        self.modeler = RS2Modeler(port=TestCloseProgram.modelerPortToUse)
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.modeler.closeProgram(False)

        RS2Modeler.startApplication(port=TestCloseProgram.modelerPortToUse, overridePathToExecutable=TestCloseProgram.pathToModelerExecutable)
        self.modeler = RS2Modeler(port=TestCloseProgram.modelerPortToUse)
        self.model = self.modeler.openFile(self.copiedModelPath)