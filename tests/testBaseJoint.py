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
        blankModelPath = f"{parentDirectory}/resources/blankProject.fez"
        self.joint = self.model.getAllJointProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testBaseJointProperty(self):
        joint = self.joint
        joint.setInitialDeformation(True)
        self.assertEqual(joint.getInitialDeformation(), True)
        joint.setJointName("test1")
        self.assertEqual(joint.getJointName(), "test1")
        joint.setJointColor(16073461)
        self.assertEqual(joint.getJointColor(), 16073461)
        joint.setSlipCriterion(JointTypes.JOINT_MATERIAL_DEPENDENT)
        self.assertEqual(joint.getSlipCriterion(), JointTypes.JOINT_MATERIAL_DEPENDENT)
