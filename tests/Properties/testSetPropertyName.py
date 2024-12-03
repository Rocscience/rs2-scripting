import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestSetPropertyName(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.bolt = self.model.getAllBoltProperties()[0]
        self.compositeLiner = self.model.getAllCompositeLinerProperties()[0]
        self.joint = self.model.getAllJointProperties()[0]
        self.liner = self.model.getAllLinerProperties()[0]
        self.material = self.model.getAllMaterialProperties()[0]
        self.pile = self.model.getAllPileProperties()[0]
        self.structuralInterface = self.model.getAllStructuralInterfaceProperties()[0]
    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)

    def testBoltRepeatedSetPropertyName(self):
        bolt = self.bolt
        bolt.setBoltName("Test")
        bolt.setBoltName("Test")
        bolt.setBoltName("Test")
        self.assertEqual(bolt.getBoltName(), "Test")

    def testCompositeLinerRepeatedSetPropertyName(self):
        compositeliner = self.compositeLiner
        compositeliner.setCompositeName("Test")
        compositeliner.setCompositeName("Test")
        compositeliner.setCompositeName("Test")
        self.assertEqual(compositeliner.getCompositeName(), "Test")

    def testJointRepeatedSetPropertyName(self):
        joint = self.joint
        joint.setJointName("Test")
        joint.setJointName("Test")
        joint.setJointName("Test")
        self.assertEqual(joint.getJointName(), "Test")

    def testLinerRepeatedSetPropertyName(self):
        liner = self.liner
        liner.setLinerName("Test")
        liner.setLinerName("Test")
        liner.setLinerName("Test")
        self.assertEqual(liner.getLinerName(), "Test")

    def testMaterialRepeatedSetPropertyName(self):
        material = self.material
        material.setMaterialName("Test")
        material.setMaterialName("Test")
        material.setMaterialName("Test")
        self.assertEqual(material.getMaterialName(), "Test")

    def testPileRepeatedSetPropertyName(self):
        pile = self.pile
        pile.setPileName("Test")
        pile.setPileName("Test")
        pile.setPileName("Test")
        self.assertEqual(pile.getPileName(), "Test")

    def testStructuralInterfaceRepeatedSetPropertyName(self):
        interface = self.structuralInterface
        interface.setStructuralInterfaceName("Test")
        interface.setStructuralInterfaceName("Test")
        interface.setStructuralInterfaceName("Test")
        self.assertEqual(interface.getStructuralInterfaceName(), "Test")