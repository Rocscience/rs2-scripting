import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestJointPiezometricID(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/example_piezometric_lines.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.joint = self.model.getAllJointProperties()[0]
    @classmethod
    def tearDownClass(self):
        self.model.close()
        os.remove(self.copiedModelPath)

    def testJointPiezoIDSuccess(self):
        joint = self.joint
        joint.setPiezoID(2)
        self.assertEqual(joint.getPiezoID(), 2)

    def testJointSetPiezoIDFailure(self):
        try:
            joint = self.joint
            joint.setPiezoID(500)
            self.fail("Expected exception")
        except:
            pass
    
    def testAllJointTypesPiezoIDSuccess(self):
        joint = self.joint
        joint.setPiezoID(1)
        self.assertEqual(joint.getPiezoID(), 1)
        self.assertEqual(joint.MohrCoulomb.getPiezoID(), 1)
        self.assertEqual(joint.BartonBandis.getPiezoID(), 1)
        self.assertEqual(joint.GeosyntheticHyperbolic.getPiezoID(), 1)
        self.assertEqual(joint.HyperbolicSoftening.getPiezoID(), 1)
        self.assertEqual(joint.MaterialDependent.getPiezoID(), 1)
        self.assertEqual(joint.DisplacementDependent.getPiezoID(), 1)