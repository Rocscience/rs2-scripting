
import unittest
import os, sys, inspect
import shutil
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*
from rs2.utilities.ColorPicker import ColorPicker


class Test_pile_unit_test(unittest.TestCase):
    
    def setUp(self):
        pass

        
    def tearDown(self):
        pass

    def test1(self):


        #parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"c:/Intel/starterProject.fez"
        self.copiedModelPath = f"c:/Intel/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        modeler = RS2Modeler()
        model = modeler.openFile(self.copiedModelPath)
        pile = model.getAllPileProperties()[0]

        pile.setPileName("Pile 1")
        #1
        pile.setSkinResistance(PileSkinResistanceType.MOHR_COULOMB)
        pile.MohrCoulombPile.setShearStiffness(1.1)
        pile.MohrCoulombPile.setNormalStiffness(2.2) 
        pile.MohrCoulombPile.setFrictionAngle(30)
        pile.MohrCoulombPile.setResidualFrictionAngle(30)
        pile.MohrCoulombPile.setCohesion(0)
        pile.MohrCoulombPile.setResidualCohesion(0)
        pile.MohrCoulombPile.setUseShearResistanceCutoff(0)
        pile.MohrCoulombPile.setPerimeter(1)
        pile.MohrCoulombPile.setUseBaseResistance(1)
        pile.MohrCoulombPile.setBaseNormalStiffness(100000)
        pile.MohrCoulombPile.setBaseForceResistance(0.1)

        self.assertEqual(pile.MohrCoulombPile.getShearStiffness(), 1.1)
        self.assertEqual(pile.MohrCoulombPile.getNormalStiffness(), 2.2)
        self.assertEqual(pile.MohrCoulombPile.getFrictionAngle(), 30)
        self.assertEqual(pile.MohrCoulombPile.getResidualFrictionAngle(), 30)
        self.assertEqual(pile.MohrCoulombPile.getCohesion(), 0)
        self.assertEqual(pile.MohrCoulombPile.getResidualCohesion(), 0)
        self.assertEqual(pile.MohrCoulombPile.getUseShearResistanceCutoff(), 0) 
        self.assertEqual(pile.MohrCoulombPile.getPerimeter(), 1)
        self.assertEqual(pile.MohrCoulombPile.getUseBaseResistance(), 1)
        self.assertEqual(pile.MohrCoulombPile.getBaseNormalStiffness(), 100000)
        self.assertEqual(pile.MohrCoulombPile.getBaseForceResistance(), 0.1)



        #2
        pile.setSkinResistance(PileSkinResistanceType.ELASTIC)
        pile.Elastic.setShearStiffness(1) 
        pile.Elastic.setNormalStiffness(2)
        
        pile.Elastic.setUseBaseResistance(True)
        pile.Elastic.setBaseNormalStiffness(3)
        pile.Elastic.setBaseForceResistance(4)

        self.assertEqual(pile.Elastic.getShearStiffness(), 1)
        self.assertEqual(pile.Elastic.getNormalStiffness(), 2)
        
        self.assertEqual(pile.Elastic.getUseBaseResistance(), True)
        self.assertEqual(pile.Elastic.getBaseNormalStiffness(), 3)
        self.assertEqual(pile.Elastic.getBaseForceResistance(), 4)


        #3
        pile.setSkinResistance(PileSkinResistanceType.MULTI_LINEAR)
        pile.MultiLinear.setShearStiffness(1.1)
        pile.MultiLinear.setNormalStiffness(2.2)
        pile.MultiLinear.setDefinitionMethod(PileDefinitionMethod.DISTANCE_FROM_TOP)
    
        pile.MultiLinear.setUseBaseResistance(True)
        pile.MultiLinear.setBaseNormalStiffness(3.3)
        pile.MultiLinear.setBaseForceResistance(4.4)


        pile.MultiLinear.setCoordinates([1,2,3,5.456],[4,5,6,7])

        self.assertEqual(pile.MultiLinear.getShearStiffness(), 1.1)
        self.assertEqual(pile.MultiLinear.getNormalStiffness(), 2.2)
        self.assertEqual(pile.MultiLinear.getDefinitionMethod(), PileDefinitionMethod.DISTANCE_FROM_TOP)
    

        self.assertEqual(pile.MultiLinear.getUseBaseResistance(), True)
        self.assertEqual(pile.MultiLinear.getBaseNormalStiffness(), 3.3) 
        self.assertEqual(pile.MultiLinear.getBaseForceResistance(), 4.4)
        self.assertEqual(pile.MultiLinear.getCoordinates(), ([1,2,3,5.456],[4,5,6,7]))
        #4
        pile.setSkinResistance(PileSkinResistanceType.MATERIAL_DEPENDENT)
        pile.MaterialDependentPile.setInterfaceCoefficient(1.2)
        pile.MaterialDependentPile.setUseStiffnessMaterialDependent(True)
        pile.MaterialDependentPile.setStiffnessCoefficient(2.2)
        pile.MaterialDependentPile.setUseShearResistanceCutoff(True)
        pile.MaterialDependentPile.setShearResistanceCutoff(3.4)
        pile.MaterialDependentPile.setPerimeter(5.6)
        
        pile.MaterialDependentPile.setUseBaseResistance(True)
        pile.MaterialDependentPile.setBaseNormalStiffness(3.3)
        pile.MaterialDependentPile.setBaseForceResistance(4.4)

        self.assertEqual(pile.MaterialDependentPile.getInterfaceCoefficient(), 1.2)
        self.assertEqual(pile.MaterialDependentPile.getUseStiffnessMaterialDependent(), True)
        self.assertEqual(pile.MaterialDependentPile.getStiffnessCoefficient(), 2.2)
        self.assertEqual(pile.MaterialDependentPile.getUseShearResistanceCutoff(), True)
        self.assertEqual(pile.MaterialDependentPile.getShearResistanceCutoff(), 3.4)
        self.assertEqual(pile.MaterialDependentPile.getPerimeter(), 5.6)
        
        self.assertEqual(pile.MaterialDependentPile.getUseBaseResistance(), True)
        self.assertEqual(pile.MaterialDependentPile.getBaseNormalStiffness(), 3.3)
        self.assertEqual(pile.MaterialDependentPile.getBaseForceResistance(), 4.4)
        
        
        
        pile.setStageForceDisplacement(True)
        pile.ForceDisplacement.setApply(PileEndCondition.DISPLACEMENT)
        pile.ForceDisplacement.setApplyOn(PileForceApplicationPoint.FP_TOP)
        pile.ForceDisplacement.setX(10.0)
        pile.ForceDisplacement.setY(20.0)

        self.assertEqual(pile.ForceDisplacement.getApply(), PileEndCondition.DISPLACEMENT)
        self.assertEqual(pile.ForceDisplacement.getApplyOn(), PileForceApplicationPoint.TOP)
        self.assertEqual(pile.ForceDisplacement.getX(), 10.0)
        self.assertEqual(pile.ForceDisplacement.getY(), 20.0)


        pile.setStageForceDisplacement(True)
        pile.ForceDisplacement.setApply(PileEndCondition.FORCE)
        pile.ForceDisplacement.setApplyOn(PileForceApplicationPoint.BOTTOM)
        pile.ForceDisplacement.setX(10.456)
        pile.ForceDisplacement.setY(20.789)

        self.assertEqual(pile.ForceDisplacement.getApply(), PileEndCondition.FORCE)
        self.assertEqual(pile.ForceDisplacement.getApplyOn(), PileForceApplicationPoint.BOTTOM)
        self.assertEqual(pile.ForceDisplacement.getX(), 10.456)
        self.assertEqual(pile.ForceDisplacement.getY(), 20.789)

        pile.setLength(4.3)
        pile.setConnectionType(PileConnectionType.SEMI_RIGID)
        pile.setOutOfPlaneSpacing(123.456)
        pile.setMMax(123.111)

        self.assertEqual(pile.getLength(), 4.3)
        self.assertEqual(pile.getConnectionType(), PileConnectionType.SEMI_RIGID)
        self.assertEqual(pile.getOutOfPlaneSpacing() ,123.456)
        self.assertEqual(pile.getMMax(), 123.111)

        ColorPicker.getColorFromRGB(42, 60, 91)
        r, g, b = ColorPicker.getRGBFromColor(pile.getPileColor())


        bolts = model.getAllBoltProperties()
        bolt = bolts[0]
    
            # Bolt 1
        bolt.setBoltType(BoltTypes.TIEBACK)
        bolt.Tieback.setBoltDiameter(1)
        bolt.Tieback.setBoltModulusE(134)
        bolt.Tieback.setBoltModel(BoltModels.PLASTIC)
        bolt.Tieback.setTensileCapacity(3)
        bolt.Tieback.setResidualTensileCapacity(4)
        bolt.Tieback.setOutofPlaneSpacing(123)
        bolt.Tieback.setMaterialDependent(True)
        bolt.Tieback.setBondStrengthCoefficient(6)
        bolt.Tieback.setBondShearStiffnessCoefficient(7)
        bolt.Tieback.setJointShear(True)
        bolt.Tieback.setBoreholeDiameter(8)
        bolt.Tieback.setPreTensioningForce(9)
        bolt.Tieback.setConstantPretensioningForceInInstallStage(True)
        bolt.Tieback.setFacePlates(True)
        bolt.Tieback.setAddPullOutForce(True)
        bolt.Tieback.setPullOutForce(10)
        bolt.Tieback.setUseBondPercentageLength(True)
        bolt.Tieback.setPercentageBondLength(11)
        bolt.Tieback.setUseSecondaryBondLength(True)
        bolt.Tieback.setSecondaryBondLengthType(SecondaryBondLengthType.PERCENTAGE_OF_LENGTH)
        bolt.Tieback.setPercentOfSecondaryBondLength(12)
        bolt.Tieback.setDelayInstallAfterBolt(13)


    
        self.assertEqual(bolt.getBoltType(), BoltTypes.TIEBACK)
        self.assertEqual(bolt.Tieback.getBoltDiameter(), 1)
        self.assertEqual(bolt.Tieback.getBoltModulusE(),134)
        self.assertEqual(bolt.Tieback.getBoltModel(), BoltModels.PLASTIC)
        self.assertEqual(bolt.Tieback.getTensileCapacity(), 3)
        self.assertEqual(bolt.Tieback.getResidualTensileCapacity(), 4)
        self.assertEqual(bolt.Tieback.getOutofPlaneSpacing(), 123)
        self.assertEqual(bolt.Tieback.getMaterialDependent(), True)
        self.assertEqual(bolt.Tieback.getBondStrengthCoefficient(), 6)
        self.assertEqual(bolt.Tieback.getBondShearStiffnessCoefficient(), 7)
        self.assertEqual(bolt.Tieback.getJointShear(), True)
        self.assertEqual(bolt.Tieback.getBoreholeDiameter(), 8)
        self.assertEqual(bolt.Tieback.getPreTensioningForce(), 9)
        self.assertEqual(bolt.Tieback.getConstantPretensioningForceInInstallStage(), True)
        self.assertEqual(bolt.Tieback.getFacePlates(), True)
        self.assertEqual(bolt.Tieback.getAddPullOutForce(), True)
        self.assertEqual(bolt.Tieback.getPullOutForce(), 10)
        self.assertEqual(bolt.Tieback.getUseBondPercentageLength(), True)
        self.assertEqual(bolt.Tieback.getPercentageBondLength(), 11)
        self.assertEqual(bolt.Tieback.getUseSecondaryBondLength(), True)
        self.assertEqual(bolt.Tieback.getSecondaryBondLengthType(), SecondaryBondLengthType.PERCENTAGE_OF_LENGTH)
        self.assertEqual(bolt.Tieback.getPercentOfSecondaryBondLength(), 12)
        self.assertEqual(bolt.Tieback.getDelayInstallAfterBolt(), 13)


        bolt.setBoltColor(ColorPicker.getColorFromRGB(255, 255, 10));



        liner = model.getLinerPropertyByName("Liner 1")
    
        liner.CableTruss.setUnitWeight(127.318)
        liner.CableTruss.setInitialTemperature(0) 
        liner.CableTruss.setCableDiameter(0.71)
        liner.CableTruss.setOutofplaneSpacing(1)
        liner.CableTruss.setYoungsModulus(4.17709e+09)
        liner.CableTruss.setMaterialType(MaterialType.ELASTIC)
        liner.CableTruss.setTensileStrengthPeak(1.04427e+07)
        liner.CableTruss.setTensileStrengthResidual(1.04427e+07)
        liner.CableTruss.setPreTensioning(True)
        liner.CableTruss.setPreTensioningForce(0)
        liner.CableTruss.setAxialStrainExpansion(0)
        liner.CableTruss.setActivateThermal(True)
        liner.CableTruss.setConductivity(1)
        liner.CableTruss.setSpecificHeatCapacity(2.11)
        liner.CableTruss.setThermalExpansion(True)
        liner.CableTruss.setExpansionCoefficient(3.11)
        liner.CableTruss.setStageCableProperties(True)




        #2
        liner.setLinerType(LinerTypes.REINFORCED_CONCRETE)
        liner.ReinforcedConcrete.setIncludeWeightInStressAnalysis(True)
        liner.ReinforcedConcrete.setConcreteUnitWeight(1)
    
        liner.ReinforcedConcrete.setReinforcement(True)
        # Set common type
        reinforce = liner.ReinforcedConcrete

        liner.ReinforcedConcrete.setSpacing(2.11)
        liner.ReinforcedConcrete.setSectionDepth(3.11)
        liner.ReinforcedConcrete.setArea(4.11)
        liner.ReinforcedConcrete.setMomentOfInertia(5.11)
        liner.ReinforcedConcrete.setConcreteYoungsModulus(6.11)
        liner.ReinforcedConcrete.setConcreteCompressiveStrength(7.11)
        liner.ReinforcedConcrete.setConcreteTensileStrength(8.11)
        liner.ReinforcedConcrete.setWeight(9.11)
    
        liner.ReinforcedConcrete.setConcrete(True)
        liner.ReinforcedConcrete.setThickness(10.11)
        liner.ReinforcedConcrete.setYoungsModulus(11.11)
        liner.ReinforcedConcrete.setPoissonRatio(12.11)
        liner.ReinforcedConcrete.setCompressiveStrength(13.11)
        liner.ReinforcedConcrete.setTensileStrength(14.11)
    
        liner.ReinforcedConcrete.setMaterialType(MaterialType.ELASTIC)
        liner.ReinforcedConcrete.setSlidingGap(True)
        liner.ReinforcedConcrete.setStrainAtLocking(15.11)
        liner.ReinforcedConcrete.setBeamElementFormulation(LinerFormulation.BERNOULLI)
        liner.ReinforcedConcrete.setAxialStrainExpansion(16.11)
    
        liner.ReinforcedConcrete.setStageConcreteProperties(True)




        bolts = model.getAllBoltProperties()
        bolt = bolts[0]




        bolt.setBoltType(BoltTypes.FULLY_BONDED)

        bolt.FullyBonded.setBoltDiameter(12.12)
        bolt.FullyBonded.setBoltModulusE(12.13) 
        bolt.FullyBonded.setTensileCapacity(12.14)
        bolt.FullyBonded.setResidualTensileCapacity(12.15)
        bolt.FullyBonded.setOutofPlaneSpacing(12.16)
        bolt.FullyBonded.setPreTensioningForce(12.17)
        bolt.FullyBonded.setConstantPretensioningForceInInstallStage(False)
        bolt.FullyBonded.setJointShear(False)
        
        self.assertEqual(bolt.FullyBonded.getBoltDiameter(), 12.12)
        self.assertEqual(bolt.FullyBonded.getBoltModulusE(), 12.13)
        self.assertEqual(bolt.FullyBonded.getTensileCapacity(), 12.14)
        self.assertEqual(bolt.FullyBonded.getResidualTensileCapacity(), 12.15)
        self.assertEqual(bolt.FullyBonded.getOutofPlaneSpacing(), 12.16)
        self.assertEqual(bolt.FullyBonded.getPreTensioningForce(), 12.17)
        self.assertEqual(bolt.FullyBonded.getConstantPretensioningForceInInstallStage(), False)
        self.assertEqual(bolt.FullyBonded.getJointShear(), False)
        





        
        bolt.setBoltType(BoltTypes.PLAIN_STRAND_CABLE)
        bolt.PlainStrandCable.setBoreholeDiameter(1.31)
        bolt.PlainStrandCable.setCableDiameter(1.2)
        bolt.PlainStrandCable.setCableModulusE(1.3)
        bolt.PlainStrandCable.setCablePeak(1.4)
        bolt.PlainStrandCable.setOutofPlaneSpacing(1.5)
        bolt.PlainStrandCable.setWaterCementRatio(0.6)
        bolt.PlainStrandCable.setJointShear(True)
        bolt.PlainStrandCable.setFacePlates(True)
        bolt.PlainStrandCable.setAddPullOutForce(True)
        bolt.PlainStrandCable.setPullOutForce(1.7)
        bolt.PlainStrandCable.setConstantShearStiffness(True)
        bolt.PlainStrandCable.setStiffness(1.8)
        bolt.PlainStrandCable.setAddBulges(True)

        self.assertEqual(bolt.PlainStrandCable.getBoreholeDiameter(), 1.31)
        self.assertEqual(bolt.PlainStrandCable.getCableDiameter(), 1.2)
        self.assertEqual(bolt.PlainStrandCable.getCableModulusE(), 1.3)
        self.assertEqual(bolt.PlainStrandCable.getCablePeak(), 1.4)
        self.assertEqual(bolt.PlainStrandCable.getOutofPlaneSpacing(), 1.5)
        self.assertEqual(bolt.PlainStrandCable.getWaterCementRatio(), 0.6)
        self.assertEqual(bolt.PlainStrandCable.getJointShear(), True)
        self.assertEqual(bolt.PlainStrandCable.getFacePlates(), True)
        self.assertEqual(bolt.PlainStrandCable.getAddPullOutForce(), True)
        self.assertEqual(bolt.PlainStrandCable.getPullOutForce(), 1.7)
        self.assertEqual(bolt.PlainStrandCable.getConstantShearStiffness(), True)
        self.assertEqual(bolt.PlainStrandCable.getStiffness(), 1.8)
        self.assertTrue(bolt.PlainStrandCable.getAddBulges())


        bolt.setBoltType(BoltTypes.FULLY_BONDED)
        bolt.FullyBonded.setBoltDiameter(1.1)
        bolt.FullyBonded.setBoltModulusE(1.2)
        bolt.FullyBonded.setTensileCapacity(1.3)
        bolt.FullyBonded.setResidualTensileCapacity(1.4)
        bolt.FullyBonded.setOutofPlaneSpacing(1.5)
        bolt.FullyBonded.setPreTensioningForce(1.6)
        bolt.FullyBonded.setConstantPretensioningForceInInstallStage(True)
        bolt.FullyBonded.setJointShear(True)
        self.assertEqual(bolt.getBoltType(), BoltTypes.FULLY_BONDED)
        self.assertEqual(bolt.FullyBonded.getBoltDiameter(), 1.1)
        self.assertEqual(bolt.FullyBonded.getBoltModulusE(), 1.2)
        self.assertEqual(bolt.FullyBonded.getTensileCapacity(), 1.3)
        self.assertEqual(bolt.FullyBonded.getResidualTensileCapacity(), 1.4)
        self.assertEqual(bolt.FullyBonded.getOutofPlaneSpacing(), 1.5)
        self.assertEqual(bolt.FullyBonded.getPreTensioningForce(), 1.6)
        self.assertEqual(bolt.FullyBonded.getConstantPretensioningForceInInstallStage(), True) 
        self.assertEqual(bolt.FullyBonded.getJointShear(), True)

        




        bolt.setBoltType(BoltTypes.FULLY_BONDED)
        bolt.FullyBonded.setBoltDiameter(1.2)
        bolt.FullyBonded.setBoltModulusE(1.3)
        bolt.FullyBonded.setTensileCapacity(1.4)
        bolt.FullyBonded.setResidualTensileCapacity(1.5)
        bolt.FullyBonded.setOutofPlaneSpacing(1.6)
        bolt.FullyBonded.setPreTensioningForce(1.7)
        bolt.FullyBonded.setConstantPretensioningForceInInstallStage(True)
        bolt.FullyBonded.setJointShear(True)




        self.assertEqual(bolt.FullyBonded.getBoltDiameter(), 1.2)
        self.assertEqual(bolt.FullyBonded.getBoltModulusE(), 1.3)
        self.assertEqual(bolt.FullyBonded.getTensileCapacity(), 1.4)
        self.assertEqual(bolt.FullyBonded.getResidualTensileCapacity(), 1.5)
        self.assertEqual(bolt.FullyBonded.getOutofPlaneSpacing(), 1.6)
        self.assertEqual(bolt.FullyBonded.getPreTensioningForce(), 1.7)






        liner = model.getLinerPropertyByName("Liner 1")
    
        liner.CableTruss.setUnitWeight(127.318)
        liner.CableTruss.setInitialTemperature(0) 
        liner.CableTruss.setCableDiameter(0.71)
        liner.CableTruss.setOutofplaneSpacing(1)
        liner.CableTruss.setYoungsModulus(4.17709e+09)
        liner.CableTruss.setMaterialType(MaterialType.ELASTIC)
        liner.CableTruss.setTensileStrengthPeak(1.04427e+07)
        liner.CableTruss.setTensileStrengthResidual(1.04427e+07)
        liner.CableTruss.setPreTensioning(True)
        liner.CableTruss.setPreTensioningForce(0)
        liner.CableTruss.setAxialStrainExpansion(123.456)
        liner.CableTruss.setActivateThermal(True)
        liner.CableTruss.setConductivity(1)
        liner.CableTruss.setSpecificHeatCapacity(2.11)
        liner.CableTruss.setThermalExpansion(True)
        liner.CableTruss.setExpansionCoefficient(3.11)
        liner.CableTruss.setStageCableProperties(True)




        
        liner = model.getLinerPropertyByName("Liner 1")
    
        liner.CableTruss.setUnitWeight(127.318)
        liner.CableTruss.setInitialTemperature(0) 
        liner.CableTruss.setCableDiameter(0.71)
        liner.CableTruss.setOutofplaneSpacing(1)
        liner.CableTruss.setYoungsModulus(4.17709e+09)
        liner.CableTruss.setMaterialType(MaterialType.ELASTIC)
        liner.CableTruss.setTensileStrengthPeak(1.04427e+07)
        liner.CableTruss.setTensileStrengthResidual(1.04427e+07)
        liner.CableTruss.setPreTensioning(True)
        liner.CableTruss.setPreTensioningForce(0)
        liner.CableTruss.setAxialStrainExpansion(123.456)
        liner.CableTruss.setActivateThermal(True)
        liner.CableTruss.setConductivity(1)
        liner.CableTruss.setSpecificHeatCapacity(2.11)
        liner.CableTruss.setThermalExpansion(True)
        liner.CableTruss.setExpansionCoefficient(3.11)
        liner.CableTruss.setStageCableProperties(True)


        liner.CableTruss.setCableDiameter(1.1)
        liner.CableTruss.setOutofPlaneSpacing(1.2)
        liner.CableTruss.setYoungsModulus(1.3)
        liner.CableTruss.setMaterialType(MaterialType.PLASTIC)
        liner.CableTruss.setTensileStrengthPeak(1.4)
        liner.CableTruss.setTensileStrengthResidual(1.5)
        liner.CableTruss.setPreTensioning(True)
        liner.CableTruss.setPreTensioningForce(1.6)
        liner.CableTruss.setAxialStrain(1.7)
        liner.CableTruss.setStageCableProperties(True)
        
        self.assertEqual(liner.CableTruss.getCableDiameter(), 1.1)
        self.assertEqual(liner.CableTruss.getOutofPlaneSpacing(), 1.2)
        self.assertEqual(liner.CableTruss.getYoungsModulus(), 1.3)
        self.assertEqual(liner.CableTruss.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(liner.CableTruss.getTensileStrengthPeak(), 1.4)
        self.assertEqual(liner.CableTruss.getTensileStrengthResidual(), 1.5)
        self.assertEqual(liner.CableTruss.getPreTensioning(), True)
        self.assertEqual(liner.CableTruss.getPreTensioningForce(), 1.6)
        self.assertEqual(liner.CableTruss.getAxialStrain(), 1.7)
        self.assertEqual(liner.CableTruss.getStageCableProperties(), True)


        bolts = model.getAllBoltProperties()
        bolt = bolts[0]

        bolt.FullyBonded.setBoltDiameter(1.1)
        bolt.FullyBonded.setBoltModulusE(1.2)
        bolt.FullyBonded.setTensileCapacity(1.7)
        bolt.FullyBonded.setResidualTensileCapacity(1.4)
        bolt.FullyBonded.setOutofPlaneSpacing(1.5)
        bolt.FullyBonded.setPreTensioningForce(1.6)
        bolt.FullyBonded.setConstantPretensioningForceInInstallStage(False)
        bolt.FullyBonded.setJointShear(True)

        self.assertEqual(bolt.FullyBonded.getBoltDiameter(), 1.1)
        self.assertEqual(bolt.FullyBonded.getBoltModulusE(), 1.2)
        self.assertEqual(bolt.FullyBonded.getTensileCapacity(), 1.7)
        self.assertEqual(bolt.FullyBonded.getResidualTensileCapacity(), 1.4)
        self.assertEqual(bolt.FullyBonded.getOutofPlaneSpacing(), 1.5)
        self.assertEqual(bolt.FullyBonded.getPreTensioningForce(), 1.6)
        self.assertEqual(bolt.FullyBonded.getConstantPretensioningForceInInstallStage(), False)
        self.assertEqual(bolt.FullyBonded.getJointShear(), True)


        pile.setPileName('Pile 1')
        model.save()
        model.close()
        pass


if __name__ == '__main__':
    unittest.main()
