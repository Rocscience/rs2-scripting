from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\Profiles_and_Boreholes.fez")

material = model.getAllMaterialProperties()[0]

material.Stiffness.setElasticType(MaterialElasticityTypes.ISOTROPIC)
isotropic = material.Stiffness.Isotropic
isotropic.setUseUnloadingCondition(True)
isotropic.setPoissonsRatio(5)
isotropic.setYoungsModulus(6)
isotropic.setUseResidualYoungsModulus(True)
isotropic.setResidualYoungsModulus(7)

# To be completed