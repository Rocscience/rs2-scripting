from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")

material = model.getAllMaterialProperties()[0]

material.Strength.setFailureCriterion(StrengthCriteriaTypes.JOINTED_MOHR_COULOMB)

jointOptions = material.Strength.JointedMohrCoulomb.getJointOptions()

jointOptions.setNumberOfJoints(2)
jointOptions.setTracePlaneProperties(1, 20.1, 2.2, 3.4)

joint = jointOptions.getJoint(1)
joint.setSlipCriterion(JointTypes.JOINT_BARTON_BANDIS)
joint.BartonBandisMaterial.setDilationAngle(30)
joint.BartonBandisMaterial.setJCS(2.2)


