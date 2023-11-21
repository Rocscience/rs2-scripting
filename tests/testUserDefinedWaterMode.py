import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestUserDefinedWaterMode(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)

    @classmethod
    def tearDownClass(self):
        self.model.close()
        os.remove(self.copiedModelPath)

    def testGetNonExistant(self):
        model = self.model

        with self.assertRaises(Exception):
            model.getUserDefinedWaterMode("testUserDefinedWaterMode")

    def testCreateDeleteUserDefinedWaterMode(self):
        model = self.model

        with self.assertRaises(Exception):
            model.getUserDefinedWaterMode("testUserDefinedWaterMode")

        model.createUserDefinedWaterMode("testUserDefinedWaterMode")
        model.getUserDefinedWaterMode("testUserDefinedWaterMode")
        model.deleteUserDefinedWaterMode("testUserDefinedWaterMode")

        with self.assertRaises(Exception):
            model.getUserDefinedWaterMode("testUserDefinedWaterMode")

    def testCreateFailureDuplicate(self):
        model = self.model

        model.createUserDefinedWaterMode("testUserDefinedWaterMode")
        with self.assertRaises(Exception):
            model.createUserDefinedWaterMode("testUserDefinedWaterMode")
        model.deleteUserDefinedWaterMode("testUserDefinedWaterMode")

    def testDeleteFailureNonexistant(self):
        model = self.model

        with self.assertRaises(Exception):
            model.deleteUserDefinedWaterMode("testUserDefinedWaterMode")

    def testDeleteFailureUsedByMaterial(self):
        #TODO: once you are able to assign a user defined water content mode to a material, test that here
        pass

    def testGetSetWaterContentFunction(self):
        model = self.model

        model.createUserDefinedWaterMode("testUserDefinedWaterMode")
        userDefinedWaterMode = model.getUserDefinedWaterMode("testUserDefinedWaterMode")

        userDefinedWaterMode.setWaterContentFunction([(1, 0.1), (2, 0.2)])
        self.assertEqual(userDefinedWaterMode.getWaterContentFunction(), [(1, 0.1), (2, 0.2)])

        model.deleteUserDefinedWaterMode("testUserDefinedWaterMode")

    def testGetSetDegreeOfSaturationFunction(self):
        model = self.model

        model.createUserDefinedWaterMode("testUserDefinedWaterMode")
        userDefinedWaterMode = model.getUserDefinedWaterMode("testUserDefinedWaterMode")

        userDefinedWaterMode.setDegreeOfSaturationFunction([(1, 0.1), (2, 0.2)])
        self.assertEqual(userDefinedWaterMode.getDegreeOfSaturationFunction(), [(1, 0.1), (2, 0.2)])

        model.deleteUserDefinedWaterMode("testUserDefinedWaterMode")

    def testGetSetStrengthFunction(self):
        model = self.model

        model.createUserDefinedWaterMode("testUserDefinedWaterMode")
        userDefinedWaterMode = model.getUserDefinedWaterMode("testUserDefinedWaterMode")

        userDefinedWaterMode.setStrengthFunction([(1, 0.1), (2, 0.2)])
        self.assertEqual(userDefinedWaterMode.getStrengthFunction(), [(1, 0.1), (2, 0.2)])

        model.deleteUserDefinedWaterMode("testUserDefinedWaterMode")