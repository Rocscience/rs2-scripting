import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestSetExtraStrengthFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)

        allMaterials = self.model.getAllMaterialProperties()

        self.material = allMaterials[0]

        self.materialNames = []
        for mat in allMaterials:
            self.materialNames.append(mat.getMaterialName())

    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)

    def testGeneralizedAnisotropicFunctionSuccess(self):
        input = [(-89, self.materialNames[0]),(0, self.materialNames[1]),(90, self.materialNames[2])]
        self.material.Strength.GeneralizedAnisotropic.setGeneralizedAnisotropicFunction(input)
        self.assertEqual(self.material.Strength.GeneralizedAnisotropic.getGeneralizedAnisotropicFunction(), input)

    