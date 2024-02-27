import unittest
import os, sys, inspect
import shutil
import parentDirectoryHelper
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import*

parentDirectoryHelper.addParentDirectoryToPath()

class TestDatum(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/starterProject.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]
        self.material.Datum.setUsingDatum(True)

    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)

    def testGetAllMaterialDatums(self):
        d1 = self.material.Datum.getDatumUnloadingYoungsModulus()
        d1.setChange(1.1)
        self.assertEqual(d1.getChange(), 1.1)

        d2 = self.material.Datum.getDatumYoungsModulus()
        d2.setChange(2.1)
        self.assertEqual(d2.getChange(), 2.1)

        d3 = self.material.Datum.getDatumCohesion()
        d3.setPeakChange(3.1)
        self.assertEqual(d3.getPeakChange(), 3.1)

        d4 = self.material.Datum.getDatumFrictionAngle()
        d4.setPeakChange(4.1)
        self.assertEqual(d4.getPeakChange(), 4.1)

    def testMaterialSetUsingDatum(self):
        self.material.Datum.setUsingDatum(False)
        self.assertEqual(self.material.Datum.getUsingDatum(), False)
        self.material.Datum.setUsingDatum(True)
        self.assertEqual(self.material.Datum.getUsingDatum(), True)

    def testBaseDatum(self):
        ym = self.material.Datum.getDatumUnloadingYoungsModulus()

        ym.setUsing(True)
        self.assertEqual(ym.getUsing(), True)
        ym.setUsing(False)
        self.assertEqual(ym.getUsing(), False)
        ym.setType(DatumType.DATUM_TYPE_DEPTH)
        self.assertEqual(ym.getType(), DatumType.DATUM_TYPE_DEPTH)
        ym.setType(DatumType.DATUM_TYPE_RADIAL)
        self.assertEqual(ym.getType(), DatumType.DATUM_TYPE_RADIAL)
        ym.setDatum(8.1)
        self.assertEqual(ym.getDatum(), 8.1)
        ym.setCenter(9.1, 10.5)
        self.assertEqual(ym.getCenter(), (9.1, 10.5))

    def testSimpleDatum(self):
        ym = self.material.Datum.getDatumUnloadingYoungsModulus()
    
        ym.setChange(20.1)
        self.assertEqual(ym.getChange(), 20.1)
        ym.setUseCutoff(True)
        self.assertEqual(ym.getUseCutoff(), True)
        ym.setUseCutoff(False)
        self.assertEqual(ym.getUseCutoff(), False)
        ym.setCutoff(30.1)
        self.assertEqual(ym.getCutoff(), 30.1)

    def testPeakResidualDatum(self):
        ym = self.material.Datum.getDatumCohesion()

        ym.setPeakChange(21.1)
        self.assertEqual(ym.getPeakChange(), 21.1)
        ym.setUsePeakCutoff(True)
        self.assertEqual(ym.getUsePeakCutoff(), True)
        ym.setUsePeakCutoff(False)
        self.assertEqual(ym.getUsePeakCutoff(), False)
        ym.setPeakCutoffValue(31.1)
        self.assertEqual(ym.getPeakCutoffValue(), 31.1)
        ym.setResidualChange(22.1)
        self.assertEqual(ym.getResidualChange(), 22.1)
        ym.setUseResidualCutoff(True)
        self.assertEqual(ym.getUseResidualCutoff(), True)
        ym.setUseResidualCutoff(False)
        self.assertEqual(ym.getUseResidualCutoff(), False)
        ym.setResidualCutoffValue(32.1)
        self.assertEqual(ym.getResidualCutoffValue(), 32.1)

class TestDatumFailures(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        parentDirectory = parentDirectoryHelper.getParentDirectory()
        blankModelPath = f"{parentDirectory}/resources/testModelWithDiscreteModulusFunction.fez"
        self.copiedModelPath = f"{parentDirectory}/resources/testProject.fez"
        shutil.copy(blankModelPath, self.copiedModelPath)
        self.modeler = RS2Modeler()
        self.model = self.modeler.openFile(self.copiedModelPath)
        self.material = self.model.getAllMaterialProperties()[0]

    @classmethod
    def tearDownClass(self):
        self.model.close()
        self.modeler.client.closeConnection()
        os.remove(self.copiedModelPath)

    def testSetDatumFailure(self):
        with self.assertRaises(Exception) as e:
            self.material.Datum.getUsingDatum()
        with self.assertRaises(Exception) as e:
            self.material.Datum.setUsingDatum(True)

        self.material.Strength.setFailureCriterion(StrengthCriteriaTypes.CAM_CLAY)
        with self.assertRaises(Exception) as e:
            self.material.Datum.getUsingDatum()        
        with self.assertRaises(Exception) as e:
            self.material.Datum.setUsingDatum(True)

        self.material.Strength.setFailureCriterion(StrengthCriteriaTypes.MODIFIED_CAM_CLAY)
        with self.assertRaises(Exception) as e:
            self.material.Datum.getUsingDatum()        
        with self.assertRaises(Exception) as e:
            self.material.Datum.setUsingDatum(True)

        self.material.Strength.setFailureCriterion(StrengthCriteriaTypes.BARCELONA_BASIC)
        with self.assertRaises(Exception) as e:
            self.material.Datum.getUsingDatum()        
        with self.assertRaises(Exception) as e:
            self.material.Datum.setUsingDatum(True)

        self.material.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
        self.material.Stiffness.setElasticType(MaterialElasticityTypes.ORTHOTROPIC)
        with self.assertRaises(Exception) as e:
            self.material.Datum.getUsingDatum()        
        with self.assertRaises(Exception) as e:
            self.material.Datum.setUsingDatum(True)

        self.material.Stiffness.setElasticType(MaterialElasticityTypes.ISOTROPIC)
        self.material.Datum.setUsingDatum(True)
        self.assertEqual(self.material.Datum.getUsingDatum(), True)
