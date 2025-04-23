from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 

RS2Modeler.startApplication(port=60069)
modeler = RS2Modeler(port=60069)
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

# Manipulation of Material Joint Mohr Coulomb Stage Factor for stage 2
material = model.getAllMaterialProperties()[0]
material.Strength.setFailureCriterion(StrengthCriteriaTypes.JOINTED_MOHR_COULOMB)
matJointOptions = material.Strength.JointedMohrCoulomb.getJointOptions()
jointmaterial = matJointOptions.getJoint(0)
jointmaterial.MohrCoulombMaterial.setApplyStageFactors(True)

definedStageFactors = jointmaterial.MohrCoulombMaterial.stageFactorInterface.getDefinedStageFactors()
newStageFactor = jointmaterial.MohrCoulombMaterial.stageFactorInterface.createStageFactor(2)
definedStageFactors[2] = newStageFactor
jointmaterial.MohrCoulombMaterial.stageFactorInterface.setDefinedStageFactors(definedStageFactors)

stageFactor = jointmaterial.MohrCoulombMaterial.stageFactorInterface.getDefinedStageFactors()[2]
stageFactor.setTensileStrengthFactor(25)
stageFactor.setPeakFrictionAngleFactor(39)
stageFactor.setPeakCohesionFactor(20)
stageFactor.setResTensileStrengthFactor(14)
stageFactor.setResCohesionFactor(14)
stageFactor.setResFrictionAngleFactor(22)
stageFactor.setDilationAngleFactor(2.7)

# Manipulation of Material Joint  Barton Bandis Stage Factor
jointmaterial.BartonBandisMaterial.setApplyStageFactors(True)
stageFactor = jointmaterial.BartonBandisMaterial.stageFactorInterface.getDefinedStageFactors()[2]
jointmaterial.BartonBandisMaterial.setJCS(36.5)
jointmaterial.BartonBandisMaterial.setJRC(28.5)
jointmaterial.BartonBandisMaterial.setResidualFrictionAngle(27.5)
jointmaterial.BartonBandisMaterial.setResidualStrength(1)
jointmaterial.BartonBandisMaterial.setApplyStageFactors(1)
jointmaterial.BartonBandisMaterial.setDilationAngle(2.3)

# Manipulation of Material Joint Geosynthetic Hyperbolic Stage Factor
jointmaterial.GeosyntheticHyperbolicMaterial.setApplyStageFactors(True)
stageFactor = jointmaterial.GeosyntheticHyperbolicMaterial.stageFactorInterface.getDefinedStageFactors()[2]
jointmaterial.GeosyntheticHyperbolicMaterial.setPeakAdhesionAtSigninf(37.5)
jointmaterial.GeosyntheticHyperbolicMaterial.setPeakFrictionAngleAtSign0(28.5)
jointmaterial.GeosyntheticHyperbolicMaterial.setResAdhesionAtSigninf(27.5)
jointmaterial.GeosyntheticHyperbolicMaterial.setResFrictionAngleAtSign0(36.7)
jointmaterial.GeosyntheticHyperbolicMaterial.setApplyStageFactors(1)
jointmaterial.GeosyntheticHyperbolicMaterial.setTensileStrength(14.6)
jointmaterial.GeosyntheticHyperbolicMaterial.setDilationRatio(2.2)

model.close()
modeler.closeProgram()