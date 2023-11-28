import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestCompositeLiner(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.compositeliner = self.model.getAllCompositeLinerProperties()[0]
    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.model._client.closeConnection()
        os.remove(self.copiedModelPath)

    # Joint reference tests
    def testGetJointPropertyNameSuccess(self):
        compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
        self.assertEqual(compositeliner.getCompositeJointPropertyName(), "Joint 1")

    def testGetJointPropertyNameFailure(self):
        try:
            self.model.getJointPropertyByName("NonExistantJointName")
            self.fail("Expected exception")
        except:
            pass

    def testSetJointPropertyNameSuccess(self):
        compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
        compositeliner.setJointApplied(True)
        compositeliner.setCompositeJointPropertyByName("Joint 2")
        compositeliner.setJointApplied(False)
        self.assertEqual(compositeliner.getCompositeJointPropertyName(), "Joint 2")

    def testSetJointPropertyNameFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.setJointApplied(True)
            compositeliner.setCompositeJointPropertyByName("NonExistantJoint")
            compositeliner.setJointApplied(False)
            self.fail("Expected exception")
        except:
            pass
    
    def testSetJointPropertyNameWithJointUnappliedFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.setCompositeJointPropertyByName("Joint 2")
            self.fail("Expected exception")
        except:
            pass

    # Liner reference tests
    def testGetLinerPropertyNameSuccess(self):
        compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
        self.assertEqual(compositeliner.getCompositeLinerPropertyName(1), "Liner 1")

    def testGetLinerPropertyNameFailure(self):
        try:
            self.model.getLinerPropertyByName("NonExistantLinerName")
            self.fail("Expected exception")
        except:
            pass

    def testGetLinerPropertyNameBeyondMaxLayerLimitFailure(self):
        try:
            compositeLiner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeLiner.getCompositeLinerPropertyName(5)
            self.fail("Expected exception")
        except:
            pass

    def testGetLinerPropertyNameBelowMinLayerLimitFailure(self):
        try:
            compositeLiner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeLiner.getCompositeLinerPropertyName(0)
            self.fail("Expected exception")
        except:
            pass

    def testSetLinerPropertyNameSuccess(self):
        compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
        compositeliner.setCompositeLinerPropertyByName(1, "Liner 2")
        self.assertEqual(compositeliner.getCompositeLinerPropertyName(1), "Liner 2")

    def testSetLinerPropertyNameFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.setCompositeLinerPropertyByName(1, "NonExistantLiner")
            self.fail("Expected exception")
        except:
            pass
        
    def testSetLinerPropertyNameBeyondMaxLayerLimitFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.setCompositeLinerPropertyByName(5, "Liner 1")
            self.fail("Expected exception")
        except:
            pass

    def testSetLinerPropertyNameBeyondMinLayerLimitFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.setCompositeLinerPropertyByName(0, "Liner 1")
            self.fail("Expected exception")
        except:
            pass

    # Joint Applied tests
    def testGetJointAppliedSuccess(self):
        compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
        self.assertEqual(compositeliner.getJointApplied(), False)

    def testSetJointAppliedSuccess(self):
        compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
        compositeliner.setJointApplied(True)
        self.assertEqual(compositeliner.getJointApplied(), True)

    # Number of layers tests
    def testGetNumberOfLayersSuccess(self):
        compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
        self.assertEqual(compositeliner.getNumberOfLayers(), 2)

    def testSetNumberOfLayersSuccess(self):
        compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
        compositeliner.setNumberOfLayers(3)
        self.assertEqual(compositeliner.getNumberOfLayers(), 3)

    def testSetNumberOfLayersBeyondMaxLimitFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.setNumberOfLayers(7)
            self.fail("Expected exception")
        except:
            pass

    def testSetNumberOfLayersBelowMinLimitFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.setNumberOfLayers(0)
            self.fail("Expected exception")
        except:
            pass

    # Install Delay tests
    def testGetInstallDelaySuccess(self):
        compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
        if (compositeliner.getNumberOfLayers() < 2):
            compositeliner.setNumberOfLayers(2)
        self.assertEqual(compositeliner.getInstallDelay(2), 0)

    def testGetInstallDelayBelowMinLayerFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.getInstallDelay(0)
            self.fail("Expected exception")
        except:
            pass

    def testGetInstallDelayBeyondMaxLayerFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.getInstallDelay(6)
            self.fail("Expected exception")
        except:
            pass 

    def testGetInstallDelayOnlyOneLayerFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.setNumberOfLayers(1)
            compositeliner.getInstallDelay(1)
            compositeliner.setNumberOfLayers(2)
            self.fail("Expected exception")
        except:
            pass     

    def testGetInstallDelayFirstLayerFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.getInstallDelay(1)
            self.fail("Expected exception")
        except:
            pass

    def testSetInstallDelayOnlyOneLayerFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.setNumberOfLayers(1)
            compositeliner.setInstallDelay(1, 1)
            compositeliner.setNumberOfLayers(2)
            self.fail("Expected exception")
        except:
            pass 

    def testSetInstallDelayBeyondMaxLayerLimitFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.setInstallDelay(6, 0)
            self.fail("Expected exception")
        except:
            pass

    def testSetInstallDelayBelowMinLayerLimitFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.setInstallDelay(0, 0)
            self.fail("Expected exception")
        except:
            pass

    def testSetInstallDelayFirstLayerFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.setInstallDelay(1, 0)
            self.fail("Expected exception")
        except:
            pass

    def testSetInstallDelaySecondLayerBeyondModelStagesFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            if (compositeliner.getNumberOfLayers() < 2):
                compositeliner.setNumberOfLayers(2)
            compositeliner.setInstallDelay(2, 3)
            self.fail("Expected exception")
        except:
            pass


    def testSetInstallDelaySecondLayerBelowModelStagesFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            if (compositeliner.getNumberOfLayers() < 2):
                compositeliner.setNumberOfLayers(2)
            compositeliner.setInstallDelay(2, -1)
            self.fail("Expected exception")
        except:
            pass

    # Removed Stages tests
    def testGetRemovedStagesFirstLayerSuccess(self):
        compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
        self.assertEqual(compositeliner.getRemovedStage(1), -1)

    def testGetRemovedStagesLayerFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.getRemovedStage(6)
            self.fail("Expected exception")
        except:
            pass

    def testSetRemovedStagesOneStageBelowSuccess(self):
        compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
        compositeliner.setRemovedStage(1, 1)
        self.assertEqual(compositeliner.getRemovedStage(1), 1)

    def testSetRemovedStagesOptionNeverSuccess(self):
        compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
        compositeliner.setRemovedStage(1, -1)
        self.assertEqual(compositeliner.getRemovedStage(1), -1)

    def testSetRemovedStagesFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.setRemovedStage(1, 0)
            self.fail("Expected exception")
        except:
            pass

    def testSetRemovedStagesBeyondMaxLayerLimitFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.setRemovedStage(5, -1)
            self.fail("Expected exception")
        except:
            pass

    def testSetRemovedStagesBelowMinLayerLimitFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.setRemovedStage(0, -1)
            self.fail("Expected exception")
        except:
            pass

    def testSetRemovedStagesFirstLayerBeyondModelStagesFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.setRemovedStage(1, 5)
            self.fail("Expected exception")
        except:
            pass
        
    def testSetRemovedStagesFirstLayerBelowModelStagesFailure(self):
        try:
            compositeliner = self.model.getCompositeLinerPropertyByName("Composite 1")
            compositeliner.setRemovedStage(1, -2)
            self.fail("Expected exception")
        except:
            pass
