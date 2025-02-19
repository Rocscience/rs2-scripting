import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestBaseMaterial(unittest.TestCase):
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
    def testBaseMaterialProperty(self):
        material = self.material
        material.setMaterialName("VYJpH")
        material.setMaterialColor(31891)
        material.setHatch(0)
        material.setHatchStyle(HatchStyle.HatchStyleVertical)
        material.setHatchColour(17887)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        material = self.material
        self.assertEqual(material.getMaterialName(), "VYJpH")
        self.assertEqual(material.getMaterialColor(), 31891)
        self.assertEqual(material.getHatch(), 0)
        self.assertEqual(material.getHatchStyle(), HatchStyle.HatchStyleVertical)
        self.assertEqual(material.getHatchColour(), 17887)
