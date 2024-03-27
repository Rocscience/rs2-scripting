from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
modeler = RS2Modeler()
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

material = model.getAllMaterialProperties()[0]
stiffness = material.Stiffness
custom = stiffness.Custom
# Manipulation of Loading Properties
custom.setUseConstantPoissonsRatio(False)
custom.setCustomStiffnessLoadingTable(mode=CustomMode.CUSTOM_Q,
                                      table=[(1, 2, 0.3), (4, 5, 0.4)])
# Manipulation of Unloading Properties
custom.setUseUnloadingCondition(True)
custom.setUnloadingCondition(UnloadingConditions.DEVIATORIC_STRESS)
custom.setUnloadingUseConstantPoissonsRatio(False)
custom.setCustomStiffnessUnloadingTable(mode=CustomMode.CUSTOM_Q,
                                        table=[(1, 2, 0.3), (4, 5, 0.4)])

# Make sure to define Stiffness Loading and Unloading tables before setting Custom Model and Stiffness Elastic Type to Custom
custom.setCustomMode(CustomMode.CUSTOM_Q)
stiffness.setElasticType(MaterialElasticityTypes.CUSTOM)


print(f"Loading Custom Table = {custom.getCustomStiffnessLoadingTable()}")
print(f"Unloading Condition = {custom.getUnloadingCondition()}")
print(f"Unloading Custom Table = {custom.getCustomStiffnessUnloadingTable()}")

# Manipulation of Stiffness Stage Factor Properties

# Make sure to your Stiffness Elastic Type isn't Custom before manipulating any stiffness related factor values
material.Stiffness.setElasticType(MaterialElasticityTypes.ISOTROPIC)

# Manipulation of Stiffness Isotripic Stage 1 factors
stiffnessStageFactor = material.Stiffness.Isotropic.stageFactorInterface.getDefinedStageFactors()[1]

stiffnessStageFactor.setPoissonsRatioFactor(3)
stiffnessStageFactor.setResidualYoungsModulusFactor(2.2)
stiffnessStageFactor.setShearModulusFactor(1.9)

print("\nIsotropic Stage Factor Values")
print(f"Poisson Ratio Factor = {stiffnessStageFactor.getPoissonsRatioFactor()}, Res. Youngs Modulus Factor = {stiffnessStageFactor.getYoungsModulusFactor()}, Shear Modulus Factor = {stiffnessStageFactor.getShearModulusFactor()}")

# Manipulation of Stiffness NonLinear Hyperbolic Stage 1 factors
nonLinearHyperbolicFactors = material.Stiffness.NonLinearHyperbolic.stageFactorInterface.getDefinedStageFactors()[1]

nonLinearHyperbolicFactors.setFailureRatioRfFactor(1)
nonLinearHyperbolicFactors.setBulkModulusExpMFactor(2)
nonLinearHyperbolicFactors.setAtmosphericPressureFactor(3.3)

print("\nNonLinear Hyperbolic Stage Factor Values")
print(f"Failure Ratio of RF = {nonLinearHyperbolicFactors.getFailureRatioRfFactor()}, Bulk Modulus ExpM = {nonLinearHyperbolicFactors.getBulkModulusExpMFactor()}, Atmospheric Pressure = {nonLinearHyperbolicFactors.getAtmosphericPressureFactor()}")

model.close()