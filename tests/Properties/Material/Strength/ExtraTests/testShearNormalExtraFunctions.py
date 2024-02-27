import unittest
import os
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestShearNormalExtraFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        cls.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, cls.copiedModelPath)
        cls.modeler = RS2Modeler()
        cls.model = cls.modeler.openFile(cls.copiedModelPath)
        cls.material = cls.model.getAllMaterialProperties()[0]

    @classmethod
    def tearDownClass(cls):
        cls.model.close()
        cls.modeler.client.closeConnection()
        os.remove(cls.copiedModelPath)

    def testSetShearNormalFunctionByName(self):
        strength = self.material.Strength
        self.model.createNewShearNormalFunction("f1")
        
        strength.setFailureCriterion(StrengthCriteriaTypes.SHEAR_NORMAL_FUNCTION)
        strength.ShearNormalFunction.setShearNormalFunctionByName("f1")

        self.assertEqual(strength.ShearNormalFunction.getShearNormalFunctionName(),"f1")

