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


material.Thermal.setWaterContent(ThermalWaterContentMethodType.THERMAL_WATER_CONTENT_DEFINE)
material.Thermal.setWaterContentValue(0.1)
material.Thermal.setThermalExpansion(True)
material.Thermal.setExpansionCoefficient(0.00002)
material.Thermal.setDispersivity(True)
material.Thermal.setLongitudinalDispersivity(1.1)

print(material.Thermal.getWaterContent())
print(material.Thermal.getWaterContentValue())
print(material.Thermal.getThermalExpansion())
print(material.Thermal.getExpansionCoefficient())
print(material.Thermal.getDispersivity())
print(material.Thermal.getLongitudinalDispersivity())


material.Thermal.Conductivity.setMethod(ThermalType.THERMAL_COTE_AND_KONRAD)
material.Thermal.Conductivity.CoteAndKonrad.setEta(1.8)
print(material.Thermal.Conductivity.getMethod())
print(material.Thermal.Conductivity.CoteAndKonrad.getEta())

waterContent = material.Thermal.SoilUnfrozenWaterContent
waterContent.setType(ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)
waterContent.HydraulicModel.setFrozenTemperature(-0.04)
waterContent.HydraulicModel.setWCSat(0.5)
waterContent.HydraulicModel.setSelectHydraulicModel(GroundWaterModes.SL_WATER_MODE_GARDNER)
waterContent.HydraulicModel.Gardner.setA(0.2)

print(waterContent.getType())
print(waterContent.HydraulicModel.getFrozenTemperature())
print(waterContent.HydraulicModel.getWCSat())
print(waterContent.HydraulicModel.getSelectHydraulicModel())
print(waterContent.HydraulicModel.Gardner.getA())