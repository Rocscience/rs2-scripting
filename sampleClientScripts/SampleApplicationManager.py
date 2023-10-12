from rs2.ApplicationManager import ApplicationManager
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *
import Constants as constants

appManager = ApplicationManager()
appManager.startApplication(constants.modelerDebugPath, constants.modelerPort)

modeler = RS2Modeler(port=constants.modelerPort)
model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")