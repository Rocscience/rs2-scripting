from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"S:\willSati\Scripting\TestModels\Profiles_and_Boreholes.fez")
compositeLiner = model.getCompositeLinerPropertyByName("Composite 1")

# Get/Set liner name
print("Composite Liner Name = ", compositeLiner.getCompositeName())
# compositeLiner.setCompositeName("Test Composite 1")

# Get/Set number of layers
print("Number of composite liner layers = ", compositeLiner.getNumberOfLayers())
compositeLiner.setNumberOfLayers(3)

# Get/Set joint interface checkbox
print("Allow Joint Interface ? = ", compositeLiner.getJointApplied())
compositeLiner.setJointApplied(True)

# Get/Set liner type reference
print("Second Layer Liner Name = ", compositeLiner.getCompositeLinerPropertyName(2))
compositeLiner.setCompositeLinerPropertyByName(2, "Liner 5")

# Get/Set joint reference name
print("Joint Name = ", compositeLiner.getCompositeJointPropertyName())
compositeLiner.setCompositeJointPropertyByName("Joint 2")

# Get/Set joint placement
print("Joint Placement = ", compositeLiner.getJointPlacement())
compositeLiner.setJointPlacement(CompositeJointPlacementTypes.BETWEEN_SECOND_AND_THIRD_LINER)

# Get/Set Install Delay
print("First Layer install delay = ", compositeLiner.getInstallDelay(1))
compositeLiner.setInstallDelay(2, 1)

# Get/Set Removed Stages
print("Third Layer Removed Stages = ", compositeLiner.getRemovedStage(3))
compositeLiner.setRemovedStage(3, -1)