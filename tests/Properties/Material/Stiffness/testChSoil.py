import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestChSoil(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
    def tearDown(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)
    def testChSoilProperty(self):
        stiffness = self.material.Stiffness
        stiffness.ChSoil.setGRef(836.5)
        stiffness.ChSoil.setNG(2628.5)
        stiffness.ChSoil.setKRef(972.5)
        stiffness.ChSoil.setMK(86.7)
        stiffness.ChSoil.setReferencePressure(762.9)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        stiffness = self.material.Stiffness
        self.assertEqual(stiffness.ChSoil.getGRef(), 836.5)
        self.assertEqual(stiffness.ChSoil.getNG(), 2628.5)
        self.assertEqual(stiffness.ChSoil.getKRef(), 972.5)
        self.assertEqual(stiffness.ChSoil.getMK(), 86.7)
        self.assertEqual(stiffness.ChSoil.getReferencePressure(), 762.9)
