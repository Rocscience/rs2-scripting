import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestForceDisplacement(unittest.TestCase):
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
    def testForceDisplacementProperty(self):
        pile = self.pile
        self.pile.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_ELASTIC)
        pile.ForceDisplacement.setApply(PileEndCondition.FP_DISPLACEMENT)
        pile.ForceDisplacement.setApplyOn(PileForceApplicationPoint.FP_BOTTOM)
        pile.ForceDisplacement.setX(836.5)
        pile.ForceDisplacement.setY(2628.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.pile = self.model.getAllPileProperties()[0]
        pile = self.pile
        self.assertEqual(pile.ForceDisplacement.getApply(), PileEndCondition.FP_DISPLACEMENT)
        self.assertEqual(pile.ForceDisplacement.getApplyOn(), PileForceApplicationPoint.FP_BOTTOM)
        self.assertEqual(pile.ForceDisplacement.getX(), 836.5)
        self.assertEqual(pile.ForceDisplacement.getY(), 2628.5)
    def testForceDisplacementStageFactors(self):
        self.pile.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_ELASTIC)
        stageFactor = self.pile.ForceDisplacement.getStageFactors()[1]
        stageFactor.setXFactor(972.5)
        stageFactor.setYFactor(86.7)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.pile = self.model.getAllPileProperties()[0]
        stageFactor = self.pile.ForceDisplacement.getStageFactors()[1]
        self.assertEqual(stageFactor.getXFactor(), 972.5)
        self.assertEqual(stageFactor.getYFactor(), 86.7)
