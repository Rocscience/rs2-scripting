from rs2.modeler.RS2Modeler import RS2Modeler
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
RS2Modeler.startApplication(port=60076)
modeler = RS2Modeler(port=60076)
model = modeler.openFile(rf"{current_dir}\example_models\ExampleModel.fez")

model.close()

modeler.closeProgram()