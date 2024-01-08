from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")

pile = model.getAllPileProperties()[0]

pile.setPileName("MultiLinear Pile")
pile.setConnectionType(PileConnectionType.CONNECT_HINGED)
pile.setLength(6)
pile.setOutOfPlaneSpacing(0.6)

pile.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_MULTI_LINEAR)
pile.MultiLinear.setShearStiffness(1001)

pile.MultiLinear.setDefinitionMethod(PileDefinitionMethod.DISTANCE_FROM_TOP)
pile.MultiLinear.setCoordinates([5,6,7],[10,11,12])

pile.MultiLinear.setUseBaseResistance(False)

pile.Beam.setApplication(PileApplicationType.APPLICATION_BY_LENGTH)
pile.Beam.defineBeamSegment([3,6], ["Liner 4", "Liner 5"])


pile.ForceDisplacement.setApply(PileEndCondition.FP_FORCE)
pile.ForceDisplacement.setX(0.5)
pile.ForceDisplacement.setY(0.6)

