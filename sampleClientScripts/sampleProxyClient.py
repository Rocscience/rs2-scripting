from rs2.RS2Modeler import RS2Modeler

modeler = RS2Modeler()

model = modeler.openFile(r"C:\Intel\simple_3_stage.fez")
boltList = model.getAllBoltProperties()
print(boltList)
bolt = model.getBoltByName("Bolt 2")
liner = model.getLinerByName("Liner 3")

bolt.setBoltType(bolt.BoltTypes.FULLY_BONDED)
print(bolt.getBoltType())

bolt.setBoltName("test2")
print(bolt.getBoltName())

bolt.setBoltDiameter(23)
print(bolt.getBoltDiameter())

bolt.setBoltModulusE(201000)
print(bolt.getBoltModulusE())

bolt.setTensileCapacity(0.2)
print(bolt.getTensileCapacity())

bolt.setResidualTensileCapacity(0.0232)
print(bolt.getResidualTensileCapacity())

bolt.setOutofPlaneSpacing(8)
print(bolt.getOutofPlaneSpacing())

bolt.setPreTensioningForce(1)
print(bolt.getPreTensioningForce())

bolt.setConstantPretensioningForceInInstallStage(False)
print(bolt.getConstantPretensioningForceInInstallStage())

bolt.setJointShear(False)
print(bolt.getJointShear())

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
