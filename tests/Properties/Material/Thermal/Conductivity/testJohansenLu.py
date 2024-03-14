import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestJohansenLu(unittest.TestCase):
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
        os.remove(self.copiedModelPath)
    def testJohansenLuProperty(self):
        conductivity = self.material.Thermal.Conductivity
        conductivity.JohansenLu.setSoilType(ThermalSoilType.COARSE)
        conductivity.JohansenLu.setQuartzContent(836.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        conductivity = self.material.Thermal.Conductivity
        self.assertEqual(conductivity.JohansenLu.getSoilType(), ThermalSoilType.COARSE)
        self.assertEqual(conductivity.JohansenLu.getQuartzContent(), 836.5)
