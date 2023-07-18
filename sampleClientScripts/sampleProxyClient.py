from rs2.RS2Modeler import RS2Modeler

modeler = RS2Modeler()

model = modeler.openFile(r"C:\Users\CarterComish\OneDrive - Rocscience Inc\Documents\bolt_and_materials.fez")
bolt = model.getFirstBolt()
liner = model.getLinerByName("Liner 3")

bolt.setBoltType(bolt.BoltTypes.FULLY_BONDED)
print(bolt.getBoltType())

bolt.setBoltName("test1")
print(bolt.getBoltName())

bolt.setBoltDiameter(24)
print(bolt.getBoltDiameter())

bolt.setBoltModulusE(202000)
print(bolt.getBoltModulusE())

bolt.setTensileCapacity(0.3)
print(bolt.getTensileCapacity())

bolt.setResidualTensileCapacity(0.0332)
print(bolt.getResidualTensileCapacity())

bolt.setOutofPlaneSpacing(9)
print(bolt.getOutofPlaneSpacing())

bolt.setPreTensioningForce(2)
print(bolt.getPreTensioningForce())

bolt.setConstantPretensioningForceInInstallStage(True)
print(bolt.getConstantPretensioningForceInInstallStage())

bolt.setJointShear(True)
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
