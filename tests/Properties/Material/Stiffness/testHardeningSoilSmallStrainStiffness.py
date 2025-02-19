import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestHardeningSoilSmallStrainStiffness(unittest.TestCase):
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
    def testHardeningSoilSmallStrainStiffnessProperty(self):
        stiffness = self.material.Stiffness
        stiffness.HardeningSoilSmallStrainStiffness.setERef50(836.5)
        stiffness.HardeningSoilSmallStrainStiffness.setERefoed(2628.5)
        stiffness.HardeningSoilSmallStrainStiffness.setERefur(972.5)
        stiffness.HardeningSoilSmallStrainStiffness.setM(86.7)
        stiffness.HardeningSoilSmallStrainStiffness.setReferencePressure(762.9)
        stiffness.HardeningSoilSmallStrainStiffness.setPoissonsRatio(1413.6)
        stiffness.HardeningSoilSmallStrainStiffness.setPlimit(468.3)
        stiffness.HardeningSoilSmallStrainStiffness.setG0ref(2350.4)
        stiffness.HardeningSoilSmallStrainStiffness.setGama07(2598.3)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        stiffness = self.material.Stiffness
        self.assertEqual(stiffness.HardeningSoilSmallStrainStiffness.getERef50(), 836.5)
        self.assertEqual(stiffness.HardeningSoilSmallStrainStiffness.getERefoed(), 2628.5)
        self.assertEqual(stiffness.HardeningSoilSmallStrainStiffness.getERefur(), 972.5)
        self.assertEqual(stiffness.HardeningSoilSmallStrainStiffness.getM(), 86.7)
        self.assertEqual(stiffness.HardeningSoilSmallStrainStiffness.getReferencePressure(), 762.9)
        self.assertEqual(stiffness.HardeningSoilSmallStrainStiffness.getPoissonsRatio(), 1413.6)
        self.assertEqual(stiffness.HardeningSoilSmallStrainStiffness.getPlimit(), 468.3)
        self.assertEqual(stiffness.HardeningSoilSmallStrainStiffness.getG0ref(), 2350.4)
        self.assertEqual(stiffness.HardeningSoilSmallStrainStiffness.getGama07(), 2598.3)
