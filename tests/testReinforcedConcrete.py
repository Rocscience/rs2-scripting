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
        blankModelPath = f"{parentDirectory}/resources/blankProject.fez"
        self.liner = self.model.getAllLinerProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testReinforcedConcreteProperty(self):
        liner = self.liner
        self.liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)
        liner.ReinforcedConcrete.setReinforcement(True)
        liner.ReinforcedConcrete.setIncludeWeightInAnalysis(True)
        liner.ReinforcedConcrete.setConcreteUnitWeight(10.1)
        liner.ReinforcedConcrete.setSpacing(10.1)
        liner.ReinforcedConcrete.setSectionDepth(10.1)
        liner.ReinforcedConcrete.setConcreteYoungsModulus(10.1)
        liner.ReinforcedConcrete.setArea(10.1)
        liner.ReinforcedConcrete.setMomentOfInertia(10.1)
        liner.ReinforcedConcrete.setConcreteCompressiveStrength(10.1)
        liner.ReinforcedConcrete.setConcreteTensileStrength(10.1)
        liner.ReinforcedConcrete.setWeight(10.1)
        liner.ReinforcedConcrete.setConcrete(True)
        liner.ReinforcedConcrete.setThickness(10.1)
        liner.ReinforcedConcrete.setYoungsModulus(10.1)
        liner.ReinforcedConcrete.setPoissonRatio(10.1)
        liner.ReinforcedConcrete.setCompressiveStrength(10.1)
        liner.ReinforcedConcrete.setTensileStrength(10.1)
        liner.ReinforcedConcrete.setMaterialType(MaterialType.PLASTIC)
        liner.ReinforcedConcrete.setSlidingGap(True)
        liner.ReinforcedConcrete.setStrainAtLocking(10.1)
        liner.ReinforcedConcrete.setBeamElementFormulation(LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        liner.ReinforcedConcrete.setActivateThermal(True)
        liner.ReinforcedConcrete.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.ReinforcedConcrete.setStaticTemperature(10.1)
        liner.ReinforcedConcrete.setConductivity(10.1)
        liner.ReinforcedConcrete.setSpecificHeatCapacity(10.1)
        liner.ReinforcedConcrete.setThermalExpansion(True)
        liner.ReinforcedConcrete.setExpansionCoefficient(10.1)
        liner.ReinforcedConcrete.setStageConcreteProperties(True)
        liner.ReinforcedConcrete.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.ReinforcedConcrete.getReinforcement(), True)
        self.assertEqual(liner.ReinforcedConcrete.getIncludeWeightInAnalysis(), True)
        self.assertEqual(liner.ReinforcedConcrete.getConcreteUnitWeight(), 10.1)
        self.assertEqual(liner.ReinforcedConcrete.getSpacing(), 10.1)
        self.assertEqual(liner.ReinforcedConcrete.getSectionDepth(), 10.1)
        self.assertEqual(liner.ReinforcedConcrete.getConcreteYoungsModulus(), 10.1)
        self.assertEqual(liner.ReinforcedConcrete.getArea(), 10.1)
        self.assertEqual(liner.ReinforcedConcrete.getMomentOfInertia(), 10.1)
        self.assertEqual(liner.ReinforcedConcrete.getConcreteCompressiveStrength(), 10.1)
        self.assertEqual(liner.ReinforcedConcrete.getConcreteTensileStrength(), 10.1)
        self.assertEqual(liner.ReinforcedConcrete.getWeight(), 10.1)
        self.assertEqual(liner.ReinforcedConcrete.getConcrete(), True)
        self.assertEqual(liner.ReinforcedConcrete.getThickness(), 10.1)
        self.assertEqual(liner.ReinforcedConcrete.getYoungsModulus(), 10.1)
        self.assertEqual(liner.ReinforcedConcrete.getPoissonRatio(), 10.1)
        self.assertEqual(liner.ReinforcedConcrete.getCompressiveStrength(), 10.1)
        self.assertEqual(liner.ReinforcedConcrete.getTensileStrength(), 10.1)
        self.assertEqual(liner.ReinforcedConcrete.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.ReinforcedConcrete.getSlidingGap(), True)
        self.assertEqual(liner.ReinforcedConcrete.getStrainAtLocking(), 10.1)
        self.assertEqual(liner.ReinforcedConcrete.getBeamElementFormulation(), LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        self.assertEqual(liner.ReinforcedConcrete.getActivateThermal(), True)
        self.assertEqual(liner.ReinforcedConcrete.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.ReinforcedConcrete.getStaticTemperature(), 10.1)
        self.assertEqual(liner.ReinforcedConcrete.getConductivity(), 10.1)
        self.assertEqual(liner.ReinforcedConcrete.getSpecificHeatCapacity(), 10.1)
        self.assertEqual(liner.ReinforcedConcrete.getThermalExpansion(), True)
        self.assertEqual(liner.ReinforcedConcrete.getExpansionCoefficient(), 10.1)
        self.assertEqual(liner.ReinforcedConcrete.getStageConcreteProperties(), True)
        self.assertEqual(liner.ReinforcedConcrete.getStaticTemperatureGridToUse(), "None")
