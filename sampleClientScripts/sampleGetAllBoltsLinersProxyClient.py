from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\bolt_and_materials.fez")
boltList = model.getAllBoltProperties()
linerList = model.getAllLinerProperties()

i = 0
newBoltNames = ["thisBolt1", "thisBolt2", "thisBolt3", "thisBolt4"]
for bolt in boltList:
	print(bolt.getBoltName())
	bolt.setBoltName(newBoltNames[i])
	print(bolt.getBoltName())
	i+=1

	bolt.FullyBonded.setBoltDiameter(23)
	print(bolt.FullyBonded.getBoltDiameter())

	bolt.FullyBonded.setBoltModulusE(201001)
	print(bolt.FullyBonded.getBoltModulusE())

	bolt.FullyBonded.setTensileCapacity(0.2)
	print(bolt.FullyBonded.getTensileCapacity())

	bolt.FullyBonded.setResidualTensileCapacity(0.0232)
	print(bolt.FullyBonded.getResidualTensileCapacity())

bolt1 = model.getBoltPropertyByName("thisBolt1")

bolt1.FullyBonded.setBoltDiameter(30)
print(bolt.FullyBonded.getBoltDiameter())

i = 0
newLinerNames = ["thisLiner1", "thisLiner2", "thisLiner3", "thisLiner4"]
for liner in linerList:
	print(liner.getLinerName())
	liner.setLinerName(newLinerNames[i])
	print(liner.getLinerName())
	i+=1

	liner.StandardBeam.setPoissonsRatio(0.49)
	print(liner.StandardBeam.getPoissonsRatio())

	liner.setLinerType(LinerTypes.STANDARD_BEAM)
	print(liner.getLinerType())

	liner.StandardBeam.setMethod(GeometryChoice.AREA)
	print(liner.StandardBeam.getMethod())

	liner.StandardBeam.setMethod(GeometryChoice.THICKNESS)
	print(liner.StandardBeam.getMethod())

	liner.StandardBeam.setThickness(20)
	print(liner.StandardBeam.getThickness())

#Thermal needs to be set to steady state for the following
#-------------------------------------------------------

	liner.StandardBeam.setActivateThermal(True)
	print(liner.StandardBeam.getActivateThermal())

	liner.StandardBeam.setStaticTemperatureMode(StaticWaterModes.GRID)
	print(liner.StandardBeam.getStaticTemperatureMode())

	liner.StandardBeam.setStaticTemperatureGridToUse("Default Grid")
	print(liner.StandardBeam.getStaticTemperatureGridToUse())

	liner.StandardBeam.setThermalExpansion(True)
	print(liner.StandardBeam.getThermalExpansion())

	liner.StandardBeam.setExpansionCoefficient(2)
	print(liner.StandardBeam.getExpansionCoefficient())


#-------------------------------------------------------

liner1 = model.getLinerPropertyByName("thisLiner2")
liner1.StandardBeam.setActivateThermal(False)
print(liner1.StandardBeam.getActivateThermal())