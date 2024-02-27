import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestPm4Silt(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SILT)
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testPm4SiltProperty(self):
        stiffness = self.material.Stiffness
        stiffness.Pm4Silt.setG0Parameter(836.5)
        stiffness.Pm4Silt.setAutoCalculateNGParameter(0)
        stiffness.Pm4Silt.setNGParameter(972.5)
        stiffness.Pm4Silt.setAutoCalculateVParameter(1)
        stiffness.Pm4Silt.setVParameter(762.9)
        stiffness.Pm4Silt.setPatmParameter(1413.6)
        stiffness.Pm4Silt.setAutoCalculateCGDParameter(0)
        stiffness.Pm4Silt.setCGDParameter(2350.4)
        stiffness.Pm4Silt.setAutoCalculateCGCParameter(1)
        stiffness.Pm4Silt.setCGCParameter(2572.7)
        stiffness.Pm4Silt.setPostShake(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        stiffness = self.material.Stiffness
        self.assertEqual(stiffness.Pm4Silt.getG0Parameter(), 836.5)
        self.assertEqual(stiffness.Pm4Silt.getAutoCalculateNGParameter(), 0)
        self.assertEqual(stiffness.Pm4Silt.getNGParameter(), 972.5)
        self.assertEqual(stiffness.Pm4Silt.getAutoCalculateVParameter(), 1)
        self.assertEqual(stiffness.Pm4Silt.getVParameter(), 762.9)
        self.assertEqual(stiffness.Pm4Silt.getPatmParameter(), 1413.6)
        self.assertEqual(stiffness.Pm4Silt.getAutoCalculateCGDParameter(), 0)
        self.assertEqual(stiffness.Pm4Silt.getCGDParameter(), 2350.4)
        self.assertEqual(stiffness.Pm4Silt.getAutoCalculateCGCParameter(), 1)
        self.assertEqual(stiffness.Pm4Silt.getCGCParameter(), 2572.7)
        self.assertEqual(stiffness.Pm4Silt.getPostShake(), 0)
