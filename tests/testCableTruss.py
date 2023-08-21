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
        liner.CableTruss.setCableDiameter(468)
        liner.CableTruss.setOutofplaneSpacing(786)
        liner.CableTruss.setYoungsModulus(2866)
        liner.CableTruss.setMaterialType(MaterialType.PLASTIC)
        liner.CableTruss.setTensileStrengthPeak(1712)
        liner.CableTruss.setTensileStrengthResidual(1226)
        liner.CableTruss.setPreTensioning(1)
        liner.CableTruss.setPreTensioningForce(2129)
        liner.CableTruss.setActivateThermal(0)
        liner.CableTruss.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.CableTruss.setStaticTemperature(2791)
        liner.CableTruss.setConductivity(2663)
        liner.CableTruss.setSpecificHeatCapacity(1064)
        liner.CableTruss.setThermalExpansion(0)
        liner.CableTruss.setExpansionCoefficient(2831)
        liner.CableTruss.setStageCableProperties(0)
        liner.CableTruss.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.CableTruss.getCableDiameter(), 468)
        self.assertEqual(liner.CableTruss.getOutofplaneSpacing(), 786)
        self.assertEqual(liner.CableTruss.getYoungsModulus(), 2866)
        self.assertEqual(liner.CableTruss.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.CableTruss.getTensileStrengthPeak(), 1712)
        self.assertEqual(liner.CableTruss.getTensileStrengthResidual(), 1226)
        self.assertEqual(liner.CableTruss.getPreTensioning(), 1)
        self.assertEqual(liner.CableTruss.getPreTensioningForce(), 2129)
        self.assertEqual(liner.CableTruss.getActivateThermal(), 0)
        self.assertEqual(liner.CableTruss.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.CableTruss.getStaticTemperature(), 2791)
        self.assertEqual(liner.CableTruss.getConductivity(), 2663)
        self.assertEqual(liner.CableTruss.getSpecificHeatCapacity(), 1064)
        self.assertEqual(liner.CableTruss.getThermalExpansion(), 0)
        self.assertEqual(liner.CableTruss.getExpansionCoefficient(), 2831)
        self.assertEqual(liner.CableTruss.getStageCableProperties(), 0)
        self.assertEqual(liner.CableTruss.getStaticTemperatureGridToUse(), "None")
