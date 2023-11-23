import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

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
        os.remove(self.copiedModelPath)
    def testInitialConditionsProperty(self):
        material = self.material
        material.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__BOTH_FIELD_AND_BODY)
        material.InitialConditions.setAccountForMoistureContentInUnitWeight(0)
        material.InitialConditions.setDryUnitWeight(2628.5)
        material.InitialConditions.setMoistUnitWeight(972.5)
        material.InitialConditions.setSaturatedUnitWeight(86.7)
        material.InitialConditions.setUnitWeight(762.9)
        material.InitialConditions.setPorosityValue(1413.6)
        material.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_PWP)
        material.InitialConditions.setInitialPoreWaterPressure(468.3)
        material.InitialConditions.setInitialRu(2350.4)
        material.InitialConditions.setInitialPiezoToUse(3023)
        material.InitialConditions.setInitialHuType(HuTypes.HT_AUTO)
        material.InitialConditions.setInitialHu(2572.7)
        material.InitialConditions.setIntiialGridToUse(6811)
        material.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
        material.InitialConditions.setInitialTemperature(3213.4)
        material.InitialConditions.setInitialTemperatureGridToUse(26814)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        material = self.material
        self.assertEqual(material.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__BOTH_FIELD_AND_BODY)
        self.assertEqual(material.InitialConditions.getAccountForMoistureContentInUnitWeight(), 0)
        self.assertEqual(material.InitialConditions.getDryUnitWeight(), 2628.5)
        self.assertEqual(material.InitialConditions.getMoistUnitWeight(), 972.5)
        self.assertEqual(material.InitialConditions.getSaturatedUnitWeight(), 86.7)
        self.assertEqual(material.InitialConditions.getUnitWeight(), 762.9)
        self.assertEqual(material.InitialConditions.getPorosityValue(), 1413.6)
        self.assertEqual(material.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_PWP)
        self.assertEqual(material.InitialConditions.getInitialPoreWaterPressure(), 468.3)
        self.assertEqual(material.InitialConditions.getInitialRu(), 2350.4)
        self.assertEqual(material.InitialConditions.getInitialPiezoToUse(), 3023)
        self.assertEqual(material.InitialConditions.getInitialHuType(), HuTypes.HT_AUTO)
        self.assertEqual(material.InitialConditions.getInitialHu(), 2572.7)
        self.assertEqual(material.InitialConditions.getIntiialGridToUse(), 6811)
        self.assertEqual(material.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
        self.assertEqual(material.InitialConditions.getInitialTemperature(), 3213.4)
        self.assertEqual(material.InitialConditions.getInitialTemperatureGridToUse(), 26814)
