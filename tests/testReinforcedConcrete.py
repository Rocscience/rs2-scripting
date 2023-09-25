import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestReinforcedConcrete(unittest.TestCase):
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
    def testReinforcedConcreteProperty(self):
        liner = self.liner
        self.liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)
        liner.ReinforcedConcrete.setConcreteUnitWeight(836.5)
        liner.ReinforcedConcrete.setIncludeWeightInAnalysis(0)
        liner.ReinforcedConcrete.setReinforcement(0)
        liner.ReinforcedConcrete.setSpacing(86.7)
        liner.ReinforcedConcrete.setSectionDepth(762.9)
        liner.ReinforcedConcrete.setArea(1413.6)
        liner.ReinforcedConcrete.setMomentOfInertia(468.3)
        liner.ReinforcedConcrete.setConcreteYoungsModulus(2350.4)
        liner.ReinforcedConcrete.setConcreteCompressiveStrength(2598.3)
        liner.ReinforcedConcrete.setConcreteTensileStrength(2572.7)
        liner.ReinforcedConcrete.setWeight(2605.0)
        liner.ReinforcedConcrete.setConcrete(1)
        liner.ReinforcedConcrete.setThickness(3213.4)
        liner.ReinforcedConcrete.setYoungsModulus(176.8)
        liner.ReinforcedConcrete.setPoissonRatio(1508.0)
        liner.ReinforcedConcrete.setCompressiveStrength(857.2)
        liner.ReinforcedConcrete.setTensileStrength(3215.6)
        liner.ReinforcedConcrete.setMaterialType(MaterialType.PLASTIC)
        liner.ReinforcedConcrete.setSlidingGap(1)
        liner.ReinforcedConcrete.setStrainAtLocking(2227.9)
        liner.ReinforcedConcrete.setBeamElementFormulation(LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        liner.ReinforcedConcrete.setActivateThermal(1)
        liner.ReinforcedConcrete.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.ReinforcedConcrete.setStaticTemperature(2917.7)
        liner.ReinforcedConcrete.setConductivity(1006.5)
        liner.ReinforcedConcrete.setSpecificHeatCapacity(1374.4)
        liner.ReinforcedConcrete.setThermalExpansion(0)
        liner.ReinforcedConcrete.setExpansionCoefficient(1702.5)
        liner.ReinforcedConcrete.setStageConcreteProperties(0)
        liner.ReinforcedConcrete.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.ReinforcedConcrete.getConcreteUnitWeight(), 836.5)
        self.assertEqual(liner.ReinforcedConcrete.getIncludeWeightInAnalysis(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getReinforcement(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getSpacing(), 86.7)
        self.assertEqual(liner.ReinforcedConcrete.getSectionDepth(), 762.9)
        self.assertEqual(liner.ReinforcedConcrete.getArea(), 1413.6)
        self.assertEqual(liner.ReinforcedConcrete.getMomentOfInertia(), 468.3)
        self.assertEqual(liner.ReinforcedConcrete.getConcreteYoungsModulus(), 2350.4)
        self.assertEqual(liner.ReinforcedConcrete.getConcreteCompressiveStrength(), 2598.3)
        self.assertEqual(liner.ReinforcedConcrete.getConcreteTensileStrength(), 2572.7)
        self.assertEqual(liner.ReinforcedConcrete.getWeight(), 2605.0)
        self.assertEqual(liner.ReinforcedConcrete.getConcrete(), 1)
        self.assertEqual(liner.ReinforcedConcrete.getThickness(), 3213.4)
        self.assertEqual(liner.ReinforcedConcrete.getYoungsModulus(), 176.8)
        self.assertEqual(liner.ReinforcedConcrete.getPoissonRatio(), 1508.0)
        self.assertEqual(liner.ReinforcedConcrete.getCompressiveStrength(), 857.2)
        self.assertEqual(liner.ReinforcedConcrete.getTensileStrength(), 3215.6)
        self.assertEqual(liner.ReinforcedConcrete.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.ReinforcedConcrete.getSlidingGap(), 1)
        self.assertEqual(liner.ReinforcedConcrete.getStrainAtLocking(), 2227.9)
        self.assertEqual(liner.ReinforcedConcrete.getBeamElementFormulation(), LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        self.assertEqual(liner.ReinforcedConcrete.getActivateThermal(), 1)
        self.assertEqual(liner.ReinforcedConcrete.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.ReinforcedConcrete.getStaticTemperature(), 2917.7)
        self.assertEqual(liner.ReinforcedConcrete.getConductivity(), 1006.5)
        self.assertEqual(liner.ReinforcedConcrete.getSpecificHeatCapacity(), 1374.4)
        self.assertEqual(liner.ReinforcedConcrete.getThermalExpansion(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getExpansionCoefficient(), 1702.5)
        self.assertEqual(liner.ReinforcedConcrete.getStageConcreteProperties(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getStaticTemperatureGridToUse(), "None")
    def testReinforcedConcreteStageFactors(self):
        self.liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)
        stageFactor = self.liner.ReinforcedConcrete.getStageFactors()[0]
        stageFactor.setThicknessFactor(2757.7)
        stageFactor.setYoungsModulusFactor(1556.5)
        stageFactor.setCompressiveStrengthFactor(892.2)
        stageFactor.setTensileStrengthFactor(1579.1)
        stageFactor.setAxialStrainExpansionFactor(23.6)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        stageFactor = self.liner.ReinforcedConcrete.getStageFactors()[0]
        self.assertEqual(stageFactor.getThicknessFactor(), 2757.7)
        self.assertEqual(stageFactor.getYoungsModulusFactor(), 1556.5)
        self.assertEqual(stageFactor.getCompressiveStrengthFactor(), 892.2)
        self.assertEqual(stageFactor.getTensileStrengthFactor(), 1579.1)
        self.assertEqual(stageFactor.getAxialStrainExpansionFactor(), 23.6)
