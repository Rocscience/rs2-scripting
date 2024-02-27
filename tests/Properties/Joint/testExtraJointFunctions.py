import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

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

    def testSlipStageSuccess(self):
        self.joint.SetAllowSlipStartFromStage(2)
        self.assertEqual(self.joint.GetAllowSlipStartFromStage(), 2)

        #test with 1 and 6 as well
        self.joint.SetAllowSlipStartFromStage(1)
        self.assertEqual(self.joint.GetAllowSlipStartFromStage(), 1)

        self.joint.SetAllowSlipStartFromStage(6)
        self.assertEqual(self.joint.GetAllowSlipStartFromStage(), 6)
        
    def testSlipStageFailureTooSmall(self):
        with self.assertRaises(Exception):
            self.joint.SetAllowSlipStartFromStage(0)
    def testSlipStageFailureTooLarge(self):
        with self.assertRaises(Exception):
            self.joint.SetAllowSlipStartFromStage(7)
    
    def testSetApplySSR(self):
        self.joint.SetApplySSR(True)
        self.assertEqual(self.joint.GetApplySSR(), True)
        self.joint.SetApplySSR(False)
        self.assertEqual(self.joint.GetApplySSR(), False)

    def testSetPermeable(self):
        self.joint.SetPermeable(True)
        self.assertEqual(self.joint.GetPermeable(), True)
        self.joint.SetPermeable(False)
        self.assertEqual(self.joint.GetPermeable(), False)

    def testSetMeshConforming(self):
        self.joint.SetMeshConforming(True)
        self.assertEqual(self.joint.GetMeshConforming(), True)
        self.joint.SetMeshConforming(False)
        self.assertEqual(self.joint.GetMeshConforming(), False)

    def testSetAllowSlipStartFromStageSuccess(self):
        self.joint.BartonBandis.setApplyStageFactors(True)
        self.joint.SetAllowSlipStartFromStage(2)
        self.assertEqual(self.joint.GetAllowSlipStartFromStage(), 2)

    def testSetAllowSlipStartFromStageFailureDisabled(self):
        self.joint.BartonBandis.setApplyStageFactors(False)
        with self.assertRaises(Exception):
            self.joint.SetAllowSlipStartFromStage(2)

    def testSetAllowSlipStartFromStageFailureInvalidStage(self):
        self.joint.BartonBandis.setApplyStageFactors(True)
        with self.assertRaises(Exception):
            self.joint.SetAllowSlipStartFromStage(7)
        with self.assertRaises(Exception):
            self.joint.SetAllowSlipStartFromStage(0)