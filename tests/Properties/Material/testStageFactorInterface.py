import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestStageFactorInterface(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProjectTransientGroundwaterAndThermal.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.sfi = self.material.StageFactors

    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.model._client.closeConnection()
        os.remove(self.copiedModelPath)

    def setUp(self) -> None:
        self.sfi.setStageStrengthStiffnessStageFactors(True)
        self.sfi.setStageHydraulicStageFactor(True)
        self.sfi.setStageThermalStageFactors(True)
        self.sfi.setStageDatumStageFactor(True)

        dfs = self.sfi.getDefinedStageFactors()

        if not (1 in dfs):
            self.sfi.createStageFactor(1)   
            dfs = self.sfi.getDefinedStageFactors()

        self.sfi.setDefinedStageFactors({1: dfs[1]})

    def testGetDefinedDisabled(self):
        dfs = self.sfi.getDefinedStageFactors()
        self.assertEqual(len(dfs), 1)

        self.sfi.setStageStrengthStiffnessStageFactors(True)
        self.sfi.setStageHydraulicStageFactor(True)
        self.sfi.setStageThermalStageFactors(True)
        self.sfi.setStageDatumStageFactor(True)

        dfs = self.sfi.getDefinedStageFactors()
        self.assertTrue(dfs[1][0] is not None)
        self.assertTrue(dfs[1][1] is not None)
        self.assertTrue(dfs[1][2] is not None)

        self.sfi.setStageDatumStageFactor(False)

        dfs = self.sfi.getDefinedStageFactors()
        self.assertTrue(dfs[1][0] is not None)
        self.assertTrue(dfs[1][1] is not None)
        self.assertTrue(dfs[1][2] is not None)

        self.sfi.setStageStrengthStiffnessStageFactors(False)

        dfs = self.sfi.getDefinedStageFactors()
        self.assertTrue(dfs[1][0] is None)
        self.assertTrue(dfs[1][1] is not None)
        self.assertTrue(dfs[1][2] is not None)

        self.sfi.setStageHydraulicStageFactor(False)

        dfs = self.sfi.getDefinedStageFactors()
        self.assertTrue(dfs[1][0] is None)
        self.assertTrue(dfs[1][1] is None)
        self.assertTrue(dfs[1][2] is not None)

        self.sfi.setStageThermalStageFactors(False)

        dfs = self.sfi.getDefinedStageFactors()
        self.assertTrue(len(dfs) == 0)

    def testSetWithMissingFactor(self):
        dfs = self.sfi.getDefinedStageFactors()
        with self.assertRaises(Exception):
            self.sfi.setDefinedStageFactors({1: (dfs[1][0], dfs[1][1], None)})
        with self.assertRaises(Exception):
            self.sfi.setDefinedStageFactors({1: (dfs[1][0], None, dfs[1][2])})
        with self.assertRaises(Exception):
            self.sfi.setDefinedStageFactors({1: (None, dfs[1][1], dfs[1][2])})
    
    def testSetWithExtraFactor(self):
        dfs = self.sfi.getDefinedStageFactors()
        with self.assertRaises(Exception):
            self.sfi.setDefinedStageFactors({1: (dfs[1][0], dfs[1][1], dfs[1][2], dfs[1][2])})
    
        self.sfi.setStageThermalStageFactors(False)
        with self.assertRaises(Exception):
            self.sfi.setDefinedStageFactors({1: (dfs[1][0], dfs[1][1], dfs[1][2])})

        self.sfi.setStageThermalStageFactors(True)
        self.sfi.setStageHydraulicStageFactor(False)
        with self.assertRaises(Exception):
            self.sfi.setDefinedStageFactors({1: (dfs[1][0], dfs[1][1], dfs[1][2])})

        self.sfi.setStageHydraulicStageFactor(True)
        self.sfi.setStageStrengthStiffnessStageFactors(False)
        self.sfi.setStageDatumStageFactor(False)
        with self.assertRaises(Exception):
            self.sfi.setDefinedStageFactors({1: (dfs[1][0], dfs[1][1], dfs[1][2])})

    def testCreateStageFactorValuesCopied(self):
        sfi = self.material.Stiffness.Isotropic.stageFactorInterface
        hyi = self.material.Hydraulic.FEAGroundwater.stageFactorInterface
        thi = self.material.Thermal.stageFactorInterface
        di = self.material.Datum.stageFactorInterface

        sfi.getDefinedStageFactors()[1].setYoungsModulusFactor(2.1)
        hyi.getDefinedStageFactors()[1].setK1AngleFactor(2.2)
        thi.getDefinedStageFactors()[1].setThermalGridFactor("Grid 2")
        di.getDefinedStageFactors()[1].getDatumYoungsStageFactor().setDatum(2.3)

        self.sfi.createStageFactor(2)
        
        self.assertEqual(sfi.getDefinedStageFactors()[2].getYoungsModulusFactor(), 2.1)
        self.assertEqual(hyi.getDefinedStageFactors()[2].getK1AngleFactor(), 2.2)
        self.assertEqual(thi.getDefinedStageFactors()[2].getThermalGridFactor(), "Grid 2")
        self.assertEqual(di.getDefinedStageFactors()[2].getDatumYoungsStageFactor().getDatum(), 2.3)

    def testCreateWithSomeDisabled(self):
        self.sfi.setStageStrengthStiffnessStageFactors(False)
        self.sfi.setStageHydraulicStageFactor(False)
        self.sfi.setStageThermalStageFactors(False)
        self.sfi.setStageDatumStageFactor(False)

        self.sfi.createStageFactor(2)

        self.assertEqual(len(self.sfi.getDefinedStageFactors()), 0)

        self.sfi.setStageStrengthStiffnessStageFactors(True)

        self.sfi.createStageFactor(2)
        self.assertTrue(self.sfi.getDefinedStageFactors()[1][0] is not None)
        self.assertTrue(self.sfi.getDefinedStageFactors()[1][1] is None)
        self.assertTrue(self.sfi.getDefinedStageFactors()[1][2] is None)

        self.assertTrue(self.sfi.getDefinedStageFactors()[2][0] is not None)
        self.assertTrue(self.sfi.getDefinedStageFactors()[2][1] is None)
        self.assertTrue(self.sfi.getDefinedStageFactors()[2][2] is None)

        self.sfi.setStageHydraulicStageFactor(True)

        self.sfi.createStageFactor(3)

        self.assertTrue(self.sfi.getDefinedStageFactors()[1][0] is not None)
        self.assertTrue(self.sfi.getDefinedStageFactors()[1][1] is not None)
        self.assertTrue(self.sfi.getDefinedStageFactors()[1][2] is None)

        self.assertTrue(self.sfi.getDefinedStageFactors()[2][0] is not None)
        self.assertTrue(self.sfi.getDefinedStageFactors()[2][1] is not None)
        self.assertTrue(self.sfi.getDefinedStageFactors()[2][2] is None)

        self.assertTrue(self.sfi.getDefinedStageFactors()[3][0] is not None)
        self.assertTrue(self.sfi.getDefinedStageFactors()[3][1] is not None)
        self.assertTrue(self.sfi.getDefinedStageFactors()[3][2] is None)

        self.sfi.setStageThermalStageFactors(True)

        self.sfi.createStageFactor(4)

        self.assertTrue(self.sfi.getDefinedStageFactors()[1][0] is not None)
        self.assertTrue(self.sfi.getDefinedStageFactors()[1][1] is not None)
        self.assertTrue(self.sfi.getDefinedStageFactors()[1][2] is not None)

        self.assertTrue(self.sfi.getDefinedStageFactors()[2][0] is not None)
        self.assertTrue(self.sfi.getDefinedStageFactors()[2][1] is not None)
        self.assertTrue(self.sfi.getDefinedStageFactors()[2][2] is not None)

        self.assertTrue(self.sfi.getDefinedStageFactors()[3][0] is not None)
        self.assertTrue(self.sfi.getDefinedStageFactors()[3][1] is not None)
        self.assertTrue(self.sfi.getDefinedStageFactors()[3][2] is not None)

        self.assertTrue(self.sfi.getDefinedStageFactors()[4][0] is not None)
        self.assertTrue(self.sfi.getDefinedStageFactors()[4][1] is not None)
        self.assertTrue(self.sfi.getDefinedStageFactors()[4][2] is not None)

    def testRemoveStageFactor(self):
        self.sfi.createStageFactor(2)
        self.sfi.createStageFactor(3)
        self.sfi.createStageFactor(4)

        self.assertTrue(self.sfi.getDefinedStageFactors()[3] is not None)

        dfs = self.sfi.getDefinedStageFactors()
        self.sfi.setDefinedStageFactors({1: dfs[1], 2: dfs[2], 4: dfs[4]})

        self.assertTrue(1 in self.sfi.getDefinedStageFactors())
        self.assertTrue(2 in self.sfi.getDefinedStageFactors())
        self.assertFalse(3 in self.sfi.getDefinedStageFactors())
        self.assertTrue(4 in self.sfi.getDefinedStageFactors())
    
    def testRemoveWithSomeDisabled(self):
        self.sfi.setStageHydraulicStageFactor(False)

        self.sfi.createStageFactor(2)
        self.sfi.createStageFactor(3)
        self.sfi.createStageFactor(4)

        self.assertTrue(self.sfi.getDefinedStageFactors()[3] is not None)

        dfs = self.sfi.getDefinedStageFactors()
        self.sfi.setDefinedStageFactors({1: dfs[1], 2: dfs[2], 4: dfs[4]})

        self.assertTrue(1 in self.sfi.getDefinedStageFactors())
        self.assertTrue(2 in self.sfi.getDefinedStageFactors())
        self.assertFalse(3 in self.sfi.getDefinedStageFactors())
        self.assertTrue(4 in self.sfi.getDefinedStageFactors())

    def testGetDefaultStageFactor(self):
        sf2 = self.sfi.createStageFactor(2)
        self.sfi.setDefinedStageFactors({2: sf2})

        self.material.Thermal.setStaticTemperatureGridToUseByName("Grid 2")
        sf1 = self.material.Thermal.stageFactorInterface.getStageFactor(1)
        self.assertEqual(sf1.getThermalGridFactor(), "Grid 2")
    def testCreateDefaultStageFactor(self):
        sf2 = self.sfi.createStageFactor(2)
        self.sfi.setDefinedStageFactors({2: sf2})

        self.material.Thermal.setStaticTemperatureGridToUseByName("Grid 2")
        self.material.StageFactors.createStageFactor(1)
        sf1 = self.material.Thermal.stageFactorInterface.getStageFactor(1)
        self.assertEqual(sf1.getThermalGridFactor(), "Grid 2")
class TestStageFactorInterfaceDynamicProperties(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/testProjectDynamicPropertiesStaticGroundwater.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.sfi = self.material.StageFactors

    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.model._client.closeConnection()
        os.remove(self.copiedModelPath)

    def setUp(self) -> None:
        self.sfi.setStageStrengthStiffnessStageFactors(True)
        self.sfi.setStageHydraulicStageFactor(True)
        self.sfi.setStageThermalStageFactors(True)
        self.sfi.setStageDatumStageFactor(True)

        dfs = self.sfi.getDefinedStageFactors()

        if not (1 in dfs):
            self.sfi.createStageFactor(1)   
            dfs = self.sfi.getDefinedStageFactors()

        self.sfi.setDefinedStageFactors({1: dfs[1]})

    def testHydroPiezoAndGridPerStage(self):
        self.sfi.createStageFactor(3)
        hyi = self.material.Hydraulic.StaticGroundwater.stageFactorInterface
        hyi.getDefinedStageFactors()[3].setPiezoToUse("2")
        hyi.getDefinedStageFactors()[1].setPiezoToUse("1")
        hyi.getDefinedStageFactors()[3].setGridToUse("Grid 3")
        hyi.getDefinedStageFactors()[1].setGridToUse("Grid 2")

        #swap
        self.sfi.setDefinedStageFactors({1: self.sfi.getDefinedStageFactors()[3], 3: self.sfi.getDefinedStageFactors()[1]})

        self.assertEqual(hyi.getDefinedStageFactors()[1].getPiezoToUse(), "2")
        self.assertEqual(hyi.getDefinedStageFactors()[3].getPiezoToUse(), "1")
        self.assertEqual(hyi.getDefinedStageFactors()[1].getGridToUse(), "Grid 3")
        self.assertEqual(hyi.getDefinedStageFactors()[3].getGridToUse(), "Grid 2")

        self.sfi.createStageFactor(2)

        self.assertEqual(hyi.getDefinedStageFactors()[2].getPiezoToUse(), hyi.getDefinedStageFactors()[1].getPiezoToUse())
        self.assertEqual(hyi.getDefinedStageFactors()[2].getGridToUse(), hyi.getDefinedStageFactors()[1].getGridToUse())

    def testGetDefaultStageFactor(self):
        sf2 = self.sfi.createStageFactor(2)
        self.sfi.setDefinedStageFactors({2: sf2})

        self.material.Hydraulic.setMaterialBehaviour(MaterialBehaviours.UNDRAINED)
        self.material.Hydraulic.FEAGroundwater.setK1SurfaceToUseByName("Anisotropic Surface 2")
        self.material.Hydraulic.StaticGroundwater.setGridToUse("Grid 2")
        self.material.Hydraulic.StaticGroundwater.setPiezoToUse("2")

        sf1 = self.material.Hydraulic.stageFactorInterface.getStageFactor(1)
        self.assertEqual(sf1.getMaterialBehaviourFactor(), MaterialBehaviours.UNDRAINED)
        sf1 = self.material.Hydraulic.FEAGroundwater.stageFactorInterface.getStageFactor(1)
        self.assertEqual(sf1.getAnisotropicSurfaceFactor(), "Anisotropic Surface 2")
        sf1 = self.material.Hydraulic.StaticGroundwater.stageFactorInterface.getStageFactor(1)
        self.assertEqual(sf1.getGridToUse(), "Grid 2")
        self.assertEqual(sf1.getPiezoToUse(), "2")

    def testCreateDefaultStageFactor(self):
        sf2 = self.sfi.createStageFactor(2)
        self.sfi.setDefinedStageFactors({2: sf2})

        self.material.Hydraulic.setMaterialBehaviour(MaterialBehaviours.UNDRAINED)
        self.material.Hydraulic.FEAGroundwater.setK1SurfaceToUseByName("Anisotropic Surface 2")
        self.material.Hydraulic.StaticGroundwater.setGridToUse("Grid 2")
        self.material.Hydraulic.StaticGroundwater.setPiezoToUse("2")

        self.material.StageFactors.createStageFactor(1)
        sf1 = self.material.Hydraulic.stageFactorInterface.getStageFactor(1)
        self.assertEqual(sf1.getMaterialBehaviourFactor(), MaterialBehaviours.UNDRAINED)
        sf1 = self.material.Hydraulic.FEAGroundwater.stageFactorInterface.getStageFactor(1)
        self.assertEqual(sf1.getAnisotropicSurfaceFactor(), "Anisotropic Surface 2")
        sf1 = self.material.Hydraulic.StaticGroundwater.stageFactorInterface.getStageFactor(1)
        self.assertEqual(sf1.getGridToUse(), "Grid 2")
        self.assertEqual(sf1.getPiezoToUse(), "2")

        