from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 

modeler = RS2Modeler()
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

liner = model.getLinerPropertyByName("Liner 1")

liner.setLinerType(LinerTypes.REINFORCED_CONCRETE)
reinforcedConcreteFactors = liner.ReinforcedConcrete.stageFactorInterface.getDefinedStageFactors()
# Get factors for stage 1
stageFactor = reinforcedConcreteFactors[1]

stageFactor.setThicknessFactor(3)
stageFactor.setConcreteYoungsModulusFactor(2.2)
stageFactor.setConcreteCompressiveStrengthFactor(4)
stageFactor.setConcreteTensileStrengthFactor(1.5)
stageFactor.setAxialStrainExpansionFactor(0.8)
stageFactor.setAreaFactor(1.1)

liner.setLinerType(LinerTypes.STANDARD_BEAM)
standardBeamFactors = liner.StandardBeam.stageFactorInterface.getDefinedStageFactors()
# Get factors for stage 1
linerStageFactors = standardBeamFactors[1]

linerStageFactors.setThicknessFactor(3)
linerStageFactors.setYoungsModulusFactor(2)
linerStageFactors.setPoissonsRatioFactor(1.45)
linerStageFactors.setAxialStrainExpansionFactor(0.8)

model.close()
