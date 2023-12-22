import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestDoubleYield(unittest.TestCase):
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
    def testDoubleYieldProperty(self):
        stiffness = self.material.Stiffness
        stiffness.DoubleYield.setKRefiso(836.5)
        stiffness.DoubleYield.setMK(2628.5)
        stiffness.DoubleYield.setRK(972.5)
        stiffness.DoubleYield.setReferencePressure(86.7)
        stiffness.DoubleYield.setPoissonsRatio(762.9)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        stiffness = self.material.Stiffness
        self.assertEqual(stiffness.DoubleYield.getKRefiso(), 836.5)
        self.assertEqual(stiffness.DoubleYield.getMK(), 2628.5)
        self.assertEqual(stiffness.DoubleYield.getRK(), 972.5)
        self.assertEqual(stiffness.DoubleYield.getReferencePressure(), 86.7)
        self.assertEqual(stiffness.DoubleYield.getPoissonsRatio(), 762.9)
