import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestMultiLinear(unittest.TestCase):
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
    def testMultiLinearProperty(self):
        pile = self.pile
        self.pile.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_MULTI_LINEAR)
        pile.MultiLinear.setShearStiffness(836.5)
        pile.MultiLinear.setNormalStiffness(2628.5)
        pile.MultiLinear.setDefinitionMethod(PileDefinitionMethod.ELEVATION)
        pile.MultiLinear.setUseBaseResistance(0)
        pile.MultiLinear.setBaseNormalStiffness(86.7)
        pile.MultiLinear.setBaseForceResistance(762.9)
        pile.MultiLinear.setCoordinates([1,2,3], [4,5,6])
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.pile = self.model.getAllPileProperties()[0]
        pile = self.pile
        self.assertEqual(pile.MultiLinear.getShearStiffness(), 836.5)
        self.assertEqual(pile.MultiLinear.getNormalStiffness(), 2628.5)
        self.assertEqual(pile.MultiLinear.getDefinitionMethod(), PileDefinitionMethod.ELEVATION)
        self.assertEqual(pile.MultiLinear.getUseBaseResistance(), 0)
        self.assertEqual(pile.MultiLinear.getBaseNormalStiffness(), 86.7)
        self.assertEqual(pile.MultiLinear.getBaseForceResistance(), 762.9)
        self.assertEqual(pile.MultiLinear.getCoordinates(), ([1,2,3],[4,5,6]))
