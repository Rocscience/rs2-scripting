import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*
from rs2.proxyObjects.LinerSubproxyObjects.CableTruss import CableTrussStageFactor, CableTrussDefinedStageFactor

parentDirectoryHelper.addParentDirectoryToPath()

class TestLinerStageFactor(unittest.TestCase):
    stageFactorDefinitionMethod = None

    def areCableStageFactorsEqual(self, sf1 : CableTrussStageFactor, sf2 : CableTrussStageFactor):
        return sf1.getUnitWeightFactor() == sf2.getUnitWeightFactor() and \
            sf1.getCableDiameterFactor() == sf2.getCableDiameterFactor() and \
            sf1.getYoungsModulusFactor() == sf2.getYoungsModulusFactor() and \
            sf1.getAxialStrainExpansionFactor() == sf2.getAxialStrainExpansionFactor() and \
            sf1.getTensileStrengthPeakFactor() == sf2.getTensileStrengthPeakFactor() and \
            sf1.getTensileStrengthResidualFactor() == sf2.getTensileStrengthResidualFactor() and \
            sf1.getConductivityFactor() == sf2.getConductivityFactor() and \
            sf1.getSpecificHeatCapacityFactor() == sf2.getSpecificHeatCapacityFactor() and \
            sf1.getExpansionCoefficientFactor() == sf2.getExpansionCoefficientFactor()

    def resetCableStageFactor(self, sf: CableTrussDefinedStageFactor):
        sf.setUnitWeightFactor(1)
        sf.setCableDiameterFactor(1)
        sf.setYoungsModulusFactor(1)
        sf.setAxialStrainExpansionFactor(1)
        sf.setTensileStrengthPeakFactor(1)
        sf.setTensileStrengthResidualFactor(1)
        sf.setConductivityFactor(1)
        sf.setSpecificHeatCapacityFactor(1)
        sf.setExpansionCoefficientFactor(1)

    @classmethod
    def setUpClass(cls):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        cls.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, cls.copiedModelPath)
        cls.modeler = RS2Modeler()
        cls.model = cls.modeler.openFile(cls.copiedModelPath)
        cls.liner = cls.model.getAllLinerProperties()[0]

        if cls.stageFactorDefinitionMethod == StageFactorDefinitionMethod.ABSOLUTE_STAGE_FACTOR:
            cls.stageFactorDefinitionOppositeMethod = StageFactorDefinitionMethod.RELATIVE_STAGE_FACTOR
        else:
            cls.stageFactorDefinitionOppositeMethod = StageFactorDefinitionMethod.ABSOLUTE_STAGE_FACTOR

    def setUp(self):
        #setup the model so that there is only 1 stage factor.
        self.liner.CableTruss.setStageCableProperties(True)
        factorMap = self.liner.CableTruss.getDefinedStageFactors()

        sf1 = factorMap[next(iter(factorMap))]#get the first defined stage factor
                        
        self.resetCableStageFactor(sf1)

        self.liner.CableTruss.setDefinedStageFactors(self.stageFactorDefinitionMethod, {1: sf1})
        
    @classmethod
    def tearDownClass(cls):
        cls.model.close()
        cls.modeler.client.closeConnection()
        os.remove(cls.copiedModelPath)


############# getStageFactor Tests #############
    def GetStageFactorSuccess(self):
        sf1 = self.liner.CableTruss.getStageFactor(1)
        self.assertTrue(self.areCableStageFactorsEqual(self.liner.CableTruss.getDefinedStageFactors()[1], sf1))

    def GetStageFactorNotEnabled(self):
        self.liner.CableTruss.setStageCableProperties(False)
    
        with self.assertRaises(Exception):
            self.liner.CableTruss.getStageFactor(1)

    def GetStageFactorInvalidStage(self):
        with self.assertRaises(Exception):
            self.liner.CableTruss.getStageFactor(0)
        with self.assertRaises(Exception):
            self.liner.CableTruss.getStageFactor(99)

    def GetStageFactorAfterLastDefined(self):
        sf1 = self.liner.CableTruss.getDefinedStageFactors()[1]
        sf1.setAxialStrainExpansionFactor(0.555)

        sf2 = self.liner.CableTruss.getStageFactor(2)

        self.assertTrue(self.areCableStageFactorsEqual(sf1, sf2))
    
    def GetStageFactorBeforeFirstDefined(self):
        defaultConductivityFactor = 1

        sf1 = self.liner.CableTruss.getDefinedStageFactors()[1]
        sf1.setConductivityFactor(0.444)

        self.liner.CableTruss.setDefinedStageFactors(self.stageFactorDefinitionMethod, {2: sf1})
        sfDefault = self.liner.CableTruss.getStageFactor(1)

        self.assertEqual(sfDefault.getConductivityFactor(), defaultConductivityFactor)

    def GetStageFactorBetweenMultiple(self):
        sf1 = self.liner.CableTruss.getDefinedStageFactors()[1]
        sf1.setAxialStrainExpansionFactor(0.1)

        sf2 = self.liner.CableTruss.createStageFactor(2)
        sf2.setAxialStrainExpansionFactor(0.2)

        sf3 = self.liner.CableTruss.createStageFactor(3)
        sf3.setAxialStrainExpansionFactor(0.3)

        sf2 = self.liner.CableTruss.getStageFactor(2)
        
        self.assertEqual(sf2.getAxialStrainExpansionFactor(), 0.2)

        sfMap = self.liner.CableTruss.getDefinedStageFactors()
        del sfMap[2]
        self.liner.CableTruss.setDefinedStageFactors(self.stageFactorDefinitionMethod, sfMap)

        #with 2 deleted, getting 2 should return 1
        sf2 = self.liner.CableTruss.getStageFactor(2)
        self.assertEqual(sf2.getAxialStrainExpansionFactor(), 0.1)
######## createStageFactor Tests ########

    def CreateStageFactorDisabled(self):
        self.liner.CableTruss.setStageCableProperties(False)
        with self.assertRaises(Exception):
            self.liner.CableTruss.createStageFactor(2)

    def CreateStageFactorAlreadyExists(self):
        with self.assertRaises(Exception):
            self.liner.CableTruss.createStageFactor(1)
    
    def CreateStageFactorStageOutOfRange(self):
        with self.assertRaises(Exception):
            self.liner.CableTruss.createStageFactor(0)
        with self.assertRaises(Exception):
            self.liner.CableTruss.createStageFactor(99)

    def CreateStageFactorSuccessCopyFromLastDefined(self):
        sf1 = self.liner.CableTruss.getDefinedStageFactors()[1]
        sf1.setAxialStrainExpansionFactor(0.555)

        sf2 = self.liner.CableTruss.createStageFactor(2)
        sf1 = self.liner.CableTruss.getDefinedStageFactors()[1]

        self.assertTrue(self.areCableStageFactorsEqual(sf2, sf1))

    def CreateDefaultStageFactorSuccess(self):
        sf1 = self.liner.CableTruss.getDefinedStageFactors()[1]
        sf1.setAxialStrainExpansionFactor(0.555)

        self.liner.CableTruss.setDefinedStageFactors(self.stageFactorDefinitionMethod, {2: sf1})

        sf1 = self.liner.CableTruss.createStageFactor(1)
        sf2 = self.liner.CableTruss.getDefinedStageFactors()[2]
        
        self.assertEqual(sf1.getAxialStrainExpansionFactor(), 1)
        self.assertEqual(sf2.getAxialStrainExpansionFactor(), 0.555)

    def CreateStageFactorMultiple(self):
        sf4 = self.liner.CableTruss.createStageFactor(4)
        sf4.setAxialStrainExpansionFactor(0.4)

        sf2 = self.liner.CableTruss.createStageFactor(2)
        sf2.setAxialStrainExpansionFactor(0.2)

        #test 1: insert between 2 and 4. Should be the same as 2
        self.liner.CableTruss.createStageFactor(3)
        sfMap = self.liner.CableTruss.getDefinedStageFactors()
        self.assertTrue(self.areCableStageFactorsEqual(sfMap[3], sfMap[2]))

        # test 2: insert after 4, should be the same as 4
        self.liner.CableTruss.createStageFactor(5)
        sfMap = self.liner.CableTruss.getDefinedStageFactors()
        self.assertTrue(self.areCableStageFactorsEqual(sfMap[5], sfMap[4]))
    
####### setDefinedStageFactors Tests #######

    def SetDefinedEmptyMapFailure(self):
        with self.assertRaises(Exception):
            self.liner.CableTruss.setDefinedStageFactors(self.stageFactorDefinitionMethod, {})
    
    def SetDefinedStageFactorOutOfRange(self):
        sf1 = self.liner.CableTruss.getDefinedStageFactors()[1]
        with self.assertRaises(Exception):
            self.liner.CableTruss.setDefinedStageFactors(self.stageFactorDefinitionMethod, {0: sf1})
        with self.assertRaises(Exception):
            self.liner.CableTruss.setDefinedStageFactors(self.stageFactorDefinitionMethod, {99: sf1})
    
    def SetDefinedStageFactorSuccess(self):
        sf1 = self.liner.CableTruss.getDefinedStageFactors()[1]
        sf1.setAxialStrainExpansionFactor(0.1)

        sf2 = self.liner.CableTruss.createStageFactor(2)
        sf2.setAxialStrainExpansionFactor(0.2)

        sf4 = self.liner.CableTruss.createStageFactor(4)
        sf4.setAxialStrainExpansionFactor(0.4)

        sf6 = self.liner.CableTruss.createStageFactor(6)
        sf6.setAxialStrainExpansionFactor(0.6)

        sfMap = self.liner.CableTruss.getDefinedStageFactors()


        self.liner.CableTruss.setDefinedStageFactors(self.stageFactorDefinitionMethod, {1: sfMap[1], 2: sfMap[2], 4: sfMap[4], 6: sfMap[6]})
        sfMap = self.liner.CableTruss.getDefinedStageFactors()

        self.assertEqual(sfMap[1].getAxialStrainExpansionFactor(), 0.1)
        self.assertEqual(sfMap[2].getAxialStrainExpansionFactor(), 0.2)
        self.assertEqual(sfMap[4].getAxialStrainExpansionFactor(), 0.4)
        self.assertEqual(sfMap[6].getAxialStrainExpansionFactor(), 0.6)

        #Now try removing 4
        self.liner.CableTruss.setDefinedStageFactors(self.stageFactorDefinitionMethod, {1: sfMap[1], 2: sfMap[2], 6: sfMap[6]})
        sfMap = self.liner.CableTruss.getDefinedStageFactors()

        self.assertEqual(len(sfMap), 3)
        self.assertEqual(sfMap[1].getAxialStrainExpansionFactor(), 0.1)
        self.assertEqual(sfMap[2].getAxialStrainExpansionFactor(), 0.2)
        self.assertEqual(sfMap[6].getAxialStrainExpansionFactor(), 0.6)

        #now try removing the bottom end
        self.liner.CableTruss.setDefinedStageFactors(self.stageFactorDefinitionMethod, {2: sfMap[2], 6: sfMap[6]})
        sfMap = self.liner.CableTruss.getDefinedStageFactors()

        self.assertEqual(len(sfMap), 2)
        self.assertEqual(sfMap[2].getAxialStrainExpansionFactor(), 0.2)
        self.assertEqual(sfMap[6].getAxialStrainExpansionFactor(), 0.6)

        #now try removing the top end
        self.liner.CableTruss.setDefinedStageFactors(self.stageFactorDefinitionMethod, {2: sfMap[2]})       
        sfMap = self.liner.CableTruss.getDefinedStageFactors()

        self.assertEqual(len(sfMap), 1)
        self.assertEqual(sfMap[2].getAxialStrainExpansionFactor(), 0.2)


        #now try adding them all back again after deleting in different stages
        sf1 = self.liner.CableTruss.createStageFactor(1)
        sf1.setAxialStrainExpansionFactor(0.1)

        sf4 = self.liner.CableTruss.createStageFactor(4)
        sf4.setAxialStrainExpansionFactor(0.4)

        sf6 = self.liner.CableTruss.createStageFactor(6)
        sf6.setAxialStrainExpansionFactor(0.6)

        sfMap = self.liner.CableTruss.getDefinedStageFactors()


        self.liner.CableTruss.setDefinedStageFactors(self.stageFactorDefinitionMethod, {1: sfMap[1], 3: sfMap[2], 5: sfMap[4], 6: sfMap[6]})
        sfMap = self.liner.CableTruss.getDefinedStageFactors()

        self.assertEqual(sfMap[1].getAxialStrainExpansionFactor(), 0.1)
        self.assertEqual(sfMap[3].getAxialStrainExpansionFactor(), 0.2)
        self.assertEqual(sfMap[5].getAxialStrainExpansionFactor(), 0.4)
        self.assertEqual(sfMap[6].getAxialStrainExpansionFactor(), 0.6)

        #now try and change the stage factor definition method
        self.liner.CableTruss.setDefinedStageFactors(self.stageFactorDefinitionOppositeMethod, {1: sfMap[1], 3: sfMap[3], 5: sfMap[5], 6: sfMap[6]})
        sfMap = self.liner.CableTruss.getDefinedStageFactors()

        self.assertEqual(sfMap[1].getAxialStrainExpansionFactor(), 0.1)
        self.assertEqual(sfMap[3].getAxialStrainExpansionFactor(), 0.2)
        self.assertEqual(sfMap[5].getAxialStrainExpansionFactor(), 0.4)
        self.assertEqual(sfMap[6].getAxialStrainExpansionFactor(), 0.6)

### Now test getDefinedStageFactors ####

    def GetDefinedStageFactorsNotEnabled(self):
        self.liner.CableTruss.setStageCableProperties(False)
        with self.assertRaises(Exception):
            self.liner.CableTruss.getDefinedStageFactors()
    
    def GetDefinedStageFactorsSuccess(self):
        sfMap = self.liner.CableTruss.getDefinedStageFactors()
        self.assertEqual(len(sfMap), 1)

        sf1 = sfMap[1]
        sf1.setAxialStrainExpansionFactor(0.1)

        sf2 = self.liner.CableTruss.createStageFactor(2)
        sf2.setAxialStrainExpansionFactor(0.2)

        sf4 = self.liner.CableTruss.createStageFactor(4)
        sf4.setAxialStrainExpansionFactor(0.4)

        sf6 = self.liner.CableTruss.createStageFactor(6)
        sf6.setAxialStrainExpansionFactor(0.6)

        sfMap = self.liner.CableTruss.getDefinedStageFactors()

        self.assertEqual(len(sfMap), 4)
        self.assertEqual(sfMap[1].getAxialStrainExpansionFactor(), 0.1)
        self.assertEqual(sfMap[2].getAxialStrainExpansionFactor(), 0.2)
        self.assertEqual(sfMap[4].getAxialStrainExpansionFactor(), 0.4)
        self.assertEqual(sfMap[6].getAxialStrainExpansionFactor(), 0.6)


#### test getStageFactorMethod ####
    def GetStageFactorMethod(self):
        factorMap = self.liner.CableTruss.getDefinedStageFactors()
        self.liner.CableTruss.setDefinedStageFactors(StageFactorDefinitionMethod.ABSOLUTE_STAGE_FACTOR, factorMap)

        self.assertEqual(self.liner.CableTruss.getStageFactorMethod(), StageFactorDefinitionMethod.ABSOLUTE_STAGE_FACTOR)

        factorMap = self.liner.CableTruss.getDefinedStageFactors()
        self.liner.CableTruss.setDefinedStageFactors(StageFactorDefinitionMethod.RELATIVE_STAGE_FACTOR, factorMap)

        self.assertEqual(self.liner.CableTruss.getStageFactorMethod(), StageFactorDefinitionMethod.RELATIVE_STAGE_FACTOR)

class TestLinerStageFactorRelative(TestLinerStageFactor):
    stageFactorDefinitionMethod = StageFactorDefinitionMethod.RELATIVE_STAGE_FACTOR
    def testGetStageFactorSuccess(self):
        self.GetStageFactorSuccess()
    def testGetStageFactorNotEnabled(self):
        self.GetStageFactorNotEnabled()
    def testGetStageFactorInvalidStage(self):
        self.GetStageFactorInvalidStage()
    def testGetStageFactorAfterLastDefined(self):
        self.GetStageFactorAfterLastDefined()
    def testGetStageFactorBeforeFirstDefined(self):
        self.GetStageFactorBeforeFirstDefined()
    def testGetStageFactorBetweenMultiple(self):
        self.GetStageFactorBetweenMultiple()
    def testCreateStageFactorDisabled(self):
        self.CreateStageFactorDisabled()
    def testCreateStageFactorAlreadyExists(self):
        self.CreateStageFactorAlreadyExists()
    def testCreateStageFactorStageOutOfRange(self):
        self.CreateStageFactorStageOutOfRange()
    def testCreateStageFactorSuccessCopyFromLastDefined(self):
        self.CreateStageFactorSuccessCopyFromLastDefined()
    def testCreateDefaultStageFactorSuccess(self):
        self.CreateDefaultStageFactorSuccess()
    def testCreateStageFactorMultiple(self):
        self.CreateStageFactorMultiple()
    def testSetDefinedEmptyMapFailure(self):
        self.SetDefinedEmptyMapFailure()
    def testSetDefinedStageFactorOutOfRange(self):
        self.SetDefinedStageFactorOutOfRange()
    def testSetDefinedStageFactorSuccess(self):
        self.SetDefinedStageFactorSuccess()
    def testGetDefinedStageFactorsNotEnabled(self):
        self.GetDefinedStageFactorsNotEnabled()
    def testGetDefinedStageFactorsSuccess(self):
        self.GetDefinedStageFactorsSuccess()
    def testGetStageFactorMethod(self):
        self.GetStageFactorMethod()

class TestLinerStageFactorAbsolute(TestLinerStageFactor):
    stageFactorDefinitionMethod = StageFactorDefinitionMethod.ABSOLUTE_STAGE_FACTOR
    def testGetStageFactorSuccess(self):
        self.GetStageFactorSuccess()
    def testGetStageFactorNotEnabled(self):
        self.GetStageFactorNotEnabled()
    def testGetStageFactorInvalidStage(self):
        self.GetStageFactorInvalidStage()
    def testGetStageFactorAfterLastDefined(self):
        self.GetStageFactorAfterLastDefined()
    def testGetStageFactorBeforeFirstDefined(self):
        self.GetStageFactorBeforeFirstDefined()
    def testGetStageFactorBetweenMultiple(self):
        self.GetStageFactorBetweenMultiple()
    def testCreateStageFactorDisabled(self):
        self.CreateStageFactorDisabled()
    def testCreateStageFactorAlreadyExists(self):
        self.CreateStageFactorAlreadyExists()
    def testCreateStageFactorStageOutOfRange(self):
        self.CreateStageFactorStageOutOfRange()
    def testCreateStageFactorSuccessCopyFromLastDefined(self):
        self.CreateStageFactorSuccessCopyFromLastDefined()
    def testCreateDefaultStageFactorSuccess(self):
        self.CreateDefaultStageFactorSuccess()
    def testCreateStageFactorMultiple(self):
        self.CreateStageFactorMultiple()
    def testSetDefinedEmptyMapFailure(self):
        self.SetDefinedEmptyMapFailure()
    def testSetDefinedStageFactorOutOfRange(self):
        self.SetDefinedStageFactorOutOfRange()
    def testSetDefinedStageFactorSuccess(self):
        self.SetDefinedStageFactorSuccess()
    def testGetDefinedStageFactorsNotEnabled(self):
        self.GetDefinedStageFactorsNotEnabled()
    def testGetDefinedStageFactorsSuccess(self):
        self.GetDefinedStageFactorsSuccess()
    def testGetStageFactorMethod(self):
        self.GetStageFactorMethod()