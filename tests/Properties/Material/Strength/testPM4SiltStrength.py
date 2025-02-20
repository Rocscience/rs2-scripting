import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestPM4SiltStrength(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SILT)
    def tearDown(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)
    def testPM4SiltStrengthProperty(self):
        strength = self.material.Strength
        strength.PM4SiltStrength.setAutoCalculateSuParameter(0)
        strength.PM4SiltStrength.setSuParameter(2628.5)
        strength.PM4SiltStrength.setSuRatioParameter(972.5)
        strength.PM4SiltStrength.setAutoCalculateEInitial(1)
        strength.PM4SiltStrength.setEInitial(762.9)
        strength.PM4SiltStrength.setAutoCalculateLambda(0)
        strength.PM4SiltStrength.setLambda(468.3)
        strength.PM4SiltStrength.setAutoCalculateFsu(0)
        strength.PM4SiltStrength.setFsu(2598.3)
        strength.PM4SiltStrength.setAutoCalculatePhiCv(0)
        strength.PM4SiltStrength.setPhiCv(2605.0)
        strength.PM4SiltStrength.setAutoCalculateNbWet(1)
        strength.PM4SiltStrength.setNbWet(176.8)
        strength.PM4SiltStrength.setAutoCalculateNbDry(1)
        strength.PM4SiltStrength.setNbDry(857.2)
        strength.PM4SiltStrength.setAutoCalculateNdParameter(0)
        strength.PM4SiltStrength.setNdParameter(1475.5)
        strength.PM4SiltStrength.setAutoCalculateADoParameter(0)
        strength.PM4SiltStrength.setADoParameter(3008.6)
        strength.PM4SiltStrength.setAutoCalculateRuMax(0)
        strength.PM4SiltStrength.setRuMax(1006.5)
        strength.PM4SiltStrength.setHp0Parameter(1374.4)
        strength.PM4SiltStrength.setAutoCalculateCEpsParameter(0)
        strength.PM4SiltStrength.setCEpsParameter(1702.5)
        strength.PM4SiltStrength.setYieldSurfaceM(857.5)
        strength.PM4SiltStrength.setAutoCalculateH0Parameter(0)
        strength.PM4SiltStrength.setH0Parameter(1772.3)
        strength.PM4SiltStrength.setAutoCalculateCKafParameter(1)
        strength.PM4SiltStrength.setCKafParameter(812.6)
        strength.PM4SiltStrength.setAutoCalculateZmax(1)
        strength.PM4SiltStrength.setZmax(2180.6)
        strength.PM4SiltStrength.setAutoCalculateCzParameter(0)
        strength.PM4SiltStrength.setCzParameter(870.1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.PM4SiltStrength.getAutoCalculateSuParameter(), 0)
        self.assertEqual(strength.PM4SiltStrength.getSuParameter(), 2628.5)
        self.assertEqual(strength.PM4SiltStrength.getSuRatioParameter(), 972.5)
        self.assertEqual(strength.PM4SiltStrength.getAutoCalculateEInitial(), 1)
        self.assertEqual(strength.PM4SiltStrength.getEInitial(), 762.9)
        self.assertEqual(strength.PM4SiltStrength.getAutoCalculateLambda(), 0)
        self.assertEqual(strength.PM4SiltStrength.getLambda(), 468.3)
        self.assertEqual(strength.PM4SiltStrength.getAutoCalculateFsu(), 0)
        self.assertEqual(strength.PM4SiltStrength.getFsu(), 2598.3)
        self.assertEqual(strength.PM4SiltStrength.getAutoCalculatePhiCv(), 0)
        self.assertEqual(strength.PM4SiltStrength.getPhiCv(), 2605.0)
        self.assertEqual(strength.PM4SiltStrength.getAutoCalculateNbWet(), 1)
        self.assertEqual(strength.PM4SiltStrength.getNbWet(), 176.8)
        self.assertEqual(strength.PM4SiltStrength.getAutoCalculateNbDry(), 1)
        self.assertEqual(strength.PM4SiltStrength.getNbDry(), 857.2)
        self.assertEqual(strength.PM4SiltStrength.getAutoCalculateNdParameter(), 0)
        self.assertEqual(strength.PM4SiltStrength.getNdParameter(), 1475.5)
        self.assertEqual(strength.PM4SiltStrength.getAutoCalculateADoParameter(), 0)
        self.assertEqual(strength.PM4SiltStrength.getADoParameter(), 3008.6)
        self.assertEqual(strength.PM4SiltStrength.getAutoCalculateRuMax(), 0)
        self.assertEqual(strength.PM4SiltStrength.getRuMax(), 1006.5)
        self.assertEqual(strength.PM4SiltStrength.getHp0Parameter(), 1374.4)
        self.assertEqual(strength.PM4SiltStrength.getAutoCalculateCEpsParameter(), 0)
        self.assertEqual(strength.PM4SiltStrength.getCEpsParameter(), 1702.5)
        self.assertEqual(strength.PM4SiltStrength.getYieldSurfaceM(), 857.5)
        self.assertEqual(strength.PM4SiltStrength.getAutoCalculateH0Parameter(), 0)
        self.assertEqual(strength.PM4SiltStrength.getH0Parameter(), 1772.3)
        self.assertEqual(strength.PM4SiltStrength.getAutoCalculateCKafParameter(), 1)
        self.assertEqual(strength.PM4SiltStrength.getCKafParameter(), 812.6)
        self.assertEqual(strength.PM4SiltStrength.getAutoCalculateZmax(), 1)
        self.assertEqual(strength.PM4SiltStrength.getZmax(), 2180.6)
        self.assertEqual(strength.PM4SiltStrength.getAutoCalculateCzParameter(), 0)
        self.assertEqual(strength.PM4SiltStrength.getCzParameter(), 870.1)
