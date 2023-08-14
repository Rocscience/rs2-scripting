from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *
modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage_with_thermal_static.fez")
bolt = model.getAllJointProperties()

bolt[0].setSlipCriterion(JointTypes.JOINT_BARTON_BANDIS)
