from rs2.ApplicationManager import ApplicationManager
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import *
import Paths as paths

appManager = ApplicationManager()
appManager.startApplication(paths.modelerDebugPath, 60057)

modeler = RS2Modeler(port=60057)
model = modeler.openFile(r"C:\scriptingModels\simple_3_stage.fez")