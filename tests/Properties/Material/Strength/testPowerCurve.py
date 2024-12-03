import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestPowerCurve(unittest.TestCase):
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
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)
    def testPowerCurveProperty(self):
        strength = self.material.Strength
        strength.PowerCurve.setMaterialType(MaterialType.PLASTIC)
        strength.PowerCurve.setAParameter(836.5)
        strength.PowerCurve.setBParameter(2628.5)
        strength.PowerCurve.setCParameter(972.5)
        strength.PowerCurve.setDParameter(86.7)
        strength.PowerCurve.setWaviness(762.9)
        strength.PowerCurve.setResidualAParameter(1413.6)
        strength.PowerCurve.setResidualBParameter(468.3)
        strength.PowerCurve.setResidualCParameter(2350.4)
        strength.PowerCurve.setResidualDParameter(2598.3)
        strength.PowerCurve.setResidualWaviness(2572.7)
        strength.PowerCurve.setDilationRatio(2605.0)
        strength.PowerCurve.setApplySSRShearStrengthReduction(1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.PowerCurve.getMaterialType(), MaterialType.PLASTIC)
        self.assertEqual(strength.PowerCurve.getAParameter(), 836.5)
        self.assertEqual(strength.PowerCurve.getBParameter(), 2628.5)
        self.assertEqual(strength.PowerCurve.getCParameter(), 972.5)
        self.assertEqual(strength.PowerCurve.getDParameter(), 86.7)
        self.assertEqual(strength.PowerCurve.getWaviness(), 762.9)
        self.assertEqual(strength.PowerCurve.getResidualAParameter(), 1413.6)
        self.assertEqual(strength.PowerCurve.getResidualBParameter(), 468.3)
        self.assertEqual(strength.PowerCurve.getResidualCParameter(), 2350.4)
        self.assertEqual(strength.PowerCurve.getResidualDParameter(), 2598.3)
        self.assertEqual(strength.PowerCurve.getResidualWaviness(), 2572.7)
        self.assertEqual(strength.PowerCurve.getDilationRatio(), 2605.0)
        self.assertEqual(strength.PowerCurve.getApplySSRShearStrengthReduction(), 1)
