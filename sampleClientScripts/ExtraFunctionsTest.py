from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage_with_thermal_static.fez")
bolt = model.getBoltPropertyByName("Bolt 2")
liner = model.getLinerPropertyByName("Liner 3")

bolt.setBoltType(BoltTypes.PLAIN_STRAND_CABLE)
print(bolt.getBoltType())

#check if the extra function "setBulgeLocations" and "getBulgeLocations" work
bolt.PlainStrandCable.setAddBulges(True)
bolt.PlainStrandCable.setBulgeLocations([33,35])
print(bolt.PlainStrandCable.getBulgeLocations())
bolt.PlainStrandCable.setBulgeType(BulgeTypes.NUT_CASE_21MM)

#check if the extra function "setStaticTemperatureGridToUse" and "getStaticTemperatureGridToUse" work
liner.setLinerType(LinerTypes.STANDARD_BEAM)
liner.StandardBeam.setActivateThermal(True)
liner.StandardBeam.setStaticTemperatureMode(StaticWaterModes.GRID)
liner.StandardBeam.setStaticTemperatureGridToUse("Grid 2")
print(liner.StandardBeam.getStaticTemperatureGridToUse())
