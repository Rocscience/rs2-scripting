from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.modeler.properties.PropertyEnums import*

pathToModelerExecutable = "C:\RS2_dev\Build\Debug_x64\RS2.exe"
pathToInterpreterExecutable = "C:\RS2_dev\Build\Debug_x64\Interpret.exe"
modelPath = r"C:\scriptingModels\Profiles_and_Boreholes.fez"

modelerPort = 60040
interpreterPort = 60041

RS2Modeler.startApplication(port=modelerPort, overridePathToExecutable=pathToModelerExecutable)
modeler = RS2Modeler(port=modelerPort)
modeler.openFile(modelPath)

RS2Interpreter.startApplication(port=interpreterPort, overridePathToExecutable=pathToInterpreterExecutable)
interpreter = RS2Interpreter()
interpreter.openFile(modelPath)

# Close modeler
modeler.closeProgram(False)
# Close interpreter
interpreter.closeProgram(False)
