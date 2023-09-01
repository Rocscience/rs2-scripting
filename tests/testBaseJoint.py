import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from src.rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestBaseJoint(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/blankProject.fez"
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
        joint.setJointName("Tx60l")
        joint.setJointColor(31270)
        joint.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SIMPLE)
        joint.setInitialDeformation(1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.getJointName(), "Tx60l")
        self.assertEqual(joint.getJointColor(), 31270)
        self.assertEqual(joint.getSlipCriterion(), JointTypes.JOINT_HYPERBOLIC_SIMPLE)
        self.assertEqual(joint.getInitialDeformation(), 1)
