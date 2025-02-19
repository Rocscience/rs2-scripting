import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestViscoElastic(unittest.TestCase):
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
    def testViscoElasticProperty(self):
        stiffness = self.material.Stiffness
        stiffness.ViscoElastic.setViscoElasticType(ViscoElasticTypes.BURGERS)
        stiffness.ViscoElastic.setBulkModulus(836.5)
        stiffness.ViscoElastic.setMaxwellShearModulus(2628.5)
        stiffness.ViscoElastic.setMaxwellViscosity(972.5)
        stiffness.ViscoElastic.setKelvinShearModulus(86.7)
        stiffness.ViscoElastic.setKelvinViscosity(762.9)
        stiffness.ViscoElastic.setShearModulus(1413.6)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        stiffness = self.material.Stiffness
        self.assertEqual(stiffness.ViscoElastic.getViscoElasticType(), ViscoElasticTypes.BURGERS)
        self.assertEqual(stiffness.ViscoElastic.getBulkModulus(), 836.5)
        self.assertEqual(stiffness.ViscoElastic.getMaxwellShearModulus(), 2628.5)
        self.assertEqual(stiffness.ViscoElastic.getMaxwellViscosity(), 972.5)
        self.assertEqual(stiffness.ViscoElastic.getKelvinShearModulus(), 86.7)
        self.assertEqual(stiffness.ViscoElastic.getKelvinViscosity(), 762.9)
        self.assertEqual(stiffness.ViscoElastic.getShearModulus(), 1413.6)
