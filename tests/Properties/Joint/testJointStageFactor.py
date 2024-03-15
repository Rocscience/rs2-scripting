import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*
from rs2.modeler.properties.joint.BartonBandis import BartonBandisStageFactor, BartonBandisDefinedStageFactor

parentDirectoryHelper.addParentDirectoryToPath()

class TestJointStageFactor(unittest.TestCase):

    def areCableStageFactorsEqual(self, sf1 : BartonBandisStageFactor, sf2 : BartonBandisStageFactor):
        return sf1.getNormalStiffnessFactor() == sf2.getNormalStiffnessFactor() and \
            sf1.getShearStiffnessFactor() == sf2.getShearStiffnessFactor() and \
            sf1.getJCSFactor() == sf2.getJCSFactor() and \
            sf1.getJRCFactor() == sf2.getJRCFactor() and \
            sf1.getResidualFrictionAngleFactor() == sf2.getResidualFrictionAngleFactor() and \
            sf1.getAdditionalPressureInsideJointFactor() == sf2.getAdditionalPressureInsideJointFactor() and \
            sf1.getGroundwaterPressureFactor() == sf2.getGroundwaterPressureFactor()

    def resetBartonBandisStageFactor(self, sf: BartonBandisDefinedStageFactor):
        sf.setNormalStiffnessFactor(1)
        sf.setShearStiffnessFactor(1)
        sf.setJCSFactor(1)
        sf.setJRCFactor(1)
        sf.setResidualFrictionAngleFactor(1)
        sf.setAdditionalPressureInsideJointFactor(1)
        sf.setGroundwaterPressureFactor(1)

    @classmethod
    def setUpClass(cls):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        cls.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, cls.copiedModelPath)
        cls.modeler = RS2Modeler()
        cls.model = cls.modeler.openFile(cls.copiedModelPath)
        cls.joint = cls.model.getAllJointProperties()[0]
        cls.stageFactorInterface = cls.joint.BartonBandis.stageFactorInterface

    def setUp(self):
        #setup the model so that there is only 1 stage factor.
        self.joint.BartonBandis.setApplyStageFactors(True)
        factorMap = self.stageFactorInterface.getDefinedStageFactors()

        sf1 = factorMap[next(iter(factorMap))]#get the first defined stage factor
                        
        self.resetBartonBandisStageFactor(sf1)

        self.stageFactorInterface.setDefinedStageFactors({1: sf1})
        
    @classmethod
    def tearDownClass(cls):
        cls.model.close()
        cls.modeler.client.closeConnection()
        os.remove(cls.copiedModelPath)


############# getStageFactor Tests #############
    def GetStageFactorSuccess(self):
        sf1 = self.stageFactorInterface.getStageFactor(1)
        self.assertTrue(self.areCableStageFactorsEqual(self.stageFactorInterface.getDefinedStageFactors()[1], sf1))

    def GetStageFactorNotEnabled(self):
        self.joint.BartonBandis.setApplyStageFactors(False)
    
        with self.assertRaises(Exception):
            self.stageFactorInterface.getStageFactor(1)

    def GetStageFactorInvalidStage(self):
        with self.assertRaises(Exception):
            self.stageFactorInterface.getStageFactor(0)
        with self.assertRaises(Exception):
            self.stageFactorInterface.getStageFactor(99)

    def GetStageFactorAfterLastDefined(self):
        sf1 = self.stageFactorInterface.getDefinedStageFactors()[1]
        sf1.setNormalStiffnessFactor(0.555)

        sf2 = self.stageFactorInterface.getStageFactor(2)

        self.assertTrue(self.areCableStageFactorsEqual(sf1, sf2))
    
    def GetStageFactorBeforeFirstDefined(self):
        defaultFactor = 1

        sf1 = self.stageFactorInterface.getDefinedStageFactors()[1]
        sf1.setShearStiffnessFactor(0.444)

        self.stageFactorInterface.setDefinedStageFactors({2: sf1})
        sfDefault = self.stageFactorInterface.getStageFactor(1)

        self.assertEqual(sfDefault.getShearStiffnessFactor(), defaultFactor)

    def GetStageFactorBetweenMultiple(self):
        sf1 = self.stageFactorInterface.getDefinedStageFactors()[1]
        sf1.setNormalStiffnessFactor(0.1)

        sf2 = self.stageFactorInterface.createStageFactor(2)
        sf2.setNormalStiffnessFactor(0.2)

        sf3 = self.stageFactorInterface.createStageFactor(3)
        sf3.setNormalStiffnessFactor(0.3)

        sf2 = self.stageFactorInterface.getStageFactor(2)
        
        self.assertEqual(sf2.getNormalStiffnessFactor(), 0.2)

        sfMap = self.stageFactorInterface.getDefinedStageFactors()
        del sfMap[2]
        self.stageFactorInterface.setDefinedStageFactors(sfMap)

        #with 2 deleted, getting 2 should return 1
        sf2 = self.stageFactorInterface.getStageFactor(2)
        self.assertEqual(sf2.getNormalStiffnessFactor(), 0.1)
######## createStageFactor Tests ########

    def CreateStageFactorDisabled(self):
        self.joint.BartonBandis.setApplyStageFactors(False)
        with self.assertRaises(Exception):
            self.stageFactorInterface.createStageFactor(2)

    def CreateStageFactorAlreadyExists(self):
        with self.assertRaises(Exception):
            self.stageFactorInterface.createStageFactor(1)
    
    def CreateStageFactorStageOutOfRange(self):
        with self.assertRaises(Exception):
            self.stageFactorInterface.createStageFactor(0)
        with self.assertRaises(Exception):
            self.stageFactorInterface.createStageFactor(99)

    def CreateStageFactorSuccessCopyFromLastDefined(self):
        sf1 = self.stageFactorInterface.getDefinedStageFactors()[1]
        sf1.setNormalStiffnessFactor(0.555)

        sf2 = self.stageFactorInterface.createStageFactor(2)
        sf1 = self.stageFactorInterface.getDefinedStageFactors()[1]

        self.assertTrue(self.areCableStageFactorsEqual(sf2, sf1))

    def CreateDefaultStageFactorSuccess(self):
        sf1 = self.stageFactorInterface.getDefinedStageFactors()[1]
        sf1.setNormalStiffnessFactor(0.555)

        self.stageFactorInterface.setDefinedStageFactors({2: sf1})

        sf1 = self.stageFactorInterface.createStageFactor(1)
        sf2 = self.stageFactorInterface.getDefinedStageFactors()[2]
        
        self.assertEqual(sf1.getNormalStiffnessFactor(), 1)
        self.assertEqual(sf2.getNormalStiffnessFactor(), 0.555)

    def CreateStageFactorMultiple(self):
        sf4 = self.stageFactorInterface.createStageFactor(4)
        sf4.setNormalStiffnessFactor(0.4)

        sf2 = self.stageFactorInterface.createStageFactor(2)
        sf2.setNormalStiffnessFactor(0.2)

        #test 1: insert between 2 and 4. Should be the same as 2
        self.stageFactorInterface.createStageFactor(3)
        sfMap = self.stageFactorInterface.getDefinedStageFactors()
        self.assertTrue(self.areCableStageFactorsEqual(sfMap[3], sfMap[2]))

        # test 2: insert after 4, should be the same as 4
        self.stageFactorInterface.createStageFactor(5)
        sfMap = self.stageFactorInterface.getDefinedStageFactors()
        self.assertTrue(self.areCableStageFactorsEqual(sfMap[5], sfMap[4]))
    
####### setDefinedStageFactors Tests #######

    def SetDefinedEmptyMapFailure(self):
        with self.assertRaises(Exception):
            self.stageFactorInterface.setDefinedStageFactors({})
    
    def SetDefinedStageFactorOutOfRange(self):
        sf1 = self.stageFactorInterface.getDefinedStageFactors()[1]
        with self.assertRaises(Exception):
            self.stageFactorInterface.setDefinedStageFactors({0: sf1})
        with self.assertRaises(Exception):
            self.stageFactorInterface.setDefinedStageFactors({99: sf1})
    
    def SetDefinedStageFactorSuccess(self):
        sf1 = self.stageFactorInterface.getDefinedStageFactors()[1]
        sf1.setNormalStiffnessFactor(0.1)

        sf2 = self.stageFactorInterface.createStageFactor(2)
        sf2.setNormalStiffnessFactor(0.2)

        sf4 = self.stageFactorInterface.createStageFactor(4)
        sf4.setNormalStiffnessFactor(0.4)

        sf6 = self.stageFactorInterface.createStageFactor(6)
        sf6.setNormalStiffnessFactor(0.6)

        sfMap = self.stageFactorInterface.getDefinedStageFactors()


        self.stageFactorInterface.setDefinedStageFactors({1: sfMap[1], 2: sfMap[2], 4: sfMap[4], 6: sfMap[6]})
        sfMap = self.stageFactorInterface.getDefinedStageFactors()

        self.assertEqual(sfMap[1].getNormalStiffnessFactor(), 0.1)
        self.assertEqual(sfMap[2].getNormalStiffnessFactor(), 0.2)
        self.assertEqual(sfMap[4].getNormalStiffnessFactor(), 0.4)
        self.assertEqual(sfMap[6].getNormalStiffnessFactor(), 0.6)

        #Now try removing 4
        self.stageFactorInterface.setDefinedStageFactors({1: sfMap[1], 2: sfMap[2], 6: sfMap[6]})
        sfMap = self.stageFactorInterface.getDefinedStageFactors()

        self.assertEqual(len(sfMap), 3)
        self.assertEqual(sfMap[1].getNormalStiffnessFactor(), 0.1)
        self.assertEqual(sfMap[2].getNormalStiffnessFactor(), 0.2)
        self.assertEqual(sfMap[6].getNormalStiffnessFactor(), 0.6)

        #now try removing the bottom end
        self.stageFactorInterface.setDefinedStageFactors({2: sfMap[2], 6: sfMap[6]})
        sfMap = self.stageFactorInterface.getDefinedStageFactors()

        self.assertEqual(len(sfMap), 2)
        self.assertEqual(sfMap[2].getNormalStiffnessFactor(), 0.2)
        self.assertEqual(sfMap[6].getNormalStiffnessFactor(), 0.6)

        #now try removing the top end
        self.stageFactorInterface.setDefinedStageFactors({2: sfMap[2]})       
        sfMap = self.stageFactorInterface.getDefinedStageFactors()

        self.assertEqual(len(sfMap), 1)
        self.assertEqual(sfMap[2].getNormalStiffnessFactor(), 0.2)


        #now try adding them all back again after deleting in different stages
        sf1 = self.stageFactorInterface.createStageFactor(1)
        sf1.setNormalStiffnessFactor(0.1)

        sf4 = self.stageFactorInterface.createStageFactor(4)
        sf4.setNormalStiffnessFactor(0.4)

        sf6 = self.stageFactorInterface.createStageFactor(6)
        sf6.setNormalStiffnessFactor(0.6)

        sfMap = self.stageFactorInterface.getDefinedStageFactors()


        self.stageFactorInterface.setDefinedStageFactors({1: sfMap[1], 3: sfMap[2], 5: sfMap[4], 6: sfMap[6]})
        sfMap = self.stageFactorInterface.getDefinedStageFactors()

        self.assertEqual(sfMap[1].getNormalStiffnessFactor(), 0.1)
        self.assertEqual(sfMap[3].getNormalStiffnessFactor(), 0.2)
        self.assertEqual(sfMap[5].getNormalStiffnessFactor(), 0.4)
        self.assertEqual(sfMap[6].getNormalStiffnessFactor(), 0.6)

        #now try and change the stage factor definition method
        self.stageFactorInterface.setDefinedStageFactors({1: sfMap[1], 3: sfMap[3], 5: sfMap[5], 6: sfMap[6]})
        sfMap = self.stageFactorInterface.getDefinedStageFactors()

        self.assertEqual(sfMap[1].getNormalStiffnessFactor(), 0.1)
        self.assertEqual(sfMap[3].getNormalStiffnessFactor(), 0.2)
        self.assertEqual(sfMap[5].getNormalStiffnessFactor(), 0.4)
        self.assertEqual(sfMap[6].getNormalStiffnessFactor(), 0.6)

### Now test getDefinedStageFactors ####

    def GetDefinedStageFactorsNotEnabled(self):
        self.joint.BartonBandis.setApplyStageFactors(False)
        with self.assertRaises(Exception):
            self.stageFactorInterface.getDefinedStageFactors()
    
    def GetDefinedStageFactorsSuccess(self):
        sfMap = self.stageFactorInterface.getDefinedStageFactors()
        self.assertEqual(len(sfMap), 1)

        sf1 = sfMap[1]
        sf1.setNormalStiffnessFactor(0.1)

        sf2 = self.stageFactorInterface.createStageFactor(2)
        sf2.setNormalStiffnessFactor(0.2)

        sf4 = self.stageFactorInterface.createStageFactor(4)
        sf4.setNormalStiffnessFactor(0.4)

        sf6 = self.stageFactorInterface.createStageFactor(6)
        sf6.setNormalStiffnessFactor(0.6)

        sfMap = self.stageFactorInterface.getDefinedStageFactors()

        self.assertEqual(len(sfMap), 4)
        self.assertEqual(sfMap[1].getNormalStiffnessFactor(), 0.1)
        self.assertEqual(sfMap[2].getNormalStiffnessFactor(), 0.2)
        self.assertEqual(sfMap[4].getNormalStiffnessFactor(), 0.4)
        self.assertEqual(sfMap[6].getNormalStiffnessFactor(), 0.6)

    def GetDefault(self):
        sfMap = self.stageFactorInterface.getDefinedStageFactors()
        self.stageFactorInterface.setDefinedStageFactors({2: sfMap[1]})
    
        self.joint.SetPermeable(True)
        self.joint.HyperbolicSoftening.setWorkSoftening(True)
        sf1 = self.stageFactorInterface.getStageFactor(1)
        self.assertEqual(sf1.getJointPermeableFactor(), True)
        self.assertEqual(self.joint.HyperbolicSoftening.stageFactorInterface.getStageFactor(1).getWorkSofteningFactor(), True)

        self.joint.SetPermeable(False)
        self.joint.HyperbolicSoftening.setWorkSoftening(False)
        sf1 = self.stageFactorInterface.getStageFactor(1)
        self.assertEqual(sf1.getJointPermeableFactor(), False)
        self.assertEqual(self.joint.HyperbolicSoftening.stageFactorInterface.getStageFactor(1).getWorkSofteningFactor(), False)

    def CreateDefault(self):
        sfMap = self.stageFactorInterface.getDefinedStageFactors()
        self.stageFactorInterface.setDefinedStageFactors({2: sfMap[1]})
    
        self.joint.SetPermeable(True)
        self.joint.HyperbolicSoftening.setWorkSoftening(True)
        sf1 = self.stageFactorInterface.createStageFactor(1)
        self.assertEqual(sf1.getJointPermeableFactor(), True)
        self.assertEqual(self.joint.HyperbolicSoftening.stageFactorInterface.getStageFactor(1).getWorkSofteningFactor(), True)

        sfMap = self.stageFactorInterface.getDefinedStageFactors()
        self.stageFactorInterface.setDefinedStageFactors({2: sfMap[1]})

        self.joint.SetPermeable(False)
        self.joint.HyperbolicSoftening.setWorkSoftening(False)
        sf1 = self.stageFactorInterface.createStageFactor(1)
        self.assertEqual(sf1.getJointPermeableFactor(), False)
        self.assertEqual(self.joint.HyperbolicSoftening.stageFactorInterface.getStageFactor(1).getWorkSofteningFactor(), False)

class TestJointStageFactorAbsolute(TestJointStageFactor):
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
    def testGetDefault(self):
        self.GetDefault()
    def testCreateDefault(self):
        self.CreateDefault()