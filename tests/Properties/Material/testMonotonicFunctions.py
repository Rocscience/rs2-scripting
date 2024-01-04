import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestMonotonicFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Strength.setUnsaturatedBehavior(UnsaturatedParameterType.UNSATURATED_SINGLE_EFFECTIVE_STRESS)
        self.material.Strength.setSingleEffectiveStressMethod(UnsaturatedSingleEffectiveStressMethod.UNSATURATED_TABULAR_VALUE)

    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)

    def testUnsaturatedZoneTable(self):
        self.material.Strength.setTabularValues(UnsaturatedTabularValueMethod.UNSATURATED_RESPECT_DEGREE_SATURATION)
        newTableCol1 = [-1.1,0,1,2]
        newTableCol2 = [-1.2,0.2,1.3,2.4]
        self.material.Strength.setUnsaturatedZoneTable(newTableCol1, newTableCol2)
        self.material.Strength.getUnsaturatedZoneTable()
    def testThermalConductivityTable(self):
        pass
    def testVolumetricHeatCapacityTable(self):
        pass
    def testTemperatureVsUnfrozenWaterContentValues(self):
        pass
    def test