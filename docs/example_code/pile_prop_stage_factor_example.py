from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 

modeler = RS2Modeler()
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

pile = model.getPilePropertyByName("Pile 1")

# Manipulation of Pile Force/Displacement factors for stage 1
forceDispFactors = pile.ForceDisplacement.stageFactorInterface.getDefinedStageFactors()
stageFactors = forceDispFactors[1]

stageFactors.setXFactor(1.5)
stageFactors.setYFactor(1.8)

print(f"X Factor : {stageFactors.getXFactor()}, Y Factor : {stageFactors.getYFactor()}")

model.close()