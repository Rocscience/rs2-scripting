import unittest
import os
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestStrengthExtraStageFactorFunctions(unittest.TestCase):
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
    
    def testResetYieldStageFactor(self):
        material = self.material
        material.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
        material.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

        stageFactor = material.Strength.stageFactorInterface.getDefinedStageFactors()[1]
        stageFactor.setResetYield(False)
        self.assertEqual(stageFactor.getResetYield(), False)
        stageFactor.setResetYield(True)
        self.assertEqual(stageFactor.getResetYield(), True)