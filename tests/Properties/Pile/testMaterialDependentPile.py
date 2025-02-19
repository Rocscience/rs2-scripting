import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestMaterialDependentPile(unittest.TestCase):
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
    def testMaterialDependentPileProperty(self):
        pile = self.pile
        self.pile.setSkinResistance(PileSkinResistanceType.MATERIAL_DEPENDENT)
        pile.MaterialDependentPile.setInterfaceCoefficient(836.5)
        pile.MaterialDependentPile.setUseStiffnessMaterialDependent(0)
        pile.MaterialDependentPile.setStiffnessCoefficient(972.5)
        pile.MaterialDependentPile.setShearStiffness(86.7)
        pile.MaterialDependentPile.setNormalStiffness(762.9)
        pile.MaterialDependentPile.setUseShearResistanceCutoff(0)
        pile.MaterialDependentPile.setShearResistanceCutoff(468.3)
        pile.MaterialDependentPile.setPerimeter(2350.4)
        pile.MaterialDependentPile.setUseBaseResistance(1)
        pile.MaterialDependentPile.setBaseNormalStiffness(2572.7)
        pile.MaterialDependentPile.setBaseForceResistance(2605.0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.pile = self.model.getAllPileProperties()[0]
        pile = self.pile
        self.assertEqual(pile.MaterialDependentPile.getInterfaceCoefficient(), 836.5)
        self.assertEqual(pile.MaterialDependentPile.getUseStiffnessMaterialDependent(), 0)
        self.assertEqual(pile.MaterialDependentPile.getStiffnessCoefficient(), 972.5)
        self.assertEqual(pile.MaterialDependentPile.getShearStiffness(), 86.7)
        self.assertEqual(pile.MaterialDependentPile.getNormalStiffness(), 762.9)
        self.assertEqual(pile.MaterialDependentPile.getUseShearResistanceCutoff(), 0)
        self.assertEqual(pile.MaterialDependentPile.getShearResistanceCutoff(), 468.3)
        self.assertEqual(pile.MaterialDependentPile.getPerimeter(), 2350.4)
        self.assertEqual(pile.MaterialDependentPile.getUseBaseResistance(), 1)
        self.assertEqual(pile.MaterialDependentPile.getBaseNormalStiffness(), 2572.7)
        self.assertEqual(pile.MaterialDependentPile.getBaseForceResistance(), 2605.0)
