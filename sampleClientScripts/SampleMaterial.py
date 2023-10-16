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
