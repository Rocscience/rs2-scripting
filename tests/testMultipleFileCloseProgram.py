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
    pathToModelerExecutable = "C:\RS2_dev\Build\Debug_x64\RS2.exe"

    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath1 = f"{parentDirectory}/resources/testProject1.fez"
        self.copiedModelPath2 = f"{parentDirectory}/resources/testProject2.fez"
        shutil.copy(blankModelPath, self.copiedModelPath1)
        shutil.copy(blankModelPath, self.copiedModelPath2)
        RS2Modeler.startApplication(60040, overridePathToExecutable=TestModelerWithChanges.pathToModelerExecutable)
        self.modeler = RS2Modeler(port=60040)
        self.model1 = self.modeler.openFile(self.copiedModelPath1)
        self.model2 = self.modeler.openFile(self.copiedModelPath2)
        self.bolt = self.model1.getAllBoltProperties()[0]
        self.joint = self.model2.getAllJointProperties()[0]
    def tearDown(self):
        self.model1.close()
        self.model2.close()
        self.modeler.closeProgram(False)
        self.model1._client.closeConnection()
        time.sleep(8)
        os.remove(self.copiedModelPath1)
        os.remove(self.copiedModelPath2)

    @unittest.skipIf(not pathToModelerExecutable, "requires path to debug build of RS2 Modeler")  
    def testModelerWithMultipleFileChangesSaved(self):
        bolt = self.bolt
        joint = self.joint
        bolt.setBoltName("VYJpH")
        bolt.setBoltColor(31891)
        bolt.setBoltType(BoltTypes.FULLY_BONDED)
        joint.setJointName("XQYpd")
        joint.setJointColor(31891)
        self.modeler.closeProgram(True)
        self.model1._client.closeConnection()
        time.sleep(8)
        RS2Modeler.startApplication(60040, overridePathToExecutable=TestModelerWithChanges.pathToModelerExecutable)
        self.modeler = RS2Modeler(port=60040)
        self.model1 = self.modeler.openFile(self.copiedModelPath1)
        self.model2 = self.modeler.openFile(self.copiedModelPath2)
        self.bolt = self.model1.getAllBoltProperties()[0]
        self.joint = self.model2.getAllJointProperties()[0]
        bolt = self.bolt
        joint = self.joint
        self.assertEqual(bolt.getBoltName(), "VYJpH")
        self.assertEqual(bolt.getBoltColor(), 31891)
        self.assertEqual(bolt.getBoltType(), BoltTypes.FULLY_BONDED)
        self.assertEqual(joint.getJointName(), "XQYpd")
        self.assertEqual(joint.getJointColor(), 31891)

    @unittest.skipIf(not pathToModelerExecutable, "requires path to debug build of RS2 Modeler")  
    def testModelerWithMultipleFileChangesNotSaved(self):
        bolt = self.bolt
        joint = self.joint
        bolt.setBoltType(BoltTypes.FULLY_BONDED)
        joint.setJointName("XQYpd")
        self.modeler.closeProgram(False)
        self.model1._client.closeConnection()
        time.sleep(8)
        RS2Modeler.startApplication(60040, overridePathToExecutable=TestModelerWithChanges.pathToModelerExecutable)
        self.modeler = RS2Modeler(port=60040)
        self.model1 = self.modeler.openFile(self.copiedModelPath1)
        self.model2 = self.modeler.openFile(self.copiedModelPath2)
        self.bolt = self.model1.getAllBoltProperties()[0]
        self.joint = self.model2.getAllJointProperties()[0]
        bolt = self.bolt
        joint = self.joint
        self.assertNotEqual(bolt.getBoltType(), BoltTypes.FULLY_BONDED)
        self.assertNotEqual(joint.getJointName(), "XQYpd")