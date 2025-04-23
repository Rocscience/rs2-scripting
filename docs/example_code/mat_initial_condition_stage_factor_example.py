from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 

RS2Modeler.startApplication(port=60075)
modeler = RS2Modeler(port=60075)
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

material = model.getAllMaterialProperties()[0]

# Make sure your material stiffness type isn't Custom before changing factor values
material.Stiffness.setElasticType(MaterialElasticityTypes.ISOTROPIC)
# Make sure to stage Strength and Stiffness Stage Factor option before manipulating any factor properties
material.StageFactors.setStageStrengthStiffnessStageFactors(True)

definedStageFactors = material.StageFactors.getDefinedStageFactors()
newStageFactor = material.StageFactors.createStageFactor(2)
definedStageFactors[2] = newStageFactor
material.StageFactors.setDefinedStageFactors(definedStageFactors)

initialConditionStage2Factor = material.InitialConditions.stageFactorInterface.getDefinedStageFactors()[2]

initialConditionStage2Factor.setUnitWeightFactor(3)
initialConditionStage2Factor.setPorosityValueFactor(5)

print(f"Unit Weight Factor = {initialConditionStage2Factor.getUnitWeightFactor()}, Porosity Value Factor = {initialConditionStage2Factor.getPorosityValueFactor()}")

model.close()

modeler.closeProgram()