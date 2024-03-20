import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestMohrCoulombPile(unittest.TestCase):
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
    def testMohrCoulombPileProperty(self):
        pile = self.pile
        self.pile.setSkinResistance(PileSkinResistanceType.MOHR_COULOMB)
        pile.MohrCoulombPile.setShearStiffness(836.5)
        pile.MohrCoulombPile.setNormalStiffness(2628.5)
        pile.MohrCoulombPile.setFrictionAngle(972.5)
        pile.MohrCoulombPile.setResidualFrictionAngle(86.7)
        pile.MohrCoulombPile.setCohesion(762.9)
        pile.MohrCoulombPile.setResidualCohesion(1413.6)
        pile.MohrCoulombPile.setUseShearResistanceCutoff(0)
        pile.MohrCoulombPile.setShearResistanceCutoff(2350.4)
        pile.MohrCoulombPile.setPerimeter(2598.3)
        pile.MohrCoulombPile.setUseBaseResistance(0)
        pile.MohrCoulombPile.setBaseNormalStiffness(2605.0)
        pile.MohrCoulombPile.setBaseForceResistance(3213.4)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.pile = self.model.getAllPileProperties()[0]
        pile = self.pile
        self.assertEqual(pile.MohrCoulombPile.getShearStiffness(), 836.5)
        self.assertEqual(pile.MohrCoulombPile.getNormalStiffness(), 2628.5)
        self.assertEqual(pile.MohrCoulombPile.getFrictionAngle(), 972.5)
        self.assertEqual(pile.MohrCoulombPile.getResidualFrictionAngle(), 86.7)
        self.assertEqual(pile.MohrCoulombPile.getCohesion(), 762.9)
        self.assertEqual(pile.MohrCoulombPile.getResidualCohesion(), 1413.6)
        self.assertEqual(pile.MohrCoulombPile.getUseShearResistanceCutoff(), 0)
        self.assertEqual(pile.MohrCoulombPile.getShearResistanceCutoff(), 2350.4)
        self.assertEqual(pile.MohrCoulombPile.getPerimeter(), 2598.3)
        self.assertEqual(pile.MohrCoulombPile.getUseBaseResistance(), 0)
        self.assertEqual(pile.MohrCoulombPile.getBaseNormalStiffness(), 2605.0)
        self.assertEqual(pile.MohrCoulombPile.getBaseForceResistance(), 3213.4)
