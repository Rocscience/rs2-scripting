from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")

structural = model.getAllStructuralInterfaceProperties()[0]

structural.setStructuralInterfaceName("Example Structural 1")
structural.setPositiveJointPropertyByName("Joint 3")
structural.setLinerPropertyByName("Liner 4")
structural.setNegativeJointPropertyByName("Joint 5")

