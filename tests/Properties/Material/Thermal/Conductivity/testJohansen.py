import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestJohansen(unittest.TestCase):
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
    def testJohansenProperty(self):
        conductivity = self.material.Thermal.Conductivity
        conductivity.Johansen.setSoilType(ThermalSoilType.COARSE)
        conductivity.Johansen.setQuartzContent(836.5)
        conductivity.Johansen.setDryConductivity(2628.5)
        conductivity.Johansen.setSaturatedUnfrozenConductivity(972.5)
        conductivity.Johansen.setSaturatedFrozenConductivity(86.7)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        conductivity = self.material.Thermal.Conductivity
        self.assertEqual(conductivity.Johansen.getSoilType(), ThermalSoilType.COARSE)
        self.assertEqual(conductivity.Johansen.getQuartzContent(), 836.5)
        self.assertEqual(conductivity.Johansen.getDryConductivity(), 2628.5)
        self.assertEqual(conductivity.Johansen.getSaturatedUnfrozenConductivity(), 972.5)
        self.assertEqual(conductivity.Johansen.getSaturatedFrozenConductivity(), 86.7)
