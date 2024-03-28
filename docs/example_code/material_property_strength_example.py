from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
modeler = RS2Modeler()
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

material = model.getAllMaterialProperties()[0]
strength = material.Strength

strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
material.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
strength.setUnsaturatedBehavior(UnsaturatedParameterType.SINGLE_EFFECTIVE_STRESS)
strength.setSingleEffectiveStressMethod(UnsaturatedSingleEffectiveStressMethod.TABULAR_VALUE)
strength.setUseCutoff(True)
strength.setCutoffValue(-0.8)
# Manipulation of Mohr-Coulomb Failure Criterion
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

# Manipulation of Snowden Mod. Anisotropic Linear Strength Function
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

model.close()