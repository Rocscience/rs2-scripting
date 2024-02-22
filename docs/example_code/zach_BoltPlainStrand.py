from operator import truediv
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.bolt import PlainStrandCable

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\plainStrand_final.fez")

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
bolt13 = boltList[12]

bolt1.setBoltType(BoltTypes.QUEENS_CABLE)
bolt1.PlainStrandCable.setBoreholeDiameter(1.21)
bolt1.PlainStrandCable.setCableDiameter(1.2)
bolt1.PlainStrandCable.setCableModulusE(1.3)
bolt1.PlainStrandCable.setCablePeak(1.4)
bolt1.PlainStrandCable.setOutofPlaneSpacing(1.5)
bolt1.PlainStrandCable.setWaterCementRatio(1.6)
bolt1.PlainStrandCable.setJointShear(True)
bolt1.PlainStrandCable.setFacePlates(True)
bolt1.PlainStrandCable.setAddPullOutForce(True)
bolt1.PlainStrandCable.setPullOutForce(1.7)
bolt1.PlainStrandCable.setConstantShearStiffness(True)
bolt1.PlainStrandCable.setStiffness(1.8)
bolt1.PlainStrandCable.setAddBulges(True)
bolt1.PlainStrandCable.setBulgeType(BulgeTypes.PHASE2_BULGE_GARFORD_25)
bolt1.PlainStrandCable.setBulgeLocations([1,2])

bolt2.setBoltType(BoltTypes.QUEENS_CABLE)
bolt2.PlainStrandCable.setJointShear(False)
bolt2.PlainStrandCable.setFacePlates(False)
bolt2.PlainStrandCable.setAddPullOutForce(False)
bolt2.PlainStrandCable.setConstantShearStiffness(False)
bolt2.PlainStrandCable.setAddBulges(False)

bolt3.setBoltType(BoltTypes.QUEENS_CABLE)
bolt3.PlainStrandCable.setJointShear(True)
bolt3.PlainStrandCable.setFacePlates(False)
bolt3.PlainStrandCable.setAddPullOutForce(False)
bolt3.PlainStrandCable.setConstantShearStiffness(False)
bolt3.PlainStrandCable.setAddBulges(False)

bolt4.setBoltType(BoltTypes.QUEENS_CABLE)
bolt4.PlainStrandCable.setJointShear(False)
bolt4.PlainStrandCable.setFacePlates(True)
bolt4.PlainStrandCable.setAddPullOutForce(False)
bolt4.PlainStrandCable.setConstantShearStiffness(False)
bolt4.PlainStrandCable.setAddBulges(False)

bolt5.setBoltType(BoltTypes.QUEENS_CABLE)
bolt5.PlainStrandCable.setJointShear(False)
bolt5.PlainStrandCable.setFacePlates(False)
bolt5.PlainStrandCable.setAddPullOutForce(True)
bolt5.PlainStrandCable.setPullOutForce(1.1)
bolt5.PlainStrandCable.setConstantShearStiffness(False)
bolt5.PlainStrandCable.setAddBulges(False)

bolt6.setBoltType(BoltTypes.QUEENS_CABLE)
bolt6.PlainStrandCable.setJointShear(False)
bolt6.PlainStrandCable.setFacePlates(False)
bolt6.PlainStrandCable.setAddPullOutForce(False)
bolt6.PlainStrandCable.setConstantShearStiffness(True)
bolt6.PlainStrandCable.setStiffness(1.1)
bolt6.PlainStrandCable.setAddBulges(False)

bolt7.setBoltType(BoltTypes.QUEENS_CABLE)
bolt7.PlainStrandCable.setJointShear(False)
bolt7.PlainStrandCable.setFacePlates(False)
bolt7.PlainStrandCable.setAddPullOutForce(False)
bolt7.PlainStrandCable.setConstantShearStiffness(False)
bolt7.PlainStrandCable.setAddBulges(True)
bolt7.PlainStrandCable.setBulgeType(BulgeTypes.PHASE2_BULGE_GARFORD_25)
bolt7.PlainStrandCable.setBulgeLocations([1,2])

bolt8.setBoltType(BoltTypes.QUEENS_CABLE)
bolt8.PlainStrandCable.setJointShear(False)
bolt8.PlainStrandCable.setFacePlates(False)
bolt8.PlainStrandCable.setAddPullOutForce(False)
bolt8.PlainStrandCable.setConstantShearStiffness(False)
bolt8.PlainStrandCable.setAddBulges(True)
bolt8.PlainStrandCable.setBulgeType(BulgeTypes.PHASE2_BULGE_NUTCASE_21)
bolt8.PlainStrandCable.setBulgeLocations([1,2])

bolt9.setBoltType(BoltTypes.QUEENS_CABLE)
bolt9.PlainStrandCable.setJointShear(True)
bolt9.PlainStrandCable.setFacePlates(False)
bolt9.PlainStrandCable.setAddPullOutForce(True)
bolt9.PlainStrandCable.setPullOutForce(1.1)
bolt9.PlainStrandCable.setConstantShearStiffness(False)
bolt9.PlainStrandCable.setAddBulges(True)
bolt9.PlainStrandCable.setBulgeType(BulgeTypes.PHASE2_BULGE_GARFORD_25)
bolt9.PlainStrandCable.setBulgeLocations([1,2])

bolt10.setBoltType(BoltTypes.QUEENS_CABLE)
bolt10.PlainStrandCable.setJointShear(False)
bolt10.PlainStrandCable.setFacePlates(True)
bolt10.PlainStrandCable.setAddPullOutForce(False)
bolt10.PlainStrandCable.setConstantShearStiffness(True)
bolt10.PlainStrandCable.setStiffness(1.1)
bolt10.PlainStrandCable.setAddBulges(False)

bolt11.setBoltType(BoltTypes.QUEENS_CABLE)
bolt11.PlainStrandCable.setJointShear(True)
bolt11.PlainStrandCable.setFacePlates(True)
bolt11.PlainStrandCable.setAddPullOutForce(True)
bolt11.PlainStrandCable.setPullOutForce(1.1)
bolt11.PlainStrandCable.setConstantShearStiffness(False)
bolt11.PlainStrandCable.setAddBulges(False)

bolt12.setBoltType(BoltTypes.QUEENS_CABLE)
bolt12.PlainStrandCable.setJointShear(False)
bolt12.PlainStrandCable.setFacePlates(False)
bolt12.PlainStrandCable.setAddPullOutForce(False)
bolt12.PlainStrandCable.setConstantShearStiffness(True)
bolt12.PlainStrandCable.setStiffness(1.1)
bolt12.PlainStrandCable.setAddBulges(True)
bolt12.PlainStrandCable.setBulgeType(BulgeTypes.PHASE2_BULGE_GARFORD_25)
bolt12.PlainStrandCable.setBulgeLocations([1,2])

bolt13.setBoltType(BoltTypes.QUEENS_CABLE)
bolt13.PlainStrandCable.setJointShear(True)
bolt13.PlainStrandCable.setFacePlates(True)
bolt13.PlainStrandCable.setAddPullOutForce(False)
bolt13.PlainStrandCable.setConstantShearStiffness(False)
bolt13.PlainStrandCable.setAddBulges(True)
bolt13.PlainStrandCable.setBulgeType(BulgeTypes.PHASE2_BULGE_GARFORD_25)
bolt13.PlainStrandCable.setBulgeLocations([1,2])

'''
assert(bolt1.PlainStrandCable.getBoreholeDiameter(), 1.21)
assert(bolt1.PlainStrandCable.getCableDiameter(), 1.2)
assert(bolt1.PlainStrandCable.getCableModulusE(), 1.3)
assert(bolt1.PlainStrandCable.getCablePeak(), 1.4)
assert(bolt1.PlainStrandCable.getOutofPlaneSpacing(), 1.5)
assert(bolt1.PlainStrandCable.getWaterCementRatio(), 1.6)
assert(bolt1.PlainStrandCable.getJointShear(), True)
assert(bolt1.PlainStrandCable.getFacePlates(), True)
assert(bolt1.PlainStrandCable.getAddPullOutForce(), True)
assert(bolt1.PlainStrandCable.getPullOutForce(), 1.7)
assert(bolt1.PlainStrandCable.getConstantShearStiffness(), True)
assert(bolt1.PlainStrandCable.getStiffness(), 1.8)
assert(bolt1.PlainStrandCable.getAddBulges(), True)
assert(bolt1.PlainStrandCable.getBulgeType(), BulgeTypes.PHASE2_BULGE_GARFORD_25)
assert(bolt1.PlainStrandCable.getBulgeLocations(), [1,2])
'''

model.save()

pass