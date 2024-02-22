from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\swellex_final.fez")

boltList = model.getAllBoltProperties()
bolt1 = boltList[0]
bolt2 = boltList[1]
bolt3 = boltList[2]
bolt4 = boltList[3]
bolt5 = boltList[4]
bolt6 = boltList[5]
bolt7 = boltList[6]
bolt8 = boltList[7]
bolt9 = boltList[8]
bolt10 = boltList[9]
bolt11 = boltList[10]
bolt12 = boltList[11]

bolt1.setBoltType(BoltTypes.SHEAR_BOLT)
bolt1.Swellex.setTensileCapacity(1.21)
bolt1.Swellex.setResidualTensileCapacity(1.2)
bolt1.Swellex.setTributaryArea(1.3)
bolt1.Swellex.setBoltModulusE(1.4)
bolt1.Swellex.setOutofPlaneSpacing(1.5)
bolt1.Swellex.setMaterialDependent(True)
bolt1.Swellex.setBondStrengthCoefficient(1.6)
bolt1.Swellex.setBondShearStiffnessCoefficient(1.7)
bolt1.Swellex.setBoltModel(BoltModels.P2_BOLT_PLASTIC)
bolt1.Swellex.setJointShear(True)
bolt1.Swellex.setPreTensioningForce(1.8)
bolt1.Swellex.setConstantPretensioningForceInInstallStage(True)
bolt1.Swellex.setFacePlates(True)
bolt1.Swellex.setAddPullOutForce(True)
bolt1.Swellex.setPullOutForce(1.9)

bolt2.setBoltType(BoltTypes.SHEAR_BOLT)
bolt2.Swellex.setMaterialDependent(False)
bolt2.Swellex.setBondShearStiffness(1.1)
bolt2.Swellex.setBondStrength(1.2)
bolt2.Swellex.setResidualBondStrength(1.13)
bolt2.Swellex.setJointShear(False)
bolt2.Swellex.setConstantPretensioningForceInInstallStage(False)
bolt2.Swellex.setFacePlates(False)
bolt2.Swellex.setAddPullOutForce(False)

bolt3.setBoltType(BoltTypes.SHEAR_BOLT)
bolt3.Swellex.setMaterialDependent(True)
bolt3.Swellex.setBondStrengthCoefficient(1.1)
bolt3.Swellex.setBondShearStiffnessCoefficient(1.2)
bolt3.Swellex.setJointShear(False)
bolt3.Swellex.setConstantPretensioningForceInInstallStage(False)
bolt3.Swellex.setFacePlates(False)
bolt3.Swellex.setAddPullOutForce(False)

bolt4.setBoltType(BoltTypes.SHEAR_BOLT)
bolt4.Swellex.setMaterialDependent(False)
bolt4.Swellex.setJointShear(True)
bolt4.Swellex.setConstantPretensioningForceInInstallStage(False)
bolt4.Swellex.setFacePlates(False)
bolt4.Swellex.setAddPullOutForce(False)

bolt5.setBoltType(BoltTypes.SHEAR_BOLT)
bolt5.Swellex.setMaterialDependent(False)
bolt5.Swellex.setJointShear(False)
bolt5.Swellex.setConstantPretensioningForceInInstallStage(True)
bolt5.Swellex.setFacePlates(False)
bolt5.Swellex.setAddPullOutForce(False)

bolt6.setBoltType(BoltTypes.SHEAR_BOLT)
bolt6.Swellex.setMaterialDependent(False)
bolt6.Swellex.setJointShear(False)
bolt6.Swellex.setConstantPretensioningForceInInstallStage(False)
bolt6.Swellex.setFacePlates(True)
bolt6.Swellex.setAddPullOutForce(False)

bolt7.setBoltType(BoltTypes.SHEAR_BOLT)
bolt7.Swellex.setMaterialDependent(False)
bolt7.Swellex.setJointShear(False)
bolt7.Swellex.setConstantPretensioningForceInInstallStage(False)
bolt7.Swellex.setFacePlates(False)
bolt7.Swellex.setAddPullOutForce(True)
bolt7.Swellex.setPullOutForce(1.1)

bolt8.setBoltType(BoltTypes.SHEAR_BOLT)
bolt8.Swellex.setMaterialDependent(True)
bolt8.Swellex.setBondStrengthCoefficient(1.1)
bolt8.Swellex.setBondShearStiffnessCoefficient(1.2)
bolt8.Swellex.setJointShear(False)
bolt8.Swellex.setConstantPretensioningForceInInstallStage(True)
bolt8.Swellex.setFacePlates(False)
bolt8.Swellex.setAddPullOutForce(True)
bolt8.Swellex.setPullOutForce(1.3)

bolt9.setBoltType(BoltTypes.SHEAR_BOLT)
bolt9.Swellex.setMaterialDependent(False)
bolt9.Swellex.setJointShear(True)
bolt9.Swellex.setConstantPretensioningForceInInstallStage(False)
bolt9.Swellex.setFacePlates(True)
bolt9.Swellex.setAddPullOutForce(False)

bolt10.setBoltType(BoltTypes.SHEAR_BOLT)
bolt10.Swellex.setMaterialDependent(True)
bolt10.Swellex.setBondStrengthCoefficient(1.1)
bolt10.Swellex.setBondShearStiffnessCoefficient(1.2)
bolt10.Swellex.setJointShear(True)
bolt10.Swellex.setConstantPretensioningForceInInstallStage(True)
bolt10.Swellex.setFacePlates(False)
bolt10.Swellex.setAddPullOutForce(False)

bolt11.setBoltType(BoltTypes.SHEAR_BOLT)
bolt11.Swellex.setMaterialDependent(False)
bolt11.Swellex.setJointShear(False)
bolt11.Swellex.setConstantPretensioningForceInInstallStage(False)
bolt11.Swellex.setFacePlates(True)
bolt11.Swellex.setAddPullOutForce(True)
bolt11.Swellex.setPullOutForce(1.1)

bolt12.setBoltType(BoltTypes.SHEAR_BOLT)
bolt12.Swellex.setMaterialDependent(True)
bolt12.Swellex.setBondStrengthCoefficient(1.1)
bolt12.Swellex.setBondShearStiffnessCoefficient(1.2)
bolt12.Swellex.setJointShear(True)
bolt12.Swellex.setConstantPretensioningForceInInstallStage(False)
bolt12.Swellex.setFacePlates(False)
bolt12.Swellex.setAddPullOutForce(True)
bolt12.Swellex.setPullOutForce(1.3)


'''
assert(bolt1.Swellex.getTensileCapacity(), 1.21)
assert(bolt1.Swellex.getResidualTensileCapacity(), 1.2)
assert(bolt1.Swellex.getTributaryArea(), 1.3)
assert(bolt1.Swellex.getBoltModulusE(), 1.4)
assert(bolt1.Swellex.getOutofPlaneSpacing(), 1.5)
assert(bolt1.Swellex.getMaterialDependent(), True)
assert(bolt1.Swellex.getBondStrengthCoefficient(), 1.6)
assert(bolt1.Swellex.getBondShearStiffnessCoefficient(), 1.7)
assert(bolt1.Swellex.getBoltModel(), BoltModels.P2_BOLT_PLASTIC)
assert(bolt1.Swellex.getJointShear(), True)
assert(bolt1.Swellex.getPreTensioningForce(), 1.8)
assert(bolt1.Swellex.getConstantPretensioningForceInInstallStage(), True)
assert(bolt1.Swellex.getFacePlates(), True)
assert(bolt1.Swellex.getAddPullOutForce(), True) 
assert(bolt1.Swellex.getPullOutForce(), 1.9)
'''

model.save()

pass