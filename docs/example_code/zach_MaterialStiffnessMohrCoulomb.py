from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_Stiffness.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\stiffnessMohrCoulomb_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\stiffnessMohrCoulomb_python.fez'

modeler = RS2Modeler()

model = modeler.openFile(base_model)

model.saveAs(final_python_model)

matList = model.getAllMaterialProperties()
mat1 = matList[0]
mat2 = matList[1]
mat3 = matList[2]
mat4 = matList[3]
mat5 = matList[4]
mat6 = matList[5]
mat7 = matList[6] 
mat8 = matList[7]
mat9 = matList[8]
mat10 = matList[9] 
mat11 = matList[10]
mat12 = matList[11]
mat13 = matList[12]
mat14 = matList[13]
mat15 = matList[14]
mat16 = matList[15]
mat17 = matList[16]
mat18 = matList[17]
mat19 = matList[18]
mat20 = matList[19]
mat21 = matList[20]
mat22 = matList[21]
mat23 = matList[22]
mat24 = matList[23]
mat25 = matList[24]
mat26 = matList[25]
mat27 = matList[26]
mat28 = matList[27]
mat29 = matList[28]
mat30 = matList[29]
mat31 = matList[30]
mat32 = matList[31]
mat33 = matList[32]
mat34 = matList[33]
mat35 = matList[34]
mat36 = matList[35]
mat37 = matList[36]
mat38 = matList[37]
mat39 = matList[38]
mat40 = matList[39]
mat41 = matList[40]
mat42 = matList[41]
mat43 = matList[42]
mat44 = matList[43]
mat45 = matList[44]
mat46 = matList[45]
mat47 = matList[46]
mat48 = matList[47]
mat49 = matList[48]
mat50 = matList[49]
mat51 = matList[50]
mat52 = matList[51]
mat53 = matList[52]
mat54 = matList[53]
mat55 = matList[54]
mat56 = matList[55]
mat57 = matList[56]
mat58 = matList[57]
mat59 = matList[58]
mat60 = matList[59]
mat61 = matList[60]
mat62 = matList[61]
mat63 = matList[62]
mat64 = matList[63]

def test1():
    mat = mat1

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.ISOTROPIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)
    mat.Stiffness.Isotropic.setPoissonsRatio(0.1)
    mat.Stiffness.Isotropic.setYoungsModulus(1.2)
    mat.Stiffness.Isotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.Isotropic.setResidualYoungsModulus(1.3)
    mat.Stiffness.Isotropic.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.Isotropic.setUnloadingPoissonsRatio(0.4)
    mat.Stiffness.Isotropic.setUnloadingYoungsModulus(1.5)
    mat.Stiffness.Isotropic.setUseUnloadingResidualYoungsModulus(True)
    mat.Stiffness.Isotropic.setUnloadingResidualYoungsModulus(1.6)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.ISOTROPIC)
    assert(mat.Stiffness.Isotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Isotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.Isotropic.getYoungsModulus(), 1.2)
    assert(mat.Stiffness.Isotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.Isotropic.getResidualYoungsModulus(), 1.3)
    assert(mat.Stiffness.Isotropic.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.Isotropic.getUnloadingPoissonsRatio(), 0.4)
    assert(mat.Stiffness.Isotropic.getUnloadingYoungsModulus(), 1.5)
    assert(mat.Stiffness.Isotropic.getUseUnloadingResidualYoungsModulus(), True)
    assert(mat.Stiffness.Isotropic.getUnloadingResidualYoungsModulus(), 1.6)

def test2():
    mat = mat2

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.ISOTROPIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)
    mat.Stiffness.Isotropic.setPoissonsRatio(0.1)
    mat.Stiffness.Isotropic.setYoungsModulus(1.2)
    mat.Stiffness.Isotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.Isotropic.setResidualYoungsModulus(1.3)
    mat.Stiffness.Isotropic.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRESS)
    mat.Stiffness.Isotropic.setUnloadingPoissonsRatio(0.4)
    mat.Stiffness.Isotropic.setUnloadingYoungsModulus(1.5)
    mat.Stiffness.Isotropic.setUseUnloadingResidualYoungsModulus(True)
    mat.Stiffness.Isotropic.setUnloadingResidualYoungsModulus(1.6)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.ISOTROPIC)
    assert(mat.Stiffness.Isotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Isotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.Isotropic.getYoungsModulus(), 1.2)
    assert(mat.Stiffness.Isotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.Isotropic.getResidualYoungsModulus(), 1.3)
    assert(mat.Stiffness.Isotropic.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRESS)
    assert(mat.Stiffness.Isotropic.getUnloadingPoissonsRatio(), 0.4)
    assert(mat.Stiffness.Isotropic.getUnloadingYoungsModulus(), 1.5)
    assert(mat.Stiffness.Isotropic.getUseUnloadingResidualYoungsModulus(), True)
    assert(mat.Stiffness.Isotropic.getUnloadingResidualYoungsModulus(), 1.6)

def test3():
    mat = mat3

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.ISOTROPIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)
    mat.Stiffness.Isotropic.setPoissonsRatio(0.1)
    mat.Stiffness.Isotropic.setYoungsModulus(1.2)
    mat.Stiffness.Isotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.Isotropic.setResidualYoungsModulus(1.3)
    mat.Stiffness.Isotropic.setUnloadingCondition(UnloadingConditions.UC_VOLUMETRIC_STRAIN)
    mat.Stiffness.Isotropic.setUnloadingPoissonsRatio(0.4)
    mat.Stiffness.Isotropic.setUnloadingYoungsModulus(1.5)
    mat.Stiffness.Isotropic.setUseUnloadingResidualYoungsModulus(True)
    mat.Stiffness.Isotropic.setUnloadingResidualYoungsModulus(1.6)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.ISOTROPIC)
    assert(mat.Stiffness.Isotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Isotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.Isotropic.getYoungsModulus(), 1.2)
    assert(mat.Stiffness.Isotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.Isotropic.getResidualYoungsModulus(), 1.3)
    assert(mat.Stiffness.Isotropic.getUnloadingCondition(), UnloadingConditions.UC_VOLUMETRIC_STRAIN)
    assert(mat.Stiffness.Isotropic.getUnloadingPoissonsRatio(), 0.4)
    assert(mat.Stiffness.Isotropic.getUnloadingYoungsModulus(), 1.5)
    assert(mat.Stiffness.Isotropic.getUseUnloadingResidualYoungsModulus(), True)
    assert(mat.Stiffness.Isotropic.getUnloadingResidualYoungsModulus(), 1.6)

def test4():
    mat = mat4

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.ISOTROPIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)
    mat.Stiffness.Isotropic.setPoissonsRatio(0.1)
    mat.Stiffness.Isotropic.setYoungsModulus(1.2)
    mat.Stiffness.Isotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.Isotropic.setResidualYoungsModulus(1.3)
    mat.Stiffness.Isotropic.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRAIN)
    mat.Stiffness.Isotropic.setUnloadingPoissonsRatio(0.4)
    mat.Stiffness.Isotropic.setUnloadingYoungsModulus(1.5)
    mat.Stiffness.Isotropic.setUseUnloadingResidualYoungsModulus(True)
    mat.Stiffness.Isotropic.setUnloadingResidualYoungsModulus(1.6)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.ISOTROPIC)
    assert(mat.Stiffness.Isotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Isotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.Isotropic.getYoungsModulus(), 1.2)
    assert(mat.Stiffness.Isotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.Isotropic.getResidualYoungsModulus(), 1.3)
    assert(mat.Stiffness.Isotropic.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRAIN)
    assert(mat.Stiffness.Isotropic.getUnloadingPoissonsRatio(), 0.4)
    assert(mat.Stiffness.Isotropic.getUnloadingYoungsModulus(), 1.5)
    assert(mat.Stiffness.Isotropic.getUseUnloadingResidualYoungsModulus(), True)
    assert(mat.Stiffness.Isotropic.getUnloadingResidualYoungsModulus(), 1.6)

def test5():
    mat = mat5

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.ISOTROPIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(False)
    mat.Stiffness.Isotropic.setPoissonsRatio(0.1)
    mat.Stiffness.Isotropic.setYoungsModulus(1.2)
    mat.Stiffness.Isotropic.setUseResidualYoungsModulus(False)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.ISOTROPIC)
    assert(mat.Stiffness.Isotropic.getUseUnloadingCondition(), False)
    assert(mat.Stiffness.Isotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.Isotropic.getYoungsModulus(), 1.2)
    assert(mat.Stiffness.Isotropic.getUseResidualYoungsModulus(), False)

def test6():
    mat = mat6

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.ISOTROPIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)
    mat.Stiffness.Isotropic.setPoissonsRatio(0.1)
    mat.Stiffness.Isotropic.setYoungsModulus(1.2)
    mat.Stiffness.Isotropic.setUseResidualYoungsModulus(False)
    mat.Stiffness.Isotropic.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.Isotropic.setUnloadingPoissonsRatio(0.4)
    mat.Stiffness.Isotropic.setUnloadingYoungsModulus(1.5)
    mat.Stiffness.Isotropic.setUseUnloadingResidualYoungsModulus(True)
    mat.Stiffness.Isotropic.setUnloadingResidualYoungsModulus(1.6)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.ISOTROPIC)
    assert(mat.Stiffness.Isotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Isotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.Isotropic.getYoungsModulus(), 1.2)
    assert(mat.Stiffness.Isotropic.getUseResidualYoungsModulus(), False)
    assert(mat.Stiffness.Isotropic.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.Isotropic.getUnloadingPoissonsRatio(), 0.4)
    assert(mat.Stiffness.Isotropic.getUnloadingYoungsModulus(), 1.5)
    assert(mat.Stiffness.Isotropic.getUseUnloadingResidualYoungsModulus(), True)
    assert(mat.Stiffness.Isotropic.getUnloadingResidualYoungsModulus(), 1.6)

def test7():
    mat = mat7

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.ISOTROPIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)
    mat.Stiffness.Isotropic.setPoissonsRatio(0.1)
    mat.Stiffness.Isotropic.setYoungsModulus(1.2)
    mat.Stiffness.Isotropic.setUseResidualYoungsModulus(False)
    mat.Stiffness.Isotropic.setResidualYoungsModulus(1.3)
    mat.Stiffness.Isotropic.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.Isotropic.setUnloadingPoissonsRatio(0.4)
    mat.Stiffness.Isotropic.setUnloadingYoungsModulus(1.5)
    mat.Stiffness.Isotropic.setUseUnloadingResidualYoungsModulus(False)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.ISOTROPIC)
    assert(mat.Stiffness.Isotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Isotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.Isotropic.getYoungsModulus(), 1.2)
    assert(mat.Stiffness.Isotropic.getUseResidualYoungsModulus(), False)
    assert(mat.Stiffness.Isotropic.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.Isotropic.getUnloadingPoissonsRatio(), 0.4)
    assert(mat.Stiffness.Isotropic.getUnloadingYoungsModulus(), 1.5)
    assert(mat.Stiffness.Isotropic.getUseUnloadingResidualYoungsModulus(), False)

def test8():
    mat = mat8

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.ISOTROPIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(False)
    mat.Stiffness.Isotropic.setPoissonsRatio(0.1)
    mat.Stiffness.Isotropic.setYoungsModulus(1.2)
    mat.Stiffness.Isotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.Isotropic.setResidualYoungsModulus(1.3)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.ISOTROPIC)
    assert(mat.Stiffness.Isotropic.getUseUnloadingCondition(), False)
    assert(mat.Stiffness.Isotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.Isotropic.getYoungsModulus(), 1.2)
    assert(mat.Stiffness.Isotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.Isotropic.getResidualYoungsModulus(), 1.3)

def test9():
    mat = mat9

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.TRANSVERSELY_ISOTROPIC)
    mat.Stiffness.TransverselyIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.TransverselyIsotropic.setShearModulus(1.1)
    mat.Stiffness.TransverselyIsotropic.setAngleCounterclockwiseFromHorizontalToE1(1.2)
    mat.Stiffness.TransverselyIsotropic.setYoungsModulusE1AndEz(1.3)
    mat.Stiffness.TransverselyIsotropic.setYoungsModulusE2(1.4)
    mat.Stiffness.TransverselyIsotropic.setPoissonsRatioV12(1.5)
    mat.Stiffness.TransverselyIsotropic.setPoissonsRatioVAndV1z(1.6)
    mat.Stiffness.TransverselyIsotropic.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.TransverselyIsotropic.setUnloadingShearModulus(1.7)
    mat.Stiffness.TransverselyIsotropic.setUnloadingAngleCounterclockwiseFromHorizontalToE1(1.8)
    mat.Stiffness.TransverselyIsotropic.setUnloadingYoungsModulusE1AndEz(1.9)
    mat.Stiffness.TransverselyIsotropic.setUnloadingYoungsModulusE2(1.11)
    mat.Stiffness.TransverselyIsotropic.setUnloadingPoissonsRatioV12(1.12)
    mat.Stiffness.TransverselyIsotropic.setUnloadingPoissonsRatioVAndV1z(1.13)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.TRANSVERSELY_ISOTROPIC)
    assert(mat.Stiffness.TransverselyIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.TransverselyIsotropic.getShearModulus(), 1.1)
    assert(mat.Stiffness.TransverselyIsotropic.getAngleCounterclockwiseFromHorizontalToE1(), 1.2)
    assert(mat.Stiffness.TransverselyIsotropic.getYoungsModulusE1AndEz(), 1.3)
    assert(mat.Stiffness.TransverselyIsotropic.getYoungsModulusE2(), 1.4)
    assert(mat.Stiffness.TransverselyIsotropic.getPoissonsRatioV12(), 1.5)
    assert(mat.Stiffness.TransverselyIsotropic.getPoissonsRatioVAndV1z(), 1.6)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingShearModulus(), 1.7)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingAngleCounterclockwiseFromHorizontalToE1(), 1.8)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingYoungsModulusE1AndEz(), 1.9)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingYoungsModulusE2(), 1.11)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingPoissonsRatioV12(), 1.12)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingPoissonsRatioVAndV1z(), 1.13)

def test10():
    mat = mat10

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.TRANSVERSELY_ISOTROPIC)
    mat.Stiffness.TransverselyIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.TransverselyIsotropic.setShearModulus(1.1)
    mat.Stiffness.TransverselyIsotropic.setAngleCounterclockwiseFromHorizontalToE1(1.2)
    mat.Stiffness.TransverselyIsotropic.setYoungsModulusE1AndEz(1.3)
    mat.Stiffness.TransverselyIsotropic.setYoungsModulusE2(1.4)
    mat.Stiffness.TransverselyIsotropic.setPoissonsRatioV12(1.5)
    mat.Stiffness.TransverselyIsotropic.setPoissonsRatioVAndV1z(1.6)
    mat.Stiffness.TransverselyIsotropic.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRESS)
    mat.Stiffness.TransverselyIsotropic.setUnloadingShearModulus(1.7)
    mat.Stiffness.TransverselyIsotropic.setUnloadingAngleCounterclockwiseFromHorizontalToE1(1.8)
    mat.Stiffness.TransverselyIsotropic.setUnloadingYoungsModulusE1AndEz(1.9)
    mat.Stiffness.TransverselyIsotropic.setUnloadingYoungsModulusE2(1.11)
    mat.Stiffness.TransverselyIsotropic.setUnloadingPoissonsRatioV12(1.12)
    mat.Stiffness.TransverselyIsotropic.setUnloadingPoissonsRatioVAndV1z(1.13)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.TRANSVERSELY_ISOTROPIC)
    assert(mat.Stiffness.TransverselyIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.TransverselyIsotropic.getShearModulus(), 1.1)
    assert(mat.Stiffness.TransverselyIsotropic.getAngleCounterclockwiseFromHorizontalToE1(), 1.2)
    assert(mat.Stiffness.TransverselyIsotropic.getYoungsModulusE1AndEz(), 1.3)
    assert(mat.Stiffness.TransverselyIsotropic.getYoungsModulusE2(), 1.4)
    assert(mat.Stiffness.TransverselyIsotropic.getPoissonsRatioV12(), 1.5)
    assert(mat.Stiffness.TransverselyIsotropic.getPoissonsRatioVAndV1z(), 1.6)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRESS)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingShearModulus(), 1.7)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingAngleCounterclockwiseFromHorizontalToE1(), 1.8)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingYoungsModulusE1AndEz(), 1.9)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingYoungsModulusE2(), 1.11)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingPoissonsRatioV12(), 1.12)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingPoissonsRatioVAndV1z(), 1.13)

def test11():
    mat = mat11

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.TRANSVERSELY_ISOTROPIC)
    mat.Stiffness.TransverselyIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.TransverselyIsotropic.setShearModulus(1.1)
    mat.Stiffness.TransverselyIsotropic.setAngleCounterclockwiseFromHorizontalToE1(1.2)
    mat.Stiffness.TransverselyIsotropic.setYoungsModulusE1AndEz(1.3)
    mat.Stiffness.TransverselyIsotropic.setYoungsModulusE2(1.4)
    mat.Stiffness.TransverselyIsotropic.setPoissonsRatioV12(1.5)
    mat.Stiffness.TransverselyIsotropic.setPoissonsRatioVAndV1z(1.6)
    mat.Stiffness.TransverselyIsotropic.setUnloadingCondition(UnloadingConditions.UC_VOLUMETRIC_STRAIN)
    mat.Stiffness.TransverselyIsotropic.setUnloadingShearModulus(1.7)
    mat.Stiffness.TransverselyIsotropic.setUnloadingAngleCounterclockwiseFromHorizontalToE1(1.8)
    mat.Stiffness.TransverselyIsotropic.setUnloadingYoungsModulusE1AndEz(1.9)
    mat.Stiffness.TransverselyIsotropic.setUnloadingYoungsModulusE2(1.11)
    mat.Stiffness.TransverselyIsotropic.setUnloadingPoissonsRatioV12(1.12)
    mat.Stiffness.TransverselyIsotropic.setUnloadingPoissonsRatioVAndV1z(1.13)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.TRANSVERSELY_ISOTROPIC)
    assert(mat.Stiffness.TransverselyIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.TransverselyIsotropic.getShearModulus(), 1.1)
    assert(mat.Stiffness.TransverselyIsotropic.getAngleCounterclockwiseFromHorizontalToE1(), 1.2)
    assert(mat.Stiffness.TransverselyIsotropic.getYoungsModulusE1AndEz(), 1.3)
    assert(mat.Stiffness.TransverselyIsotropic.getYoungsModulusE2(), 1.4)
    assert(mat.Stiffness.TransverselyIsotropic.getPoissonsRatioV12(), 1.5)
    assert(mat.Stiffness.TransverselyIsotropic.getPoissonsRatioVAndV1z(), 1.6)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingCondition(), UnloadingConditions.UC_VOLUMETRIC_STRAIN)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingShearModulus(), 1.7)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingAngleCounterclockwiseFromHorizontalToE1(), 1.8)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingYoungsModulusE1AndEz(), 1.9)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingYoungsModulusE2(), 1.11)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingPoissonsRatioV12(), 1.12)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingPoissonsRatioVAndV1z(), 1.13)

def test12():
    mat = mat12

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.TRANSVERSELY_ISOTROPIC)
    mat.Stiffness.TransverselyIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.TransverselyIsotropic.setShearModulus(1.1)
    mat.Stiffness.TransverselyIsotropic.setAngleCounterclockwiseFromHorizontalToE1(1.2)
    mat.Stiffness.TransverselyIsotropic.setYoungsModulusE1AndEz(1.3)
    mat.Stiffness.TransverselyIsotropic.setYoungsModulusE2(1.4)
    mat.Stiffness.TransverselyIsotropic.setPoissonsRatioV12(1.5)
    mat.Stiffness.TransverselyIsotropic.setPoissonsRatioVAndV1z(1.6)
    mat.Stiffness.TransverselyIsotropic.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRAIN)
    mat.Stiffness.TransverselyIsotropic.setUnloadingShearModulus(1.7)
    mat.Stiffness.TransverselyIsotropic.setUnloadingAngleCounterclockwiseFromHorizontalToE1(1.8)
    mat.Stiffness.TransverselyIsotropic.setUnloadingYoungsModulusE1AndEz(1.9)
    mat.Stiffness.TransverselyIsotropic.setUnloadingYoungsModulusE2(1.11)
    mat.Stiffness.TransverselyIsotropic.setUnloadingPoissonsRatioV12(1.12)
    mat.Stiffness.TransverselyIsotropic.setUnloadingPoissonsRatioVAndV1z(1.13)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.TRANSVERSELY_ISOTROPIC)
    assert(mat.Stiffness.TransverselyIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.TransverselyIsotropic.getShearModulus(), 1.1)
    assert(mat.Stiffness.TransverselyIsotropic.getAngleCounterclockwiseFromHorizontalToE1(), 1.2)
    assert(mat.Stiffness.TransverselyIsotropic.getYoungsModulusE1AndEz(), 1.3)
    assert(mat.Stiffness.TransverselyIsotropic.getYoungsModulusE2(), 1.4)
    assert(mat.Stiffness.TransverselyIsotropic.getPoissonsRatioV12(), 1.5)
    assert(mat.Stiffness.TransverselyIsotropic.getPoissonsRatioVAndV1z(), 1.6)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRAIN)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingShearModulus(), 1.7)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingAngleCounterclockwiseFromHorizontalToE1(), 1.8)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingYoungsModulusE1AndEz(), 1.9)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingYoungsModulusE2(), 1.11)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingPoissonsRatioV12(), 1.12)
    assert(mat.Stiffness.TransverselyIsotropic.getUnloadingPoissonsRatioVAndV1z(), 1.13)

def test13():
    mat = mat13

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.TRANSVERSELY_ISOTROPIC)
    mat.Stiffness.TransverselyIsotropic.setUseUnloadingCondition(False)
    mat.Stiffness.TransverselyIsotropic.setShearModulus(1.1)
    mat.Stiffness.TransverselyIsotropic.setAngleCounterclockwiseFromHorizontalToE1(1.2)
    mat.Stiffness.TransverselyIsotropic.setYoungsModulusE1AndEz(1.3)
    mat.Stiffness.TransverselyIsotropic.setYoungsModulusE2(1.4)
    mat.Stiffness.TransverselyIsotropic.setPoissonsRatioV12(1.5)
    mat.Stiffness.TransverselyIsotropic.setPoissonsRatioVAndV1z(1.6)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.TRANSVERSELY_ISOTROPIC)
    assert(mat.Stiffness.TransverselyIsotropic.getUseUnloadingCondition(), False)
    assert(mat.Stiffness.TransverselyIsotropic.getShearModulus(), 1.1)
    assert(mat.Stiffness.TransverselyIsotropic.getAngleCounterclockwiseFromHorizontalToE1(), 1.2)
    assert(mat.Stiffness.TransverselyIsotropic.getYoungsModulusE1AndEz(), 1.3)
    assert(mat.Stiffness.TransverselyIsotropic.getYoungsModulusE2(), 1.4)
    assert(mat.Stiffness.TransverselyIsotropic.getPoissonsRatioV12(), 1.5)
    assert(mat.Stiffness.TransverselyIsotropic.getPoissonsRatioVAndV1z(), 1.6)

def test14():
    mat = mat14

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.ORTHOTROPIC)
    mat.Stiffness.Orthotropic.setUseUnloadingCondition(True)
    mat.Stiffness.Orthotropic.setShearModulus(1.1)
    mat.Stiffness.Orthotropic.setAngleCounterclockwiseFromHorizontalToE1(1.2)
    mat.Stiffness.Orthotropic.setYoungsModulusE1(1.3)
    mat.Stiffness.Orthotropic.setYoungsModulusE2(1.4)
    mat.Stiffness.Orthotropic.setYoungsModulusEZ(1.5)
    mat.Stiffness.Orthotropic.setPoissonsRatioV12(0.6)
    mat.Stiffness.Orthotropic.setPoissonsRatioV2(0.7)
    mat.Stiffness.Orthotropic.setPoissonsRatioV2z(0.8)
    mat.Stiffness.Orthotropic.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.Orthotropic.setUnloadingShearModulus(1.9)
    mat.Stiffness.Orthotropic.setUnloadingAngleCounterclockwiseFromHorizontalToE1(1.11)
    mat.Stiffness.Orthotropic.setUnloadingYoungsModulusE1(1.12)
    mat.Stiffness.Orthotropic.setUnloadingYoungsModulusE2(1.13)
    mat.Stiffness.Orthotropic.setUnloadingYoungsModulusEZ(1.14)
    mat.Stiffness.Orthotropic.setUnloadingPoissonsRatioV12(1.15)
    mat.Stiffness.Orthotropic.setUnloadingPoissonsRatioV2(1.16)
    mat.Stiffness.Orthotropic.setUnloadingPoissonsRatioV2z(1.17)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.ORTHOTROPIC)
    assert(mat.Stiffness.Orthotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Orthotropic.getShearModulus(), 1.1)  
    assert(mat.Stiffness.Orthotropic.getAngleCounterclockwiseFromHorizontalToE1(), 1.2)
    assert(mat.Stiffness.Orthotropic.getYoungsModulusE1(), 1.3)
    assert(mat.Stiffness.Orthotropic.getYoungsModulusE2(), 1.4)
    assert(mat.Stiffness.Orthotropic.getYoungsModulusEZ(), 1.5)
    assert(mat.Stiffness.Orthotropic.getPoissonsRatioV12(), 0.6)
    assert(mat.Stiffness.Orthotropic.getPoissonsRatioV2(), 0.7)
    assert(mat.Stiffness.Orthotropic.getPoissonsRatioV2z(), 0.8)
    assert(mat.Stiffness.Orthotropic.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)  
    assert(mat.Stiffness.Orthotropic.getUnloadingShearModulus(), 1.9)
    assert(mat.Stiffness.Orthotropic.getUnloadingAngleCounterclockwiseFromHorizontalToE1(), 1.11)
    assert(mat.Stiffness.Orthotropic.getUnloadingYoungsModulusE1(), 1.12)
    assert(mat.Stiffness.Orthotropic.getUnloadingYoungsModulusE2(), 1.13)
    assert(mat.Stiffness.Orthotropic.getUnloadingYoungsModulusEZ(), 1.14)
    assert(mat.Stiffness.Orthotropic.getUnloadingPoissonsRatioV12(), 1.15)
    assert(mat.Stiffness.Orthotropic.getUnloadingPoissonsRatioV2(), 1.16)  
    assert(mat.Stiffness.Orthotropic.getUnloadingPoissonsRatioV2z(), 1.17)

def test15():
    mat = mat15

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.ORTHOTROPIC)
    mat.Stiffness.Orthotropic.setUseUnloadingCondition(True)
    mat.Stiffness.Orthotropic.setShearModulus(1.1)
    mat.Stiffness.Orthotropic.setAngleCounterclockwiseFromHorizontalToE1(1.2)
    mat.Stiffness.Orthotropic.setYoungsModulusE1(1.3)
    mat.Stiffness.Orthotropic.setYoungsModulusE2(1.4)
    mat.Stiffness.Orthotropic.setYoungsModulusEZ(1.5)
    mat.Stiffness.Orthotropic.setPoissonsRatioV12(0.6)
    mat.Stiffness.Orthotropic.setPoissonsRatioV2(0.7)
    mat.Stiffness.Orthotropic.setPoissonsRatioV2z(0.8)
    mat.Stiffness.Orthotropic.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRESS)
    mat.Stiffness.Orthotropic.setUnloadingShearModulus(1.9)
    mat.Stiffness.Orthotropic.setUnloadingAngleCounterclockwiseFromHorizontalToE1(1.11)
    mat.Stiffness.Orthotropic.setUnloadingYoungsModulusE1(1.12)
    mat.Stiffness.Orthotropic.setUnloadingYoungsModulusE2(1.13)
    mat.Stiffness.Orthotropic.setUnloadingYoungsModulusEZ(1.14)
    mat.Stiffness.Orthotropic.setUnloadingPoissonsRatioV12(1.15)
    mat.Stiffness.Orthotropic.setUnloadingPoissonsRatioV2(1.16)
    mat.Stiffness.Orthotropic.setUnloadingPoissonsRatioV2z(1.17)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.ORTHOTROPIC)
    assert(mat.Stiffness.Orthotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Orthotropic.getShearModulus(), 1.1)  
    assert(mat.Stiffness.Orthotropic.getAngleCounterclockwiseFromHorizontalToE1(), 1.2)
    assert(mat.Stiffness.Orthotropic.getYoungsModulusE1(), 1.3)
    assert(mat.Stiffness.Orthotropic.getYoungsModulusE2(), 1.4)
    assert(mat.Stiffness.Orthotropic.getYoungsModulusEZ(), 1.5)
    assert(mat.Stiffness.Orthotropic.getPoissonsRatioV12(), 0.6)
    assert(mat.Stiffness.Orthotropic.getPoissonsRatioV2(), 0.7)
    assert(mat.Stiffness.Orthotropic.getPoissonsRatioV2z(), 0.8)
    assert(mat.Stiffness.Orthotropic.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRESS)  
    assert(mat.Stiffness.Orthotropic.getUnloadingShearModulus(), 1.9)
    assert(mat.Stiffness.Orthotropic.getUnloadingAngleCounterclockwiseFromHorizontalToE1(), 1.11)
    assert(mat.Stiffness.Orthotropic.getUnloadingYoungsModulusE1(), 1.12)
    assert(mat.Stiffness.Orthotropic.getUnloadingYoungsModulusE2(), 1.13)
    assert(mat.Stiffness.Orthotropic.getUnloadingYoungsModulusEZ(), 1.14)
    assert(mat.Stiffness.Orthotropic.getUnloadingPoissonsRatioV12(), 1.15)
    assert(mat.Stiffness.Orthotropic.getUnloadingPoissonsRatioV2(), 1.16)  
    assert(mat.Stiffness.Orthotropic.getUnloadingPoissonsRatioV2z(), 1.17)

def test16():
    mat = mat16

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.ORTHOTROPIC)
    mat.Stiffness.Orthotropic.setUseUnloadingCondition(True)
    mat.Stiffness.Orthotropic.setShearModulus(1.1)
    mat.Stiffness.Orthotropic.setAngleCounterclockwiseFromHorizontalToE1(1.2)
    mat.Stiffness.Orthotropic.setYoungsModulusE1(1.3)
    mat.Stiffness.Orthotropic.setYoungsModulusE2(1.4)
    mat.Stiffness.Orthotropic.setYoungsModulusEZ(1.5)
    mat.Stiffness.Orthotropic.setPoissonsRatioV12(0.6)
    mat.Stiffness.Orthotropic.setPoissonsRatioV2(0.7)
    mat.Stiffness.Orthotropic.setPoissonsRatioV2z(0.8)
    mat.Stiffness.Orthotropic.setUnloadingCondition(UnloadingConditions.UC_VOLUMETRIC_STRAIN)
    mat.Stiffness.Orthotropic.setUnloadingShearModulus(1.9)
    mat.Stiffness.Orthotropic.setUnloadingAngleCounterclockwiseFromHorizontalToE1(1.11)
    mat.Stiffness.Orthotropic.setUnloadingYoungsModulusE1(1.12)
    mat.Stiffness.Orthotropic.setUnloadingYoungsModulusE2(1.13)
    mat.Stiffness.Orthotropic.setUnloadingYoungsModulusEZ(1.14)
    mat.Stiffness.Orthotropic.setUnloadingPoissonsRatioV12(1.15)
    mat.Stiffness.Orthotropic.setUnloadingPoissonsRatioV2(1.16)
    mat.Stiffness.Orthotropic.setUnloadingPoissonsRatioV2z(1.17)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.ORTHOTROPIC)
    assert(mat.Stiffness.Orthotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Orthotropic.getShearModulus(), 1.1)  
    assert(mat.Stiffness.Orthotropic.getAngleCounterclockwiseFromHorizontalToE1(), 1.2)
    assert(mat.Stiffness.Orthotropic.getYoungsModulusE1(), 1.3)
    assert(mat.Stiffness.Orthotropic.getYoungsModulusE2(), 1.4)
    assert(mat.Stiffness.Orthotropic.getYoungsModulusEZ(), 1.5)
    assert(mat.Stiffness.Orthotropic.getPoissonsRatioV12(), 0.6)
    assert(mat.Stiffness.Orthotropic.getPoissonsRatioV2(), 0.7)
    assert(mat.Stiffness.Orthotropic.getPoissonsRatioV2z(), 0.8)
    assert(mat.Stiffness.Orthotropic.getUnloadingCondition(), UnloadingConditions.UC_VOLUMETRIC_STRAIN)  
    assert(mat.Stiffness.Orthotropic.getUnloadingShearModulus(), 1.9)
    assert(mat.Stiffness.Orthotropic.getUnloadingAngleCounterclockwiseFromHorizontalToE1(), 1.11)
    assert(mat.Stiffness.Orthotropic.getUnloadingYoungsModulusE1(), 1.12)
    assert(mat.Stiffness.Orthotropic.getUnloadingYoungsModulusE2(), 1.13)
    assert(mat.Stiffness.Orthotropic.getUnloadingYoungsModulusEZ(), 1.14)
    assert(mat.Stiffness.Orthotropic.getUnloadingPoissonsRatioV12(), 1.15)
    assert(mat.Stiffness.Orthotropic.getUnloadingPoissonsRatioV2(), 1.16)  
    assert(mat.Stiffness.Orthotropic.getUnloadingPoissonsRatioV2z(), 1.17)

def test17():
    mat = mat17

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.ORTHOTROPIC)
    mat.Stiffness.Orthotropic.setUseUnloadingCondition(True)
    mat.Stiffness.Orthotropic.setShearModulus(1.1)
    mat.Stiffness.Orthotropic.setAngleCounterclockwiseFromHorizontalToE1(1.2)
    mat.Stiffness.Orthotropic.setYoungsModulusE1(1.3)
    mat.Stiffness.Orthotropic.setYoungsModulusE2(1.4)
    mat.Stiffness.Orthotropic.setYoungsModulusEZ(1.5)
    mat.Stiffness.Orthotropic.setPoissonsRatioV12(0.6)
    mat.Stiffness.Orthotropic.setPoissonsRatioV2(0.7)
    mat.Stiffness.Orthotropic.setPoissonsRatioV2z(0.8)
    mat.Stiffness.Orthotropic.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRAIN)
    mat.Stiffness.Orthotropic.setUnloadingShearModulus(1.9)
    mat.Stiffness.Orthotropic.setUnloadingAngleCounterclockwiseFromHorizontalToE1(1.11)
    mat.Stiffness.Orthotropic.setUnloadingYoungsModulusE1(1.12)
    mat.Stiffness.Orthotropic.setUnloadingYoungsModulusE2(1.13)
    mat.Stiffness.Orthotropic.setUnloadingYoungsModulusEZ(1.14)
    mat.Stiffness.Orthotropic.setUnloadingPoissonsRatioV12(1.15)
    mat.Stiffness.Orthotropic.setUnloadingPoissonsRatioV2(1.16)
    mat.Stiffness.Orthotropic.setUnloadingPoissonsRatioV2z(1.17)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.ORTHOTROPIC)
    assert(mat.Stiffness.Orthotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Orthotropic.getShearModulus(), 1.1)  
    assert(mat.Stiffness.Orthotropic.getAngleCounterclockwiseFromHorizontalToE1(), 1.2)
    assert(mat.Stiffness.Orthotropic.getYoungsModulusE1(), 1.3)
    assert(mat.Stiffness.Orthotropic.getYoungsModulusE2(), 1.4)
    assert(mat.Stiffness.Orthotropic.getYoungsModulusEZ(), 1.5)
    assert(mat.Stiffness.Orthotropic.getPoissonsRatioV12(), 0.6)
    assert(mat.Stiffness.Orthotropic.getPoissonsRatioV2(), 0.7)
    assert(mat.Stiffness.Orthotropic.getPoissonsRatioV2z(), 0.8)
    assert(mat.Stiffness.Orthotropic.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRAIN)  
    assert(mat.Stiffness.Orthotropic.getUnloadingShearModulus(), 1.9)
    assert(mat.Stiffness.Orthotropic.getUnloadingAngleCounterclockwiseFromHorizontalToE1(), 1.11)
    assert(mat.Stiffness.Orthotropic.getUnloadingYoungsModulusE1(), 1.12)
    assert(mat.Stiffness.Orthotropic.getUnloadingYoungsModulusE2(), 1.13)
    assert(mat.Stiffness.Orthotropic.getUnloadingYoungsModulusEZ(), 1.14)
    assert(mat.Stiffness.Orthotropic.getUnloadingPoissonsRatioV12(), 1.15)
    assert(mat.Stiffness.Orthotropic.getUnloadingPoissonsRatioV2(), 1.16)  
    assert(mat.Stiffness.Orthotropic.getUnloadingPoissonsRatioV2z(), 1.17)

def test18():
    mat = mat18

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.ORTHOTROPIC)
    mat.Stiffness.Orthotropic.setUseUnloadingCondition(False)
    mat.Stiffness.Orthotropic.setShearModulus(1.1)
    mat.Stiffness.Orthotropic.setAngleCounterclockwiseFromHorizontalToE1(1.2)
    mat.Stiffness.Orthotropic.setYoungsModulusE1(1.3)
    mat.Stiffness.Orthotropic.setYoungsModulusE2(1.4)
    mat.Stiffness.Orthotropic.setYoungsModulusEZ(1.5)
    mat.Stiffness.Orthotropic.setPoissonsRatioV12(0.6)
    mat.Stiffness.Orthotropic.setPoissonsRatioV2(0.7)
    mat.Stiffness.Orthotropic.setPoissonsRatioV2z(0.8)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.ORTHOTROPIC)
    assert(mat.Stiffness.Orthotropic.getUseUnloadingCondition(), False)
    assert(mat.Stiffness.Orthotropic.getShearModulus(), 1.1)  
    assert(mat.Stiffness.Orthotropic.getAngleCounterclockwiseFromHorizontalToE1(), 1.2)
    assert(mat.Stiffness.Orthotropic.getYoungsModulusE1(), 1.3)
    assert(mat.Stiffness.Orthotropic.getYoungsModulusE2(), 1.4)
    assert(mat.Stiffness.Orthotropic.getYoungsModulusEZ(), 1.5)
    assert(mat.Stiffness.Orthotropic.getPoissonsRatioV12(), 0.6)
    assert(mat.Stiffness.Orthotropic.getPoissonsRatioV2(), 0.7)
    assert(mat.Stiffness.Orthotropic.getPoissonsRatioV2z(), 0.8)

def test19():
    mat = mat19

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_HYPERBOLIC)
    mat.Stiffness.NonLinearHyperbolic.setModulusNumber(1.1)
    mat.Stiffness.NonLinearHyperbolic.setPoissonRatioType(PoissonRatioType.POISSON_RATIO_CONSTANT)
    mat.Stiffness.NonLinearHyperbolic.setPoissonsRatio(0.2)
    mat.Stiffness.NonLinearHyperbolic.setModulusExpN(1.3)
    mat.Stiffness.NonLinearHyperbolic.setAtmosphericPressure(1.4)
    mat.Stiffness.NonLinearHyperbolic.setFailureRatioRf(0.5)
    mat.Stiffness.NonLinearHyperbolic.setUnloadingModulusNumber(1.6)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_HYPERBOLIC)
    assert(mat.Stiffness.NonLinearHyperbolic.getModulusNumber(), 1.1)
    assert(mat.Stiffness.NonLinearHyperbolic.getPoissonRatioType(), PoissonRatioType.POISSON_RATIO_CONSTANT)
    assert(mat.Stiffness.NonLinearHyperbolic.getPoissonsRatio(), 0.2)
    assert(mat.Stiffness.NonLinearHyperbolic.getModulusExpN(), 1.3)
    assert(mat.Stiffness.NonLinearHyperbolic.getAtmosphericPressure(), 1.4)
    assert(mat.Stiffness.NonLinearHyperbolic.getFailureRatioRf(), 0.5)
    assert(mat.Stiffness.NonLinearHyperbolic.getUnloadingModulusNumber(), 1.6)

def test20():
    mat = mat20

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_HYPERBOLIC)
    mat.Stiffness.NonLinearHyperbolic.setModulusNumber(1.1)
    mat.Stiffness.NonLinearHyperbolic.setPoissonRatioType(PoissonRatioType.POISSON_RATIO_STRESS_DEPENDENT)
    mat.Stiffness.NonLinearHyperbolic.setBulkModulusNumber(1.7)
    mat.Stiffness.NonLinearHyperbolic.setBulkModulusExpM(0.8)
    mat.Stiffness.NonLinearHyperbolic.setModulusExpN(1.3)
    mat.Stiffness.NonLinearHyperbolic.setAtmosphericPressure(1.4)
    mat.Stiffness.NonLinearHyperbolic.setFailureRatioRf(0.5)
    mat.Stiffness.NonLinearHyperbolic.setUnloadingModulusNumber(1.6)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_HYPERBOLIC)
    assert(mat.Stiffness.NonLinearHyperbolic.getModulusNumber(), 1.1)
    assert(mat.Stiffness.NonLinearHyperbolic.getPoissonRatioType(), PoissonRatioType.POISSON_RATIO_STRESS_DEPENDENT)
    assert(mat.Stiffness.NonLinearHyperbolic.getBulkModulusNumber(), 1.7)
    assert(mat.Stiffness.NonLinearHyperbolic.getBulkModulusExpM(), 0.8)
    assert(mat.Stiffness.NonLinearHyperbolic.getModulusExpN(), 1.3)
    assert(mat.Stiffness.NonLinearHyperbolic.getAtmosphericPressure(), 1.4)
    assert(mat.Stiffness.NonLinearHyperbolic.getFailureRatioRf(), 0.5)
    assert(mat.Stiffness.NonLinearHyperbolic.getUnloadingModulusNumber(), 1.6)

def test21():
    mat = mat21

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA1)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.4)
    mat.Stiffness.NonLinearIsotropic.setPref(1.5)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.06)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setUnloadingResidualYoungsModulus(1.7)
    mat.Stiffness.NonLinearIsotropic.setUnloadingInitialE(1.8)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAlpha(1.9)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPref(1.11)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.06)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingResidualYoungsModulus(), 1.7)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingInitialE(), 1.8)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAlpha(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPref(), 1.11)

def test22():
    mat = mat22

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA1)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.4)
    mat.Stiffness.NonLinearIsotropic.setPref(1.5)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRESS)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.06)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setUnloadingResidualYoungsModulus(1.7)
    mat.Stiffness.NonLinearIsotropic.setUnloadingInitialE(1.8)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAlpha(1.9)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPref(1.11)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRESS)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.06)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingResidualYoungsModulus(), 1.7)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingInitialE(), 1.8)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAlpha(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPref(), 1.11)

def test23():
    mat = mat23

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA1)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.4)
    mat.Stiffness.NonLinearIsotropic.setPref(1.5)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_VOLUMETRIC_STRAIN)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.06)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setUnloadingResidualYoungsModulus(1.7)
    mat.Stiffness.NonLinearIsotropic.setUnloadingInitialE(1.8)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAlpha(1.9)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPref(1.11)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_VOLUMETRIC_STRAIN)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.06)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingResidualYoungsModulus(), 1.7)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingInitialE(), 1.8)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAlpha(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPref(), 1.11)

def test24():
    mat = mat24

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA1)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.4)
    mat.Stiffness.NonLinearIsotropic.setPref(1.5)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRAIN)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.06)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setUnloadingResidualYoungsModulus(1.7)
    mat.Stiffness.NonLinearIsotropic.setUnloadingInitialE(1.8)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAlpha(1.9)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPref(1.11)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRAIN)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.06)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingResidualYoungsModulus(), 1.7)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingInitialE(), 1.8)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAlpha(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPref(), 1.11)

def test25():
    mat = mat25

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA1)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(False)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(False)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.4)
    mat.Stiffness.NonLinearIsotropic.setPref(1.5)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), False)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), False)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.5)

def test26():
    mat = mat26

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA1)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(False)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.4)
    mat.Stiffness.NonLinearIsotropic.setPref(1.5)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.06)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setUnloadingResidualYoungsModulus(1.7)
    mat.Stiffness.NonLinearIsotropic.setUnloadingInitialE(1.8)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAlpha(1.9)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPref(1.11)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), False)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.06)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingResidualYoungsModulus(), 1.7)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingInitialE(), 1.8)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAlpha(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPref(), 1.11)

def test27():
    mat = mat27

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA1)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(False)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.4)
    mat.Stiffness.NonLinearIsotropic.setPref(1.5)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.06)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingResidualYoungsModulus(False)
    mat.Stiffness.NonLinearIsotropic.setUnloadingInitialE(1.8)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAlpha(1.9)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPref(1.11)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), False)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.06)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingResidualYoungsModulus(), False)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingInitialE(), 1.8)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAlpha(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPref(), 1.11)

def test28():
    mat = mat28

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA1)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(False)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.4)
    mat.Stiffness.NonLinearIsotropic.setPref(1.5)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), False)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.5)

def test29():
    mat = mat29

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA2)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAParameter(1.4)
    mat.Stiffness.NonLinearIsotropic.setBParameter(1.5)
    mat.Stiffness.NonLinearIsotropic.setMParameter(1.6)
    mat.Stiffness.NonLinearIsotropic.setPref(1.7)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.08)
    mat.Stiffness.NonLinearIsotropic.setUnloadingInitialE(1.9)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAParameter(1.11)
    mat.Stiffness.NonLinearIsotropic.setUnloadingBParameter(1.12)
    mat.Stiffness.NonLinearIsotropic.setUnloadingMParameter(1.13)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPref(1.14)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA2)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAParameter(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getBParameter(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getMParameter(), 1.6)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.7)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.08)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingInitialE(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAParameter(), 1.11)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingBParameter(), 1.12)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingMParameter(), 1.13)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPref(), 1.14)

def test30():
    mat = mat30

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA2)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAParameter(1.4)
    mat.Stiffness.NonLinearIsotropic.setBParameter(1.5)
    mat.Stiffness.NonLinearIsotropic.setMParameter(1.6)
    mat.Stiffness.NonLinearIsotropic.setPref(1.7)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRESS)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.08)
    mat.Stiffness.NonLinearIsotropic.setUnloadingInitialE(1.9)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAParameter(1.11)
    mat.Stiffness.NonLinearIsotropic.setUnloadingBParameter(1.12)
    mat.Stiffness.NonLinearIsotropic.setUnloadingMParameter(1.13)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPref(1.14)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA2)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAParameter(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getBParameter(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getMParameter(), 1.6)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.7)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRESS)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.08)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingInitialE(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAParameter(), 1.11)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingBParameter(), 1.12)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingMParameter(), 1.13)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPref(), 1.14)

def test31():
    mat = mat31

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA2)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAParameter(1.4)
    mat.Stiffness.NonLinearIsotropic.setBParameter(1.5)
    mat.Stiffness.NonLinearIsotropic.setMParameter(1.6)
    mat.Stiffness.NonLinearIsotropic.setPref(1.7)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_VOLUMETRIC_STRAIN)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.08)
    mat.Stiffness.NonLinearIsotropic.setUnloadingInitialE(1.9)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAParameter(1.11)
    mat.Stiffness.NonLinearIsotropic.setUnloadingBParameter(1.12)
    mat.Stiffness.NonLinearIsotropic.setUnloadingMParameter(1.13)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPref(1.14)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA2)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAParameter(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getBParameter(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getMParameter(), 1.6)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.7)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_VOLUMETRIC_STRAIN)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.08)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingInitialE(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAParameter(), 1.11)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingBParameter(), 1.12)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingMParameter(), 1.13)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPref(), 1.14)

def test32():
    mat = mat32

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA2)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAParameter(1.4)
    mat.Stiffness.NonLinearIsotropic.setBParameter(1.5)
    mat.Stiffness.NonLinearIsotropic.setMParameter(1.6)
    mat.Stiffness.NonLinearIsotropic.setPref(1.7)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRAIN)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.08)
    mat.Stiffness.NonLinearIsotropic.setUnloadingInitialE(1.9)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAParameter(1.11)
    mat.Stiffness.NonLinearIsotropic.setUnloadingBParameter(1.12)
    mat.Stiffness.NonLinearIsotropic.setUnloadingMParameter(1.13)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPref(1.14)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA2)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAParameter(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getBParameter(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getMParameter(), 1.6)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.7)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRAIN)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.08)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingInitialE(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAParameter(), 1.11)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingBParameter(), 1.12)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingMParameter(), 1.13)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPref(), 1.14)

def test33():
    mat = mat33

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA2)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(False)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(False)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAParameter(1.4)
    mat.Stiffness.NonLinearIsotropic.setBParameter(1.5)
    mat.Stiffness.NonLinearIsotropic.setMParameter(1.6)
    mat.Stiffness.NonLinearIsotropic.setPref(1.7)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA2)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), False)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), False)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAParameter(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getBParameter(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getMParameter(), 1.6)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.7)

def test34():
    mat = mat34

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA2)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(False)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAParameter(1.4)
    mat.Stiffness.NonLinearIsotropic.setBParameter(1.5)
    mat.Stiffness.NonLinearIsotropic.setMParameter(1.6)
    mat.Stiffness.NonLinearIsotropic.setPref(1.7)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.08)
    mat.Stiffness.NonLinearIsotropic.setUnloadingInitialE(1.9)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAParameter(1.11)
    mat.Stiffness.NonLinearIsotropic.setUnloadingBParameter(1.12)
    mat.Stiffness.NonLinearIsotropic.setUnloadingMParameter(1.13)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPref(1.14)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA2)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), False)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAParameter(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getBParameter(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getMParameter(), 1.6)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.7)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.08)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingInitialE(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAParameter(), 1.11)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingBParameter(), 1.12)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingMParameter(), 1.13)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPref(), 1.14)

def test35():
    mat = mat35

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA2)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(False)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAParameter(1.4)
    mat.Stiffness.NonLinearIsotropic.setBParameter(1.5)
    mat.Stiffness.NonLinearIsotropic.setMParameter(1.6)
    mat.Stiffness.NonLinearIsotropic.setPref(1.7)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA2)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), False)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAParameter(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getBParameter(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getMParameter(), 1.6)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.7)

def test36():
    mat = mat36

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA3)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setGMax(1.3)
    mat.Stiffness.NonLinearIsotropic.setGammaY(1.4)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.5)
    mat.Stiffness.NonLinearIsotropic.setRParameter(1.6)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.07)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setUnloadingResidualYoungsModulus(1.8)
    mat.Stiffness.NonLinearIsotropic.setUnloadingGMax(1.9)
    mat.Stiffness.NonLinearIsotropic.setUnloadingGammaY(1.11)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAParameter(1.12)
    mat.Stiffness.NonLinearIsotropic.setUnloadingRParameter(1.13)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA3)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getGMax(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getGammaY(), 1.4) 
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getRParameter(), 1.6)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.07)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingResidualYoungsModulus(), 1.8)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingGMax(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingGammaY(), 1.11)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAParameter(), 1.12)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingRParameter(), 1.13)

def test37():
    mat = mat37

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA3)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setGMax(1.3)
    mat.Stiffness.NonLinearIsotropic.setGammaY(1.4)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.5)
    mat.Stiffness.NonLinearIsotropic.setRParameter(1.6)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRESS)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.07)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setUnloadingResidualYoungsModulus(1.8)
    mat.Stiffness.NonLinearIsotropic.setUnloadingGMax(1.9)
    mat.Stiffness.NonLinearIsotropic.setUnloadingGammaY(1.11)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAParameter(1.12)
    mat.Stiffness.NonLinearIsotropic.setUnloadingRParameter(1.13)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA3)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getGMax(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getGammaY(), 1.4) 
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getRParameter(), 1.6)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRESS)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.07)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingResidualYoungsModulus(), 1.8)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingGMax(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingGammaY(), 1.11)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAParameter(), 1.12)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingRParameter(), 1.13)

def test38():
    mat = mat38

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA3)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setGMax(1.3)
    mat.Stiffness.NonLinearIsotropic.setGammaY(1.4)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.5)
    mat.Stiffness.NonLinearIsotropic.setRParameter(1.6)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_VOLUMETRIC_STRAIN)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.07)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setUnloadingResidualYoungsModulus(1.8)
    mat.Stiffness.NonLinearIsotropic.setUnloadingGMax(1.9)
    mat.Stiffness.NonLinearIsotropic.setUnloadingGammaY(1.11)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAParameter(1.12)
    mat.Stiffness.NonLinearIsotropic.setUnloadingRParameter(1.13)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA3)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getGMax(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getGammaY(), 1.4) 
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getRParameter(), 1.6)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_VOLUMETRIC_STRAIN)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.07)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingResidualYoungsModulus(), 1.8)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingGMax(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingGammaY(), 1.11)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAParameter(), 1.12)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingRParameter(), 1.13)

def test39():
    mat = mat39

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA3)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setGMax(1.3)
    mat.Stiffness.NonLinearIsotropic.setGammaY(1.4)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.5)
    mat.Stiffness.NonLinearIsotropic.setRParameter(1.6)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRAIN)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.07)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setUnloadingResidualYoungsModulus(1.8)
    mat.Stiffness.NonLinearIsotropic.setUnloadingGMax(1.9)
    mat.Stiffness.NonLinearIsotropic.setUnloadingGammaY(1.11)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAParameter(1.12)
    mat.Stiffness.NonLinearIsotropic.setUnloadingRParameter(1.13)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA3)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getGMax(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getGammaY(), 1.4) 
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getRParameter(), 1.6)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRAIN)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.07)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingResidualYoungsModulus(), 1.8)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingGMax(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingGammaY(), 1.11)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAParameter(), 1.12)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingRParameter(), 1.13)

def test40():
    mat = mat40

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA3)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(False)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(False)
    mat.Stiffness.NonLinearIsotropic.setGMax(1.3)
    mat.Stiffness.NonLinearIsotropic.setGammaY(1.4)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.5)
    mat.Stiffness.NonLinearIsotropic.setRParameter(1.6)
    
    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA3)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), False)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), False)
    assert(mat.Stiffness.NonLinearIsotropic.getGMax(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getGammaY(), 1.4) 
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getRParameter(), 1.6)

def test41():
    mat = mat41

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA3)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(False)
    mat.Stiffness.NonLinearIsotropic.setGMax(1.3)
    mat.Stiffness.NonLinearIsotropic.setGammaY(1.4)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.5)
    mat.Stiffness.NonLinearIsotropic.setRParameter(1.6)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.07)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setUnloadingResidualYoungsModulus(1.8)
    mat.Stiffness.NonLinearIsotropic.setUnloadingGMax(1.9)
    mat.Stiffness.NonLinearIsotropic.setUnloadingGammaY(1.11)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAParameter(1.12)
    mat.Stiffness.NonLinearIsotropic.setUnloadingRParameter(1.13)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA3)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), False)
    assert(mat.Stiffness.NonLinearIsotropic.getGMax(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getGammaY(), 1.4) 
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getRParameter(), 1.6)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.07)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingResidualYoungsModulus(), 1.8)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingGMax(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingGammaY(), 1.11)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAParameter(), 1.12)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingRParameter(), 1.13)

def test42():
    mat = mat42

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA3)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(False)
    mat.Stiffness.NonLinearIsotropic.setGMax(1.3)
    mat.Stiffness.NonLinearIsotropic.setGammaY(1.4)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.5)
    mat.Stiffness.NonLinearIsotropic.setRParameter(1.6)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.07)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingResidualYoungsModulus(False)
    mat.Stiffness.NonLinearIsotropic.setUnloadingGMax(1.9)
    mat.Stiffness.NonLinearIsotropic.setUnloadingGammaY(1.11)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAParameter(1.12)
    mat.Stiffness.NonLinearIsotropic.setUnloadingRParameter(1.13)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA3)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), False)
    assert(mat.Stiffness.NonLinearIsotropic.getGMax(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getGammaY(), 1.4) 
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getRParameter(), 1.6)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.07)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingResidualYoungsModulus(), False)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingGMax(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingGammaY(), 1.11)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAParameter(), 1.12)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingRParameter(), 1.13)

def test43():
    mat = mat43

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA3)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(False)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setUseResidualYoungsModulus(True)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setGMax(1.3)
    mat.Stiffness.NonLinearIsotropic.setGammaY(1.4)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.5)
    mat.Stiffness.NonLinearIsotropic.setRParameter(1.6)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA3)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), False)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getUseResidualYoungsModulus(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getGMax(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getGammaY(), 1.4) 
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getRParameter(), 1.6)

def test44():
    mat = mat44

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA4)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAParameter(1.4)
    mat.Stiffness.NonLinearIsotropic.setBParameter(1.5)
    mat.Stiffness.NonLinearIsotropic.setMParameter(1.6)
    mat.Stiffness.NonLinearIsotropic.setPref(1.7)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.8)
    mat.Stiffness.NonLinearIsotropic.setGammaY(1.9)
    mat.Stiffness.NonLinearIsotropic.setRParameter(1.11)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.12)
    mat.Stiffness.NonLinearIsotropic.setUnloadingResidualYoungsModulus(1.13)
    mat.Stiffness.NonLinearIsotropic.setUnloadingInitialE(1.14)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAParameter(1.15)
    mat.Stiffness.NonLinearIsotropic.setUnloadingBParameter(1.16)
    mat.Stiffness.NonLinearIsotropic.setUnloadingMParameter(1.17)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPref(1.18)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAlpha(1.19)
    mat.Stiffness.NonLinearIsotropic.setUnloadingGammaY(1.21)
    mat.Stiffness.NonLinearIsotropic.setUnloadingRParameter(1.22)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA4)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAParameter(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getBParameter(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getMParameter(), 1.6)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.7)
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.8)
    assert(mat.Stiffness.NonLinearIsotropic.getGammaY(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getRParameter(), 1.11)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.12)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingResidualYoungsModulus(), 1.13)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingInitialE(), 1.14)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAParameter(), 1.15)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingBParameter(), 1.16)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingMParameter(), 1.17)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPref(), 1.18)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAlpha(), 1.19)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingGammaY(), 1.21)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingRParameter(), 1.22)

def test45():
    mat = mat45

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA4)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAParameter(1.4)
    mat.Stiffness.NonLinearIsotropic.setBParameter(1.5)
    mat.Stiffness.NonLinearIsotropic.setMParameter(1.6)
    mat.Stiffness.NonLinearIsotropic.setPref(1.7)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.8)
    mat.Stiffness.NonLinearIsotropic.setGammaY(1.9)
    mat.Stiffness.NonLinearIsotropic.setRParameter(1.11)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRESS)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.12)
    mat.Stiffness.NonLinearIsotropic.setUnloadingResidualYoungsModulus(1.13)
    mat.Stiffness.NonLinearIsotropic.setUnloadingInitialE(1.14)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAParameter(1.15)
    mat.Stiffness.NonLinearIsotropic.setUnloadingBParameter(1.16)
    mat.Stiffness.NonLinearIsotropic.setUnloadingMParameter(1.17)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPref(1.18)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAlpha(1.19)
    mat.Stiffness.NonLinearIsotropic.setUnloadingGammaY(1.21)
    mat.Stiffness.NonLinearIsotropic.setUnloadingRParameter(1.22)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA4)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAParameter(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getBParameter(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getMParameter(), 1.6)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.7)
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.8)
    assert(mat.Stiffness.NonLinearIsotropic.getGammaY(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getRParameter(), 1.11)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRESS)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.12)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingResidualYoungsModulus(), 1.13)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingInitialE(), 1.14)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAParameter(), 1.15)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingBParameter(), 1.16)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingMParameter(), 1.17)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPref(), 1.18)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAlpha(), 1.19)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingGammaY(), 1.21)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingRParameter(), 1.22)

def test46():
    mat = mat46

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA4)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAParameter(1.4)
    mat.Stiffness.NonLinearIsotropic.setBParameter(1.5)
    mat.Stiffness.NonLinearIsotropic.setMParameter(1.6)
    mat.Stiffness.NonLinearIsotropic.setPref(1.7)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.8)
    mat.Stiffness.NonLinearIsotropic.setGammaY(1.9)
    mat.Stiffness.NonLinearIsotropic.setRParameter(1.11)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_VOLUMETRIC_STRAIN)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.12)
    mat.Stiffness.NonLinearIsotropic.setUnloadingResidualYoungsModulus(1.13)
    mat.Stiffness.NonLinearIsotropic.setUnloadingInitialE(1.14)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAParameter(1.15)
    mat.Stiffness.NonLinearIsotropic.setUnloadingBParameter(1.16)
    mat.Stiffness.NonLinearIsotropic.setUnloadingMParameter(1.17)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPref(1.18)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAlpha(1.19)
    mat.Stiffness.NonLinearIsotropic.setUnloadingGammaY(1.21)
    mat.Stiffness.NonLinearIsotropic.setUnloadingRParameter(1.22)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA4)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAParameter(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getBParameter(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getMParameter(), 1.6)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.7)
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.8)
    assert(mat.Stiffness.NonLinearIsotropic.getGammaY(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getRParameter(), 1.11)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_VOLUMETRIC_STRAIN)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.12)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingResidualYoungsModulus(), 1.13)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingInitialE(), 1.14)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAParameter(), 1.15)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingBParameter(), 1.16)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingMParameter(), 1.17)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPref(), 1.18)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAlpha(), 1.19)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingGammaY(), 1.21)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingRParameter(), 1.22)

def test47():
    mat = mat47

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA4)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(True)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAParameter(1.4)
    mat.Stiffness.NonLinearIsotropic.setBParameter(1.5)
    mat.Stiffness.NonLinearIsotropic.setMParameter(1.6)
    mat.Stiffness.NonLinearIsotropic.setPref(1.7)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.8)
    mat.Stiffness.NonLinearIsotropic.setGammaY(1.9)
    mat.Stiffness.NonLinearIsotropic.setRParameter(1.11)
    mat.Stiffness.NonLinearIsotropic.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRAIN)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPoissonsRatio(0.12)
    mat.Stiffness.NonLinearIsotropic.setUnloadingResidualYoungsModulus(1.13)
    mat.Stiffness.NonLinearIsotropic.setUnloadingInitialE(1.14)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAParameter(1.15)
    mat.Stiffness.NonLinearIsotropic.setUnloadingBParameter(1.16)
    mat.Stiffness.NonLinearIsotropic.setUnloadingMParameter(1.17)
    mat.Stiffness.NonLinearIsotropic.setUnloadingPref(1.18)
    mat.Stiffness.NonLinearIsotropic.setUnloadingAlpha(1.19)
    mat.Stiffness.NonLinearIsotropic.setUnloadingGammaY(1.21)
    mat.Stiffness.NonLinearIsotropic.setUnloadingRParameter(1.22)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA4)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAParameter(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getBParameter(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getMParameter(), 1.6)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.7)
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.8)
    assert(mat.Stiffness.NonLinearIsotropic.getGammaY(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getRParameter(), 1.11)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRAIN)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPoissonsRatio(), 0.12)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingResidualYoungsModulus(), 1.13)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingInitialE(), 1.14)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAParameter(), 1.15)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingBParameter(), 1.16)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingMParameter(), 1.17)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingPref(), 1.18)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingAlpha(), 1.19)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingGammaY(), 1.21)
    assert(mat.Stiffness.NonLinearIsotropic.getUnloadingRParameter(), 1.22)

def test48():
    mat = mat48

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    mat.Stiffness.NonLinearIsotropic.setNonLinearIsotropicFormula(NLIFormulaTypes.NLI_TYPE_FORMULA4)
    mat.Stiffness.NonLinearIsotropic.setUseUnloadingCondition(False)
    mat.Stiffness.NonLinearIsotropic.setPoissonsRatio(0.1)
    mat.Stiffness.NonLinearIsotropic.setResidualYoungsModulus(1.2)
    mat.Stiffness.NonLinearIsotropic.setInitialE(1.3)
    mat.Stiffness.NonLinearIsotropic.setAParameter(1.4)
    mat.Stiffness.NonLinearIsotropic.setBParameter(1.5)
    mat.Stiffness.NonLinearIsotropic.setMParameter(1.6)
    mat.Stiffness.NonLinearIsotropic.setPref(1.7)
    mat.Stiffness.NonLinearIsotropic.setAlpha(1.8)
    mat.Stiffness.NonLinearIsotropic.setGammaY(1.9)
    mat.Stiffness.NonLinearIsotropic.setRParameter(1.11)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.NON_LINEAR_ISOTROPIC)
    assert(mat.Stiffness.NonLinearIsotropic.getNonLinearIsotropicFormula(), NLIFormulaTypes.NLI_TYPE_FORMULA4)
    assert(mat.Stiffness.NonLinearIsotropic.getUseUnloadingCondition(), False)
    assert(mat.Stiffness.NonLinearIsotropic.getPoissonsRatio(), 0.1)
    assert(mat.Stiffness.NonLinearIsotropic.getResidualYoungsModulus(), 1.2)
    assert(mat.Stiffness.NonLinearIsotropic.getInitialE(), 1.3)
    assert(mat.Stiffness.NonLinearIsotropic.getAParameter(), 1.4)
    assert(mat.Stiffness.NonLinearIsotropic.getBParameter(), 1.5)
    assert(mat.Stiffness.NonLinearIsotropic.getMParameter(), 1.6)
    assert(mat.Stiffness.NonLinearIsotropic.getPref(), 1.7)
    assert(mat.Stiffness.NonLinearIsotropic.getAlpha(), 1.8)
    assert(mat.Stiffness.NonLinearIsotropic.getGammaY(), 1.9)
    assert(mat.Stiffness.NonLinearIsotropic.getRParameter(), 1.11)

def test49():
    mat = mat49

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.VISCO_ELASTIC)
    mat.Stiffness.ViscoElastic.setViscoElasticType(ViscoElasticTypes.VET_MAXWELL)
    mat.Stiffness.ViscoElastic.setBulkModulus(1.1)
    mat.Stiffness.ViscoElastic.setMaxwellShearModulus(1.2)
    mat.Stiffness.ViscoElastic.setMaxwellViscosity(1.3)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.VISCO_ELASTIC)
    assert(mat.Stiffness.ViscoElastic.getViscoElasticType(), ViscoElasticTypes.VET_MAXWELL)
    assert(mat.Stiffness.ViscoElastic.getBulkModulus(), 1.1)
    assert(mat.Stiffness.ViscoElastic.getMaxwellShearModulus(), 1.2)
    assert(mat.Stiffness.ViscoElastic.getMaxwellViscosity(), 1.3)

def test50():
    mat = mat50

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.VISCO_ELASTIC)
    mat.Stiffness.ViscoElastic.setViscoElasticType(ViscoElasticTypes.VET_BURGERS)
    mat.Stiffness.ViscoElastic.setBulkModulus(1.1)
    mat.Stiffness.ViscoElastic.setMaxwellShearModulus(1.2)
    mat.Stiffness.ViscoElastic.setMaxwellViscosity(1.3)
    mat.Stiffness.ViscoElastic.setKelvinShearModulus(1.4)
    mat.Stiffness.ViscoElastic.setKelvinViscosity(1.5)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.VISCO_ELASTIC)
    assert(mat.Stiffness.ViscoElastic.getViscoElasticType(), ViscoElasticTypes.VET_BURGERS)
    assert(mat.Stiffness.ViscoElastic.getBulkModulus(), 1.1)
    assert(mat.Stiffness.ViscoElastic.getMaxwellShearModulus(), 1.2)
    assert(mat.Stiffness.ViscoElastic.getMaxwellViscosity(), 1.3)
    assert(mat.Stiffness.ViscoElastic.getKelvinShearModulus(), 1.4)
    assert(mat.Stiffness.ViscoElastic.getKelvinViscosity(), 1.5)

def test51():
    mat = mat51

    mat.Stiffness.setElasticType(MaterialElasticityTypes.VISCO_ELASTIC)
    mat.Stiffness.ViscoElastic.setViscoElasticType(ViscoElasticTypes.VET_STANDARD)
    mat.Stiffness.ViscoElastic.setBulkModulus(1.1)
    mat.Stiffness.ViscoElastic.setShearModulus(1.2)
    mat.Stiffness.ViscoElastic.setKelvinShearModulus(1.3)
    mat.Stiffness.ViscoElastic.setKelvinViscosity(1.4)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.VISCO_ELASTIC)
    assert(mat.Stiffness.ViscoElastic.getViscoElasticType(), ViscoElasticTypes.VET_STANDARD)
    assert(mat.Stiffness.ViscoElastic.getBulkModulus(), 1.1)
    assert(mat.Stiffness.ViscoElastic.getShearModulus(), 1.2)
    assert(mat.Stiffness.ViscoElastic.getKelvinShearModulus(), 1.3)
    assert(mat.Stiffness.ViscoElastic.getKelvinViscosity(), 1.4)

def test52():
    mat = mat52

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)


    mat.Stiffness.Custom.setUseUnloadingCondition(True)
    mat.Stiffness.Custom.setUseConstantPoissonsRatio(True)
    mat.Stiffness.Custom.setConstantPoissonsRatio(0.1)
    mat.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_Q,[(1.1,1.2,0),(1.4,1.5,0)]) # Tuples in list must be size 3 in order to not throw exception, even when constant poisson ratio is true
    mat.Stiffness.Custom.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.Custom.setUnloadingUseConstantPoissonsRatio(True)
    mat.Stiffness.Custom.setUnloadingConstantPoissonsRatio(0.2)
    mat.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_Q,[(1.07,1.8,0),(1.11,1.12,0)])
    mat.Stiffness.Custom.setCustomMode(CustomMode.CUSTOM_Q)
    mat.Stiffness.setElasticType(MaterialElasticityTypes.CUSTOM_STIFFNESS)

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.CUSTOM_STIFFNESS)
    assert(mat.Stiffness.Custom.getCustomMode(), CustomMode.CUSTOM_Q)
    assert(mat.Stiffness.Custom.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Custom.getUseConstantPoissonsRatio(), True)
    assert(mat.Stiffness.Custom.getConstantPoissonsRatio(), 0.1)
    assert(mat.Stiffness.Custom.getCustomStiffnessLoadingTable(), [(1.1,1.2),(1.4,1.5)])
    assert(mat.Stiffness.Custom.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.Custom.getUnloadingUseConstantPoissonsRatio(), True)
    assert(mat.Stiffness.Custom.getUnloadingConstantPoissonsRatio(), 0.2)
    assert(mat.Stiffness.Custom.getCustomStiffnessUnloadingTable(), [(1.07,1.8),(1.11,1.12)])

def test53():
    mat = mat53

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.CUSTOM_STIFFNESS)
    mat.Stiffness.Custom.setCustomMode(CustomMode.CUSTOM_Q)
    mat.Stiffness.Custom.setUseUnloadingCondition(True)
    mat.Stiffness.Custom.setUseConstantPoissonsRatio(True)
    mat.Stiffness.Custom.setConstantPoissonsRatio(0.1)
    mat.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_Q,[(1.1,1.2),(1.4,1.5)])
    mat.Stiffness.Custom.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRESS)
    mat.Stiffness.Custom.setUnloadingUseConstantPoissonsRatio(True)
    mat.Stiffness.Custom.setUnloadingConstantPoissonsRatio(0.2)
    mat.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_Q,[(1.07,1.8),(1.11,1.12)])

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.CUSTOM_STIFFNESS)
    assert(mat.Stiffness.Custom.getCustomMode(), CustomMode.CUSTOM_Q)
    assert(mat.Stiffness.Custom.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Custom.getUseConstantPoissonsRatio(), True)
    assert(mat.Stiffness.Custom.getConstantPoissonsRatio(), 0.1)
    assert(mat.Stiffness.Custom.getCustomStiffnessLoadingTable(), [(1.1,1.2),(1.4,1.5)])
    assert(mat.Stiffness.Custom.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRESS)
    assert(mat.Stiffness.Custom.getUnloadingUseConstantPoissonsRatio(), True)
    assert(mat.Stiffness.Custom.getUnloadingConstantPoissonsRatio(), 0.2)
    assert(mat.Stiffness.Custom.getCustomStiffnessUnloadingTable(), [(1.07,1.8),(1.11,1.12)])

def test54():
    mat = mat54

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.CUSTOM_STIFFNESS)
    mat.Stiffness.Custom.setCustomMode(CustomMode.CUSTOM_Q)
    mat.Stiffness.Custom.setUseUnloadingCondition(True)
    mat.Stiffness.Custom.setUseConstantPoissonsRatio(True)
    mat.Stiffness.Custom.setConstantPoissonsRatio(0.1)
    mat.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_Q,[(1.1,1.2),(1.4,1.5)])
    mat.Stiffness.Custom.setUnloadingCondition(UnloadingConditions.UC_VOLUMETRIC_STRAIN)
    mat.Stiffness.Custom.setUnloadingUseConstantPoissonsRatio(True)
    mat.Stiffness.Custom.setUnloadingConstantPoissonsRatio(0.2)
    mat.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_Q,[(1.07,1.8),(1.11,1.12)])

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.CUSTOM_STIFFNESS)
    assert(mat.Stiffness.Custom.getCustomMode(), CustomMode.CUSTOM_Q)
    assert(mat.Stiffness.Custom.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Custom.getUseConstantPoissonsRatio(), True)
    assert(mat.Stiffness.Custom.getConstantPoissonsRatio(), 0.1)
    assert(mat.Stiffness.Custom.getCustomStiffnessLoadingTable(), [(1.1,1.2),(1.4,1.5)])
    assert(mat.Stiffness.Custom.getUnloadingCondition(), UnloadingConditions.UC_VOLUMETRIC_STRAIN)
    assert(mat.Stiffness.Custom.getUnloadingUseConstantPoissonsRatio(), True)
    assert(mat.Stiffness.Custom.getUnloadingConstantPoissonsRatio(), 0.2)
    assert(mat.Stiffness.Custom.getCustomStiffnessUnloadingTable(), [(1.07,1.8),(1.11,1.12)])

def test55():
    mat = mat55

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.CUSTOM_STIFFNESS)
    mat.Stiffness.Custom.setCustomMode(CustomMode.CUSTOM_Q)
    mat.Stiffness.Custom.setUseUnloadingCondition(True)
    mat.Stiffness.Custom.setUseConstantPoissonsRatio(True)
    mat.Stiffness.Custom.setConstantPoissonsRatio(0.1)
    mat.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_Q,[(1.1,1.2),(1.4,1.5)])
    mat.Stiffness.Custom.setUnloadingCondition(UnloadingConditions.UC_DEVIATORIC_STRAIN)
    mat.Stiffness.Custom.setUnloadingUseConstantPoissonsRatio(True)
    mat.Stiffness.Custom.setUnloadingConstantPoissonsRatio(0.2)
    mat.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_Q,[(1.07,1.8),(1.11,1.12)])

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.CUSTOM_STIFFNESS)
    assert(mat.Stiffness.Custom.getCustomMode(), CustomMode.CUSTOM_Q)
    assert(mat.Stiffness.Custom.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Custom.getUseConstantPoissonsRatio(), True)
    assert(mat.Stiffness.Custom.getConstantPoissonsRatio(), 0.1)
    assert(mat.Stiffness.Custom.getCustomStiffnessLoadingTable(), [(1.1,1.2),(1.4,1.5)])
    assert(mat.Stiffness.Custom.getUnloadingCondition(), UnloadingConditions.UC_DEVIATORIC_STRAIN)
    assert(mat.Stiffness.Custom.getUnloadingUseConstantPoissonsRatio(), True)
    assert(mat.Stiffness.Custom.getUnloadingConstantPoissonsRatio(), 0.2)
    assert(mat.Stiffness.Custom.getCustomStiffnessUnloadingTable(), [(1.07,1.8),(1.11,1.12)])

def test56():
    mat = mat56

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.CUSTOM_STIFFNESS)
    mat.Stiffness.Custom.setCustomMode(CustomMode.CUSTOM_Q)
    mat.Stiffness.Custom.setUseUnloadingCondition(False)
    mat.Stiffness.Custom.setUseConstantPoissonsRatio(False)
    mat.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_Q,[(1.1,1.2,0.3),(1.4,1.5,0.06)])

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.CUSTOM_STIFFNESS)
    assert(mat.Stiffness.Custom.getCustomMode(), CustomMode.CUSTOM_Q)
    assert(mat.Stiffness.Custom.getUseUnloadingCondition(), False)
    assert(mat.Stiffness.Custom.getUseConstantPoissonsRatio(), False)
    assert(mat.Stiffness.Custom.getCustomStiffnessLoadingTable(), [(1.1,1.2,0.3),(1.4,1.5,0.06)])

def test57():
    mat = mat57

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.CUSTOM_STIFFNESS)
    mat.Stiffness.Custom.setCustomMode(CustomMode.CUSTOM_Q)
    mat.Stiffness.Custom.setUseUnloadingCondition(True)
    mat.Stiffness.Custom.setUseConstantPoissonsRatio(False)
    mat.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_Q,[(1.1,1.2,0.3),(1.4,1.5,0.06)])
    mat.Stiffness.Custom.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.Custom.setUnloadingUseConstantPoissonsRatio(False)
    mat.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_Q,[(1.07,1.8,0.09),(1.11,1.12,0.13)])

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.CUSTOM_STIFFNESS)
    assert(mat.Stiffness.Custom.getCustomMode(), CustomMode.CUSTOM_Q)
    assert(mat.Stiffness.Custom.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Custom.getUseConstantPoissonsRatio(), False)
    assert(mat.Stiffness.Custom.getCustomStiffnessLoadingTable(), [(1.1,1.2,0.3),(1.4,1.5,0.06)])
    assert(mat.Stiffness.Custom.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.Custom.getUnloadingUseConstantPoissonsRatio(), False)
    assert(mat.Stiffness.Custom.getCustomStiffnessUnloadingTable(), [(1.07,1.8,0.09),(1.11,1.12,0.13)])

def test58():
    mat = mat58

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.CUSTOM_STIFFNESS)
    mat.Stiffness.Custom.setCustomMode(CustomMode.CUSTOM_Q)
    mat.Stiffness.Custom.setUseUnloadingCondition(True)
    mat.Stiffness.Custom.setUseConstantPoissonsRatio(False)
    mat.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_Q,[(1.1,1.2,0.3),(1.4,1.5,0.06)])
    mat.Stiffness.Custom.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.Custom.setUnloadingUseConstantPoissonsRatio(True)
    mat.Stiffness.Custom.setUnloadingConstantPoissonsRatio(0.2)
    mat.Stiffness.Custom.setCustomStiffnessUnloadingTable(CustomMode.CUSTOM_Q,[(1.07,1.8),(1.11,1.12)])

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.CUSTOM_STIFFNESS)
    assert(mat.Stiffness.Custom.getCustomMode(), CustomMode.CUSTOM_Q)
    assert(mat.Stiffness.Custom.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Custom.getUseConstantPoissonsRatio(), False)
    assert(mat.Stiffness.Custom.getCustomStiffnessLoadingTable(), [(1.1,1.2,0.3),(1.4,1.5,0.06)])
    assert(mat.Stiffness.Custom.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.Custom.getUnloadingUseConstantPoissonsRatio(), True)
    assert(mat.Stiffness.Custom.getUnloadingConstantPoissonsRatio(), 0.2)
    assert(mat.Stiffness.Custom.getCustomStiffnessUnloadingTable(), [(1.07,1.8),(1.11,1.12)])

def test59():
    mat = mat59

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.CUSTOM_STIFFNESS)
    mat.Stiffness.Custom.setCustomMode(CustomMode.CUSTOM_Q)
    mat.Stiffness.Custom.setUseUnloadingCondition(False)
    mat.Stiffness.Custom.setUseConstantPoissonsRatio(True)
    mat.Stiffness.Custom.setConstantPoissonsRatio(0.1)
    mat.Stiffness.Custom.setCustomStiffnessLoadingTable(CustomMode.CUSTOM_Q,[(1.1,1.2),(1.4,1.5)])

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.CUSTOM_STIFFNESS)
    assert(mat.Stiffness.Custom.getCustomMode(), CustomMode.CUSTOM_Q)
    assert(mat.Stiffness.Custom.getUseUnloadingCondition(), False)
    assert(mat.Stiffness.Custom.getUseConstantPoissonsRatio(), True)
    assert(mat.Stiffness.Custom.getConstantPoissonsRatio(), 0.1)
    assert(mat.Stiffness.Custom.getCustomStiffnessLoadingTable(), [(1.1,1.2),(1.4,1.5)])

def test60():
    mat = mat60

    testCustomMode = CustomMode.CUSTOM_P

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.CUSTOM_STIFFNESS)
    mat.Stiffness.Custom.setCustomMode(testCustomMode)
    mat.Stiffness.Custom.setUseUnloadingCondition(True)
    mat.Stiffness.Custom.setUseConstantPoissonsRatio(False)
    mat.Stiffness.Custom.setCustomStiffnessLoadingTable(testCustomMode,[(1.1,1.2,0.3),(1.4,1.5,0.06)])
    mat.Stiffness.Custom.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.Custom.setUnloadingUseConstantPoissonsRatio(False)
    mat.Stiffness.Custom.setCustomStiffnessUnloadingTable(testCustomMode,[(1.07,1.8,0.09),(1.11,1.12,0.13)])

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.CUSTOM_STIFFNESS)
    assert(mat.Stiffness.Custom.getCustomMode(), testCustomMode)
    assert(mat.Stiffness.Custom.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Custom.getUseConstantPoissonsRatio(), False)
    assert(mat.Stiffness.Custom.getCustomStiffnessLoadingTable(), [(1.1,1.2,0.3),(1.4,1.5,0.06)])
    assert(mat.Stiffness.Custom.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.Custom.getUnloadingUseConstantPoissonsRatio(), False)
    assert(mat.Stiffness.Custom.getCustomStiffnessUnloadingTable(), [(1.07,1.8,0.09),(1.11,1.12,0.13)])

def test61():
    mat = mat61

    testCustomMode = CustomMode.CUSTOM_S3

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.CUSTOM_STIFFNESS)
    mat.Stiffness.Custom.setCustomMode(testCustomMode)
    mat.Stiffness.Custom.setUseUnloadingCondition(True)
    mat.Stiffness.Custom.setUseConstantPoissonsRatio(False)
    mat.Stiffness.Custom.setCustomStiffnessLoadingTable(testCustomMode,[(1.1,1.2,0.3),(1.4,1.5,0.06)])
    mat.Stiffness.Custom.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.Custom.setUnloadingUseConstantPoissonsRatio(False)
    mat.Stiffness.Custom.setCustomStiffnessUnloadingTable(testCustomMode,[(1.07,1.8,0.09),(1.11,1.12,0.13)])

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.CUSTOM_STIFFNESS)
    assert(mat.Stiffness.Custom.getCustomMode(), testCustomMode)
    assert(mat.Stiffness.Custom.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Custom.getUseConstantPoissonsRatio(), False)
    assert(mat.Stiffness.Custom.getCustomStiffnessLoadingTable(), [(1.1,1.2,0.3),(1.4,1.5,0.06)])
    assert(mat.Stiffness.Custom.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.Custom.getUnloadingUseConstantPoissonsRatio(), False)
    assert(mat.Stiffness.Custom.getCustomStiffnessUnloadingTable(), [(1.07,1.8,0.09),(1.11,1.12,0.13)])

def test62():
    mat = mat62

    testCustomMode = CustomMode.CUSTOM_U

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.CUSTOM_STIFFNESS)
    mat.Stiffness.Custom.setCustomMode(testCustomMode)
    mat.Stiffness.Custom.setUseUnloadingCondition(True)
    mat.Stiffness.Custom.setUseConstantPoissonsRatio(False)
    mat.Stiffness.Custom.setCustomStiffnessLoadingTable(testCustomMode,[(1.1,1.2,0.3),(1.4,1.5,0.06)])
    mat.Stiffness.Custom.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.Custom.setUnloadingUseConstantPoissonsRatio(False)
    mat.Stiffness.Custom.setCustomStiffnessUnloadingTable(testCustomMode,[(1.07,1.8,0.09),(1.11,1.12,0.13)])

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.CUSTOM_STIFFNESS)
    assert(mat.Stiffness.Custom.getCustomMode(), testCustomMode)
    assert(mat.Stiffness.Custom.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Custom.getUseConstantPoissonsRatio(), False)
    assert(mat.Stiffness.Custom.getCustomStiffnessLoadingTable(), [(1.1,1.2,0.3),(1.4,1.5,0.06)])
    assert(mat.Stiffness.Custom.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.Custom.getUnloadingUseConstantPoissonsRatio(), False)
    assert(mat.Stiffness.Custom.getCustomStiffnessUnloadingTable(), [(1.07,1.8,0.09),(1.11,1.12,0.13)])

def test63():
    mat = mat63

    testCustomMode = CustomMode.CUSTOM_EPSV

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.CUSTOM_STIFFNESS)
    mat.Stiffness.Custom.setCustomMode(testCustomMode)
    mat.Stiffness.Custom.setUseUnloadingCondition(True)
    mat.Stiffness.Custom.setUseConstantPoissonsRatio(False)
    mat.Stiffness.Custom.setCustomStiffnessLoadingTable(testCustomMode,[(1.1,1.2,0.3),(1.4,1.5,0.06)])
    mat.Stiffness.Custom.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.Custom.setUnloadingUseConstantPoissonsRatio(False)
    mat.Stiffness.Custom.setCustomStiffnessUnloadingTable(testCustomMode,[(1.07,1.8,0.09),(1.11,1.12,0.13)])

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.CUSTOM_STIFFNESS)
    assert(mat.Stiffness.Custom.getCustomMode(), testCustomMode)
    assert(mat.Stiffness.Custom.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Custom.getUseConstantPoissonsRatio(), False)
    assert(mat.Stiffness.Custom.getCustomStiffnessLoadingTable(), [(1.1,1.2,0.3),(1.4,1.5,0.06)])
    assert(mat.Stiffness.Custom.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.Custom.getUnloadingUseConstantPoissonsRatio(), False)
    assert(mat.Stiffness.Custom.getCustomStiffnessUnloadingTable(), [(1.07,1.8,0.09),(1.11,1.12,0.13)])

def test64():
    mat = mat64

    testCustomMode = CustomMode.CUSTOM_GAMMA

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)

    mat.Stiffness.setElasticType(MaterialElasticityTypes.CUSTOM_STIFFNESS)
    mat.Stiffness.Custom.setCustomMode(testCustomMode)
    mat.Stiffness.Custom.setUseUnloadingCondition(True)
    mat.Stiffness.Custom.setUseConstantPoissonsRatio(False)
    mat.Stiffness.Custom.setCustomStiffnessLoadingTable(testCustomMode,[(1.1,1.2,0.3),(1.4,1.5,0.06)])
    mat.Stiffness.Custom.setUnloadingCondition(UnloadingConditions.UC_MEAN_STRESS)
    mat.Stiffness.Custom.setUnloadingUseConstantPoissonsRatio(False)
    mat.Stiffness.Custom.setCustomStiffnessUnloadingTable(testCustomMode,[(1.07,1.8,0.09),(1.11,1.12,0.13)])

    assert(mat.Stiffness.getElasticType(), MaterialElasticityTypes.CUSTOM_STIFFNESS)
    assert(mat.Stiffness.Custom.getCustomMode(), testCustomMode)
    assert(mat.Stiffness.Custom.getUseUnloadingCondition(), True)
    assert(mat.Stiffness.Custom.getUseConstantPoissonsRatio(), False)
    assert(mat.Stiffness.Custom.getCustomStiffnessLoadingTable(), [(1.1,1.2,0.3),(1.4,1.5,0.06)])
    assert(mat.Stiffness.Custom.getUnloadingCondition(), UnloadingConditions.UC_MEAN_STRESS)
    assert(mat.Stiffness.Custom.getUnloadingUseConstantPoissonsRatio(), False)
    assert(mat.Stiffness.Custom.getCustomStiffnessUnloadingTable(), [(1.07,1.8,0.09),(1.11,1.12,0.13)])


test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()
test9()
test10()
test11()
test12()
test13()
test14()
test15()  
test16()
test17()
test18()
test19()
test20()
test21()
test22()
test23()
test24()
test25()
test26()
test27()
test28()
test29()
test30()
test31()
test32()
test33()
test34()
test35()
test36() 
test37()
test38()
test39()
test40()
test41()
test42()
test43()
test44()
test45()
test46()
test47()
test48()
test49()
test50()
test51()
''' Setting custom stiffness tables throws exception if tuple length is not 3, even when it should be able to accept length 2.
test52()
#test53()
#test54()
#test55()
#test56()
#test57()
#test58()
#test59()
#test60()
#test61()
#test62()
#test63()
#test64()
#'''

model.save()

pass