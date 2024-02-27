import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

parentDirectoryHelper.addParentDirectoryToPath()

class TestSnowdenAnisotropicFunction(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.mat = self.model.getAllMaterialProperties()[0]

        self.BeddingStrengthFunction = self.mat.Strength.SnowdenModAnisotropicLinear.getBeddingStrengthFunction()
        self.RocMassStrengthFunction = self.mat.Strength.SnowdenModAnisotropicLinear.getRockMassStrengthFunction()
    @classmethod
    def tearDownClass(self):
        self.model.close()
        os.remove(self.copiedModelPath)

    def testGetSetFunctionType(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_COHESION_PHI)
        self.assertEqual(self.BeddingStrengthFunction.getFunctionType(), SnowdenAnisotropicFunctionType.FUNCTION_TYPE_COHESION_PHI)
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_SHEAR_NORMAL)
        self.assertEqual(self.BeddingStrengthFunction.getFunctionType(), SnowdenAnisotropicFunctionType.FUNCTION_TYPE_SHEAR_NORMAL)
    
    def testStrengthProperties(self):
        self.BeddingStrengthFunction.setDilationRatio(0.5)
        self.BeddingStrengthFunction.setPeakTensileStrength(1.0)
        self.BeddingStrengthFunction.setResidualTensileStrength(0.5)

        self.assertEqual(self.BeddingStrengthFunction.getDilationRatio(), 0.5)
        self.assertEqual(self.BeddingStrengthFunction.getPeakTensileStrength(), 1.0)
        self.assertEqual(self.BeddingStrengthFunction.getResidualTensileStrength(), 0.5)

    def testStrengthPropertiesFailure(self):
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setDilationRatio(-0.5)
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setDilationRatio(2)
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setPeakTensileStrength(-1.0)
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setResidualTensileStrength(-0.5)


    def testSetShearNormalFunction(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_SHEAR_NORMAL)

        normalStress = [0, 1.1, 2.2]
        shearStress = [0, 2.2, 3.3]
        self.BeddingStrengthFunction.setShearNormalFunction(normalStress, shearStress)
        self.assertEqual(self.BeddingStrengthFunction.getNormalStress(), normalStress)
        self.assertEqual(self.BeddingStrengthFunction.getShearStress(), shearStress)
    
    def testSetShearNormalFunctionFailureLessthan2Points(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_SHEAR_NORMAL)

        normalStress = [1]
        shearStress = [0.0, 1.1, 2.2]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setShearNormalFunction(normalStress, shearStress)

        normalStress = [0, 1.1, 2.2]
        shearStress = [1]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setShearNormalFunction(normalStress, shearStress)

    def testSetShearNormalFunctionFailureNegativeShear(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_SHEAR_NORMAL)

        normalStress = [0, 1.1, 2.2]
        shearStress = [0, -1.1, 2.2]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setShearNormalFunction(normalStress, shearStress)

    def testSetShearNormalFunctionWithResidual(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_SHEAR_NORMAL)

        normalStress = [0, 1.1, 2.2]
        shearStress = [0, 2.2, 3.3]
        residualShearStress = [0, 1.1, 2.2]
        self.BeddingStrengthFunction.setShearNormalFunctionWithResidual(normalStress, shearStress, residualShearStress)
        self.assertEqual(self.BeddingStrengthFunction.getNormalStress(), normalStress)
        self.assertEqual(self.BeddingStrengthFunction.getShearStress(), shearStress)
        self.assertEqual(self.BeddingStrengthFunction.getResidualShearStress(), residualShearStress)

    def testSetShearNormalFunctionWithResidualFailureLessthan2Points(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_SHEAR_NORMAL)

        normalStress = [1]
        shearStress = [0.0, 1.1, 2.2]
        residualShearStress = [0, 1.1, 2.2]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setShearNormalFunctionWithResidual(normalStress, shearStress, residualShearStress)

        normalStress = [0, 1.1, 2.2]
        shearStress = [1]
        residualShearStress = [0, 1.1, 2.2]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setShearNormalFunctionWithResidual(normalStress, shearStress, residualShearStress)

        normalStress = [0, 1.1, 2.2]
        shearStress = [0, 1.1, 2.2]
        residualShearStress = [1]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setShearNormalFunctionWithResidual(normalStress, shearStress, residualShearStress)

    def testSetShearNormalFunctionWithResidualFailureNegativeShear(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_SHEAR_NORMAL)

        normalStress = [0, 1.1, 2.2]
        shearStress = [0, -1.1, 2.2]
        residualShearStress = [0, 1.1, 2.2]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setShearNormalFunctionWithResidual(normalStress, shearStress, residualShearStress)

        normalStress = [0, 1.1, 2.2]
        shearStress = [0, 1.1, 2.2]
        residualShearStress = [0, -1.1, 2.2]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setShearNormalFunctionWithResidual(normalStress, shearStress, residualShearStress)

    def testSetShearNormalFunctionWithResidualFailureResidualGreaterThanShear(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_SHEAR_NORMAL)

        normalStress = [0, 1.1, 2.2]
        shearStress = [0, 1.1, 2.2]
        residualShearStress = [0, 1.1, 3.2]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setShearNormalFunctionWithResidual(normalStress, shearStress, residualShearStress)
        
    def testSetCohesionFrictionFunction(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_COHESION_PHI)

        normalStress = [0, 1.1, 2.2]
        cohesion = [0, 2.2, 3.3]
        frictionAngle = [0, 1.1, 2.2]
        self.BeddingStrengthFunction.setCohesionFrictionFunction(normalStress, cohesion, frictionAngle)
        self.assertEqual(self.BeddingStrengthFunction.getNormalStress(), normalStress)
        self.assertEqual(self.BeddingStrengthFunction.getCohesion(), cohesion)
        self.assertEqual(self.BeddingStrengthFunction.getFrictionAngle(), frictionAngle)

    def testSetCohesionFrictionFunctionFailureLessthan2Points(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_COHESION_PHI)

        normalStress = [1]
        cohesion = [0, 2.2, 3.3]
        frictionAngle = [0, 1.1, 2.2]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setCohesionFrictionFunction(normalStress, cohesion, frictionAngle)

        normalStress = [0, 1.1, 2.2]
        cohesion = [1]
        frictionAngle = [0, 1.1, 2.2]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setCohesionFrictionFunction(normalStress, cohesion, frictionAngle)

        normalStress = [0, 1.1, 2.2]
        cohesion = [0, 2.2, 3.3]
        frictionAngle = [1]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setCohesionFrictionFunction(normalStress, cohesion, frictionAngle)

    def testSetCohesionFrictionFunctionFailureNegativeCohesion(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_COHESION_PHI)

        normalStress = [0, 1.1, 2.2]
        cohesion = [0, -2.2, 3.3]
        frictionAngle = [0, 1.1, 2.2]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setCohesionFrictionFunction(normalStress, cohesion, frictionAngle)

    def testSetCohesionFrictionFunctionFailureNegativeFrictionAngle(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_COHESION_PHI)

        normalStress = [0, 1.1, 2.2]
        cohesion = [0, 2.2, 3.3]
        frictionAngle = [0, -1.1, 2.2]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setCohesionFrictionFunction(normalStress, cohesion, frictionAngle)

    #friction angle cannot be greater than 90
    def testSetCohesionFrictionFunctionFailureFrictionAngleGreaterThan90(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_COHESION_PHI)

        normalStress = [0, 1.1, 2.2]
        cohesion = [0, 2.2, 3.3]
        frictionAngle = [0, 1.1, 91]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setCohesionFrictionFunction(normalStress, cohesion, frictionAngle)
    
    def testSetCohesionFrictionFunctionWithResidual(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_COHESION_PHI)

        normalStress = [0, 1.1, 2.2]
        cohesion = [0, 2.2, 3.3]
        frictionAngle = [0, 1.1, 2.2]
        residualCohesion = [0, 1.1, 2.2]
        residualFrictionAngle = [0, 1.1, 2.2]
        self.BeddingStrengthFunction.setCohesionFrictionFunctionWithResidual(normalStress, cohesion, frictionAngle, residualCohesion, residualFrictionAngle)
        self.assertEqual(self.BeddingStrengthFunction.getNormalStress(), normalStress)
        self.assertEqual(self.BeddingStrengthFunction.getCohesion(), cohesion)
        self.assertEqual(self.BeddingStrengthFunction.getFrictionAngle(), frictionAngle)
        self.assertEqual(self.BeddingStrengthFunction.getResidualCohesion(), residualCohesion)
        self.assertEqual(self.BeddingStrengthFunction.getResidualFrictionAngle(), residualFrictionAngle)

    def testSetCohesionFrictionFunctionWithResidualFailureLessthan2Points(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_COHESION_PHI)

        normalStress = [1]
        cohesion = [0, 2.2, 3.3]
        frictionAngle = [0, 1.1, 2.2]
        residualCohesion = [0, 1.1, 2.2]
        residualFrictionAngle = [0, 1.1, 2.2]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setCohesionFrictionFunctionWithResidual(normalStress, cohesion, frictionAngle, residualCohesion, residualFrictionAngle)

        normalStress = [0, 1.1, 2.2]
        cohesion = [1]
        frictionAngle = [0, 1.1, 2.2]
        residualCohesion = [0, 1.1, 2.2]
        residualFrictionAngle = [0, 1.1, 2.2]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setCohesionFrictionFunctionWithResidual(normalStress, cohesion, frictionAngle, residualCohesion, residualFrictionAngle)

        normalStress = [0, 1.1, 2.2]
        cohesion = [0, 2.2, 3.3]
        frictionAngle = [1]
        residualCohesion = [0, 1.1, 2.2]
        residualFrictionAngle = [0, 1.1, 2.2]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setCohesionFrictionFunctionWithResidual(normalStress, cohesion, frictionAngle, residualCohesion, residualFrictionAngle)

        normalStress = [0, 1.1, 2.2]
        cohesion = [0, 2.2, 3.3]
        frictionAngle = [0, 1.1, 2.2]
        residualCohesion = [1]
        residualFrictionAngle = [0, 1.1, 2.2]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setCohesionFrictionFunctionWithResidual(normalStress, cohesion, frictionAngle, residualCohesion, residualFrictionAngle)

        normalStress = [0, 1.1, 2.2]
        cohesion = [0, 2.2, 3.3]
        frictionAngle = [0, 1.1, 2.2]
        residualCohesion = [0, 1.1, 2.2]
        residualFrictionAngle = [1]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setCohesionFrictionFunctionWithResidual(normalStress, cohesion, frictionAngle, residualCohesion, residualFrictionAngle)
        
    def testSetCohesionFrictionFunctionWithResidualFailureNegativeCohesion(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_COHESION_PHI)

        normalStress = [0, 1.1, 2.2]
        cohesion = [0, -2.2, 3.3]
        frictionAngle = [0, 1.1, 2.2]
        residualCohesion = [0, 1.1, 2.2]
        residualFrictionAngle = [0, 1.1, 2.2]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setCohesionFrictionFunctionWithResidual(normalStress, cohesion, frictionAngle, residualCohesion, residualFrictionAngle)
    
    def testSetCohesionFrictionFunctionWithResidualFailureNegativeFrictionAngle(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_COHESION_PHI)

        normalStress = [0, 1.1, 2.2]
        cohesion = [0, 2.2, 3.3]
        frictionAngle = [0, -1.1, 2.2]
        residualCohesion = [0, 1.1, 2.2]
        residualFrictionAngle = [0, 1.1, 2.2]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setCohesionFrictionFunctionWithResidual(normalStress, cohesion, frictionAngle, residualCohesion, residualFrictionAngle)
    
    def testSetCohesionFrictionFunctionWithResidualFailureResidualCohesionGreaterThanCohesion(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_COHESION_PHI)

        normalStress = [0, 1.1, 2.2]
        cohesion = [0, 2.2, 3.3]
        frictionAngle = [0, 1.1, 2.2]
        residualCohesion = [0, 1.1, 4.3]
        residualFrictionAngle = [0, 1.1, 2.2]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setCohesionFrictionFunctionWithResidual(normalStress, cohesion, frictionAngle, residualCohesion, residualFrictionAngle)
    
    def testSetCohesionFrictionFunctionWithResidualFailureResidualFrictionAngleGreaterThanFrictionAngle(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_COHESION_PHI)

        normalStress = [0, 1.1, 2.2]
        cohesion = [0, 2.2, 3.3]
        frictionAngle = [0, 1.1, 2.2]
        residualCohesion = [0, 1.1, 2.2]
        residualFrictionAngle = [0, 1.1, 4.2]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setCohesionFrictionFunctionWithResidual(normalStress, cohesion, frictionAngle, residualCohesion, residualFrictionAngle)

    #check that friction angle cannot be greater than 90
    def testSetCohesionFrictionFunctionWithResidualFailureResidualFrictionAngleGreaterThan90(self):
        self.BeddingStrengthFunction.setFunctionType(SnowdenAnisotropicFunctionType.FUNCTION_TYPE_COHESION_PHI)
        
        normalStress = [0, 1.1, 2.2]
        cohesion = [0, 2.2, 3.3]
        frictionAngle = [0, 1.1, 2.2]
        residualCohesion = [0, 1.1, 2.2]
        residualFrictionAngle = [0, 1.1, 91]
        with self.assertRaises(Exception):
            self.BeddingStrengthFunction.setCohesionFrictionFunctionWithResidual(normalStress, cohesion, frictionAngle, residualCohesion, residualFrictionAngle)

    def testRockMassFunction(self):
        self.RocMassStrengthFunction.setDilationRatio(0.55)
        self.RocMassStrengthFunction.setPeakTensileStrength(1.5)
        self.RocMassStrengthFunction.setResidualTensileStrength(0.55)

        self.assertEqual(self.RocMassStrengthFunction.getDilationRatio(), 0.55)
        self.assertEqual(self.RocMassStrengthFunction.getPeakTensileStrength(), 1.5)
        self.assertEqual(self.RocMassStrengthFunction.getResidualTensileStrength(), 0.55)