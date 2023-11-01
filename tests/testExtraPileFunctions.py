#Manually generated

import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestPileExtras(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.pile = self.model.getAllPileProperties()[0]
    def tearDown(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)

    def testSetCoordinatesFailure(self):
        try:
            self.pile.MultiLinear.setCoordinates([1,2,3],[4,5,6,7])
            self.fail("Expected an exception")
        except:
            pass

    def testSetCoordinatesSuccess(self):
        self.pile.MultiLinear.setCoordinates([1,2,3],[4,5,6])
        self.assertEqual(self.pile.MultiLinear.getCoordinates(), ([1,2,3],[4,5,6]))
    
    def testSetBeamLinerPropertyFilure(self):
        try:
            self.pile.Beam.setLinerProperty("NonExistant")
            self.fail("Expected an exception")
        except:
            pass

    def testSetBeamLinerPropertySuccess(self):
        self.pile.Beam.setLinerProperty("Liner 1")
        self.assertEqual(self.pile.Beam.getLinerProperty(), "Liner 1")

    def testDefineBeamSegmentFailureMismatchLengths(self):
        try:
            self.pile.Beam.defineBeamSegment([1,2,3], ["Liner 1","Liner 2","Liner 3","Liner 4"])
            self.fail("Expected vectors required to be of same length")
        except:
            pass

    def testDefineBeamSegmentFailureNonExistantLiner(self):
        try:
            self.pile.Beam.defineBeamSegment([1,2,3], ["Liner 1","Liner 2","NonExistant"])
            self.fail("Expected invalid liner name")
        except:
            pass

    def testDefineBeamSegmentSuccess(self):
        self.pile.Beam.defineBeamSegment([1,2,3], ["Liner 1","Liner 2","Liner 3"])
        self.assertEqual(self.pile.Beam.getBeamSegment(), ([1,2,3], ["Liner 1","Liner 2","Liner 3"]))

