from rs2.RS2Modeler import RS2Modeler

modeler = RS2Modeler()

model = modeler.openFile(r"C:\Users\CarterComish\OneDrive - Rocscience Inc\Documents\bolt_and_materials.fez")
boltList = model.getAllBoltProperties()
linerList = model.getAllLinerProperties()

i = 0
newBoltNames = ["thisBolt1", "thisBolt2", "thisBolt3", "thisBolt4"]
for bolt in boltList:
	print(bolt.getBoltName())
	bolt.setBoltName(newBoltNames[i])
	print(bolt.getBoltName())
	i+=1

	bolt.setBoltDiameter(23)
	print(bolt.getBoltDiameter())

	bolt.setBoltModulusE(201001)
	print(bolt.getBoltModulusE())

	bolt.setTensileCapacity(0.2)
	print(bolt.getTensileCapacity())

	bolt.setResidualTensileCapacity(0.0232)
	print(bolt.getResidualTensileCapacity())

bolt1 = model.getBoltByName("thisBolt1")

bolt1.setBoltDiameter(30)
print(bolt.getBoltDiameter())

i = 0
newLinerNames = ["thisLiner1", "thisLiner2", "thisLiner3", "thisLiner4"]
for liner in linerList:
	print(liner.getLinerName())
	liner.setLinerName(newLinerNames[i])
	print(liner.getLinerName())
	i+=1

	liner.setPoissonsRatio(0.49)
	print(liner.getPoissonsRatio())

	liner.setLinerType(liner.LinerTypes.P2_LINER_STANDARD_BEAM)
	print(liner.getLinerType())

	liner.setMethod(liner.GeometryChoice.LNP_USE_AREA)
	print(liner.getMethod())

	liner.setMethod(liner.GeometryChoice.LNP_USE_THICKNESS)
	print(liner.getMethod())

	liner.setThickness(20)
	print(liner.getThickness())

#Thermal needs to be set to steady state for the following
#-------------------------------------------------------

	liner.setActivateThermal(True)
	print(liner.getActivateThermal())

	liner.setStaticTemperatureMode(liner.StaticWaterModes.SWM_GRID)
	print(liner.getStaticTemperatureMode())

	liner.setStaticTemperatureGridToUse("Default Grid")
	print(liner.getStaticTemperatureGridToUse())

	liner.setThermalExpansion(True)
	print(liner.getThermalExpansion())

	liner.setExpansionCoefficient(2)
	print(liner.getExpansionCoefficient())


#-------------------------------------------------------

liner1 = model.getLinerByName("thisLiner2")
liner1.setActivateThermal(False)
print(liner1.getActivateThermal())
# model.saveAndCompute()

# The following functions show the save and compute functionality.

# modeler.saveAndComputeGroundwaterOnly()
# modeler.saveFile()
# modeler.saveAndComputeFile(ignoreBernoulliLinerWarning=True)
# modeler.saveFileAs(r'C:\RS2ScriptingExample.fez')
# modeler.closeFile()


# def RGB(r,g,b):
#     return int(r + (g << 8) + (b << 16))

# color = RGB(255,255,0)
# print(color)
# bolt.setBoltColor(color)
# print(bolt.getBoltColor())
# bolt.setAddBulges(True)
