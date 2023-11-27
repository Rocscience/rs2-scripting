import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestNorsand(unittest.TestCase):
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
    def testNorsandProperty(self):
        stiffness = self.material.Stiffness
        stiffness.Norsand.setShearModulusAtReferencePressure(836.5)
        stiffness.Norsand.setReferencePressureForShearModulus(2628.5)
        stiffness.Norsand.setModulusExponent(972.5)
        stiffness.Norsand.setPoissonsRatio(86.7)
        stiffness.Norsand.setMinimumShearModulus(762.9)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        stiffness = self.material.Stiffness
        self.assertEqual(stiffness.Norsand.getShearModulusAtReferencePressure(), 836.5)
        self.assertEqual(stiffness.Norsand.getReferencePressureForShearModulus(), 2628.5)
        self.assertEqual(stiffness.Norsand.getModulusExponent(), 972.5)
        self.assertEqual(stiffness.Norsand.getPoissonsRatio(), 86.7)
        self.assertEqual(stiffness.Norsand.getMinimumShearModulus(), 762.9)
