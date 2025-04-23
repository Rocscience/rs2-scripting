from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
RS2Modeler.startApplication(port=60084)
modeler = RS2Modeler(port=60084)
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

structural = model.getAllStructuralInterfaceProperties()[0]

structural.setStructuralInterfaceName("Example Structural 1")
structural.setPositiveJointPropertyByName("Joint 3")
structural.setLinerPropertyByName("Liner 4")
structural.setNegativeJointPropertyByName("Joint 5")

model.close()

modeler.closeProgram()