import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestBasePile(unittest.TestCase):
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
    def testBasePileProperty(self):
        pile = self.pile
        pile.setPileName("VYJpH")
        pile.setPileColor(31891)
        pile.setConnectionType(PileConnectionType.SEMI_RIGID)
        pile.setSkinResistance(PileSkinResistanceType.MATERIAL_DEPENDENT)
        pile.setMMax(2.2)
        pile.setOutOfPlaneSpacing(2.3)
        pile.setLength(2.2)
        pile.setStageForceDisplacement(True)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.pile = self.model.getAllPileProperties()[0]
        pile = self.pile
        self.assertEqual(pile.getPileName(), "VYJpH")
        self.assertEqual(pile.getPileColor(), 31891)
        self.assertEqual(pile.getConnectionType(), PileConnectionType.SEMI_RIGID)
        self.assertEqual(pile.getSkinResistance(), PileSkinResistanceType.MATERIAL_DEPENDENT)
        self.assertEqual(pile.getMMax(), 2.2)
        self.assertEqual(pile.getOutOfPlaneSpacing(), 2.3)
        self.assertEqual(pile.getLength(), 2.2)
        self.assertEqual(pile.getStageForceDisplacement(), True)
