import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestSwellingRock(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
    def tearDown(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)
    def testSwellingRockProperty(self):
        stiffness = self.material.Stiffness
        stiffness.SwellingRock.setAngleToBeddingPlanes(836.5)
        stiffness.SwellingRock.setElasticModulusTangentialToBeddingPlane(2628.5)
        stiffness.SwellingRock.setElasticModulusNormalToBeddingPlanes(972.5)
        stiffness.SwellingRock.setPoissonsRatioOutOfBeddingPlanes(86.7)
        stiffness.SwellingRock.setPoissonsRatioWithinBeddingPlanes(762.9)
        stiffness.SwellingRock.setShearModulus(1413.6)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        stiffness = self.material.Stiffness
        self.assertEqual(stiffness.SwellingRock.getAngleToBeddingPlanes(), 836.5)
        self.assertEqual(stiffness.SwellingRock.getElasticModulusTangentialToBeddingPlane(), 2628.5)
        self.assertEqual(stiffness.SwellingRock.getElasticModulusNormalToBeddingPlanes(), 972.5)
        self.assertEqual(stiffness.SwellingRock.getPoissonsRatioOutOfBeddingPlanes(), 86.7)
        self.assertEqual(stiffness.SwellingRock.getPoissonsRatioWithinBeddingPlanes(), 762.9)
        self.assertEqual(stiffness.SwellingRock.getShearModulus(), 1413.6)
