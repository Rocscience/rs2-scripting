import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestCableTruss(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/BlankModelWithStageFactors.fez"
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
        liner.CableTruss.setCableDiameter(2706.5)
        liner.CableTruss.setOutofplaneSpacing(2997.5)
        liner.CableTruss.setYoungsModulus(1636.7)
        liner.CableTruss.setMaterialType(MaterialType.PLASTIC)
        liner.CableTruss.setTensileStrengthPeak(3135.1)
        liner.CableTruss.setTensileStrengthResidual(202.8)
        liner.CableTruss.setPreTensioning(1)
        liner.CableTruss.setPreTensioningForce(913.5)
        liner.CableTruss.setActivateThermal(0)
        liner.CableTruss.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.CableTruss.setStaticTemperature(2636.3)
        liner.CableTruss.setConductivity(269.9)
        liner.CableTruss.setSpecificHeatCapacity(2689.0)
        liner.CableTruss.setThermalExpansion(0)
        liner.CableTruss.setExpansionCoefficient(1478.8)
        liner.CableTruss.setStageCableProperties(0)
        liner.CableTruss.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.CableTruss.getCableDiameter(), 2706.5)
        self.assertEqual(liner.CableTruss.getOutofplaneSpacing(), 2997.5)
        self.assertEqual(liner.CableTruss.getYoungsModulus(), 1636.7)
        self.assertEqual(liner.CableTruss.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.CableTruss.getTensileStrengthPeak(), 3135.1)
        self.assertEqual(liner.CableTruss.getTensileStrengthResidual(), 202.8)
        self.assertEqual(liner.CableTruss.getPreTensioning(), 1)
        self.assertEqual(liner.CableTruss.getPreTensioningForce(), 913.5)
        self.assertEqual(liner.CableTruss.getActivateThermal(), 0)
        self.assertEqual(liner.CableTruss.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.CableTruss.getStaticTemperature(), 2636.3)
        self.assertEqual(liner.CableTruss.getConductivity(), 269.9)
        self.assertEqual(liner.CableTruss.getSpecificHeatCapacity(), 2689.0)
        self.assertEqual(liner.CableTruss.getThermalExpansion(), 0)
        self.assertEqual(liner.CableTruss.getExpansionCoefficient(), 1478.8)
        self.assertEqual(liner.CableTruss.getStageCableProperties(), 0)
        self.assertEqual(liner.CableTruss.getStaticTemperatureGridToUse(), "None")
    def testCableTrussStageFactors(self):
        self.liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)
        stageFactor = self.liner.CableTruss.getStageFactors()[0]
        stageFactor.setYoungsModulusFactor(1581.3)
        stageFactor.setAxialStrainExpansionFactor(436.0)
        stageFactor.setTensileStrengthPeakFactor(1760.4)
        stageFactor.setTensileStrengthResidualFactor(735.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        stageFactor = self.liner.CableTruss.getStageFactors()[0]
        self.assertEqual(stageFactor.getYoungsModulusFactor(), 1581.3)
        self.assertEqual(stageFactor.getAxialStrainExpansionFactor(), 436.0)
        self.assertEqual(stageFactor.getTensileStrengthPeakFactor(), 1760.4)
        self.assertEqual(stageFactor.getTensileStrengthResidualFactor(), 735.5)
