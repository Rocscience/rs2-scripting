from RS2Modeler import RS2Modeler

modeler = RS2Modeler()

model = modeler.openFile(r"C:\Intel\simple_3_stage.fez")
bolt = model.getFirstBolt()

bolt.setBoltType(bolt.BoltTypes.FULLY_BONDED)
print(bolt.getBoltType())

bolt.setBoltName("test1")
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

#model.saveAndCompute()

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
