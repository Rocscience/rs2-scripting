from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
RS2Modeler.startApplication(port=60072)
modeler = RS2Modeler(port=60072)
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

material = model.getAllMaterialProperties()[0]

material.InitialConditions.setInitialElementLoading(InitialElementLoadingType.BODY_FORCE_ONLY)

material.Stiffness.setElasticType(MaterialElasticityTypes.TRANSVERSELY_ISOTROPIC)
material.Stiffness.TransverselyIsotropic.setUseUnloadingCondition(True)

material.Strength.setFailureCriterion(StrengthCriteriaTypes.HOEK_BROWN)
material.Strength.HoekBrown.setCompressiveStrength(101)

material.Hydraulic.StaticGroundwater.setStaticWaterMode(StaticWaterModes.PORE_WATER_PRESSURE)
material.Hydraulic.setMaterialBehaviour(MaterialBehaviours.UNDRAINED)

model.close()

modeler.closeProgram()