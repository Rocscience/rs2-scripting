import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.RS2Modeler import RS2Modeler
from rs2.PropertyEnums import*
from rs2.proxyObjects.PileSubproxyObjects.ForceDisplacement import ForceDisplacementStageFactor, ForceDisplacementDefinedStageFactor

parentDirectoryHelper.addParentDirectoryToPath()

class TestPileStageFactor(unittest.TestCase):

    def areCableStageFactorsEqual(self, sf1 : ForceDisplacementStageFactor, sf2 : ForceDisplacementStageFactor):
        return sf1.getXFactor() == sf2.getXFactor() and sf1.getYFactor() == sf2.getYFactor()

    def resetCableStageFactor(self, sf: ForceDisplacementDefinedStageFactor):
        sf.setXFactor(1)
        sf.setYFactor(1)

    @classmethod
    def setUpClass(cls):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        cls.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, cls.copiedModelPath)
        cls.modeler = RS2Modeler()
        cls.model = cls.modeler.openFile(cls.copiedModelPath)
        cls.pile = cls.model.getAllPileProperties()[0]

    def setUp(self):
        #setup the model so that there is only 1 stage factor.
        self.pile.setStageForceDisplacement(True)
        factorMap = self.pile.ForceDisplacement.getDefinedStageFactors()

        sf1 = factorMap[next(iter(factorMap))]#get the first defined stage factor
                        
        self.resetCableStageFactor(sf1)

        self.pile.ForceDisplacement.setDefinedStageFactors({1: sf1})
        
    @classmethod
    def tearDownClass(cls):
        cls.model.close()
        cls.modeler.client.closeConnection()
        os.remove(cls.copiedModelPath)


############# getStageFactor Tests #############
    def GetStageFactorSuccess(self):
        sf1 = self.pile.ForceDisplacement.getStageFactor(1)
        self.assertTrue(self.areCableStageFactorsEqual(self.pile.ForceDisplacement.getDefinedStageFactors()[1], sf1))

    def GetStageFactorNotEnabled(self):
        self.pile.setStageForceDisplacement(False)
    
        with self.assertRaises(Exception):
            self.pile.ForceDisplacement.getStageFactor(1)

    def GetStageFactorInvalidStage(self):
        with self.assertRaises(Exception):
            self.pile.ForceDisplacement.getStageFactor(0)
        with self.assertRaises(Exception):
            self.pile.ForceDisplacement.getStageFactor(99)

    def GetStageFactorAfterLastDefined(self):
        sf1 = self.pile.ForceDisplacement.getDefinedStageFactors()[1]
        sf1.setXFactor(0.555)

        sf2 = self.pile.ForceDisplacement.getStageFactor(2)

        self.assertTrue(self.areCableStageFactorsEqual(sf1, sf2))
    
    def GetStageFactorBeforeFirstDefined(self):
        defaultConductivityFactor = 1

        sf1 = self.pile.ForceDisplacement.getDefinedStageFactors()[1]
        sf1.setYFactor(0.444)

        self.pile.ForceDisplacement.setDefinedStageFactors({2: sf1})
        sfDefault = self.pile.ForceDisplacement.getStageFactor(1)

        self.assertEqual(sfDefault.getYFactor(), defaultConductivityFactor)

    def GetStageFactorBetweenMultiple(self):
        sf1 = self.pile.ForceDisplacement.getDefinedStageFactors()[1]
        sf1.setXFactor(0.1)

        sf2 = self.pile.ForceDisplacement.createStageFactor(2)
        sf2.setXFactor(0.2)

        sf3 = self.pile.ForceDisplacement.createStageFactor(3)
        sf3.setXFactor(0.3)

        sf2 = self.pile.ForceDisplacement.getStageFactor(2)
        
        self.assertEqual(sf2.getXFactor(), 0.2)

        sfMap = self.pile.ForceDisplacement.getDefinedStageFactors()
        del sfMap[2]
        self.pile.ForceDisplacement.setDefinedStageFactors(sfMap)

        #with 2 deleted, getting 2 should return 1
        sf2 = self.pile.ForceDisplacement.getStageFactor(2)
        self.assertEqual(sf2.getXFactor(), 0.1)
######## createStageFactor Tests ########

    def CreateStageFactorDisabled(self):
        self.pile.setStageForceDisplacement(False)
        with self.assertRaises(Exception):
            self.pile.ForceDisplacement.createStageFactor(2)

    def CreateStageFactorAlreadyExists(self):
        with self.assertRaises(Exception):
            self.pile.ForceDisplacement.createStageFactor(1)
    
    def CreateStageFactorStageOutOfRange(self):
        with self.assertRaises(Exception):
            self.pile.ForceDisplacement.createStageFactor(0)
        with self.assertRaises(Exception):
            self.pile.ForceDisplacement.createStageFactor(99)

    def CreateStageFactorSuccessCopyFromLastDefined(self):
        sf1 = self.pile.ForceDisplacement.getDefinedStageFactors()[1]
        sf1.setXFactor(0.555)

        sf2 = self.pile.ForceDisplacement.createStageFactor(2)
        sf1 = self.pile.ForceDisplacement.getDefinedStageFactors()[1]

        self.assertTrue(self.areCableStageFactorsEqual(sf2, sf1))

    def CreateDefaultStageFactorSuccess(self):
        sf1 = self.pile.ForceDisplacement.getDefinedStageFactors()[1]
        sf1.setXFactor(0.555)

        self.pile.ForceDisplacement.setDefinedStageFactors({2: sf1})

        sf1 = self.pile.ForceDisplacement.createStageFactor(1)
        sf2 = self.pile.ForceDisplacement.getDefinedStageFactors()[2]
        
        self.assertEqual(sf1.getXFactor(), 1)
        self.assertEqual(sf2.getXFactor(), 0.555)

    def CreateStageFactorMultiple(self):
        sf4 = self.pile.ForceDisplacement.createStageFactor(4)
        sf4.setXFactor(0.4)

        sf2 = self.pile.ForceDisplacement.createStageFactor(2)
        sf2.setXFactor(0.2)

        #test 1: insert between 2 and 4. Should be the same as 2
        self.pile.ForceDisplacement.createStageFactor(3)
        sfMap = self.pile.ForceDisplacement.getDefinedStageFactors()
        self.assertTrue(self.areCableStageFactorsEqual(sfMap[3], sfMap[2]))

        # test 2: insert after 4, should be the same as 4
        self.pile.ForceDisplacement.createStageFactor(5)
        sfMap = self.pile.ForceDisplacement.getDefinedStageFactors()
        self.assertTrue(self.areCableStageFactorsEqual(sfMap[5], sfMap[4]))
    
####### setDefinedStageFactors Tests #######

    def SetDefinedEmptyMapFailure(self):
        with self.assertRaises(Exception):
            self.pile.ForceDisplacement.setDefinedStageFactors({})
    
    def SetDefinedStageFactorOutOfRange(self):
        sf1 = self.pile.ForceDisplacement.getDefinedStageFactors()[1]
        with self.assertRaises(Exception):
            self.pile.ForceDisplacement.setDefinedStageFactors({0: sf1})
        with self.assertRaises(Exception):
            self.pile.ForceDisplacement.setDefinedStageFactors({99: sf1})
    
    def SetDefinedStageFactorSuccess(self):
        sf1 = self.pile.ForceDisplacement.getDefinedStageFactors()[1]
        sf1.setXFactor(0.1)

        sf2 = self.pile.ForceDisplacement.createStageFactor(2)
        sf2.setXFactor(0.2)

        sf4 = self.pile.ForceDisplacement.createStageFactor(4)
        sf4.setXFactor(0.4)

        sf6 = self.pile.ForceDisplacement.createStageFactor(6)
        sf6.setXFactor(0.6)

        sfMap = self.pile.ForceDisplacement.getDefinedStageFactors()


        self.pile.ForceDisplacement.setDefinedStageFactors({1: sfMap[1], 2: sfMap[2], 4: sfMap[4], 6: sfMap[6]})
        sfMap = self.pile.ForceDisplacement.getDefinedStageFactors()

        self.assertEqual(sfMap[1].getXFactor(), 0.1)
        self.assertEqual(sfMap[2].getXFactor(), 0.2)
        self.assertEqual(sfMap[4].getXFactor(), 0.4)
        self.assertEqual(sfMap[6].getXFactor(), 0.6)

        #Now try removing 4
        self.pile.ForceDisplacement.setDefinedStageFactors({1: sfMap[1], 2: sfMap[2], 6: sfMap[6]})
        sfMap = self.pile.ForceDisplacement.getDefinedStageFactors()

        self.assertEqual(len(sfMap), 3)
        self.assertEqual(sfMap[1].getXFactor(), 0.1)
        self.assertEqual(sfMap[2].getXFactor(), 0.2)
        self.assertEqual(sfMap[6].getXFactor(), 0.6)

        #now try removing the bottom end
        self.pile.ForceDisplacement.setDefinedStageFactors({2: sfMap[2], 6: sfMap[6]})
        sfMap = self.pile.ForceDisplacement.getDefinedStageFactors()

        self.assertEqual(len(sfMap), 2)
        self.assertEqual(sfMap[2].getXFactor(), 0.2)
        self.assertEqual(sfMap[6].getXFactor(), 0.6)

        #now try removing the top end
        self.pile.ForceDisplacement.setDefinedStageFactors({2: sfMap[2]})       
        sfMap = self.pile.ForceDisplacement.getDefinedStageFactors()

        self.assertEqual(len(sfMap), 1)
        self.assertEqual(sfMap[2].getXFactor(), 0.2)


        #now try adding them all back again after deleting in different stages
        sf1 = self.pile.ForceDisplacement.createStageFactor(1)
        sf1.setXFactor(0.1)

        sf4 = self.pile.ForceDisplacement.createStageFactor(4)
        sf4.setXFactor(0.4)

        sf6 = self.pile.ForceDisplacement.createStageFactor(6)
        sf6.setXFactor(0.6)

        sfMap = self.pile.ForceDisplacement.getDefinedStageFactors()


        self.pile.ForceDisplacement.setDefinedStageFactors({1: sfMap[1], 3: sfMap[2], 5: sfMap[4], 6: sfMap[6]})
        sfMap = self.pile.ForceDisplacement.getDefinedStageFactors()

        self.assertEqual(sfMap[1].getXFactor(), 0.1)
        self.assertEqual(sfMap[3].getXFactor(), 0.2)
        self.assertEqual(sfMap[5].getXFactor(), 0.4)
        self.assertEqual(sfMap[6].getXFactor(), 0.6)

        #now try and change the stage factor definition method
        self.pile.ForceDisplacement.setDefinedStageFactors({1: sfMap[1], 3: sfMap[3], 5: sfMap[5], 6: sfMap[6]})
        sfMap = self.pile.ForceDisplacement.getDefinedStageFactors()

        self.assertEqual(sfMap[1].getXFactor(), 0.1)
        self.assertEqual(sfMap[3].getXFactor(), 0.2)
        self.assertEqual(sfMap[5].getXFactor(), 0.4)
        self.assertEqual(sfMap[6].getXFactor(), 0.6)

### Now test getDefinedStageFactors ####

    def GetDefinedStageFactorsNotEnabled(self):
        self.pile.setStageForceDisplacement(False)
        with self.assertRaises(Exception):
            self.pile.ForceDisplacement.getDefinedStageFactors()
    
    def GetDefinedStageFactorsSuccess(self):
        sfMap = self.pile.ForceDisplacement.getDefinedStageFactors()
        self.assertEqual(len(sfMap), 1)

        sf1 = sfMap[1]
        sf1.setXFactor(0.1)

        sf2 = self.pile.ForceDisplacement.createStageFactor(2)
        sf2.setXFactor(0.2)

        sf4 = self.pile.ForceDisplacement.createStageFactor(4)
        sf4.setXFactor(0.4)

        sf6 = self.pile.ForceDisplacement.createStageFactor(6)
        sf6.setXFactor(0.6)

        sfMap = self.pile.ForceDisplacement.getDefinedStageFactors()

        self.assertEqual(len(sfMap), 4)
        self.assertEqual(sfMap[1].getXFactor(), 0.1)
        self.assertEqual(sfMap[2].getXFactor(), 0.2)
        self.assertEqual(sfMap[4].getXFactor(), 0.4)
        self.assertEqual(sfMap[6].getXFactor(), 0.6)

class TestPileStageFactorAbsolute(TestPileStageFactor):
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