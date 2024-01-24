import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestMohrCoulombMaterial(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.mat = self.model.getAllMaterialProperties()[0]
        self.mat.Strength.setFailureCriterion(StrengthCriteriaTypes.JOINTED_MOHR_COULOMB)
        self.matJointOptions = self.mat.Strength.JointedMohrCoulomb.getJointOptions()
        self.jointmaterial = self.matJointOptions.getJoint(0)
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testMohrCoulombMaterialProperty(self):
        jointmaterial = self.jointmaterial
        jointmaterial.MohrCoulombMaterial.setDilationAngle(836.5)
        jointmaterial.MohrCoulombMaterial.setTensileStrength(2628.5)
        jointmaterial.MohrCoulombMaterial.setPeakFrictionAngle(972.5)
        jointmaterial.MohrCoulombMaterial.setPeakCohesion(86.7)
        jointmaterial.MohrCoulombMaterial.setResidualStrength(1)
        jointmaterial.MohrCoulombMaterial.setResTensileStrength(1413.6)
        jointmaterial.MohrCoulombMaterial.setResCohesion(468.3)
        jointmaterial.MohrCoulombMaterial.setResFrictionAngle(2350.4)
        jointmaterial.MohrCoulombMaterial.setApplyStageFactors(1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.mat = self.model.getAllMaterialProperties()[0]
        self.mat.Strength.setFailureCriterion(StrengthCriteriaTypes.JOINTED_MOHR_COULOMB)
        self.matJointOptions = self.mat.Strength.JointedMohrCoulomb.getJointOptions()
        self.jointmaterial = self.matJointOptions.getJoint(0)
        jointmaterial = self.jointmaterial
        self.assertEqual(jointmaterial.MohrCoulombMaterial.getDilationAngle(), 836.5)
        self.assertEqual(jointmaterial.MohrCoulombMaterial.getTensileStrength(), 2628.5)
        self.assertEqual(jointmaterial.MohrCoulombMaterial.getPeakFrictionAngle(), 972.5)
        self.assertEqual(jointmaterial.MohrCoulombMaterial.getPeakCohesion(), 86.7)
        self.assertEqual(jointmaterial.MohrCoulombMaterial.getResidualStrength(), 1)
        self.assertEqual(jointmaterial.MohrCoulombMaterial.getResTensileStrength(), 1413.6)
        self.assertEqual(jointmaterial.MohrCoulombMaterial.getResCohesion(), 468.3)
        self.assertEqual(jointmaterial.MohrCoulombMaterial.getResFrictionAngle(), 2350.4)
        self.assertEqual(jointmaterial.MohrCoulombMaterial.getApplyStageFactors(), 1)
