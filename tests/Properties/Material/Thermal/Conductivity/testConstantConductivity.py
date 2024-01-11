import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestConstantConductivity(unittest.TestCase):
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
    def testConstantConductivityProperty(self):
        conductivity = self.material.Thermal.Conductivity
        conductivity.ConstantConductivity.setUnfrozenConductivity(836.5)
        conductivity.ConstantConductivity.setFrozenConductivity(2628.5)
        conductivity.ConstantConductivity.setFrozenTemperature(972.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        conductivity = self.material.Thermal.Conductivity
        self.assertEqual(conductivity.ConstantConductivity.getUnfrozenConductivity(), 836.5)
        self.assertEqual(conductivity.ConstantConductivity.getFrozenConductivity(), 2628.5)
        self.assertEqual(conductivity.ConstantConductivity.getFrozenTemperature(), 972.5)
