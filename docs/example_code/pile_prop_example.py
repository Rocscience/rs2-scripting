from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
RS2Modeler.startApplication(port=60081)
modeler = RS2Modeler(port=60081)
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

pile = model.getAllPileProperties()[0]

pile.setPileName("MultiLinear Pile")
pile.setConnectionType(PileConnectionType.HINGED)
pile.setLength(6)
pile.setOutOfPlaneSpacing(0.6)

pile.setSkinResistance(PileSkinResistanceType.MULTI_LINEAR)
pile.MultiLinear.setShearStiffness(1001)

pile.MultiLinear.setDefinitionMethod(PileDefinitionMethod.DISTANCE_FROM_TOP)
pile.MultiLinear.setCoordinates([5,6,7],[10,11,12])

pile.MultiLinear.setUseBaseResistance(False)

pile.Beam.setApplication(PileApplicationType.DEFINE_BEAM_SEGMENT_BY_LENGTH)
pile.Beam.defineBeamSegment([3,6], ["Liner 4", "Liner 5"])

pile.ForceDisplacement.setApply(PileEndCondition.FORCE)
pile.ForceDisplacement.setX(0.5)
pile.ForceDisplacement.setY(0.6)

model.close()

modeler.closeProgram()