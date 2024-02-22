from math import fabs
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\fullyBonded_final.fez")

boltList = model.getAllBoltProperties()
bolt1 = boltList[0]
bolt2 = boltList[1]
bolt3 = boltList[2]
bolt4 = boltList[3]
bolt5 = boltList[4]

bolt1.setBoltType(BoltTypes.FULLY_BONDED)
bolt1.FullyBonded.setBoltDiameter(1.1)
bolt1.FullyBonded.setBoltModulusE(1.2) 
bolt1.FullyBonded.setTensileCapacity(1.43)
bolt1.FullyBonded.setResidualTensileCapacity(1.4)
bolt1.FullyBonded.setOutofPlaneSpacing(1.5)
bolt1.FullyBonded.setPreTensioningForce(1.6)
bolt1.FullyBonded.setConstantPretensioningForceInInstallStage(True)
bolt1.FullyBonded.setJointShear(True)

bolt2.setBoltType(BoltTypes.FULLY_BONDED)
bolt2.FullyBonded.setConstantPretensioningForceInInstallStage(False)
bolt2.FullyBonded.setJointShear(False)                         

bolt3.setBoltType(BoltTypes.FULLY_BONDED)
bolt3.FullyBonded.setConstantPretensioningForceInInstallStage(True)
bolt3.FullyBonded.setJointShear(False)

bolt4.setBoltType(BoltTypes.FULLY_BONDED)
bolt4.FullyBonded.setConstantPretensioningForceInInstallStage(False)
bolt4.FullyBonded.setJointShear(True)   

assert(bolt1.FullyBonded.getBoltDiameter(), 1.1)
assert(bolt1.FullyBonded.getBoltModulusE(), 1.2)
assert(bolt1.FullyBonded.getTensileCapacity(), 1.43)
assert(bolt1.FullyBonded.getResidualTensileCapacity(), 1.4)
assert(bolt1.FullyBonded.getOutofPlaneSpacing(), 1.5)  
assert(bolt1.FullyBonded.getPreTensioningForce(), 1.6)
assert(bolt1.FullyBonded.getConstantPretensioningForceInInstallStage(), True) 
assert(bolt1.FullyBonded.getJointShear(), True)

assert(bolt2.FullyBonded.getConstantPretensioningForceInInstallStage(), False) 
assert(bolt2.FullyBonded.getJointShear(), False)

assert(bolt3.FullyBonded.getConstantPretensioningForceInInstallStage(), True) 
assert(bolt3.FullyBonded.getJointShear(), False)

assert(bolt4.FullyBonded.getConstantPretensioningForceInInstallStage(), False) 
assert(bolt4.FullyBonded.getJointShear(), True)

model.save()

pass