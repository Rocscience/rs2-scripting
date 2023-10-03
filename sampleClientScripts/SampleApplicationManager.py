from rs2.ApplicationManager import ApplicationManager
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *

appManager = ApplicationManager()
appManager.startApplication(r"C:\Users\WilliamSati\source\repos\RS2\RS2_2018\Build\Debug_x64\RS2.exe", 60057)

modeler = RS2Modeler(port=60057)
model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")