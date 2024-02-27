import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestStaticGroundwater(unittest.TestCase):
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
    def testStaticGroundwaterProperty(self):
        hydraulic = self.material.Hydraulic
        hydraulic.StaticGroundwater.setStaticWaterMode(StaticWaterModes.SWM_PWP)
        hydraulic.StaticGroundwater.setStaticPoreWaterPressure(836.5)
        hydraulic.StaticGroundwater.setRuValue(2628.5)
        hydraulic.StaticGroundwater.setHuType(HuTypes.HT_AUTO)
        hydraulic.StaticGroundwater.setHuValue(972.5)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        hydraulic = self.material.Hydraulic
        self.assertEqual(hydraulic.StaticGroundwater.getStaticWaterMode(), StaticWaterModes.SWM_PWP)
        self.assertEqual(hydraulic.StaticGroundwater.getStaticPoreWaterPressure(), 836.5)
        self.assertEqual(hydraulic.StaticGroundwater.getRuValue(), 2628.5)
        self.assertEqual(hydraulic.StaticGroundwater.getHuType(), HuTypes.HT_AUTO)
        self.assertEqual(hydraulic.StaticGroundwater.getHuValue(), 972.5)
