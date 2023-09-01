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
        liner.CableTruss.setCableDiameter(1806.1)
        liner.CableTruss.setOutofplaneSpacing(2454.7)
        liner.CableTruss.setYoungsModulus(2603.4)
        liner.CableTruss.setMaterialType(MaterialType.PLASTIC)
        liner.CableTruss.setTensileStrengthPeak(1503.2)
        liner.CableTruss.setTensileStrengthResidual(2481.6)
        liner.CableTruss.setPreTensioning(1)
        liner.CableTruss.setPreTensioningForce(2454.1)
        liner.CableTruss.setActivateThermal(1)
        liner.CableTruss.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.CableTruss.setStaticTemperature(1997.4)
        liner.CableTruss.setConductivity(895.6)
        liner.CableTruss.setSpecificHeatCapacity(201.8)
        liner.CableTruss.setThermalExpansion(1)
        liner.CableTruss.setExpansionCoefficient(214.5)
        liner.CableTruss.setStageCableProperties(1)
        liner.CableTruss.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.CableTruss.getCableDiameter(), 1806.1)
        self.assertEqual(liner.CableTruss.getOutofplaneSpacing(), 2454.7)
        self.assertEqual(liner.CableTruss.getYoungsModulus(), 2603.4)
        self.assertEqual(liner.CableTruss.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.CableTruss.getTensileStrengthPeak(), 1503.2)
        self.assertEqual(liner.CableTruss.getTensileStrengthResidual(), 2481.6)
        self.assertEqual(liner.CableTruss.getPreTensioning(), 1)
        self.assertEqual(liner.CableTruss.getPreTensioningForce(), 2454.1)
        self.assertEqual(liner.CableTruss.getActivateThermal(), 1)
        self.assertEqual(liner.CableTruss.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.CableTruss.getStaticTemperature(), 1997.4)
        self.assertEqual(liner.CableTruss.getConductivity(), 895.6)
        self.assertEqual(liner.CableTruss.getSpecificHeatCapacity(), 201.8)
        self.assertEqual(liner.CableTruss.getThermalExpansion(), 1)
        self.assertEqual(liner.CableTruss.getExpansionCoefficient(), 214.5)
        self.assertEqual(liner.CableTruss.getStageCableProperties(), 1)
        self.assertEqual(liner.CableTruss.getStaticTemperatureGridToUse(), "None")
