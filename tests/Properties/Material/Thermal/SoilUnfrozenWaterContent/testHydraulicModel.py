import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestHydraulicModel(unittest.TestCase):
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
    def testHydraulicModelProperty(self):
        soilunfrozenwatercontent = self.material.Thermal.SoilUnfrozenWaterContent
        soilunfrozenwatercontent.HydraulicModel.setFrozenTemperature(836.5)
        soilunfrozenwatercontent.HydraulicModel.setSelectHydraulicModel(GroundWaterModes.FREDLUND_AND_XING)
        soilunfrozenwatercontent.HydraulicModel.setWCSat(0.3)
        soilunfrozenwatercontent.HydraulicModel.setWCRes(0.4)
        self.model.save()
        self.model.close()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        soilunfrozenwatercontent = self.material.Thermal.SoilUnfrozenWaterContent
        self.assertEqual(soilunfrozenwatercontent.HydraulicModel.getFrozenTemperature(), 836.5)
        self.assertEqual(soilunfrozenwatercontent.HydraulicModel.getSelectHydraulicModel(), GroundWaterModes.FREDLUND_AND_XING)
        self.assertEqual(soilunfrozenwatercontent.HydraulicModel.getWCSat(), 0.3)
        self.assertEqual(soilunfrozenwatercontent.HydraulicModel.getWCRes(), 0.4)
