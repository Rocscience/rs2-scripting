import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestIsotropic(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testIsotropicProperty(self):
        stiffness = self.material.Stiffness
        stiffness.Isotropic.setUseUnloadingCondition(0)
        stiffness.Isotropic.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRESS)
        stiffness.Isotropic.setElasticParameters(ElasticParameters.CONSTANT_POISSON_RATIO)
        stiffness.Isotropic.setShearModulus(2628.5)
        stiffness.Isotropic.setPoissonsRatio(972.5)
        stiffness.Isotropic.setYoungsModulus(86.7)
        stiffness.Isotropic.setUseResidualYoungsModulus(1)
        stiffness.Isotropic.setResidualYoungsModulus(1413.6)
        stiffness.Isotropic.setUnloadingPoissonsRatio(468.3)
        stiffness.Isotropic.setUnloadingYoungsModulus(2350.4)
        stiffness.Isotropic.setUseUnloadingResidualYoungsModulus(1)
        stiffness.Isotropic.setUnloadingResidualYoungsModulus(2572.7)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        stiffness = self.material.Stiffness
        self.assertEqual(stiffness.Isotropic.getUseUnloadingCondition(), 0)
        self.assertEqual(stiffness.Isotropic.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRESS)
        self.assertEqual(stiffness.Isotropic.getElasticParameters(), ElasticParameters.CONSTANT_POISSON_RATIO)
        self.assertEqual(stiffness.Isotropic.getShearModulus(), 2628.5)
        self.assertEqual(stiffness.Isotropic.getPoissonsRatio(), 972.5)
        self.assertEqual(stiffness.Isotropic.getYoungsModulus(), 86.7)
        self.assertEqual(stiffness.Isotropic.getUseResidualYoungsModulus(), 1)
        self.assertEqual(stiffness.Isotropic.getResidualYoungsModulus(), 1413.6)
        self.assertEqual(stiffness.Isotropic.getUnloadingPoissonsRatio(), 468.3)
        self.assertEqual(stiffness.Isotropic.getUnloadingYoungsModulus(), 2350.4)
        self.assertEqual(stiffness.Isotropic.getUseUnloadingResidualYoungsModulus(), 1)
        self.assertEqual(stiffness.Isotropic.getUnloadingResidualYoungsModulus(), 2572.7)