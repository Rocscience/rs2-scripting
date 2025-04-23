from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 

RS2Modeler.startApplication(port=60063)
modeler = RS2Modeler(port=60063)
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

liner = model.getLinerPropertyByName("Liner 1")

liner.setLinerType(LinerTypes.REINFORCED_CONCRETE)
liner.ReinforcedConcrete.setStageConcreteProperties(True)
definedStageFactors = liner.ReinforcedConcrete.stageFactorInterface.getDefinedStageFactors()
newStageFactor = liner.ReinforcedConcrete.stageFactorInterface.createStageFactor(2)
definedStageFactors[2] = newStageFactor
liner.ReinforcedConcrete.stageFactorInterface.setDefinedStageFactors(StageFactorDefinitionMethod.RELATIVE_STAGE_FACTOR, definedStageFactors)

# Get factors for stage 2
reinforcedConcreteFactors = liner.ReinforcedConcrete.stageFactorInterface.getDefinedStageFactors()
stageFactor = reinforcedConcreteFactors[2]

stageFactor.setThicknessFactor(3)
stageFactor.setConcreteYoungsModulusFactor(2.2)
stageFactor.setConcreteCompressiveStrengthFactor(4)
stageFactor.setConcreteTensileStrengthFactor(1.5)
stageFactor.setAxialStrainExpansionFactor(0.8)
stageFactor.setAreaFactor(1.1)

liner.setLinerType(LinerTypes.STANDARD_BEAM)
liner.StandardBeam.setStageLinerProperties(True)
standardBeamFactors = liner.StandardBeam.stageFactorInterface.getDefinedStageFactors()
linerStageFactors = standardBeamFactors[2]

linerStageFactors.setThicknessFactor(3)
linerStageFactors.setYoungsModulusFactor(2)
linerStageFactors.setPoissonsRatioFactor(1.45)
linerStageFactors.setAxialStrainExpansionFactor(0.8)

model.close()
modeler.closeProgram()