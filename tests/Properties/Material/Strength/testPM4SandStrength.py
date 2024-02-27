import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestPM4SandStrength(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SAND)
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testPM4SandStrengthProperty(self):
        strength = self.material.Strength
        strength.PM4SandStrength.setDr(836.5)
        strength.PM4SandStrength.setQParameter(2628.5)
        strength.PM4SandStrength.setRParameter(972.5)
        strength.PM4SandStrength.setEMax(86.7)
        strength.PM4SandStrength.setEMin(762.9)
        strength.PM4SandStrength.setPhiCv(1413.6)
        strength.PM4SandStrength.setNbParameter(468.3)
        strength.PM4SandStrength.setNdParameter(2350.4)
        strength.PM4SandStrength.setAutoCalculateADoParameter(1)
        strength.PM4SandStrength.setADoParameter(2572.7)
        strength.PM4SandStrength.setHp0Parameter(2605.0)
        strength.PM4SandStrength.setAutoCalculateCDRParameter(1)
        strength.PM4SandStrength.setCDRParameter(176.8)
        strength.PM4SandStrength.setAutoCalculateCEpsParameter(1)
        strength.PM4SandStrength.setCEpsParameter(857.2)
        strength.PM4SandStrength.setYieldSurfaceM(3215.6)
        strength.PM4SandStrength.setAutoCalculateH0Parameter(1)
        strength.PM4SandStrength.setH0Parameter(2227.9)
        strength.PM4SandStrength.setAutoCalculateCKafParameter(1)
        strength.PM4SandStrength.setCKafParameter(2917.7)
        strength.PM4SandStrength.setAutoCalculateZmax(1)
        strength.PM4SandStrength.setZmax(1374.4)
        strength.PM4SandStrength.setAutoCalculateCzParameter(0)
        strength.PM4SandStrength.setCzParameter(1702.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.PM4SandStrength.getDr(), 836.5)
        self.assertEqual(strength.PM4SandStrength.getQParameter(), 2628.5)
        self.assertEqual(strength.PM4SandStrength.getRParameter(), 972.5)
        self.assertEqual(strength.PM4SandStrength.getEMax(), 86.7)
        self.assertEqual(strength.PM4SandStrength.getEMin(), 762.9)
        self.assertEqual(strength.PM4SandStrength.getPhiCv(), 1413.6)
        self.assertEqual(strength.PM4SandStrength.getNbParameter(), 468.3)
        self.assertEqual(strength.PM4SandStrength.getNdParameter(), 2350.4)
        self.assertEqual(strength.PM4SandStrength.getAutoCalculateADoParameter(), 1)
        self.assertEqual(strength.PM4SandStrength.getADoParameter(), 2572.7)
        self.assertEqual(strength.PM4SandStrength.getHp0Parameter(), 2605.0)
        self.assertEqual(strength.PM4SandStrength.getAutoCalculateCDRParameter(), 1)
        self.assertEqual(strength.PM4SandStrength.getCDRParameter(), 176.8)
        self.assertEqual(strength.PM4SandStrength.getAutoCalculateCEpsParameter(), 1)
        self.assertEqual(strength.PM4SandStrength.getCEpsParameter(), 857.2)
        self.assertEqual(strength.PM4SandStrength.getYieldSurfaceM(), 3215.6)
        self.assertEqual(strength.PM4SandStrength.getAutoCalculateH0Parameter(), 1)
        self.assertEqual(strength.PM4SandStrength.getH0Parameter(), 2227.9)
        self.assertEqual(strength.PM4SandStrength.getAutoCalculateCKafParameter(), 1)
        self.assertEqual(strength.PM4SandStrength.getCKafParameter(), 2917.7)
        self.assertEqual(strength.PM4SandStrength.getAutoCalculateZmax(), 1)
        self.assertEqual(strength.PM4SandStrength.getZmax(), 1374.4)
        self.assertEqual(strength.PM4SandStrength.getAutoCalculateCzParameter(), 0)
        self.assertEqual(strength.PM4SandStrength.getCzParameter(), 1702.5)
