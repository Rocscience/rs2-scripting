from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")
bolt = model.getBoltPropertyByName("Bolt 2")
liner = model.getLinerPropertyByName("Liner 3")

bolt.setBoltType(BoltTypes.FULLY_BONDED)
print(bolt.getBoltType())

bolt.FullyBonded.setBoltDiameter(23)
print(bolt.FullyBonded.getBoltDiameter())

bolt.FullyBonded.setBoltModulusE(201000)
print(bolt.FullyBonded.getBoltModulusE())

bolt.FullyBonded.setTensileCapacity(0.2)
print(bolt.FullyBonded.getTensileCapacity())

bolt.FullyBonded.setResidualTensileCapacity(0.0232)
print(bolt.FullyBonded.getResidualTensileCapacity())

bolt.FullyBonded.setOutofPlaneSpacing(8)
print(bolt.FullyBonded.getOutofPlaneSpacing())

bolt.FullyBonded.setPreTensioningForce(1)
print(bolt.FullyBonded.getPreTensioningForce())

bolt.FullyBonded.setConstantPretensioningForceInInstallStage(False)
print(bolt.FullyBonded.getConstantPretensioningForceInInstallStage())

bolt.FullyBonded.setJointShear(False)
print(bolt.FullyBonded.getJointShear())

liner.StandardBeam.setPoissonsRatio(0.49)
print(liner.StandardBeam.getPoissonsRatio())

liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)
print(liner.getLinerType())

liner.StandardBeam.setMethod(GeometryChoice.LNP_USE_AREA)
print(liner.StandardBeam.getMethod())

liner.StandardBeam.setMethod(GeometryChoice.LNP_USE_THICKNESS)
print(liner.StandardBeam.getMethod())

liner.StandardBeam.setThickness(20)
print(liner.StandardBeam.getThickness())

#Thermal needs to be set to static for the following
#-------------------------------------------------------

liner.StandardBeam.setActivateThermal(True)
print(liner.StandardBeam.getActivateThermal())

liner.StandardBeam.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
print(liner.StandardBeam.getStaticTemperatureMode())

liner.StandardBeam.setStaticTemperatureGridToUse("Default Grid")
print(liner.StandardBeam.getStaticTemperatureGridToUse())

liner.StandardBeam.setThermalExpansion(True)
print(liner.StandardBeam.getThermalExpansion())

liner.StandardBeam.setExpansionCoefficient(2)
print(liner.StandardBeam.getExpansionCoefficient())
