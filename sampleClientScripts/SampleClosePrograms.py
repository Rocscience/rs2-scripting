from rs2.RS2Modeler import RS2Modeler
from rs2.RS2Interpreter import RS2Interpreter
from rs2.PropertyEnums import *

modeler = RS2Modeler()
interpreter = RS2Interpreter()

# Close modeler
modeler.closeProgram(False)
# Close interpreter
interpreter.closeProgram(False)
