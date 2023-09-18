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
        liner.ReinforcedConcrete.setConcreteUnitWeight(2933.1)
        liner.ReinforcedConcrete.setIncludeWeightInAnalysis(0)
        liner.ReinforcedConcrete.setReinforcement(True)
        liner.ReinforcedConcrete.setSpacing(3106.8)
        liner.ReinforcedConcrete.setSectionDepth(1102.7)
        liner.ReinforcedConcrete.setArea(2512.8)
        liner.ReinforcedConcrete.setMomentOfInertia(1979.3)
        liner.ReinforcedConcrete.setConcreteYoungsModulus(1436.4)
        liner.ReinforcedConcrete.setConcreteCompressiveStrength(3131.0)
        liner.ReinforcedConcrete.setConcreteTensileStrength(2578.3)
        liner.ReinforcedConcrete.setWeight(2486.5)
        liner.ReinforcedConcrete.setConcrete(0)
        liner.ReinforcedConcrete.setThickness(2080.7)
        liner.ReinforcedConcrete.setYoungsModulus(2604.8)
        liner.ReinforcedConcrete.setPoissonRatio(3198.2)
        liner.ReinforcedConcrete.setCompressiveStrength(720.8)
        liner.ReinforcedConcrete.setTensileStrength(952.3)
        liner.ReinforcedConcrete.setMaterialType(MaterialType.PLASTIC)
        liner.ReinforcedConcrete.setSlidingGap(0)
        liner.ReinforcedConcrete.setStrainAtLocking(2825.2)
        liner.ReinforcedConcrete.setBeamElementFormulation(LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        liner.ReinforcedConcrete.setActivateThermal(0)
        liner.ReinforcedConcrete.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
        liner.ReinforcedConcrete.setStaticTemperature(1382.6)
        liner.ReinforcedConcrete.setConductivity(907.2)
        liner.ReinforcedConcrete.setSpecificHeatCapacity(1372.2)
        liner.ReinforcedConcrete.setThermalExpansion(0)
        liner.ReinforcedConcrete.setExpansionCoefficient(919.8)
        liner.ReinforcedConcrete.setStageConcreteProperties(1)
        liner.ReinforcedConcrete.setStaticTemperatureGridToUse("None")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]
        liner = self.liner
        self.assertEqual(liner.ReinforcedConcrete.getConcreteUnitWeight(), 2933.1)
        self.assertEqual(liner.ReinforcedConcrete.getIncludeWeightInAnalysis(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getReinforcement(), True)
        self.assertEqual(liner.ReinforcedConcrete.getSpacing(), 3106.8)
        self.assertEqual(liner.ReinforcedConcrete.getSectionDepth(), 1102.7)
        self.assertEqual(liner.ReinforcedConcrete.getArea(), 2512.8)
        self.assertEqual(liner.ReinforcedConcrete.getMomentOfInertia(), 1979.3)
        self.assertEqual(liner.ReinforcedConcrete.getConcreteYoungsModulus(), 1436.4)
        self.assertEqual(liner.ReinforcedConcrete.getConcreteCompressiveStrength(), 3131.0)
        self.assertEqual(liner.ReinforcedConcrete.getConcreteTensileStrength(), 2578.3)
        self.assertEqual(liner.ReinforcedConcrete.getWeight(), 2486.5)
        self.assertEqual(liner.ReinforcedConcrete.getConcrete(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getThickness(), 2080.7)
        self.assertEqual(liner.ReinforcedConcrete.getYoungsModulus(), 2604.8)
        self.assertEqual(liner.ReinforcedConcrete.getPoissonRatio(), 3198.2)
        self.assertEqual(liner.ReinforcedConcrete.getCompressiveStrength(), 720.8)
        self.assertEqual(liner.ReinforcedConcrete.getTensileStrength(), 952.3)
        self.assertEqual(liner.ReinforcedConcrete.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.ReinforcedConcrete.getSlidingGap(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getStrainAtLocking(), 2825.2)
        self.assertEqual(liner.ReinforcedConcrete.getBeamElementFormulation(), LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
        self.assertEqual(liner.ReinforcedConcrete.getActivateThermal(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
        self.assertEqual(liner.ReinforcedConcrete.getStaticTemperature(), 1382.6)
        self.assertEqual(liner.ReinforcedConcrete.getConductivity(), 907.2)
        self.assertEqual(liner.ReinforcedConcrete.getSpecificHeatCapacity(), 1372.2)
        self.assertEqual(liner.ReinforcedConcrete.getThermalExpansion(), 0)
        self.assertEqual(liner.ReinforcedConcrete.getExpansionCoefficient(), 919.8)
        self.assertEqual(liner.ReinforcedConcrete.getStageConcreteProperties(), 1)
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
