import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestManzariAndDafaliasStrength(unittest.TestCase):
    def setUp(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Strength.setFailureCriterion(StrengthCriteriaTypes.MANZARI_AND_DAFALIAS)
    def tearDown(self):
        self.model.close()
        os.remove(self.copiedModelPath)
    def testManzariAndDafaliasStrengthProperty(self):
        strength = self.material.Strength
        strength.ManzariAndDafaliasStrength.setCriticalStateM(836.5)
        strength.ManzariAndDafaliasStrength.setCParameter(2628.5)
        strength.ManzariAndDafaliasStrength.setLambdaC(972.5)
        strength.ManzariAndDafaliasStrength.setE0Parameter(86.7)
        strength.ManzariAndDafaliasStrength.setXiParameter(762.9)
        strength.ManzariAndDafaliasStrength.setYieldSurfaceM(1413.6)
        strength.ManzariAndDafaliasStrength.setH0Parameter(468.3)
        strength.ManzariAndDafaliasStrength.setChParameter(2350.4)
        strength.ManzariAndDafaliasStrength.setNbParameter(2598.3)
        strength.ManzariAndDafaliasStrength.setA0Parameter(2572.7)
        strength.ManzariAndDafaliasStrength.setNdParameter(2605.0)
        strength.ManzariAndDafaliasStrength.setZmax(3213.4)
        strength.ManzariAndDafaliasStrength.setCzParameter(176.8)
        strength.ManzariAndDafaliasStrength.setApplySSRShearStrengthReduction(1)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        strength = self.material.Strength
        self.assertEqual(strength.ManzariAndDafaliasStrength.getCriticalStateM(), 836.5)
        self.assertEqual(strength.ManzariAndDafaliasStrength.getCParameter(), 2628.5)
        self.assertEqual(strength.ManzariAndDafaliasStrength.getLambdaC(), 972.5)
        self.assertEqual(strength.ManzariAndDafaliasStrength.getE0Parameter(), 86.7)
        self.assertEqual(strength.ManzariAndDafaliasStrength.getXiParameter(), 762.9)
        self.assertEqual(strength.ManzariAndDafaliasStrength.getYieldSurfaceM(), 1413.6)
        self.assertEqual(strength.ManzariAndDafaliasStrength.getH0Parameter(), 468.3)
        self.assertEqual(strength.ManzariAndDafaliasStrength.getChParameter(), 2350.4)
        self.assertEqual(strength.ManzariAndDafaliasStrength.getNbParameter(), 2598.3)
        self.assertEqual(strength.ManzariAndDafaliasStrength.getA0Parameter(), 2572.7)
        self.assertEqual(strength.ManzariAndDafaliasStrength.getNdParameter(), 2605.0)
        self.assertEqual(strength.ManzariAndDafaliasStrength.getZmax(), 3213.4)
        self.assertEqual(strength.ManzariAndDafaliasStrength.getCzParameter(), 176.8)
        self.assertEqual(strength.ManzariAndDafaliasStrength.getApplySSRShearStrengthReduction(), 1)
