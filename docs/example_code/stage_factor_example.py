from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 

RS2Modeler.startApplication(port=60083)
modeler = RS2Modeler(port=60083)
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

joint = model.getAllJointProperties()[0]
liner = model.getAllLinerProperties()[0]
material = model.getAllMaterialProperties()[0]

# Manipulation of AbsoluteStageFactorInterface type object
joint.setSlipCriterion(JointTypes.MOHR_COULOMB)
definedStageFactors = joint.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()
newStageFactor = joint.MohrCoulomb.stageFactorInterface.createStageFactor(2)
definedStageFactors[2] = newStageFactor
joint.MohrCoulomb.stageFactorInterface.setDefinedStageFactors(definedStageFactors)

mohrCoulombFactors = joint.MohrCoulomb.stageFactorInterface.getDefinedStageFactors()
stage2mohrCoulombFactors = mohrCoulombFactors[2]

stage2mohrCoulombFactors.setNormalStiffnessFactor(3)
stage2mohrCoulombFactors.setShearStiffnessFactor(3) 
stage2mohrCoulombFactors.setTensileStrengthFactor(3) 

# Manipulation of RelativeStageFactorInterface type object
liner.setLinerType(LinerTypes.REINFORCED_CONCRETE)
liner.ReinforcedConcrete.setStageConcreteProperties(True)
definedStageFactors = liner.ReinforcedConcrete.stageFactorInterface.getDefinedStageFactors()
newStageFactor = liner.ReinforcedConcrete.stageFactorInterface.createStageFactor(2)
definedStageFactors[2] = newStageFactor
liner.ReinforcedConcrete.stageFactorInterface.setDefinedStageFactors(StageFactorDefinitionMethod.RELATIVE_STAGE_FACTOR, definedStageFactors)

reinforcedConcreteFactors = liner.ReinforcedConcrete.stageFactorInterface.getDefinedStageFactors()
stageFactor = reinforcedConcreteFactors[2]

stageFactor.setThicknessFactor(3)
stageFactor.setConcreteYoungsModulusFactor(2.2)
stageFactor.setConcreteCompressiveStrengthFactor(4)

# Manipulation of AbsoluteStageFactorGettersInterface type object
material.Stiffness.setElasticType(MaterialElasticityTypes.ISOTROPIC)
material.StageFactors.setStageStrengthStiffnessStageFactors(True)

definedStageFactors = material.StageFactors.getDefinedStageFactors()
newStageFactor = material.StageFactors.createStageFactor(2)
definedStageFactors[2] = newStageFactor
material.StageFactors.setDefinedStageFactors(definedStageFactors)

strengthFactor = material.Strength.stageFactorInterface.getDefinedStageFactors()[2]

strengthFactor.setResetYield(True)
strengthFactor.setAirEntryValueFactor(1.5)
strengthFactor.setUnsaturatedShearStrengthAngleFactor(3.9)

model.close()

modeler.closeProgram()