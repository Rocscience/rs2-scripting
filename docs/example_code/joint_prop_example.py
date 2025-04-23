from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
RS2Modeler.startApplication(port=60060)
modeler = RS2Modeler(port=60060)

model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

jointList = model.getAllJointProperties()
joint1 = jointList[0]
joint2 = jointList[1]
joint3 = jointList[2]

joint1.setJointName("Example Joint 1")
joint1.setSlipCriterion(JointTypes.MOHR_COULOMB)
joint1.MohrCoulomb.setTensileStrength(50)
joint1.MohrCoulomb.setNormalStiffness(150000)
joint1.MohrCoulomb.setApplyAdditionalPressureInsideJoint(True)

print(joint1.MohrCoulomb.getTensileStrength())
print(joint1.MohrCoulomb.getNormalStiffness())
print(joint1.MohrCoulomb.getApplyAdditionalPressureInsideJoint())

joint2.setJointName("Example Joint 2")
joint2.setSlipCriterion(JointTypes.HYPERBOLIC_SOFTENING)
joint2.HyperbolicSoftening.setProperties(PeakCohesion=155, ShearStiffness=15000, ApplyPressureToLinerSideOnly=False)

print(joint2.HyperbolicSoftening.getProperties())

joint3.setJointName("Example Joint 3")
joint3.setSlipCriterion(JointTypes.DISPLACEMENT_DEPENDENT)
joint3.DisplacementDependent.setProperties(AdditionalPressureType=AdditionalPressureType.PRESSURE, AdditionalPressureInsideJoint=5)
# Not all functions are accessible through the setProperties method. 
# Consult setProperties method definition in documentation to determine properties available.
joint3.DisplacementDependent.setDisplacementDependentTable([[2,8,9,12],[5,6,7,8]])

print(joint3.DisplacementDependent.getProperties())
# Not all functions are accessible through the getProperties method. 
# Consult getProperties method definition in documentation to determine properties available.
print(joint3.DisplacementDependent.getDisplacementDependentTable())

model.close()
modeler.closeProgram()