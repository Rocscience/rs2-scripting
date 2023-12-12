import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Interpreter import RS2Interpreter
from rs2.generatedInterpreterClientScripts.PropertyEnums import *
from rs2.PropertyEnums import *
import time

parentDirectoryHelper.addParentDirectoryToPath()

class TestGetMeshResults(unittest.TestCase):
    pathToComputedModel = "C:\scriptingModels\Profiles_and_Boreholes.fez"

    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = TestGetMeshResults.pathToComputedModel
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.interpreter = RS2Interpreter()
        # self.model = self.interpreter.openFile(self.copiedModelPath)
    def tearDown(self):
        time.sleep(2)
        os.remove(self.copiedModelPath)
    
    @unittest.skipIf(not pathToComputedModel, "requires path to computed model for RS2 Interpreter")  
    def testGetMeshResultsSuccess(self):
        interpreter = self.interpreter
        interpreter.getMeshResults(ExportResultType.VOLUMETRIC_PLASTIC_STRAIN)
    
    @unittest.skipIf(not pathToComputedModel, "requires path to computed model for RS2 Interpreter")  
    def testGetMeshResultsFailure(self):
        try:
            interpreter = self.interpreter
            interpreter.getMeshResults(CompositeJointPlacementTypes.BETWEEN_FIRST_AND_SECOND_LINER)
            self.fail("Expected exception")
        except:
            pass