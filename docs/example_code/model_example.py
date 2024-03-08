from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\Model_example.fez")

bolt = model.getAllBoltProperties()[0]
liner = model.getAllLinerProperties()[0]
joint = model.getAllJointProperties()[0]

bolt.setBoltType(BoltTypes.SWELLEX)
liner.setLinerType(LinerTypes.REINFORCED_CONCRETE)
joint.setSlipCriterion(JointTypes.MATERIAL_DEPENDENT)

model.save()
model.compute()
model.close()