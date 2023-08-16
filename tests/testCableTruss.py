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
        liner.CableTruss.setCableDiameter(10.1)
        liner.CableTruss.setOutofplaneSpacing(10.1)
        liner.CableTruss.setYoungsModulus(10.1)
        liner.CableTruss.setMaterialType(MaterialType.PLASTIC)
        liner.CableTruss.setTensileStrengthPeak(10.1)
        liner.CableTruss.setTensileStrengthResidual(10.1)
        liner.CableTruss.setPreTensioning(True)
        liner.CableTruss.setPreTensioningForce(10.1)
        liner.CableTruss.setActivateThermal(True)
        liner.CableTruss.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.CableTruss.setStaticTemperature(10.1)
        liner.CableTruss.setConductivity(10.1)
        liner.CableTruss.setSpecificHeatCapacity(10.1)
        liner.CableTruss.setThermalExpansion(True)
        liner.CableTruss.setExpansionCoefficient(10.1)
        liner.CableTruss.setStageCableProperties(True)
        liner.CableTruss.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.CableTruss.getCableDiameter(), 10.1)
        self.assertEqual(liner.CableTruss.getOutofplaneSpacing(), 10.1)
        self.assertEqual(liner.CableTruss.getYoungsModulus(), 10.1)
        self.assertEqual(liner.CableTruss.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.CableTruss.getTensileStrengthPeak(), 10.1)
        self.assertEqual(liner.CableTruss.getTensileStrengthResidual(), 10.1)
        self.assertEqual(liner.CableTruss.getPreTensioning(), True)
        self.assertEqual(liner.CableTruss.getPreTensioningForce(), 10.1)
        self.assertEqual(liner.CableTruss.getActivateThermal(), True)
        self.assertEqual(liner.CableTruss.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.CableTruss.getStaticTemperature(), 10.1)
        self.assertEqual(liner.CableTruss.getConductivity(), 10.1)
        self.assertEqual(liner.CableTruss.getSpecificHeatCapacity(), 10.1)
        self.assertEqual(liner.CableTruss.getThermalExpansion(), True)
        self.assertEqual(liner.CableTruss.getExpansionCoefficient(), 10.1)
        self.assertEqual(liner.CableTruss.getStageCableProperties(), True)
        self.assertEqual(liner.CableTruss.getStaticTemperatureGridToUse(), "None")
