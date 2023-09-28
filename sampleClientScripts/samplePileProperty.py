from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")
pile = model.getAllPileProperties()[0]
pile.setConnectionType(PileConnectionType.CONNECT_HINGED)

print(pile.getConnectionType())
