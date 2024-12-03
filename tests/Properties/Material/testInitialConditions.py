import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestInitialConditions(unittest.TestCase):
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
    def testInitialConditionsProperty(self):
        material = self.material
        material.InitialConditions.setInitialElementLoading(InitialElementLoadingType.FIELD_STRESS_AND_BODY_FORCE)
        material.InitialConditions.setAccountForMoistureContentInUnitWeight(0)
        material.InitialConditions.setDryUnitWeight(0.015)
        material.InitialConditions.setMoistUnitWeight(0.02)
        material.InitialConditions.setSaturatedUnitWeight(0.025)
        material.InitialConditions.setUnitWeight(2628.5)
        material.InitialConditions.setPorosityValue(0.5)
        material.InitialConditions.setInitialWaterCondition(StaticWaterModes.PORE_WATER_PRESSURE)
        material.InitialConditions.setInitialPoreWaterPressure(972.5)
        material.InitialConditions.setInitialRu(86.7)
        material.InitialConditions.setInitialHuType(HuTypes.AUTO)
        material.InitialConditions.setInitialHu(762.9)
        material.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.PORE_WATER_PRESSURE)
        material.InitialConditions.setInitialTemperature(1413.6)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        material = self.material
        self.assertEqual(material.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.FIELD_STRESS_AND_BODY_FORCE)
        self.assertEqual(material.InitialConditions.getAccountForMoistureContentInUnitWeight(), 0)
        self.assertEqual(material.InitialConditions.getDryUnitWeight(), 0.015)
        self.assertEqual(material.InitialConditions.getMoistUnitWeight(), 0.02)
        self.assertEqual(material.InitialConditions.getSaturatedUnitWeight(), 0.025)
        self.assertEqual(material.InitialConditions.getUnitWeight(), 2628.5)
        self.assertEqual(material.InitialConditions.getPorosityValue(), 0.5)
        self.assertEqual(material.InitialConditions.getInitialWaterCondition(), StaticWaterModes.PORE_WATER_PRESSURE)
        self.assertEqual(material.InitialConditions.getInitialPoreWaterPressure(), 972.5)
        self.assertEqual(material.InitialConditions.getInitialRu(), 86.7)
        self.assertEqual(material.InitialConditions.getInitialHuType(), HuTypes.AUTO)
        self.assertEqual(material.InitialConditions.getInitialHu(), 762.9)
        self.assertEqual(material.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.PORE_WATER_PRESSURE)
        self.assertEqual(material.InitialConditions.getInitialTemperature(), 1413.6)
    def testInitialConditionsStageFactors(self):
        material = self.material
        stageFactor = material.InitialConditions.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setUnitWeightFactor(468.3)
        stageFactor.setPorosityValueFactor(2350.4)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        material = self.material
        stageFactor = material.InitialConditions.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getUnitWeightFactor(), 468.3)
        self.assertEqual(stageFactor.getPorosityValueFactor(), 2350.4)
