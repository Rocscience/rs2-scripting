import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestManzariAndDafalias(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Strength.setFailureCriterion(StrengthCriteriaTypes.MANZARI_AND_DAFALIAS)
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testManzariAndDafaliasProperty(self):
        stiffness = self.material.Stiffness
        stiffness.ManzariAndDafalias.setG0Parameter(836.5)
        stiffness.ManzariAndDafalias.setVParameter(2628.5)
        stiffness.ManzariAndDafalias.setPatmParameter(972.5)
        stiffness.ManzariAndDafalias.setInitialVoidRatio(86.7)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        stiffness = self.material.Stiffness
        self.assertEqual(stiffness.ManzariAndDafalias.getG0Parameter(), 836.5)
        self.assertEqual(stiffness.ManzariAndDafalias.getVParameter(), 2628.5)
        self.assertEqual(stiffness.ManzariAndDafalias.getPatmParameter(), 972.5)
        self.assertEqual(stiffness.ManzariAndDafalias.getInitialVoidRatio(), 86.7)
