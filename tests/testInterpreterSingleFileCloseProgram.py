import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.interpreter.RS2Interpreter import RS2Interpreter

parentDirectoryHelper.addParentDirectoryToPath()

class TestCloseProgram(unittest.TestCase):
    pathToInterpreterExecutable = ""
    interpreterPortToUse = 60041

    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        interpreterModelPath = f"{parentDirectory}/resources/example_computed_model.fez"
        self.interpreterModelPath = f"{parentDirectory}/resources/testInterpreterProject.fez"
        shutil.copy(interpreterModelPath, self.interpreterModelPath)
        RS2Interpreter.startApplication(port=TestCloseProgram.interpreterPortToUse, overridePathToExecutable=TestCloseProgram.pathToInterpreterExecutable)
        self.interpreter = RS2Interpreter(port=TestCloseProgram.interpreterPortToUse)
        self.interpreterModel = self.interpreter.openFile(self.interpreterModelPath)

    def tearDown(self):
        os.remove(self.interpreterModelPath)
        self.interpreter.closeProgram(False)
    
    @unittest.skipIf(not pathToInterpreterExecutable, "requires path to debug build of RS2 Interpreter")  
    def testCloseInterpreterWithChangesSaved(self):
        queryID = self.interpreterModel.AddMaterialQuery(points=[[-2.5, 2.5], [-6, 2.5]])
        self.interpreter.closeProgram(True)
        RS2Interpreter.startApplication(port=TestCloseProgram.interpreterPortToUse, overridePathToExecutable=TestCloseProgram.pathToInterpreterExecutable)
        self.interpreter = RS2Interpreter(port=TestCloseProgram.interpreterPortToUse)
        self.interpreterModel = self.interpreter.openFile(self.interpreterModelPath)
        resultForQuery = self.interpreterModel.GetMaterialQueryResults()
        resultQueryID = None
        self.assertEqual(len(resultForQuery), 1)
        resultQueryID = resultForQuery[0].GetUniqueIdentifier()
        self.assertEqual(queryID, resultQueryID)

    @unittest.skipIf(not pathToInterpreterExecutable, "requires path to debug build of RS2 Interpreter")  
    def testCloseInterpreterWithChangesNotSaved(self):
        # Add a material query to avoid getting No Material Query Error when testing with second query not saved changes
        self.interpreterModel.AddMaterialQuery(points=[[-2.5, 2.5], [-6, 2.5]])
        self.interpreterModel.save()
        
        queryID = self.interpreterModel.AddMaterialQuery(points=[[-2.5, 2.5], [-6, 2.5]])
        self.interpreter.closeProgram(False)
        RS2Interpreter.startApplication(port=TestCloseProgram.interpreterPortToUse, overridePathToExecutable=TestCloseProgram.pathToInterpreterExecutable)
        self.interpreter = RS2Interpreter(port=TestCloseProgram.interpreterPortToUse)
        self.interpreterModel = self.interpreter.openFile(self.interpreterModelPath)
        resultForQuery = self.interpreterModel.GetMaterialQueryResults()
        resultQueryID = None
        self.assertEqual(len(resultForQuery), 1)
        resultQueryID = resultForQuery[0].GetUniqueIdentifier()
        self.assertNotEqual(queryID, resultQueryID)

    @unittest.skipIf(not pathToInterpreterExecutable, "requires path to debug build of RS2 Interpreter")  
    def testPortAvailabilityAfterCloseInterpreter(self):
        self.interpreter.closeProgram(False)
        RS2Interpreter.startApplication(port=TestCloseProgram.interpreterPortToUse, overridePathToExecutable=TestCloseProgram.pathToInterpreterExecutable)
        self.interpreter = RS2Interpreter(port=TestCloseProgram.interpreterPortToUse)
        self.interpreterModel = self.interpreter.openFile(self.interpreterModelPath)
        self.interpreter.closeProgram(False)

        RS2Interpreter.startApplication(port=TestCloseProgram.interpreterPortToUse, overridePathToExecutable=TestCloseProgram.pathToInterpreterExecutable)
        self.interpreter = RS2Interpreter(port=TestCloseProgram.interpreterPortToUse)
        self.interpreterModel = self.interpreter.openFile(self.interpreterModelPath)
