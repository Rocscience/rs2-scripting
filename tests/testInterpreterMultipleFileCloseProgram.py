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
        blankModelPath = f"{parentDirectory}/resources/example_computed_model.fez"
        self.copiedModelPath1 = f"{parentDirectory}/resources/testProject1.fez"
        self.copiedModelPath2 = f"{parentDirectory}/resources/testProject2.fez"
        shutil.copy(blankModelPath, self.copiedModelPath1)
        shutil.copy(blankModelPath, self.copiedModelPath2)
        RS2Interpreter.startApplication(port=TestCloseProgram.interpreterPortToUse, overridePathToExecutable=TestCloseProgram.pathToInterpreterExecutable)
        self.interpreter = RS2Interpreter(port=TestCloseProgram.interpreterPortToUse)
        self.interpreterModel1 = self.interpreter.openFile(self.copiedModelPath1)
        self.interpreterModel2 = self.interpreter.openFile(self.copiedModelPath2)
    def tearDown(self):
        os.remove(self.copiedModelPath1)
        os.remove(self.copiedModelPath2)
        self.interpreter.closeProgram(False)
    
    @unittest.skipIf(not pathToInterpreterExecutable, "requires path to debug build of RS2 Interpreter")  
    def testCloseInterpreterWithChangesSaved(self):
        model1_queryID = self.interpreterModel1.AddMaterialQuery(points=[[-2.5, 2.5], [-6, 2.5]])
        model2_queryID = self.interpreterModel2.AddMaterialQuery(points=[[-6, 0], [-6, 2]])
        self.interpreter.closeProgram(True)
        RS2Interpreter.startApplication(port=TestCloseProgram.interpreterPortToUse, overridePathToExecutable=TestCloseProgram.pathToInterpreterExecutable)
        self.interpreter = RS2Interpreter(port=TestCloseProgram.interpreterPortToUse)
        self.interpreterModel1 = self.interpreter.openFile(self.copiedModelPath1)
        self.interpreterModel2 = self.interpreter.openFile(self.copiedModelPath2)
        model1_resultForQuery = self.interpreterModel1.GetMaterialQueryResults()
        model2_resultForQuery = self.interpreterModel2.GetMaterialQueryResults()
        model1_resultQueryID = model2_resultQueryID = None
        self.assertEqual(len(model1_resultForQuery), 1)
        model1_resultQueryID = model1_resultForQuery[0].GetUniqueIdentifier()
        self.assertEqual(len(model2_resultForQuery), 1)
        model2_resultQueryID = model2_resultForQuery[0].GetUniqueIdentifier()
        self.assertEqual(model1_queryID, model1_resultQueryID)
        self.assertEqual(model2_queryID, model2_resultQueryID)

    @unittest.skipIf(not pathToInterpreterExecutable, "requires path to debug build of RS2 Interpreter")  
    def testCloseInterpreterWithChangesNotSaved(self):
        # Add a material query to each model to avoid No Query found exception
        self.interpreterModel1.AddMaterialQuery([[10, -5], [10, 0]])
        self.interpreterModel2.AddMaterialQuery([[12, -5], [12, 0]])
        self.interpreterModel1.save()
        self.interpreterModel2.save()
        # Add new material query points
        model1_queryID = self.interpreterModel1.AddMaterialQuery(points=[[-2.5, 2.5], [-6, 2.5]])
        model2_queryID = self.interpreterModel2.AddMaterialQuery(points=[[-6, 0], [-6, 2]])
        self.interpreter.closeProgram(False)
        RS2Interpreter.startApplication(port=TestCloseProgram.interpreterPortToUse, overridePathToExecutable=TestCloseProgram.pathToInterpreterExecutable)
        self.interpreter = RS2Interpreter(port=TestCloseProgram.interpreterPortToUse)
        self.interpreterModel1 = self.interpreter.openFile(self.copiedModelPath1)
        self.interpreterModel2 = self.interpreter.openFile(self.copiedModelPath2)
        model1_resultForQuery = self.interpreterModel1.GetMaterialQueryResults()
        model2_resultForQuery = self.interpreterModel2.GetMaterialQueryResults()
        model1_resultQueryID = model2_resultQueryID = None
        self.assertEqual(len(model1_resultForQuery), 1)
        model1_resultQueryID = model1_resultForQuery[0].GetUniqueIdentifier()
        self.assertEqual(len(model2_resultForQuery), 1)
        model2_resultQueryID = model2_resultForQuery[0].GetUniqueIdentifier()
        self.assertNotEqual(model1_queryID, model1_resultQueryID)
        self.assertNotEqual(model2_queryID, model2_resultQueryID)

    @unittest.skipIf(not pathToInterpreterExecutable, "requires path to debug build of RS2 Interpreter")  
    def testPortAvailabilityAfterCloseInterpreter(self):
        self.interpreter.closeProgram(False)
        RS2Interpreter.startApplication(port=TestCloseProgram.interpreterPortToUse, overridePathToExecutable=TestCloseProgram.pathToInterpreterExecutable)
        self.interpreter = RS2Interpreter(port=TestCloseProgram.interpreterPortToUse)
        self.interpreterModel1 = self.interpreter.openFile(self.copiedModelPath1)
        self.interpreterModel2 = self.interpreter.openFile(self.copiedModelPath2)
        self.interpreter.closeProgram(False)

        RS2Interpreter.startApplication(port=TestCloseProgram.interpreterPortToUse, overridePathToExecutable=TestCloseProgram.pathToInterpreterExecutable)
        self.interpreter = RS2Interpreter(port=TestCloseProgram.interpreterPortToUse)
        self.interpreterModel1 = self.interpreter.openFile(self.copiedModelPath1)
        self.interpreterModel2 = self.interpreter.openFile(self.copiedModelPath2)
