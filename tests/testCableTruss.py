import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from src.rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestCableTruss(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/blankProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testCableTrussProperty(self):
        liner = self.liner
        self.liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)
        liner.CableTruss.setCableDiameter(836.5)
        liner.CableTruss.setOutofplaneSpacing(2628.5)
        liner.CableTruss.setYoungsModulus(972.5)
        liner.CableTruss.setMaterialType(MaterialType.PLASTIC)
        liner.CableTruss.setTensileStrengthPeak(86.7)
        liner.CableTruss.setTensileStrengthResidual(762.9)
        liner.CableTruss.setPreTensioning(0)
        liner.CableTruss.setPreTensioningForce(468.3)
        liner.CableTruss.setActivateThermal(0)
        liner.CableTruss.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.CableTruss.setStaticTemperature(2598.3)
        liner.CableTruss.setConductivity(2572.7)
        liner.CableTruss.setSpecificHeatCapacity(2605.0)
        liner.CableTruss.setThermalExpansion(1)
        liner.CableTruss.setExpansionCoefficient(176.8)
        liner.CableTruss.setStageCableProperties(1)
        liner.CableTruss.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.CableTruss.getCableDiameter(), 836.5)
        self.assertEqual(liner.CableTruss.getOutofplaneSpacing(), 2628.5)
        self.assertEqual(liner.CableTruss.getYoungsModulus(), 972.5)
        self.assertEqual(liner.CableTruss.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.CableTruss.getTensileStrengthPeak(), 86.7)
        self.assertEqual(liner.CableTruss.getTensileStrengthResidual(), 762.9)
        self.assertEqual(liner.CableTruss.getPreTensioning(), 0)
        self.assertEqual(liner.CableTruss.getPreTensioningForce(), 468.3)
        self.assertEqual(liner.CableTruss.getActivateThermal(), 0)
        self.assertEqual(liner.CableTruss.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.CableTruss.getStaticTemperature(), 2598.3)
        self.assertEqual(liner.CableTruss.getConductivity(), 2572.7)
        self.assertEqual(liner.CableTruss.getSpecificHeatCapacity(), 2605.0)
        self.assertEqual(liner.CableTruss.getThermalExpansion(), 1)
        self.assertEqual(liner.CableTruss.getExpansionCoefficient(), 176.8)
        self.assertEqual(liner.CableTruss.getStageCableProperties(), 1)
        self.assertEqual(liner.CableTruss.getStaticTemperatureGridToUse(), "None")
