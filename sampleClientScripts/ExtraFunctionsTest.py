from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *
modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage_with_thermal_static.fez")
bolt = model.getBoltByName("Bolt 2")
liner = model.getLinerByName("Liner 3")

bolt.setBoltType(BoltTypes.QUEENS_CABLE)
print(bolt.getBoltType())

#check if the extra function "setBulgeLocations" and "getBulgeLocations" work
bolt.PlainStrandCable.setAddBulges(True)
bolt.PlainStrandCable.setBulgeLocations([33,35])
print(bolt.PlainStrandCable.getBulgeLocations())
bolt.PlainStrandCable.setBulgeType(BulgeTypes.PHASE2_BULGE_NUTCASE_21)

#check if the extra function "setStaticTemperatureGridToUse" and "getStaticTemperatureGridToUse" work
liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)
liner.StandardBeam.setActivateThermal(True)
liner.StandardBeam.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
liner.StandardBeam.setStaticTemperatureGridToUse("Grid 2")
print(liner.StandardBeam.getStaticTemperatureGridToUse())
