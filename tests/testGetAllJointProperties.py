import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper

parentDirectoryHelper.addParentDirectoryToPath()

from src.rs2.RS2Modeler import RS2Modeler
class TestGetAllJointProperties(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/blankProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.jointList = self.model.getAllJointProperties()

    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    
    def testJointListSize(self):
        jointList = self.jointList
        self.assertEqual(len(jointList), 5)

    def testJointListOrder(self):
        jointList = self.jointList
        for jointID, joint in enumerate(jointList, start=1):
            self.assertEqual(joint.getJointName(), f"Joint {jointID}") 