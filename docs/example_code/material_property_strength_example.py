from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
RS2Modeler.startApplication(port=60070)
modeler = RS2Modeler(port=60070)
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

material = model.getAllMaterialProperties()[0]
strength = material.Strength

strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
material.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
strength.setUnsaturatedBehavior(UnsaturatedParameterType.SINGLE_EFFECTIVE_STRESS)
strength.setSingleEffectiveStressMethod(UnsaturatedSingleEffectiveStressMethod.TABULAR_VALUE)
strength.setUseCutoff(True)
strength.setCutoffValue(-0.8)

mohr_coulomb = strength.MohrCoulombStrength
mohr_coulomb.setPeakTensileStrength(1)
mohr_coulomb.setPeakFrictionAngle(30)
mohr_coulomb.setPeakCohesion(12)
mohr_coulomb.setResidualTensileStrength(2)
mohr_coulomb.setResidualFrictionAngle(35)
mohr_coulomb.setResidualCohesion(13.5)
mohr_coulomb.setDilationAngle(15)
print(f"Peak Tensile Strength = {mohr_coulomb.getPeakTensileStrength()}, Peak Friction Angle = {mohr_coulomb.getPeakFrictionAngle()}, Peak Cohesion = {mohr_coulomb.getPeakCohesion()}")
print(f"Res Peak Tensile = {mohr_coulomb.getResidualTensileStrength()}, Res Peak Friction = {mohr_coulomb.getResidualFrictionAngle()}, Res Cohesion = {mohr_coulomb.getResidualFrictionAngle()}")

tabularValueMethod = strength.setTabularValues(UnsaturatedTabularValueMethod.WITH_RESPECT_TO_SUCTION)
strength.setUnsaturatedZoneTableWithRespectToSuction(coefficients=[1, 2], values=[5, 6])

snowdenAnisotripicFunction = material.Strength.SnowdenModAnisotropicLinear.getBeddingStrengthFunction()
snowdenAnisotripicFunction.setDilationRatio(0.74)
snowdenAnisotripicFunction.setPeakTensileStrength(5)
snowdenAnisotripicFunction.setResidualTensileStrength(8)
snowdenAnisotripicFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_SHEAR_NORMAL)
snowdenAnisotripicFunction.setShearNormalFunctionWithResidual(normalStress=[1 , 2],
                                                              shearStress=[3, 4],
                                                              residualShearStress=[2.2, 3.6])
print(f"Normal Stress = {snowdenAnisotripicFunction.getNormalStress()}")
print(f"Shear Stress = {snowdenAnisotripicFunction.getShearStress()}")
print(f"Residual Shear Stress = {snowdenAnisotripicFunction.getResidualShearStress()}\n")


# Manipulation of Strength Stage Factor Properties for stage 2
# Make sure to your Stiffness Elastic Type isn't Custom before manipulating any factor values
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

print("\nStrength Stage Factor Values:")
print(f"Reset Yield = {strengthFactor.getResetYield()}, Air Entry Value = {strengthFactor.getAirEntryValueFactor()}, Unsaturated Shear Strength Angle = {strengthFactor.getUnsaturatedShearStrengthAngleFactor()}")

# Manipulation of Strength Basic Barcelona Model Stage 2 factors
material.Strength.setFailureCriterion(StrengthCriteriaTypes.BARCELONA_BASIC)
barcelonaFactors = material.Strength.BarcelonaBasic.stageFactorInterface.getDefinedStageFactors()[2]

barcelonaFactors.setGammaFactor(3.3)
barcelonaFactors.setLambdaFactor(2)
barcelonaFactors.setNParameterFactor(5)

print("\nStrength Basic Barcelona Model Stage Factor Values")
print(f"Gamma Factor = {barcelonaFactors.getGammaFactor()}, Lambda Factor = {barcelonaFactors.getLambdaFactor()},N Parameter Factor = {barcelonaFactors.getNParameterFactor()}")

# Manipulation of Strength Hoek Brown Stage 2 factors
material.Strength.setFailureCriterion(StrengthCriteriaTypes.HOEK_BROWN)
hoekBrownFactors = material.Strength.HoekBrown.stageFactorInterface.getDefinedStageFactors()[2]

hoekBrownFactors.setDilationParameterFactor(2.2)
hoekBrownFactors.setCompressiveStrengthFactor(5)
hoekBrownFactors.setMbParameterFactor(1)

print("\nHoek Brown Stage Factor Values")
print(f"Dilation Parameter = {hoekBrownFactors.getDilationParameterFactor()}, Compressive Strength = {hoekBrownFactors.getCompressiveStrengthFactor()}, MB Parameter = {hoekBrownFactors.getMbParameterFactor()}")

model.close()

modeler.closeProgram()