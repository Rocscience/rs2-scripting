import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestStageFactors(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProjectTransientGroundwaterAndThermal.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]

        self.strengthStiffnessInterface = self.material.InitialConditions.stageFactorInterface
        self.thermalInterface = self.material.Thermal.stageFactorInterface
        self.hydraulicInterface = self.material.Hydraulic.FEAGroundwater.stageFactorInterface
        self.datumInterface = self.material.Datum.stageFactorInterface
        
    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.model._client.closeConnection()
        os.remove(self.copiedModelPath)

    def SetEnableAllStageFactorInterfaces(self, enable: bool):
        self.material.StageFactors.setStageStrengthStiffnessStageFactors(enable)
        self.material.StageFactors.setStageThermalStageFactors(enable)
        self.material.StageFactors.setStageHydraulicStageFactor(enable)
        self.material.StageFactors.setStageDatumStageFactor(enable)

    def testResetAllStageFactors(self):
        self.SetEnableAllStageFactorInterfaces(False)
        self.material.StageFactors.setStageStrengthStiffnessStageFactors(True)

        sf1 = self.strengthStiffnessInterface.getDefinedStageFactors()[1]
        self.strengthStiffnessInterface.setDefinedStageFactors({1: sf1})

        self.SetEnableAllStageFactorInterfaces(True)

        self.assertEqual(len(self.strengthStiffnessInterface.getDefinedStageFactors()), 1)
        self.assertEqual(len(self.thermalInterface.getDefinedStageFactors()), 1)
        self.assertEqual(len(self.hydraulicInterface.getDefinedStageFactors()), 1)
        self.assertEqual(len(self.datumInterface.getDefinedStageFactors()), 1)

        
    def testRestoreStageFactorsFromNoneEnabled(self):
        self.SetEnableAllStageFactorInterfaces(False)
        self.material.StageFactors.setStageStrengthStiffnessStageFactors(True)

        sf1 = self.strengthStiffnessInterface.getDefinedStageFactors()[1]
        sf1.setPorosityValueFactor(0.123)
        self.strengthStiffnessInterface.setDefinedStageFactors({1: sf1, 2: sf1, 3: sf1})

        self.material.StageFactors.setStageStrengthStiffnessStageFactors(False)
        self.material.StageFactors.setStageStrengthStiffnessStageFactors(True)

        recoveredFactors = self.strengthStiffnessInterface.getDefinedStageFactors()

        self.assertEqual(len(recoveredFactors), 3)
        self.assertEqual(recoveredFactors[1].getPorosityValueFactor(), 0.123)
        self.assertEqual(recoveredFactors[2].getPorosityValueFactor(), 0.123)
        self.assertEqual(recoveredFactors[3].getPorosityValueFactor(), 0.123)

    def testAddWhileOtherDisabled(self):
        self.SetEnableAllStageFactorInterfaces(False)
        self.material.StageFactors.setStageStrengthStiffnessStageFactors(True)

        sf1 = self.strengthStiffnessInterface.getDefinedStageFactors()[1]
        sf1.setPorosityValueFactor(0.123)
        self.strengthStiffnessInterface.setDefinedStageFactors({1: sf1, 2: sf1, 3: sf1, 4: sf1})

        self.material.StageFactors.setStageHydraulicStageFactor(True)
        self.material.StageFactors.setStageDatumStageFactor(True)
        self.material.StageFactors.setStageThermalStageFactors(True)

        strengthStiffnessFactors = self.strengthStiffnessInterface.getDefinedStageFactors()
        thermalFactors = self.thermalInterface.getDefinedStageFactors()
        hydraulicFactors = self.hydraulicInterface.getDefinedStageFactors()
        datumFactors = self.datumInterface.getDefinedStageFactors()

        self.assertEqual(len(strengthStiffnessFactors), 4)
        self.assertEqual(len(thermalFactors), 4)
        self.assertEqual(len(hydraulicFactors), 4)
        self.assertEqual(len(datumFactors), 4)

        strengthStiffnessFactors.pop(4)
        self.strengthStiffnessInterface.setDefinedStageFactors(strengthStiffnessFactors)

    def testReorderWithMultipleActive(self):
        self.SetEnableAllStageFactorInterfaces(True)


        sfmGroup = self.strengthStiffnessInterface.getDefinedStageFactors()
        sfhGroup = self.hydraulicInterface.getDefinedStageFactors()
        sftGroup = self.thermalInterface.getDefinedStageFactors()
        sfdGroup = self.datumInterface.getDefinedStageFactors()

        sfmGroup[1].setPorosityValueFactor(0.1)
        sfmGroup[2].setPorosityValueFactor(0.2)
        sfmGroup[3].setPorosityValueFactor(0.3)

        sfhGroup[1].setK1AngleFactor(0.1)
        sfhGroup[2].setK1AngleFactor(0.2)
        sfhGroup[3].setK1AngleFactor(0.3)

        sftGroup[1].setThermalGridFactor("Default Grid")
        sftGroup[2].setThermalGridFactor("Grid 2")
        sftGroup[3].setThermalGridFactor("Grid 3")

        sfdGroup[1].getDatumYoungsStageFactor().setChange(0.1)
        sfdGroup[2].getDatumYoungsStageFactor().setChange(0.2)
        sfdGroup[3].getDatumYoungsStageFactor().setChange(0.3)

        self.strengthStiffnessInterface.setDefinedStageFactors({1: sfmGroup[3], 2: sfmGroup[1], 3: sfmGroup[2]})

        sfmGroup = self.strengthStiffnessInterface.getDefinedStageFactors()
        sfhGroup = self.hydraulicInterface.getDefinedStageFactors()
        sftGroup = self.thermalInterface.getDefinedStageFactors()
        sfdGroup = self.datumInterface.getDefinedStageFactors()

        self.assertEqual(sfmGroup[1].getPorosityValueFactor(), 0.3)
        self.assertEqual(sfmGroup[2].getPorosityValueFactor(), 0.1)
        self.assertEqual(sfmGroup[3].getPorosityValueFactor(), 0.2)

        self.assertEqual(sfhGroup[1].getK1AngleFactor(), 0.3)
        self.assertEqual(sfhGroup[2].getK1AngleFactor(), 0.1)
        self.assertEqual(sfhGroup[3].getK1AngleFactor(), 0.2)

        self.assertEqual(sftGroup[1].getThermalGridFactor(), "Grid 3")
        self.assertEqual(sftGroup[2].getThermalGridFactor(), "Default Grid")
        self.assertEqual(sftGroup[3].getThermalGridFactor(), "Grid 2")

        self.assertEqual(sfdGroup[1].getDatumYoungsStageFactor().getChange(), 0.3)
        self.assertEqual(sfdGroup[2].getDatumYoungsStageFactor().getChange(), 0.1)
        self.assertEqual(sfdGroup[3].getDatumYoungsStageFactor().getChange(), 0.2)

    def testDeleteOneDeletesOthers(self):
        self.SetEnableAllStageFactorInterfaces(True)

        sfmGroup = self.strengthStiffnessInterface.getDefinedStageFactors()
        self.strengthStiffnessInterface.setDefinedStageFactors({1: sfmGroup[3], 3: sfmGroup[2]})

        self.assertEqual(len(self.strengthStiffnessInterface.getDefinedStageFactors()), 2)
        self.assertEqual(len(self.hydraulicInterface.getDefinedStageFactors()), 2)
        self.assertEqual(len(self.thermalInterface.getDefinedStageFactors()), 2)
        self.assertEqual(len(self.datumInterface.getDefinedStageFactors()), 2)

        self.strengthStiffnessInterface.createStageFactor(2)

    def testCreateOneCreatesOthers(self):
        self.SetEnableAllStageFactorInterfaces(True)

        self.strengthStiffnessInterface.createStageFactor(4)

        self.assertEqual(len(self.strengthStiffnessInterface.getDefinedStageFactors()), 4)
        self.assertEqual(len(self.hydraulicInterface.getDefinedStageFactors()), 4)
        self.assertEqual(len(self.thermalInterface.getDefinedStageFactors()), 4)
        self.assertEqual(len(self.datumInterface.getDefinedStageFactors()), 4)
    
        sfs = self.strengthStiffnessInterface.getDefinedStageFactors()
        sfs.pop(4)
        self.strengthStiffnessInterface.setDefinedStageFactors(sfs)

    def testCreateOthersDisabled(self):
        self.SetEnableAllStageFactorInterfaces(False)
        self.material.StageFactors.setStageStrengthStiffnessStageFactors(True)

        self.strengthStiffnessInterface.createStageFactor(4)
        self.SetEnableAllStageFactorInterfaces(True)

        self.assertEqual(len(self.strengthStiffnessInterface.getDefinedStageFactors()), 4)
        self.assertEqual(len(self.hydraulicInterface.getDefinedStageFactors()), 4)
        self.assertEqual(len(self.thermalInterface.getDefinedStageFactors()), 4)
        self.assertEqual(len(self.datumInterface.getDefinedStageFactors()), 4)

        sfs = self.strengthStiffnessInterface.getDefinedStageFactors()
        sfs.pop(4)
        self.strengthStiffnessInterface.setDefinedStageFactors(sfs)
class TestStaticHydraulicStageFactors(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/testProjectDynamicPropertiesStaticGroundwater.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]

        self.strengthStiffnessInterface = self.material.InitialConditions.stageFactorInterface
        self.thermalInterface = self.material.Thermal.stageFactorInterface
        self.hydraulicInterface = self.material.Hydraulic.FEAGroundwater.stageFactorInterface
        self.datumInterface = self.material.Datum.stageFactorInterface
        
    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.model._client.closeConnection()
        os.remove(self.copiedModelPath)

    def testReorderStaticStageFactorProperties(self):
        staticStageFactorInterface = self.material.Hydraulic.StaticGroundwater.stageFactorInterface

        sfhGroup = staticStageFactorInterface.getDefinedStageFactors()

        sfhGroup[1].setGridToUse("Default Grid")
        sfhGroup[2].setGridToUse("Grid 2")
        sfhGroup[3].setGridToUse("Grid 3")

        sfhGroup[1].setPiezoToUse("None")
        sfhGroup[2].setPiezoToUse("1")
        sfhGroup[3].setPiezoToUse("2")
        
        staticStageFactorInterface.setDefinedStageFactors({1: sfhGroup[3], 2: sfhGroup[1], 3: sfhGroup[2]})

        sfhGroup = staticStageFactorInterface.getDefinedStageFactors()

        self.assertEqual(sfhGroup[1].getGridToUse(), "Grid 3")
        self.assertEqual(sfhGroup[2].getGridToUse(), "Default Grid")
        self.assertEqual(sfhGroup[3].getGridToUse(), "Grid 2")

        self.assertEqual(sfhGroup[1].getPiezoToUse(), "2")
        self.assertEqual(sfhGroup[2].getPiezoToUse(), "None")
        self.assertEqual(sfhGroup[3].getPiezoToUse(), "1")
