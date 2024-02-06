from rs2.utilities.ApplicationManager import ApplicationManager
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

portToUse = 60054

appManager = ApplicationManager()
appManager.startApplication(portToUse)

modeler = RS2Modeler(port=portToUse)
model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")