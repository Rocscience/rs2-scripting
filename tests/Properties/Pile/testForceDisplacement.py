import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

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
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)
    def testForceDisplacementProperty(self):
        pile = self.pile
        self.pile.setSkinResistance(PileSkinResistanceType.ELASTIC)
        pile.ForceDisplacement.setApply(PileEndCondition.DISPLACEMENT)
        pile.ForceDisplacement.setApplyOn(PileForceApplicationPoint.BOTTOM)
        pile.ForceDisplacement.setX(836.5)
        pile.ForceDisplacement.setY(2628.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.pile = self.model.getAllPileProperties()[0]
        pile = self.pile
        self.assertEqual(pile.ForceDisplacement.getApply(), PileEndCondition.DISPLACEMENT)
        self.assertEqual(pile.ForceDisplacement.getApplyOn(), PileForceApplicationPoint.BOTTOM)
        self.assertEqual(pile.ForceDisplacement.getX(), 836.5)
        self.assertEqual(pile.ForceDisplacement.getY(), 2628.5)
    def testForceDisplacementStageFactors(self):
        pile = self.pile
        self.pile.setSkinResistance(PileSkinResistanceType.ELASTIC)
        stageFactor = pile.ForceDisplacement.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setXFactor(972.5)
        stageFactor.setYFactor(86.7)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.pile = self.model.getAllPileProperties()[0]
        pile = self.pile
        stageFactor = pile.ForceDisplacement.stageFactorInterface.getDefinedStageFactors()[1]
        self.assertEqual(stageFactor.getXFactor(), 972.5)
        self.assertEqual(stageFactor.getYFactor(), 86.7)
