import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestElastic(unittest.TestCase):
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
    def testElasticProperty(self):
        pile = self.pile
        self.pile.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_ELASTIC)
        pile.Elastic.setShearStiffness(836.5)
        pile.Elastic.setNormalStiffness(2628.5)
        pile.Elastic.setUseBaseResistance(0)
        pile.Elastic.setBaseNormalStiffness(86.7)
        pile.Elastic.setBaseForceResistance(762.9)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.pile = self.model.getAllPileProperties()[0]
        pile = self.pile
        self.assertEqual(pile.Elastic.getShearStiffness(), 836.5)
        self.assertEqual(pile.Elastic.getNormalStiffness(), 2628.5)
        self.assertEqual(pile.Elastic.getUseBaseResistance(), 0)
        self.assertEqual(pile.Elastic.getBaseNormalStiffness(), 86.7)
        self.assertEqual(pile.Elastic.getBaseForceResistance(), 762.9)
