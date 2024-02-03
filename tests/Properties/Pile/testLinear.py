import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestLinear(unittest.TestCase):
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
    def testLinearProperty(self):
        pile = self.pile
        self.pile.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_LINEAR)
        pile.Linear.setShearStiffness(836.5)
        pile.Linear.setNormalStiffness(2628.5)
        pile.Linear.setMaxTractionAtTheTop(972.5)
        pile.Linear.setMaxTractionAtTheBottom(86.7)
        pile.Linear.setUseBaseResistance(1)
        pile.Linear.setBaseNormalStiffness(1413.6)
        pile.Linear.setBaseForceResistance(468.3)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.pile = self.model.getAllPileProperties()[0]
        pile = self.pile
        self.assertEqual(pile.Linear.getShearStiffness(), 836.5)
        self.assertEqual(pile.Linear.getNormalStiffness(), 2628.5)
        self.assertEqual(pile.Linear.getMaxTractionAtTheTop(), 972.5)
        self.assertEqual(pile.Linear.getMaxTractionAtTheBottom(), 86.7)
        self.assertEqual(pile.Linear.getUseBaseResistance(), 1)
        self.assertEqual(pile.Linear.getBaseNormalStiffness(), 1413.6)
        self.assertEqual(pile.Linear.getBaseForceResistance(), 468.3)
