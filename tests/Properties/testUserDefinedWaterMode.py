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
        blankModelPath = f"{parentDirectory}/resources/starterProjectTransientGroundwater.fez"
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
            model.getUserDefinedPermeabilityAndWaterContentMode("testUserDefinedWaterMode")

    def testCreateDeleteUserDefinedWaterMode(self):
        model = self.model

        with self.assertRaises(Exception):
            model.getUserDefinedPermeabilityAndWaterContentMode("testUserDefinedWaterMode")

        model.createUserDefinedPermeabilityAndWaterContentMode("testUserDefinedWaterMode")
        model.getUserDefinedPermeabilityAndWaterContentMode("testUserDefinedWaterMode")
        model.deleteUserDefinedPermeabilityAndWaterContentMode("testUserDefinedWaterMode")

        with self.assertRaises(Exception):
            model.getUserDefinedPermeabilityAndWaterContentMode("testUserDefinedWaterMode")

    def testCreateFailureDuplicate(self):
        model = self.model

        model.createUserDefinedPermeabilityAndWaterContentMode("testUserDefinedWaterMode")
        with self.assertRaises(Exception):
            model.createUserDefinedPermeabilityAndWaterContentMode("testUserDefinedWaterMode")
        model.deleteUserDefinedPermeabilityAndWaterContentMode("testUserDefinedWaterMode")

    def testDeleteFailureNonexistant(self):
        model = self.model

        with self.assertRaises(Exception):
            model.deleteUserDefinedPermeabilityAndWaterContentMode("testUserDefinedWaterMode")

    def testDeleteFailureUsedByMaterial(self):
        #TODO: once you are able to assign a user defined water content mode to a material, test that here
        pass

    def testGetSetWaterContentFunction(self):
        model = self.model

        model.createUserDefinedPermeabilityAndWaterContentMode("testUserDefinedWaterMode")
        userDefinedWaterMode = model.getUserDefinedPermeabilityAndWaterContentMode("testUserDefinedWaterMode")

        userDefinedWaterMode.setWaterContentFunction([(1, 0.1), (2, 0.2)])
        self.assertEqual(userDefinedWaterMode.getWaterContentFunction(), [(1, 0.1), (2, 0.2)])

        model.deleteUserDefinedPermeabilityAndWaterContentMode("testUserDefinedWaterMode")

    def testGetSetDegreeOfSaturationFunction(self):
        model = self.model

        userDefinedWaterMode = model.createUserDefinedPermeabilityAndWaterContentMode("testUserDefinedWaterMode")

        userDefinedWaterMode.setDegreeOfSaturationFunction([(1, 0.1), (2, 0.2)])
        self.assertEqual(userDefinedWaterMode.getDegreeOfSaturationFunction(), [(1, 0.1), (2, 0.2)])

        model.deleteUserDefinedPermeabilityAndWaterContentMode("testUserDefinedWaterMode")

    def testGetSetStrengthFunction(self):
        model = self.model

        model.createUserDefinedPermeabilityAndWaterContentMode("testUserDefinedWaterMode")
        userDefinedWaterMode = model.getUserDefinedPermeabilityAndWaterContentMode("testUserDefinedWaterMode")

        userDefinedWaterMode.setPermeabilityFunction([(1, 0.1), (2, 0.2)])
        self.assertEqual(userDefinedWaterMode.getPermeabilityFunction(), [(1, 0.1), (2, 0.2)])

        model.deleteUserDefinedPermeabilityAndWaterContentMode("testUserDefinedWaterMode")