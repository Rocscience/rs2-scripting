from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")

composite = model.getAllCompositeLinerProperties()[0]

composite.setCompositeName("Example Composite 1")
composite.setNumberOfLayers(3)

composite.setCompositeLinerPropertyByName(1, "Liner 2")
composite.setCompositeLinerPropertyByName(2, "Liner 3")
composite.setCompositeLinerPropertyByName(3, "Liner 5")

composite.setInstallDelay(2, 2)
composite.setInstallDelay(3, 1)

composite.setRemovedStage(1, 1)
composite.setRemovedStage(2, 2)
composite.setRemovedStage(3, -1)

composite.setJointApplied(True)
composite.setCompositeJointPropertyByName("Joint 5")
composite.setJointPlacement(CompositeJointPlacementTypes.BETWEEN_THIRD_AND_FOURTH_LINER)