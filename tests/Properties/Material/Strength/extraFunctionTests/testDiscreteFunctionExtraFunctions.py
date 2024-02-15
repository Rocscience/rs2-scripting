import unittest
import os
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestDiscreteFunctionExtraFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        cls.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, cls.copiedModelPath)
        cls.modeler = RS2Modeler()
        cls.model = cls.modeler.openFile(cls.copiedModelPath)
        cls.material = cls.model.getAllMaterialProperties()[0]
        cls.model.createNewDiscreteFunction("df1")
        cls.model.createNewDiscreteFunction("df2")

    @classmethod
    def tearDownClass(cls):
        cls.model.close()
        cls.modeler.client.closeConnection()
        os.remove(cls.copiedModelPath)

    def testSetDiscreteFunction(self):
        strength = self.material.Strength

        strength.setFailureCriterion(StrengthCriteriaTypes.DISCRETE_FUNCTION)
        strength.DiscreteFunction.setSelectedDiscreteFunctionByName("df1")
        self.assertEqual(strength.DiscreteFunction.getSelectedDiscreteFunctionName(),"df1")

        strength.DiscreteFunction.setSelectedDiscreteFunctionByName("df2")
        self.assertEqual(strength.DiscreteFunction.getSelectedDiscreteFunctionName(),"df2")

    def testSetDiscreteFunctionFailure(self):
        strength = self.material.Strength

        with self.assertRaises(Exception):
            strength.DiscreteFunction.setSelectedDiscreteFunctionByName("nonExistant")