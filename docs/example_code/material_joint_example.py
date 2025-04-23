from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
RS2Modeler.startApplication(port=60068)
modeler = RS2Modeler(port=60068)
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

material = model.getAllMaterialProperties()[0]

material.Strength.setFailureCriterion(StrengthCriteriaTypes.JOINTED_MOHR_COULOMB)

jointOptions = material.Strength.JointedMohrCoulomb.getJointOptions()

jointOptions.setNumberOfJoints(2)
jointOptions.setTracePlaneProperties(1, 20.1, 2.2, 3.4)

joint = jointOptions.getJoint(1)
joint.setSlipCriterion(JointTypes.BARTON_BANDIS)
joint.BartonBandisMaterial.setDilationAngle(30)
joint.BartonBandisMaterial.setJCS(2.2)

model.close()

modeler.closeProgram()