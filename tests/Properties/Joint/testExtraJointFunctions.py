import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestExtraJointFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]

    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)

    def testSetDisplacementDependentTableTooShort(self):
        self.joint.setSlipCriterion(JointTypes.JOINT_DISPLACEMENT_DEPENDENT)
        self.assertEqual(self.joint.getSlipCriterion(), JointTypes.JOINT_DISPLACEMENT_DEPENDENT)
 
        self.joint.DisplacementDependent.setDisplacementDependentTable([[1,2,3.3,4],[4,5,6,7]])
        self.assertEqual(self.joint.DisplacementDependent.getDisplacementDependentTable(), [[1,2,3.3,4],[4,5,6,7]])

    def testSetDisplacementDependentTableNotEnoughRows(self):
        self.joint.setSlipCriterion(JointTypes.JOINT_DISPLACEMENT_DEPENDENT)
        self.assertEqual(self.joint.getSlipCriterion(), JointTypes.JOINT_DISPLACEMENT_DEPENDENT)

        with self.assertRaises(Exception):
            self.joint.DisplacementDependent.setDisplacementDependentTable([[1,2,3,4]])

    def testSetDisplacementDependentTableNotEnoughColumns(self):
        self.joint.setSlipCriterion(JointTypes.JOINT_DISPLACEMENT_DEPENDENT)
        self.assertEqual(self.joint.getSlipCriterion(), JointTypes.JOINT_DISPLACEMENT_DEPENDENT)

        with self.assertRaises(Exception):
            self.joint.DisplacementDependent.setDisplacementDependentTable([[1,2],[3,4]])
    
    #non ascending order
    def testSetDisplacementDependentTableNotAscendingOrder(self):
        self.joint.setSlipCriterion(JointTypes.JOINT_DISPLACEMENT_DEPENDENT)
        self.assertEqual(self.joint.getSlipCriterion(), JointTypes.JOINT_DISPLACEMENT_DEPENDENT)

        with self.assertRaises(Exception):
            self.joint.DisplacementDependent.setDisplacementDependentTable([[1,2,3,4],[4,5,6,7],[2,6,7,8]])
    