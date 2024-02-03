import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestShanselMaterialDependentVerticalStress(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)

        allMaterials = self.model.getAllMaterialProperties()

        self.material = allMaterials[0]
        self.material.Strength.setFailureCriterion(StrengthCriteriaTypes.SHANSEP)
        self.material.Strength.Shansep.setUseMaterialDependentStress(True)

        self.materialNames = []
        for mat in allMaterials:
            self.materialNames.append(mat.getMaterialName())

    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)

    def testSuccess(self):
        intput = [(self.materialNames[0],0.3),(self.materialNames[1],0.4),(self.materialNames[2],0.5)]
        self.material.Strength.Shansep.setShansepMaterialDependentVerticalStress(intput)
        self.assertEqual(self.material.Strength.Shansep.getShansepMaterialDependentVerticalStress(), intput)
    
    def testFailInvalidMaterialName(self):
        intput = [(self.materialNames[0],0.3),(self.materialNames[1],0.4),("invalid",0.5)]
        with self.assertRaises(Exception):
            self.material.Strength.Shansep.setShansepMaterialDependentVerticalStress(intput)

    def testFailDuplicateMaterialName(self):
        intput = [(self.materialNames[0],0.3),(self.materialNames[1],0.4),(self.materialNames[1],0.5)]
        with self.assertRaises(Exception):
            self.material.Strength.Shansep.setShansepMaterialDependentVerticalStress(intput)
        
    def testFailFactorOutOfRange(self):
        intput = [(self.materialNames[0],0.3),(self.materialNames[1],0.4),(self.materialNames[2],1.1)]
        with self.assertRaises(Exception):
            self.material.Strength.Shansep.setShansepMaterialDependentVerticalStress(intput)

        intput = [(self.materialNames[0],0.3),(self.materialNames[1],0.4),(self.materialNames[2],-0.1)]
        with self.assertRaises(Exception):
            self.material.Strength.Shansep.setShansepMaterialDependentVerticalStress(intput)