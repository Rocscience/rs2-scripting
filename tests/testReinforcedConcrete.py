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
        liner.ReinforcedConcrete.setConcreteUnitWeight(2236.1)
        liner.ReinforcedConcrete.setIncludeWeightInAnalysis(1)
        liner.ReinforcedConcrete.setReinforcement(True)
        liner.ReinforcedConcrete.setSpacing(1416.1)
        liner.ReinforcedConcrete.setSectionDepth(1633.6)
        liner.ReinforcedConcrete.setArea(1333.7)
        liner.ReinforcedConcrete.setMomentOfInertia(1837.3)
        liner.ReinforcedConcrete.setConcreteYoungsModulus(94.3)
        liner.ReinforcedConcrete.setConcreteCompressiveStrength(260.9)
        liner.ReinforcedConcrete.setConcreteTensileStrength(3117.2)
        liner.ReinforcedConcrete.setWeight(2355.2)
        liner.ReinforcedConcrete.setConcrete(0)
        liner.ReinforcedConcrete.setThickness(697.2)
        liner.ReinforcedConcrete.setYoungsModulus(75.4)
        liner.ReinforcedConcrete.setPoissonRatio(190.8)
        liner.ReinforcedConcrete.setCompressiveStrength(1870.0)
        liner.ReinforcedConcrete.setTensileStrength(2933.1)
        liner.ReinforcedConcrete.setMaterialType(MaterialType.PLASTIC)
        liner.ReinforcedConcrete.setSlidingGap(0)
        liner.ReinforcedConcrete.setStrainAtLocking(3106.8)
        liner.ReinforcedConcrete.setBeamElementFormulation(LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        liner.ReinforcedConcrete.setActivateThermal(0)
        liner.ReinforcedConcrete.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.ReinforcedConcrete.setStaticTemperature(2512.8)
        liner.ReinforcedConcrete.setConductivity(1979.3)
        liner.ReinforcedConcrete.setSpecificHeatCapacity(1436.4)
        liner.ReinforcedConcrete.setThermalExpansion(0)
        liner.ReinforcedConcrete.setExpansionCoefficient(2578.3)
        liner.ReinforcedConcrete.setStageConcreteProperties(1)
        liner.ReinforcedConcrete.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.ReinforcedConcrete.getConcreteUnitWeight(), 2236.1)
        self.assertEqual(liner.ReinforcedConcrete.getIncludeWeightInAnalysis(), 1)
        self.assertEqual(liner.ReinforcedConcrete.getReinforcement(), True)
        self.assertEqual(liner.ReinforcedConcrete.getSpacing(), 1416.1)
        self.assertEqual(liner.ReinforcedConcrete.getSectionDepth(), 1633.6)
        self.assertEqual(liner.ReinforcedConcrete.getArea(), 1333.7)
        self.assertEqual(liner.ReinforcedConcrete.getMomentOfInertia(), 1837.3)
        self.assertEqual(liner.ReinforcedConcrete.getConcreteYoungsModulus(), 94.3)
        self.assertEqual(liner.ReinforcedConcrete.getConcreteCompressiveStrength(), 260.9)
        self.assertEqual(liner.ReinforcedConcrete.getConcreteTensileStrength(), 3117.2)
        self.assertEqual(liner.ReinforcedConcrete.getWeight(), 2355.2)
        self.assertEqual(liner.ReinforcedConcrete.getConcrete(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getThickness(), 697.2)
        self.assertEqual(liner.ReinforcedConcrete.getYoungsModulus(), 75.4)
        self.assertEqual(liner.ReinforcedConcrete.getPoissonRatio(), 190.8)
        self.assertEqual(liner.ReinforcedConcrete.getCompressiveStrength(), 1870.0)
        self.assertEqual(liner.ReinforcedConcrete.getTensileStrength(), 2933.1)
        self.assertEqual(liner.ReinforcedConcrete.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.ReinforcedConcrete.getSlidingGap(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getStrainAtLocking(), 3106.8)
        self.assertEqual(liner.ReinforcedConcrete.getBeamElementFormulation(), LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        self.assertEqual(liner.ReinforcedConcrete.getActivateThermal(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.ReinforcedConcrete.getStaticTemperature(), 2512.8)
        self.assertEqual(liner.ReinforcedConcrete.getConductivity(), 1979.3)
        self.assertEqual(liner.ReinforcedConcrete.getSpecificHeatCapacity(), 1436.4)
        self.assertEqual(liner.ReinforcedConcrete.getThermalExpansion(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getExpansionCoefficient(), 2578.3)
        self.assertEqual(liner.ReinforcedConcrete.getStageConcreteProperties(), 1)
        self.assertEqual(liner.ReinforcedConcrete.getStaticTemperatureGridToUse(), "None")
