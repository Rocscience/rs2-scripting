from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 

modeler = RS2Modeler()
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

material = model.getAllMaterialProperties()[0]

# Get Stage Factor for stage 1

# Make sure your material stiffness type isn't Custom changing factor values
material.Stiffness.setElasticType(MaterialElasticityTypes.ISOTROPIC)
# Make sure to stage Strength and Stiffness Stage Factor option before manipulating any factor properties
material.StageFactors.setStageStrengthStiffnessStageFactors(True)
initialConditionStageFactor = material.InitialConditions.stageFactorInterface.getDefinedStageFactors()[1]
# Update the stage factor fields for the model
initialConditionStageFactor.setUnitWeightFactor(3)
initialConditionStageFactor.setPorosityValueFactor(5)

print(f"Unit Wegiht Factor = {initialConditionStageFactor.getUnitWeightFactor()}, Porosity Value Factor = {initialConditionStageFactor.getPorosityValueFactor()}")

model.close()