import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestHydraulic(unittest.TestCase):
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
    def testHydraulicProperty(self):
        material = self.material
        material.Hydraulic.setMaterialBehaviour(MaterialBehaviours.UNDRAINED)
        material.Hydraulic.setFluidBulkModulus(836.5)
        material.Hydraulic.setUseBiotsCoefficientForCalculatingEffectiveStress(0)
        material.Hydraulic.setAccountForWaterContentInCompressibility(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        material = self.material
        self.assertEqual(material.Hydraulic.getMaterialBehaviour(), MaterialBehaviours.UNDRAINED)
        self.assertEqual(material.Hydraulic.getFluidBulkModulus(), 836.5)
        self.assertEqual(material.Hydraulic.getUseBiotsCoefficientForCalculatingEffectiveStress(), 0)
        self.assertEqual(material.Hydraulic.getAccountForWaterContentInCompressibility(), 0)
