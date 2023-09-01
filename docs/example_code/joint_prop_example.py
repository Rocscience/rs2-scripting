from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")

jointList = model.getAllJointProperties()
joint1 = jointList[0]
joint2 = jointList[1]
joint3 = jointList[2]

#Assigning joint1 properties individually
joint1.setJointName("Test Joint 1")
joint1.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
joint1.MohrCoulomb.setTensileStrength(50)
joint1.MohrCoulomb.setNormalStiffness(150000)
joint1.MohrCoulomb.setApplyAdditionalPressureInsideJoint(True)

#Retrieving joint1 properties individiually
print(joint1.MohrCoulomb.getTensileStrength())
print(joint1.MohrCoulomb.getNormalStiffness())
print(joint1.MohrCoulomb.getApplyAdditionalPressureInsideJoint())

#Bulk assignment of joint2 properties
joint2.setJointName("Test Joint 2")
joint2.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SOFTENING)
joint2.HyperbolicSoftening.setProperties(PeakCohesion=155, ShearStiffness=15000, ApplyPressureToLinerSideOnly=False)

#Bulk retrieval of joint2 properties
print(joint2.HyperbolicSoftening.getProperties())

#Assignment of joint3 properties
joint3.setJointName("Test Joint 3")
joint3.setSlipCriterion(JointTypes.JOINT_DISPLACEMENT_DEPENDENT)
joint3.DisplacementDependent.setProperties(AdditionalPressureType=AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_VALUE, AdditionalPressureInsideJoint=5)
#Not all functions are accesible through the setProperties method. 
#Consult setProperties method definition in documentation to determine properties available.
joint3.DisplacementDependent.setDisplacementDependentTable([[2,8,9,12],[5,6,7,8]])

#Retrieval of joint properties
print(joint3.DisplacementDependent.getProperties())
#Not all functions are accesible through the getProperties method. 
#Consult getProperties method definition in documentation to determine properties available.
print(joint3.DisplacementDependent.getDisplacementDependentTable())