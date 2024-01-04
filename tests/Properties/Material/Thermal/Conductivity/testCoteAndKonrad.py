import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestCoteAndKonrad(unittest.TestCase):
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
    def testCoteAndKonradProperty(self):
        conductivity = self.material.Thermal.Conductivity
        conductivity.CoteAndKonrad.setParticleConductivity(836.5)
        conductivity.CoteAndKonrad.setUnfrozenKappa(2628.5)
        conductivity.CoteAndKonrad.setFrozenKappa(972.5)
        conductivity.CoteAndKonrad.setChi(86.7)
        conductivity.CoteAndKonrad.setEta(762.9)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        conductivity = self.material.Thermal.Conductivity
        self.assertEqual(conductivity.CoteAndKonrad.getParticleConductivity(), 836.5)
        self.assertEqual(conductivity.CoteAndKonrad.getUnfrozenKappa(), 2628.5)
        self.assertEqual(conductivity.CoteAndKonrad.getFrozenKappa(), 972.5)
        self.assertEqual(conductivity.CoteAndKonrad.getChi(), 86.7)
        self.assertEqual(conductivity.CoteAndKonrad.getEta(), 762.9)
