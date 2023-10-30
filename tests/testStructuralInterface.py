import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestStructuralInterface(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.structuralinterface = self.model.getAllStructuralInterfaceProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testStructuralInterfaceProperty(self):
        structuralinterface = self.structuralinterface
        structuralinterface.setStructuralInterfaceName("Structural 1")
        structuralinterface.setColor(8421376)
        structuralinterface.setPositiveJointPropertyByName("Joint 1")
        structuralinterface.setNegativeJointPropertyByName("Joint 2")
        structuralinterface.setLinerPropertyByName("Liner 1")
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.structuralinterface = self.model.getAllStructuralInterfaceProperties()[0]
        structuralinterface = self.structuralinterface
        self.assertEqual(structuralinterface.getStructuralInterfaceName(), "Structural 1")
        self.assertEqual(structuralinterface.getColor(), 8421376)
        self.assertEqual(structuralinterface.getPositiveJointPropertyName(), "Joint 1")
        self.assertEqual(structuralinterface.getNegativeJointPropertyName(), "Joint 2")
        self.assertEqual(structuralinterface.getLinerPropertyName(), "Liner 1")
