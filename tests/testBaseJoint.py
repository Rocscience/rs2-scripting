import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

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
        joint.setJointName("QpSv9")
        joint.setJointColor(17399)
        joint.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SIMPLE)
        joint.setInitialDeformation(0)
        joint.SetApplySSR(True)
        joint.SetPermeable(True)
        joint.SetMeshConforming(True)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
        joint = self.joint
        self.assertEqual(joint.getJointName(), "QpSv9")
        self.assertEqual(joint.getJointColor(), 17399)
        self.assertEqual(joint.getSlipCriterion(), JointTypes.JOINT_HYPERBOLIC_SIMPLE)
        self.assertEqual(joint.getInitialDeformation(), 0)
        self.assertEqual(joint.GetApplySSR(), True)
        self.assertEqual(joint.GetPermeable(), True)
        self.assertEqual(joint.GetMeshConforming(), True)
