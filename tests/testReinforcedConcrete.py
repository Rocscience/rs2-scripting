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
        liner.ReinforcedConcrete.setConcreteUnitWeight(2512.8)
        liner.ReinforcedConcrete.setIncludeWeightInAnalysis(0)
        liner.ReinforcedConcrete.setReinforcement(True)
        liner.ReinforcedConcrete.setSpacing(519.0)
        liner.ReinforcedConcrete.setSectionDepth(2655.5)
        liner.ReinforcedConcrete.setArea(2779.9)
        liner.ReinforcedConcrete.setMomentOfInertia(1868.2)
        liner.ReinforcedConcrete.setConcreteYoungsModulus(171.0)
        liner.ReinforcedConcrete.setConcreteCompressiveStrength(2925.6)
        liner.ReinforcedConcrete.setConcreteTensileStrength(1867.7)
        liner.ReinforcedConcrete.setWeight(3071.2)
        liner.ReinforcedConcrete.setConcrete(0)
        liner.ReinforcedConcrete.setThickness(2416.0)
        liner.ReinforcedConcrete.setYoungsModulus(2750.5)
        liner.ReinforcedConcrete.setPoissonRatio(899.6)
        liner.ReinforcedConcrete.setCompressiveStrength(505.3)
        liner.ReinforcedConcrete.setTensileStrength(1549.2)
        liner.ReinforcedConcrete.setMaterialType(MaterialType.PLASTIC)
        liner.ReinforcedConcrete.setSlidingGap(0)
        liner.ReinforcedConcrete.setStrainAtLocking(2203.7)
        liner.ReinforcedConcrete.setBeamElementFormulation(LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        liner.ReinforcedConcrete.setActivateThermal(0)
        liner.ReinforcedConcrete.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.ReinforcedConcrete.setStaticTemperature(3047.0)
        liner.ReinforcedConcrete.setConductivity(25.0)
        liner.ReinforcedConcrete.setSpecificHeatCapacity(826.6)
        liner.ReinforcedConcrete.setThermalExpansion(1)
        liner.ReinforcedConcrete.setExpansionCoefficient(3090.6)
        liner.ReinforcedConcrete.setStageConcreteProperties(0)
        liner.ReinforcedConcrete.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.ReinforcedConcrete.getConcreteUnitWeight(), 2512.8)
        self.assertEqual(liner.ReinforcedConcrete.getIncludeWeightInAnalysis(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getReinforcement(), True)
        self.assertEqual(liner.ReinforcedConcrete.getSpacing(), 519.0)
        self.assertEqual(liner.ReinforcedConcrete.getSectionDepth(), 2655.5)
        self.assertEqual(liner.ReinforcedConcrete.getArea(), 2779.9)
        self.assertEqual(liner.ReinforcedConcrete.getMomentOfInertia(), 1868.2)
        self.assertEqual(liner.ReinforcedConcrete.getConcreteYoungsModulus(), 171.0)
        self.assertEqual(liner.ReinforcedConcrete.getConcreteCompressiveStrength(), 2925.6)
        self.assertEqual(liner.ReinforcedConcrete.getConcreteTensileStrength(), 1867.7)
        self.assertEqual(liner.ReinforcedConcrete.getWeight(), 3071.2)
        self.assertEqual(liner.ReinforcedConcrete.getConcrete(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getThickness(), 2416.0)
        self.assertEqual(liner.ReinforcedConcrete.getYoungsModulus(), 2750.5)
        self.assertEqual(liner.ReinforcedConcrete.getPoissonRatio(), 899.6)
        self.assertEqual(liner.ReinforcedConcrete.getCompressiveStrength(), 505.3)
        self.assertEqual(liner.ReinforcedConcrete.getTensileStrength(), 1549.2)
        self.assertEqual(liner.ReinforcedConcrete.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.ReinforcedConcrete.getSlidingGap(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getStrainAtLocking(), 2203.7)
        self.assertEqual(liner.ReinforcedConcrete.getBeamElementFormulation(), LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        self.assertEqual(liner.ReinforcedConcrete.getActivateThermal(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.ReinforcedConcrete.getStaticTemperature(), 3047.0)
        self.assertEqual(liner.ReinforcedConcrete.getConductivity(), 25.0)
        self.assertEqual(liner.ReinforcedConcrete.getSpecificHeatCapacity(), 826.6)
        self.assertEqual(liner.ReinforcedConcrete.getThermalExpansion(), 1)
        self.assertEqual(liner.ReinforcedConcrete.getExpansionCoefficient(), 3090.6)
        self.assertEqual(liner.ReinforcedConcrete.getStageConcreteProperties(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getStaticTemperatureGridToUse(), "None")
