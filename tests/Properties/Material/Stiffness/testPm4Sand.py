import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestPm4Sand(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SAND)
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testPm4SandProperty(self):
        stiffness = self.material.Stiffness
        stiffness.Pm4Sand.setG0Parameter(836.5)
        stiffness.Pm4Sand.setVParameter(2628.5)
        stiffness.Pm4Sand.setPatmParameter(972.5)
        stiffness.Pm4Sand.setAutoCalculateCGDParameter(1)
        stiffness.Pm4Sand.setCGDParameter(762.9)
        stiffness.Pm4Sand.setAutoCalculatePSedParameter(0)
        stiffness.Pm4Sand.setPSedParameter(468.3)
        stiffness.Pm4Sand.setPostShake(0)
        stiffness.Pm4Sand.setAutoCalculateFSedMin(1)
        stiffness.Pm4Sand.setFSedMin(2572.7)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        stiffness = self.material.Stiffness
        self.assertEqual(stiffness.Pm4Sand.getG0Parameter(), 836.5)
        self.assertEqual(stiffness.Pm4Sand.getVParameter(), 2628.5)
        self.assertEqual(stiffness.Pm4Sand.getPatmParameter(), 972.5)
        self.assertEqual(stiffness.Pm4Sand.getAutoCalculateCGDParameter(), 1)
        self.assertEqual(stiffness.Pm4Sand.getCGDParameter(), 762.9)
        self.assertEqual(stiffness.Pm4Sand.getAutoCalculatePSedParameter(), 0)
        self.assertEqual(stiffness.Pm4Sand.getPSedParameter(), 468.3)
        self.assertEqual(stiffness.Pm4Sand.getPostShake(), 0)
        self.assertEqual(stiffness.Pm4Sand.getAutoCalculateFSedMin(), 1)
        self.assertEqual(stiffness.Pm4Sand.getFSedMin(), 2572.7)
