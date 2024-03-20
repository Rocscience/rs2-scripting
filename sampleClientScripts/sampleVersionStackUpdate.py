from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
from rs2.interpreter.RS2Interpreter import RS2Interpreter



source = r"C:\scriptingModels\2_material.fez"
destination = r"C:\scriptingModels\output.fez"
destination_2 = r"C:\scriptingModels\output2.fez"

modeler = RS2Modeler()
model = modeler.openFile(source)
model.save()
model.save()
model.saveAs(destination)
model.save()
model.save()

model.compute()


interpret_instance = RS2Interpreter()
model = interpret_instance.openFile(destination_2)
model.save()
model.save()
#model.saveAs(destination_2)


pass
pass