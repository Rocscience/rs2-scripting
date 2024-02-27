import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestStiffnessTables(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Stiffness.setElasticType(MaterialElasticityTypes.CUSTOM_STIFFNESS)

    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)

    def testCustomStiffnessLoadingTableSuccess(self):
        self.material.Stiffness.Custom.setCustomMode(CustomMode.CUSTOM_P)
        self.assertEqual(self.material.Stiffness.Custom.getCustomMode(), CustomMode.CUSTOM_P)

        newTable = [(1,2,0.3),(4,5,0.4)]
        self.material.Stiffness.Custom.setUseConstantPoissonsRatio(False)
        self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_P, newTable)
        self.assertEqual(self.material.Stiffness.Custom.getCustomStiffnessLoadingTable(), newTable)
    
        #if constant poisson ratio is used, then the poisson ratio column should be zeroed out.
        newTableZeroPoisson = [(1,2,0),(4,5,0)]
        self.material.Stiffness.Custom.setUseConstantPoissonsRatio(True)
        self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_P, newTable)
        self.assertEqual(self.material.Stiffness.Custom.getCustomStiffnessLoadingTable(), newTableZeroPoisson)

        #should be able to set for another type of custom mode
        newTable2 = [(2,3,0.4),(5,6,0.45)]
        self.material.Stiffness.Custom.setUseConstantPoissonsRatio(False)
        self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_Q, newTable2)

        self.assertEqual(self.material.Stiffness.Custom.getCustomStiffnessLoadingTable(), newTableZeroPoisson)
        self.material.Stiffness.Custom.setCustomMode(CustomMode.CUSTOM_Q)
        self.assertEqual(self.material.Stiffness.Custom.getCustomStiffnessLoadingTable(), newTable2)

    def testCustomStiffnessLoadingTableValidationFailure(self):
        self.material.Stiffness.Custom.setCustomMode(CustomMode.CUSTOM_P)
        self.assertEqual(self.material.Stiffness.Custom.getCustomMode(), CustomMode.CUSTOM_P)

        #too few rows
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_P, [(1,2,0.3,4)])
        
        #non-increasing first column
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_P, [(1,2,0.3),(1,5,0.4)])
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_EPSV, [(1,2,0.3),(0.4,5,0.4)])
            
        #invalid mode parameter
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_Q, [(-1,2,0.3),(4,5,0.4)])
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_GAMMA, [(-1,2,0.3),(4,5,0.4)])

        #invalid youngs modulus parameter
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_P, [(1,-2,0.3),(4,5,0.4)])
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_P, [(1,2,0.3),(4,-5,0.4)])
        
        #invalid poisson ratio parameter
        self.material.Stiffness.Custom.setUseConstantPoissonsRatio(False)
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_P, [(1,2,-0.3),(4,5,0.4)])
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_P, [(1,2,0.3),(4,5,-0.4)])
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_P, [(1,2,0.5),(4,5,0.4)])
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_P, [(1,2,0.3),(4,5,0.5)])

        #invalid poisson ratio with constant poisson ratio
        self.material.Stiffness.Custom.setUseConstantPoissonsRatio(True)
        self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_P, [(1,2,-0.3),(4,5,0.4)])
        self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_P, [(1,2,0.3),(4,5,-0.4)])
        self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_P, [(1,2,0.5),(4,5,0.4)])
        self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_P, [(1,2,0.3),(4,5,0.5)])


class TestStiffnessUnloadingTables(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]

        #requires a table to exist before setting stiffness type to custom
        newTable = [(1,2,0.3),(4,5,0.4)]
        self.material.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_P, newTable)
        self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_P, newTable)
        self.material.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_Q, newTable)

        self.material.Stiffness.setElasticType(MaterialElasticityTypes.CUSTOM_STIFFNESS)
        self.material.Stiffness.Custom.setUseUnloadingCondition(True)
    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)

    def testCustomStiffnessUnloadingTableSuccess(self):
        self.material.Stiffness.Custom.setCustomMode(CustomMode.CUSTOM_P)
        self.assertEqual(self.material.Stiffness.Custom.getCustomMode(), CustomMode.CUSTOM_P)

        newTable = [(1,2,0.3),(4,5,0.4)]
        self.material.Stiffness.Custom.setUnloadingUseConstantPoissonsRatio(False)
        self.material.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_P, newTable)
        self.assertEqual(self.material.Stiffness.Custom.getCustomStiffnessUnloadingTable(), newTable)
    
        #if constant poisson ratio is used, then the poisson ratio column should be zeroed out.
        newTableZeroPoisson = [(1,2,0),(4,5,0)]
        self.material.Stiffness.Custom.setUnloadingUseConstantPoissonsRatio(True)
        self.material.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_P, newTable)
        self.assertEqual(self.material.Stiffness.Custom.getCustomStiffnessUnloadingTable(), newTableZeroPoisson)

        #should be able to set for another type of custom mode
        newTable2 = [(2,3,0.4),(5,6,0.45)]
        self.material.Stiffness.Custom.setUnloadingUseConstantPoissonsRatio(False)
        self.material.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_Q, newTable2)

        self.assertEqual(self.material.Stiffness.Custom.getCustomStiffnessUnloadingTable(), newTableZeroPoisson)
        self.material.Stiffness.Custom.setCustomMode(CustomMode.CUSTOM_Q)
        self.assertEqual(self.material.Stiffness.Custom.getCustomStiffnessUnloadingTable(), newTable2)

    def testCustomStiffnessUnloadingTableValidationFailure(self):
        self.material.Stiffness.Custom.setCustomMode(CustomMode.CUSTOM_P)
        self.assertEqual(self.material.Stiffness.Custom.getCustomMode(), CustomMode.CUSTOM_P)

        #too few rows
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_P, [(1,2,0.3,4)])
        
        #non-increasing first column
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_P, [(1,2,0.3),(1,5,0.4)])
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_EPSV, [(1,2,0.3),(0.4,5,0.4)])
            
        #invalid mode parameter
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_Q, [(-1,2,0.3),(4,5,0.4)])
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_GAMMA, [(-1,2,0.3),(4,5,0.4)])

        #invalid youngs modulus parameter
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_P, [(1,-2,0.3),(4,5,0.4)])
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_P, [(1,2,0.3),(4,-5,0.4)])
        
        #invalid poisson ratio parameter
        self.material.Stiffness.Custom.setUnloadingUseConstantPoissonsRatio(False)
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_P, [(1,2,-0.3),(4,5,0.4)])
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_P, [(1,2,0.3),(4,5,-0.4)])
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_P, [(1,2,0.5),(4,5,0.4)])
        with self.assertRaises(Exception):
            self.material.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_P, [(1,2,0.3),(4,5,0.5)])

        #invalid poisson ratio with constant poisson ratio
        self.material.Stiffness.Custom.setUnloadingUseConstantPoissonsRatio(True)
        self.material.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_P, [(1,2,-0.3),(4,5,0.4)])
        self.material.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_P, [(1,2,0.3),(4,5,-0.4)])
        self.material.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_P, [(1,2,0.5),(4,5,0.4)])
        self.material.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_P, [(1,2,0.3),(4,5,0.5)])
