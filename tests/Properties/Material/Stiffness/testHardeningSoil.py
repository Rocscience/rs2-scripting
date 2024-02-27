import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestHardeningSoil(unittest.TestCase):
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
        os.remove(self.copiedModelPath)
    def testHardeningSoilProperty(self):
        stiffness = self.material.Stiffness
        stiffness.HardeningSoil.setERef50(836.5)
        stiffness.HardeningSoil.setERefoed(2628.5)
        stiffness.HardeningSoil.setERefur(972.5)
        stiffness.HardeningSoil.setM(86.7)
        stiffness.HardeningSoil.setReferencePressure(762.9)
        stiffness.HardeningSoil.setPoissonsRatio(1413.6)
        stiffness.HardeningSoil.setPlimit(468.3)
        stiffness.HardeningSoil.setG0ref(2350.4)
        stiffness.HardeningSoil.setGama07(2598.3)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        stiffness = self.material.Stiffness
        self.assertEqual(stiffness.HardeningSoil.getERef50(), 836.5)
        self.assertEqual(stiffness.HardeningSoil.getERefoed(), 2628.5)
        self.assertEqual(stiffness.HardeningSoil.getERefur(), 972.5)
        self.assertEqual(stiffness.HardeningSoil.getM(), 86.7)
        self.assertEqual(stiffness.HardeningSoil.getReferencePressure(), 762.9)
        self.assertEqual(stiffness.HardeningSoil.getPoissonsRatio(), 1413.6)
        self.assertEqual(stiffness.HardeningSoil.getPlimit(), 468.3)
        self.assertEqual(stiffness.HardeningSoil.getG0ref(), 2350.4)
        self.assertEqual(stiffness.HardeningSoil.getGama07(), 2598.3)
