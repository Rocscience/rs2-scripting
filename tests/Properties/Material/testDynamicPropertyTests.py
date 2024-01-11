import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestDynamicProperties(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/testProjectDynamicProperties.fez"
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

    def testInitialPiezoSuccess(self):
        self.material.InitialConditions.setInitialPiezoByName("1")
        self.assertEqual(self.material.InitialConditions.getInitialPiezoName(), "1")

        self.material.InitialConditions.setInitialPiezoByName("None")
        self.assertEqual(self.material.InitialConditions.getInitialPiezoName(), "None")

    def testInitialPiezoFail(self):
        with self.assertRaises(Exception):
            self.material.InitialConditions.setInitialPiezoByName("Not a piezo")
    
    def testInitialGridSuccess(self):
        self.material.InitialConditions.setInitialGridByName("Grid 2")
        self.assertEqual(self.material.InitialConditions.getInitialGridName(), "Grid 2")

        self.material.InitialConditions.setInitialGridByName("None")
        self.assertEqual(self.material.InitialConditions.getInitialGridName(), "None")

    def testInitialGridFail(self):
        with self.assertRaises(Exception):
            self.material.InitialConditions.setInitialGridByName("Not a grid")

    def testInitialTemperatureGridSuccess(self):
        self.material.InitialConditions.setInitialTemperatureGridByName("Grid 2")
        self.assertEqual(self.material.InitialConditions.getInitialTemperatureGridName(), "Grid 2")

        self.material.InitialConditions.setInitialTemperatureGridByName("None")
        self.assertEqual(self.material.InitialConditions.getInitialTemperatureGridName(), "None")

    def testInitialTemperatureGridFail(self):
        with self.assertRaises(Exception):
            self.material.InitialConditions.setInitialTemperatureGridByName("Not a grid")
    
    def testAnisotropicSurfaceSuccess(self):
        self.material.Strength.setFailureCriterion(StrengthCriteriaTypes.SNOWDEN_MODIFIED_ANISOTROPIC_LINEAR)
        self.material.Strength.SnowdenModAnisotropicLinear.setAnisotropyDefinition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_SURFACE)
        self.material.Strength.SnowdenModAnisotropicLinear.setAnisotropicSurfaceByName("Anisotropic Surface 1")
        self.assertEqual(self.material.Strength.SnowdenModAnisotropicLinear.getAnisotropicSurfaceName(), "Anisotropic Surface 1")

    def testAnisotropicSurfaceFail(self):
        self.material.Strength.setFailureCriterion(StrengthCriteriaTypes.SNOWDEN_MODIFIED_ANISOTROPIC_LINEAR)
        self.material.Strength.SnowdenModAnisotropicLinear.setAnisotropyDefinition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_SURFACE)
        with self.assertRaises(Exception):
            self.material.Strength.SnowdenModAnisotropicLinear.setAnisotropicSurfaceByName("Not a surface")

    def testSetBaseMaterialSuccess(self):
        self.material.Strength.GeneralizedAnisotropic.setGeneralizedAnisotropicFunction([(-89, self.materialNames[0]),(90,  self.materialNames[1])])
        self.material.Strength.GeneralizedAnisotropic.setBaseMaterialByName(self.materialNames[1])
        self.assertEqual(self.material.Strength.GeneralizedAnisotropic.getBaseMaterialName(), self.materialNames[1])
    
    def testSetBaseMaterialFail(self):
        self.material.Strength.GeneralizedAnisotropic.setGeneralizedAnisotropicFunction([(-89, self.materialNames[0]),(90,  self.materialNames[1])])
        self.material.Strength.GeneralizedAnisotropic.setBaseMaterialByName(self.materialNames[1])
    
        #not a material
        with self.assertRaises(Exception):
            self.material.Strength.GeneralizedAnisotropic.setBaseMaterialByName("Not a material")
        #material not in generalized anisotropic function
        with self.assertRaises(Exception):
            self.material.Strength.GeneralizedAnisotropic.setBaseMaterialByName(self.materialNames[2])
    
        self.assertEqual(self.material.Strength.GeneralizedAnisotropic.getBaseMaterialName(), self.materialNames[1])

    def testPiezoToUseSuccess(self):
        self.material.Hydraulic.StaticGroundwater.setPiezoToUse("1")
        self.assertEqual(self.material.Hydraulic.StaticGroundwater.getPiezoToUse(), "1")
    
        self.material.Hydraulic.StaticGroundwater.setPiezoToUse("None")
        self.assertEqual(self.material.Hydraulic.StaticGroundwater.getPiezoToUse(), "None")

    def testPiezoToUseFail(self):
        with self.assertRaises(Exception):
            self.material.Hydraulic.StaticGroundwater.setPiezoToUse("Not a piezo")
    
    def testGridToUseSuccess(self):
        self.material.Hydraulic.StaticGroundwater.setGridToUse("Grid 2")
        self.assertEqual(self.material.Hydraulic.StaticGroundwater.getGridToUse(), "Grid 2")
    
        self.material.Hydraulic.StaticGroundwater.setGridToUse("None")
        self.assertEqual(self.material.Hydraulic.StaticGroundwater.getGridToUse(), "None")

    def testGridToUseFail(self):
        with self.assertRaises(Exception):
            self.material.Hydraulic.StaticGroundwater.setGridToUse("Not a grid")
    
    def testK1SurfaceToUseByName(self):
        self.material.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_SURFACE)
        self.material.Hydraulic.FEAGroundwater.setK1SurfaceToUseByName("Anisotropic Surface 1")
        self.assertEqual(self.material.Hydraulic.FEAGroundwater.getK1SurfaceToUse(), "Anisotropic Surface 1")

    def testK1SurfaceToUseFail(self):
        self.material.Hydraulic.FEAGroundwater.setK1SurfaceToUseByName("Anisotropic Surface 1")

        self.material.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_SURFACE)
        with self.assertRaises(Exception):
            self.material.Hydraulic.FEAGroundwater.setK1SurfaceToUseByName("Not a surface")
    
        self.assertEqual(self.material.Hydraulic.FEAGroundwater.getK1SurfaceToUse(), "Anisotropic Surface 1")

    def testUserDefinedPermeabilityAndWaterContentFunction(self):
        self.material.Hydraulic.FEAGroundwater.UserDefined.setUserDefinedPermeabilityAndWaterContentFunction("User Defined 2")
        self.assertEqual(self.material.Hydraulic.FEAGroundwater.UserDefined.getUserDefinedPermeabilityAndWaterContentFunction(), "User Defined 2")
        
        self.material.Hydraulic.FEAGroundwater.UserDefined.setUserDefinedPermeabilityAndWaterContentFunction("User Defined 1")
        self.assertEqual(self.material.Hydraulic.FEAGroundwater.UserDefined.getUserDefinedPermeabilityAndWaterContentFunction(), "User Defined 1")

    def testUserDefinedPermeabilityAndWaterContentFunctionFail(self):
        self.material.Hydraulic.FEAGroundwater.UserDefined.setUserDefinedPermeabilityAndWaterContentFunction("User Defined 1")

        with self.assertRaises(Exception):
            self.material.Hydraulic.FEAGroundwater.UserDefined.setUserDefinedPermeabilityAndWaterContentFunction("Not a function")
        
        self.assertEqual(self.material.Hydraulic.FEAGroundwater.UserDefined.getUserDefinedPermeabilityAndWaterContentFunction(), "User Defined 1")
    
    def testStaticTemperatureGridToUseByName(self):
        self.material.Thermal.setStaticTemperatureGridToUseByName("Grid 2")
        self.assertEqual(self.material.Thermal.getStaticTemperatureGridToUse(), "Grid 2")

        self.material.Thermal.setStaticTemperatureGridToUseByName("None")
        self.assertEqual(self.material.Thermal.getStaticTemperatureGridToUse(), "None")

    def testStaticTemperatureGridToUseFail(self):
        with self.assertRaises(Exception):
            self.material.Thermal.setStaticTemperatureGridToUseByName("Not a grid")