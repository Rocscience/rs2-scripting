import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from src.rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestReinforcedConcrete(unittest.TestCase):
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
    def testReinforcedConcreteProperty(self):
        liner = self.liner
        self.liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)
        liner.ReinforcedConcrete.setConcreteUnitWeight(69)
        liner.ReinforcedConcrete.setIncludeWeightInAnalysis(0)
        liner.ReinforcedConcrete.setReinforcement(1)
        liner.ReinforcedConcrete.setSpacing(494)
        liner.ReinforcedConcrete.setSectionDepth(3100)
        liner.ReinforcedConcrete.setArea(807)
        liner.ReinforcedConcrete.setMomentOfInertia(1460)
        liner.ReinforcedConcrete.setConcreteYoungsModulus(1937)
        liner.ReinforcedConcrete.setConcreteCompressiveStrength(599)
        liner.ReinforcedConcrete.setConcreteTensileStrength(2101)
        liner.ReinforcedConcrete.setWeight(418)
        liner.ReinforcedConcrete.setConcrete(0)
        liner.ReinforcedConcrete.setThickness(1663)
        liner.ReinforcedConcrete.setYoungsModulus(2710)
        liner.ReinforcedConcrete.setPoissonRatio(2415)
        liner.ReinforcedConcrete.setCompressiveStrength(1490)
        liner.ReinforcedConcrete.setTensileStrength(222)
        liner.ReinforcedConcrete.setMaterialType(MaterialType.PLASTIC)
        liner.ReinforcedConcrete.setSlidingGap(0)
        liner.ReinforcedConcrete.setStrainAtLocking(1903)
        liner.ReinforcedConcrete.setBeamElementFormulation(LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        liner.ReinforcedConcrete.setActivateThermal(1)
        liner.ReinforcedConcrete.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.ReinforcedConcrete.setStaticTemperature(2448)
        liner.ReinforcedConcrete.setConductivity(167)
        liner.ReinforcedConcrete.setSpecificHeatCapacity(2995)
        liner.ReinforcedConcrete.setThermalExpansion(0)
        liner.ReinforcedConcrete.setExpansionCoefficient(2197)
        liner.ReinforcedConcrete.setStageConcreteProperties(0)
        liner.ReinforcedConcrete.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.ReinforcedConcrete.getConcreteUnitWeight(), 69)
        self.assertEqual(liner.ReinforcedConcrete.getIncludeWeightInAnalysis(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getReinforcement(), 1)
        self.assertEqual(liner.ReinforcedConcrete.getSpacing(), 494)
        self.assertEqual(liner.ReinforcedConcrete.getSectionDepth(), 3100)
        self.assertEqual(liner.ReinforcedConcrete.getArea(), 807)
        self.assertEqual(liner.ReinforcedConcrete.getMomentOfInertia(), 1460)
        self.assertEqual(liner.ReinforcedConcrete.getConcreteYoungsModulus(), 1937)
        self.assertEqual(liner.ReinforcedConcrete.getConcreteCompressiveStrength(), 599)
        self.assertEqual(liner.ReinforcedConcrete.getConcreteTensileStrength(), 2101)
        self.assertEqual(liner.ReinforcedConcrete.getWeight(), 418)
        self.assertEqual(liner.ReinforcedConcrete.getConcrete(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getThickness(), 1663)
        self.assertEqual(liner.ReinforcedConcrete.getYoungsModulus(), 2710)
        self.assertEqual(liner.ReinforcedConcrete.getPoissonRatio(), 2415)
        self.assertEqual(liner.ReinforcedConcrete.getCompressiveStrength(), 1490)
        self.assertEqual(liner.ReinforcedConcrete.getTensileStrength(), 222)
        self.assertEqual(liner.ReinforcedConcrete.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.ReinforcedConcrete.getSlidingGap(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getStrainAtLocking(), 1903)
        self.assertEqual(liner.ReinforcedConcrete.getBeamElementFormulation(), LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        self.assertEqual(liner.ReinforcedConcrete.getActivateThermal(), 1)
        self.assertEqual(liner.ReinforcedConcrete.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.ReinforcedConcrete.getStaticTemperature(), 2448)
        self.assertEqual(liner.ReinforcedConcrete.getConductivity(), 167)
        self.assertEqual(liner.ReinforcedConcrete.getSpecificHeatCapacity(), 2995)
        self.assertEqual(liner.ReinforcedConcrete.getThermalExpansion(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getExpansionCoefficient(), 2197)
        self.assertEqual(liner.ReinforcedConcrete.getStageConcreteProperties(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getStaticTemperatureGridToUse(), "None")
