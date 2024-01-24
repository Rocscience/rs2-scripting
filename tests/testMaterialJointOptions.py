import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestMaterialJointOptions(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.mat = self.model.getAllMaterialProperties()[0]
        self.matJointOptions = self.mat.Strength.JointedMohrCoulomb.getJointOptions()
    @classmethod
    def tearDownClass(self):
        self.model.close()
        os.remove(self.copiedModelPath)

    def testNumberOfJointsSuccess(self):
        self.matJointOptions.setNumberOfJoints(1)
        self.assertEqual(self.matJointOptions.getNumberOfJoints(), 1)

        self.matJointOptions.setNumberOfJoints(2)
        self.assertEqual(self.matJointOptions.getNumberOfJoints(), 2)

        self.matJointOptions.setNumberOfJoints(3)
        self.assertEqual(self.matJointOptions.getNumberOfJoints(), 3)

    def testNumberOfJointsFailure(self):
        with self.assertRaises(Exception):
            self.matJointOptions.setNumberOfJoints(0)
        with self.assertRaises(Exception):
            self.matJointOptions.setNumberOfJoints(4)
    
    def testSetInclination(self):
        self.matJointOptions.setNumberOfJoints(1)
        self.matJointOptions.setInclination(0, 0.1)

        self.assertEqual(self.matJointOptions.getNumberOfJoints(), 1)
        self.assertEqual(self.matJointOptions.getInclination(0), 0.1)


    def testSetTracePlane(self):
        self.matJointOptions.setNumberOfJoints(1)
        self.assertEqual(self.matJointOptions.getNumberOfJoints(), 1)

        self.matJointOptions.setUseTracePlane(0, True)
        self.assertEqual(self.matJointOptions.getUseTracePlane(0), True)

        self.matJointOptions.setTracePlaneProperties(0, 0.1, 0.2, 0.3)
        self.assertEqual(self.matJointOptions.getTracePlaneProperties(0), (0.1, 0.2, 0.3))