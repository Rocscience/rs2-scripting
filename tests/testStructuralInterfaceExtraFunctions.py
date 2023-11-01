import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*
from rs2.ColorPicker import ColorPicker

parentDirectoryHelper.addParentDirectoryToPath()

class TestStructuralInterface(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.liner = self.model.getAllLinerProperties()[0]

    def tearDown(self):
        self.model.close()
        self.model._client.closeConnection()
        os.remove(self.copiedModelPath)

    # Interface Name tests
    def testGetStructuralInterfaceNameSuccess(self):
        interface = self.model.getStructuralInterfacePropertyByName("Structural 1")
        self.assertEqual(interface.getStructuralInterfaceName(), "Structural 1")

    def testGetStructuralInterfaceNameFailure(self):
        try:
            self.model.getStructuralInterfacePropertyByName("NonExistantInterfaceName")
            self.fail("Expected exception")
        except:
            pass

    def testSetStructuralInterfaceSuccess(self):
        interface = self.model.getStructuralInterfacePropertyByName("Structural 1")
        interface.setStructuralInterfaceName("Test Name")
        self.assertEqual(interface.getStructuralInterfaceName(), "Test Name")

    def testSetStructuralInterfaceColorFailure(self):
        try:
            interface = self.model.getStructuralInterfacePropertyByName("Structural 2")
            interface.setColor(ColorPicker.getColorFromRGB(260, 10, 152))
            self.fail("Expected exception")
        except:
            pass

    # Liner reference tests
    def testGetLinerPropertyNameSuccess(self):
        interface = self.model.getStructuralInterfacePropertyByName("Structural 2")
        self.assertEqual(interface.getLinerPropertyName(), "Liner 1")

    def testGetLinerPropertyNameFailure(self):
        try:
            self.model.getLinerPropertyByName("NonExistantLinerName")
            self.fail("Expected exception")
        except:
            pass

    def testSetLinerPropertyNameSuccess(self):
        interface = self.model.getStructuralInterfacePropertyByName("Structural 2")
        interface.setLinerPropertyByName("Liner 2")
        self.assertEqual(interface.getLinerPropertyName(), "Liner 2")

    def testSetLinerPropertyNameFailure(self):
        try:
            interface = self.model.getStructuralInterfacePropertyByName("Structural 2")
            interface.setLinerPropertyByName("NonExistantLiner")
            self.fail("Expected exception")
        except:
            pass

    # Positive Side Joint Reference tests
    def testGetPositiveJointPropertyNameSuccess(self):
        interface = self.model.getStructuralInterfacePropertyByName("Structural 2")
        self.assertEqual(interface.getPositiveJointPropertyName(), "Joint 1")

    def testGetPositiveNegativeJointPropertyNameFailure(self):
        try:
            self.model.getJointPropertyByName("NonExistantJointName")
            self.fail("Expected exception")
        except:
            pass

    def testSetPositiveJointPropertyNameSuccess(self):
        interface = self.model.getStructuralInterfacePropertyByName("Structural 2")
        interface.setPositiveJointPropertyByName("Joint 2")
        self.assertEqual(interface.getPositiveJointPropertyName(), "Joint 2")

    def testSetPositiveNegativeJointPropertyNameFailure(self):
        try:
            interface = self.model.getStructuralInterfacePropertyByName("Structural 2")
            interface.setPositiveJointPropertyByName("NonExistantJoint")
            self.fail("Expected exception")
        except:
            pass
    
    # Negative Side Joint Reference tests
    def testGetNegativeJointPropertyNameSuccess(self):
        interface = self.model.getStructuralInterfacePropertyByName("Structural 2")
        self.assertEqual(interface.getNegativeJointPropertyName(), "Joint 1")

    def testSetNegativeJointPropertyNameSuccess(self):
        interface = self.model.getStructuralInterfacePropertyByName("Structural 2")
        interface.setNegativeJointPropertyByName("Joint 2")
        self.assertEqual(interface.getNegativeJointPropertyName(), "Joint 2")
