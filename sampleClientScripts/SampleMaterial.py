from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")
material = model.getMaterialPropertyByName("Material 1")
material.setHatch(True)
material.setHatchStyle(HatchStyle.HatchStyleDarkVertical)
print(material.getMaterialName())
print(material.getHatchStyle())

material.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__BODY_FORCE_ONLY)
material.InitialConditions.setPorosityValue(0.6)

print(material.InitialConditions.getInitialElementLoading())
print(material.InitialConditions.getPorosityValue())

material.Stiffness.setElasticType(MaterialElasticityTypes.ORTHOTROPIC)
material.Stiffness.Orthotropic.setUseUnloadingCondition(True)
material.Stiffness.Orthotropic.setPoissonsRatioV12(0.3)
material.Stiffness.Orthotropic.setAngleCounterclockwiseFromHorizontalToE1(5)

print(material.Stiffness.getElasticType())
print(material.Stiffness.Orthotropic.getUseUnloadingCondition())
print(material.Stiffness.Orthotropic.getPoissonsRatioV12())
print(material.Stiffness.Orthotropic.getAngleCounterclockwiseFromHorizontalToE1())

material.Strength.setFailureCriterion(StrengthCriteriaTypes.HOEK_BROWN)

material.Strength.setUnsaturatedBehavior(UnsaturatedParameterType.UNSATURATED_SINGLE_EFFECTIVE_STRESS)
material.Strength.setSingleEffectiveStressMethod(UnsaturatedSingleEffectiveStressMethod.UNSATURATED_BISHOP)
material.Strength.setUseCutoff(True)
material.Strength.setCutoffValue(-0.2)

print(material.Strength.getUnsaturatedBehavior())
print(material.Strength.getSingleEffectiveStressMethod())
print(material.Strength.getUseCutoff())
print(material.Strength.getCutoffValue())

materialH = material.Strength.HoekBrown
materialH.setMaterialType(MaterialType.PLASTIC)
materialH.setCompressiveStrength(101.1)

print(materialH.getMaterialType())
print(materialH.getCompressiveStrength())


material.Hydraulic.setMaterialBehaviour(MaterialBehaviours.UNDRAINED)
material.Hydraulic.setFluidBulkModulus(2201)

print(material.Hydraulic.getMaterialBehaviour())
print(material.Hydraulic.getFluidBulkModulus())

materialGroundwater = material.Hydraulic.FEAGroundwater
materialGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_FREDLUND)
materialGroundwater.setK1Angle(20)
materialGroundwater.setMvModel(MVModel.MV_1D_ELASTIC)

print(materialGroundwater.getModel())
print(materialGroundwater.getK1Angle())
print(materialGroundwater.getMvModel())

materialFredlung = material.Hydraulic.FEAGroundwater.Fredlung
materialFredlung.setA(2.2)
materialFredlung.setWCSat(0.3)

print(materialFredlung.getA())
print(materialFredlung.getWCSat())