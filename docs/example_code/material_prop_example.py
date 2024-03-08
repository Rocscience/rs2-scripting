from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")

material = model.getAllMaterialProperties()[0]

material.InitialConditions.setInitialElementLoading(InitialElementLoadingType.BODY_FORCE_ONLY)

material.Stiffness.setElasticType(MaterialElasticityTypes.TRANSVERSELY_ISOTROPIC)
material.Stiffness.TransverselyIsotropic.setUseUnloadingCondition(True)

material.Strength.setFailureCriterion(StrengthCriteriaTypes.HOEK_BROWN)
material.Strength.HoekBrown.setCompressiveStrength(101)

material.Hydraulic.StaticGroundwater.setStaticWaterMode(StaticWaterModes.PORE_WATER_PRESSURE)
material.Hydraulic.setMaterialBehaviour(MaterialBehaviours.UNDRAINED)


