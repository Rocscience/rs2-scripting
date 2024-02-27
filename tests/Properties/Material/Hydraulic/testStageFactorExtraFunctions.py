import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestStageFactorExtraFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/testProjectDynamicProperties.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.model._client.closeConnection()
        os.remove(self.copiedModelPath)

    def testSetMaterialBehaviourFactor(self):
        sf1 = self.material.Hydraulic.stageFactorInterface.getDefinedStageFactors()[1]
        sf1.setMaterialBehaviourFactor(MaterialBehaviours.DRAINED)
        self.assertEqual(sf1.getMaterialBehaviourFactor(), MaterialBehaviours.DRAINED)
        sf1.setMaterialBehaviourFactor(MaterialBehaviours.UNDRAINED)
        self.assertEqual(sf1.getMaterialBehaviourFactor(), MaterialBehaviours.UNDRAINED)

    def testSetK1SurfaceFactor(self):
        sf1 = self.material.Hydraulic.FEAGroundwater.stageFactorInterface.getDefinedStageFactors()[1]
        sf1.setSurfaceFactor("Anisotropic Surface 2")
        self.assertEqual(sf1.getSurfaceFactor(), "Anisotropic Surface 2")
        sf1.setSurfaceFactor("Anisotropic Surface 1")
        self.assertEqual(sf1.getSurfaceFactor(), "Anisotropic Surface 1")
    
    def testSetK1SurfaceFactorFailure(self):
        sf1 = self.material.Hydraulic.FEAGroundwater.stageFactorInterface.getDefinedStageFactors()[1]
        with self.assertRaises(Exception):
            sf1.setSurfaceFactor("NonExistant Surface")


class TestStageFactorStaticGroundwaterExtraFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/testProjectDynamicPropertiesStaticGroundwater.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.model._client.closeConnection()
        os.remove(self.copiedModelPath)
    def testSetGridStageFactor(self):
        self.material.Hydraulic.StaticGroundwater.setStaticWaterMode(StaticWaterModes.SWM_GRID)
        sf1 = self.material.Hydraulic.StaticGroundwater.stageFactorInterface.getDefinedStageFactors()[1]
        sf1.setGridToUse("Grid 2")
        self.assertEqual(sf1.getGridToUse(), "Grid 2")
        sf1.setGridToUse("Grid 3")
        self.assertEqual(sf1.getGridToUse(), "Grid 3")
        sf1.setGridToUse("None")
        self.assertEqual(sf1.getGridToUse(), "None")
        sf1.setGridToUse("Default Grid")
        self.assertEqual(sf1.getGridToUse(), "Default Grid")
    def testSetPiezoStageFactor(self):
        self.material.Hydraulic.StaticGroundwater.setStaticWaterMode(StaticWaterModes.SWM_PIEZO)
        sf1 = self.material.Hydraulic.StaticGroundwater.stageFactorInterface.getDefinedStageFactors()[1]
        sf1.setPiezoToUse("1")
        self.assertEqual(sf1.getPiezoToUse(), "1")
        sf1.setPiezoToUse("2")
        self.assertEqual(sf1.getPiezoToUse(), "2")
        sf1.setPiezoToUse("None")
        self.assertEqual(sf1.getPiezoToUse(), "None")
