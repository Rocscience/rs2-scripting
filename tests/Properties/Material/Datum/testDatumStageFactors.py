import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestDatumStageFactors(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/testAllDatumsEnabled.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        
    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.model._client.closeConnection()
        os.remove(self.copiedModelPath)

    def testDatumStageFactor(self):
       
        self.material.StageFactors.setStageDatumStageFactor(True)
        
        sf1 = self.material.Datum.stageFactorInterface.getDefinedStageFactors()[1]
        sf1Young = sf1.getDatumYoungsStageFactor()
        sf1Cohesion = sf1.getDatumCohesionStageFactor()
        sf1FrictionAngle = sf1.getDatumFrictionStageFactor()

        sf1Young.setChange(0.1)
        sf1Young.setPeakCutoffValue(0.2)
        sf1Young.setResidualChange(0.3)
        sf1Young.setResidualCutoffValue(0.4)
        sf1Young.setDatum(0.5)

        sf1Cohesion.setChange(0.11)
        sf1Cohesion.setPeakCutoffValue(0.22)
        sf1Cohesion.setResidualChange(0.33)
        sf1Cohesion.setResidualCutoffValue(0.44)
        sf1Cohesion.setDatum(0.55)   

        sf1FrictionAngle.setChange(0.111)
        sf1FrictionAngle.setPeakCutoffValue(0.222)
        sf1FrictionAngle.setResidualChange(0.333)
        sf1FrictionAngle.setResidualCutoffValue(0.444)
        sf1FrictionAngle.setDatum(0.555)

        self.assertEqual(sf1Young.getChange(), 0.1)
        self.assertEqual(sf1Young.getPeakCutoffValue(), 0.2)
        self.assertEqual(sf1Young.getResidualChange(), 0.3)
        self.assertEqual(sf1Young.getResidualCutoffValue(), 0.4)
        self.assertEqual(sf1Young.getDatum(), 0.5)

        self.assertEqual(sf1Cohesion.getChange(), 0.11)
        self.assertEqual(sf1Cohesion.getPeakCutoffValue(), 0.22)
        self.assertEqual(sf1Cohesion.getResidualChange(), 0.33)
        self.assertEqual(sf1Cohesion.getResidualCutoffValue(), 0.44)
        self.assertEqual(sf1Cohesion.getDatum(), 0.55)

        self.assertEqual(sf1FrictionAngle.getChange(), 0.111)
        self.assertEqual(sf1FrictionAngle.getPeakCutoffValue(), 0.222)
        self.assertEqual(sf1FrictionAngle.getResidualChange(), 0.333)
        self.assertEqual(sf1FrictionAngle.getResidualCutoffValue(), 0.444)
        self.assertEqual(sf1FrictionAngle.getDatum(), 0.555)

