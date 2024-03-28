from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 

modeler = RS2Modeler()
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

material = model.getAllMaterialProperties()[0]

# Make sure your material stiffness type isn't Custom before changing factor values
material.Stiffness.setElasticType(MaterialElasticityTypes.ISOTROPIC)
# Make sure to stage Strength and Stiffness Stage Factor option before manipulating any factor properties
material.StageFactors.setStageStrengthStiffnessStageFactors(True)

initialConditionStage1Factor = material.InitialConditions.stageFactorInterface.getDefinedStageFactors()[1]

initialConditionStage1Factor.setUnitWeightFactor(3)
initialConditionStage1Factor.setPorosityValueFactor(5)

print(f"Unit Wegiht Factor = {initialConditionStage1Factor.getUnitWeightFactor()}, Porosity Value Factor = {initialConditionStage1Factor.getPorosityValueFactor()}")

model.close()