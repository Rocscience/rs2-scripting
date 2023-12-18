from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"S:\willSati\Scripting\TestModels\Profiles_and_Boreholes.fez")
structuralInterface = model.getStructuralInterfacePropertyByName("Structural 1")

# Get/Set Interface Name
print("Structural Interface Name =", structuralInterface.getStructuralInterfaceName())
# structuralInterface.setStructuralInterfaceName("Structural 1")

# Get Color
print("Structural Interface Color = ", structuralInterface.getColor())

# Get/Set + and - side joint names
print("Positive Joint Name = ", structuralInterface.getPositiveJointPropertyName())
structuralInterface.setPositiveJointPropertyByName("Joint 1")
print("Negative Joint Name = ", structuralInterface.getNegativeJointPropertyName())
structuralInterface.setNegativeJointPropertyByName("Joint 3")

# Get/Set Liner Name
print("Liner Name = ", structuralInterface.getLinerPropertyName())
structuralInterface.setLinerPropertyByName("Liner 2")