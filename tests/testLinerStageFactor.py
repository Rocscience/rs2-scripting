import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestLinerStageFactor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        cls.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, cls.copiedModelPath)
        cls.modeler = RS2Modeler()
        cls.model = cls.modeler.openFile(cls.copiedModelPath)
        cls.liner = cls.model.getAllLinerProperties()[0]

        #setup the model so that there is only 1 stage factor.
        sf1 = cls.liner.CableTruss.getStageFactor(1)
        cls.liner.CableTruss.setDefinedStageFactors(StageFactorDefinitionMethod.ABSOLUTE_STAGE_FACTOR, {1: sf1})

    @classmethod
    def tearDownClass(cls):
        cls.model.close()
        os.remove(cls.copiedModelPath)

    def testGetLinerStageFactors(self):
        self.assertEqual(len(self.liner.CableTruss.getDefinedStageFactors()), 1)