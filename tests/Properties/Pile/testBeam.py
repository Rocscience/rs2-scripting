import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestBeam(unittest.TestCase):
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
        os.remove(self.copiedModelPath)
    def testBeamProperty(self):
        pile = self.pile
        self.pile.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_ELASTIC)
        pile.Beam.setLinerProperty("Liner 1")
        pile.Beam.defineBeamSegment([1,2], ["Liner 1","Liner 2"])
        pile.Beam.setApplication(PileApplicationType.APPLICATION_BY_LENGTH)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.pile = self.model.getAllPileProperties()[0]
        pile = self.pile
        self.assertEqual(pile.Beam.getLinerProperty(), "Liner 1")
        self.assertEqual(pile.Beam.getBeamSegment(), ([1,2],["Liner 1","Liner 2"]))
        self.assertEqual(pile.Beam.getApplication(), PileApplicationType.APPLICATION_BY_LENGTH)
