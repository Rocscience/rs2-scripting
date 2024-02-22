import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestBaseJoint(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testBaseJointProperty(self):
        joint = self.joint
        joint.setJointName("VYJpH")
        joint.setJointColor(31891)
        joint.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SIMPLE)
        joint.setInitialDeformation(0)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.getJointName(), "VYJpH")
        self.assertEqual(joint.getJointColor(), 31891)
        self.assertEqual(joint.getSlipCriterion(), JointTypes.JOINT_HYPERBOLIC_SIMPLE)
        self.assertEqual(joint.getInitialDeformation(), 0)
    def testRepeatedSetPropertyName(self):
        joint = self.joint
        joint.setJointName("Test")
        joint.setJointName("Test")
        joint.setJointName("Test")
        self.assertEqual(joint.getJointName(), "Test")
