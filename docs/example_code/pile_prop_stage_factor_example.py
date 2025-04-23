from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 

RS2Modeler.startApplication(port=60082)
modeler = RS2Modeler(port=60082)
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

pile = model.getPilePropertyByName("Pile 1")

# Manipulation of Pile Force/Displacement factors for stage 2
pile.setStageForceDisplacement(True)
definedStageFactors = pile.ForceDisplacement.stageFactorInterface.getDefinedStageFactors()
newStageFactor = pile.ForceDisplacement.stageFactorInterface.createStageFactor(2)
definedStageFactors[2] = newStageFactor
pile.ForceDisplacement.stageFactorInterface.setDefinedStageFactors(definedStageFactors)

stageFactors = pile.ForceDisplacement.stageFactorInterface.getDefinedStageFactors()[2]

stageFactors.setXFactor(1.5)
stageFactors.setYFactor(1.8)

print(f"X Factor : {stageFactors.getXFactor()}, Y Factor : {stageFactors.getYFactor()}")

model.close()

modeler.closeProgram()