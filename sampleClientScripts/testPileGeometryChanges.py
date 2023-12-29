from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *
modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\pilesWithMesh.fez")
pile = model.getAllPileProperties()[0]

pile.setLength(200)
assert pile.getLength() == 200

model.close()


model = modeler.openFile(r"C:\scriptingModels\pilesWithMesh.fez")
pile = model.getAllPileProperties()[0]

pile.Beam.setLinerProperty("Liner 2")
assert pile.Beam.getLinerProperty() == "Liner 2"

model.close()


model = modeler.openFile(r"C:\scriptingModels\pilesWithMesh.fez")
pile = model.getAllPileProperties()[0]

pile.Beam.setApplication(PileApplicationType.APPLICATION_BY_LENGTH)
assert pile.Beam.getApplication() == PileApplicationType.APPLICATION_BY_LENGTH

pile.Beam.defineBeamSegment([1,2,3], ["Liner 1","Liner 2","Liner 3"])
assert pile.Beam.getBeamSegment() == ([1,2,3], ["Liner 1","Liner 2","Liner 3"])

model.close()
