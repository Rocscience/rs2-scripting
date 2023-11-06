import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.RS2Interpreter import RS2Interpreter
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestModelerWithChangesSaved(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        RS2Modeler.startApplication(60054, overridePathToExecutable=r"C:\RS2_dev\Build\Debug_x64\RS2.exe")
        self.modeler = RS2Modeler(port=60054)
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
    def tearDown(self):
        self.model.close()
        self.model._client.closeConnection()
        os.remove(self.copiedModelPath)
    def testModelerWithChangesSaved(self):
        bolt = self.bolt
        bolt.setBoltName("VYJpH")
        bolt.setBoltColor(31891)
        bolt.setBoltType(BoltTypes.FULLY_BONDED)
        self.modeler.closeProgram(True)
        self.model._client.closeConnection()
        RS2Modeler.startApplication(60050, overridePathToExecutable=r"C:\RS2_dev\Build\Debug_x64\RS2.exe")
        self.modeler = RS2Modeler(port=60050)
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        bolt = self.bolt
        self.assertEqual(bolt.getBoltName(), "VYJpH")
        self.assertEqual(bolt.getBoltColor(), 31891)
        self.assertEqual(bolt.getBoltType(), BoltTypes.FULLY_BONDED)

# class TestModelerWithChangesUnsaved(unittest.TestCase):
#     def setUp(self):
#         parentDirectory = parentDirectoryHelper.getParentDirectory()
#         blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
#         self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
#         shutil.copy(blankModelPath, self.copiedModelPath)
#         self.modeler = RS2Modeler()
#         self.model = self.modeler.openFile(self.copiedModelPath)
#         self.bolt = self.model.getAllBoltProperties()[0]
#     def tearDown(self):
#         self.model.close()
#         os.remove(self.copiedModelPath)
#     def testModelerWithChangesUnsaved(self):
#         bolt = self.bolt
#         bolt.setBoltName("VYJpH")
#         bolt.setBoltColor(31891)
#         bolt.setBoltType(BoltTypes.QUEENS_CABLE)
#         self.modeler.closeProgram(False)
#         self.model = self.modeler.openFile(self.copiedModelPath)
#         self.bolt = self.model.getAllBoltProperties()[0]
#         bolt = self.bolt
#         self.assertNotEqual(bolt.getBoltName(), "VYJpH")
#         self.assertNotEqual(bolt.getBoltColor(), 31891)
#         self.assertNotEqual(bolt.getBoltType(), BoltTypes.QUEENS_CABLE)
