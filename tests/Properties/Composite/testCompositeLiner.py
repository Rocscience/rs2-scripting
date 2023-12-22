import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestCompositeLiner(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.compositeliner = self.model.getAllCompositeLinerProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testCompositeLinerProperty(self):
        compositeliner = self.compositeliner
        compositeliner.setCompositeName("VYJpH")
        compositeliner.setCompositeColor(31891)
        compositeliner.setJointPlacement(CompositeJointPlacementTypes.BETWEEN_SOIL_ROCK_AND_FIRST_LINER)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.compositeliner = self.model.getAllCompositeLinerProperties()[0]
        compositeliner = self.compositeliner
        self.assertEqual(compositeliner.getCompositeName(), "VYJpH")
        self.assertEqual(compositeliner.getCompositeColor(), 31891)
        self.assertEqual(compositeliner.getJointPlacement(), CompositeJointPlacementTypes.BETWEEN_SOIL_ROCK_AND_FIRST_LINER)
