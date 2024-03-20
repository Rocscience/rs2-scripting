from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\materialDatum_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\materialDatum_python.fez'

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

def test1():
    mat = mat1

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    ymDatum = mat.Datum.getDatumYoungsModulus()

    ymDatum.setUsing(True)
    ymDatum.setType(DatumType.DATUM_TYPE_DEPTH)
    ymDatum.setDatum(1.1)
    ymDatum.setChange(1.2)
    ymDatum.setUseCutoff(True)
    ymDatum.setCutoff(1.3)

    assert(ymDatum.getUsing(),True)
    assert(ymDatum.getType(), DatumType.DATUM_TYPE_DEPTH)
    assert(ymDatum.getDatum(),1.1)
    assert(ymDatum.getChange(),1.2)
    assert(ymDatum.getUseCutoff(), True)
    assert(ymDatum.getCutoff(),1.3)

def test2():
    mat = mat2

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    ymDatum = mat.Datum.getDatumYoungsModulus()

    ymDatum.setUsing(True)
    ymDatum.setType(DatumType.DATUM_TYPE_DEPTH)
    ymDatum.setDatum(1.1)
    ymDatum.setChange(1.2)
    ymDatum.setUseCutoff(False)

    assert(ymDatum.getUsing(),True)
    assert(ymDatum.getType(), DatumType.DATUM_TYPE_DEPTH)
    assert(ymDatum.getDatum(),1.1)
    assert(ymDatum.getChange(),1.2)
    assert(ymDatum.getUseCutoff(), False)

def test3():
    mat = mat3

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    ymDatum = mat.Datum.getDatumYoungsModulus()

    ymDatum.setUsing(True)
    ymDatum.setType(DatumType.DATUM_TYPE_RADIAL)
    ymDatum.setCenter(1.4,1.5)
    ymDatum.setChange(1.2)
    ymDatum.setUseCutoff(True)
    ymDatum.setCutoff(1.3)

    assert(ymDatum.getUsing(),True)
    assert(ymDatum.getType(), DatumType.DATUM_TYPE_DEPTH)
    assert(ymDatum.getCenter(),(1.4,1.5))
    assert(ymDatum.getChange(),1.2)
    assert(ymDatum.getUseCutoff(), True)
    assert(ymDatum.getCutoff(),1.3)

def test4():
    mat = mat4

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    ymDatum = mat.Datum.getDatumYoungsModulus()

    ymDatum.setUsing(True)
    ymDatum.setType(DatumType.DATUM_TYPE_RADIAL)
    ymDatum.setCenter(1.4,1.5)
    ymDatum.setChange(1.2)
    ymDatum.setUseCutoff(False)

    assert(ymDatum.getUsing(),True)
    assert(ymDatum.getType(), DatumType.DATUM_TYPE_DEPTH)
    assert(ymDatum.getCenter(),(1.4,1.5))
    assert(ymDatum.getChange(),1.2)
    assert(ymDatum.getUseCutoff(), False)

def test5():
    mat = mat5

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    unloadingYMDatum = mat.Datum.getDatumUnloadingYoungsModulus()

    unloadingYMDatum.setUsing(True)
    unloadingYMDatum.setType(DatumType.DATUM_TYPE_DEPTH)
    unloadingYMDatum.setDatum(1.1)
    unloadingYMDatum.setChange(1.2)
    unloadingYMDatum.setUseCutoff(True)
    unloadingYMDatum.setCutoff(1.3)

    assert(unloadingYMDatum.getUsing(),True)
    assert(unloadingYMDatum.getType(), DatumType.DATUM_TYPE_DEPTH)
    assert(unloadingYMDatum.getDatum(),1.1)
    assert(unloadingYMDatum.getChange(),1.2)
    assert(unloadingYMDatum.getUseCutoff(), True)
    assert(unloadingYMDatum.getCutoff(),1.3)

def test6():
    mat = mat6

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    unloadingYMDatum = mat.Datum.getDatumUnloadingYoungsModulus()
    
    unloadingYMDatum.setUsing(True)
    unloadingYMDatum.setType(DatumType.DATUM_TYPE_DEPTH)
    unloadingYMDatum.setDatum(1.1)
    unloadingYMDatum.setChange(1.2)
    unloadingYMDatum.setUseCutoff(False)

    assert(unloadingYMDatum.getUsing(),True)
    assert(unloadingYMDatum.getType(), DatumType.DATUM_TYPE_DEPTH)
    assert(unloadingYMDatum.getDatum(),1.1)
    assert(unloadingYMDatum.getChange(),1.2)
    assert(unloadingYMDatum.getUseCutoff(), False)

def test7():
    mat = mat7

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    unloadingYMDatum = mat.Datum.getDatumUnloadingYoungsModulus()
    
    unloadingYMDatum.setUsing(True)
    unloadingYMDatum.setType(DatumType.DATUM_TYPE_RADIAL)
    unloadingYMDatum.setCenter(1.4,1.5)
    unloadingYMDatum.setChange(1.2)
    unloadingYMDatum.setUseCutoff(True)
    unloadingYMDatum.setCutoff(1.3)

    assert(unloadingYMDatum.getUsing(),True)
    assert(unloadingYMDatum.getType(), DatumType.DATUM_TYPE_DEPTH)
    assert(unloadingYMDatum.getCenter(),(1.4,1.5))
    assert(unloadingYMDatum.getChange(),1.2)
    assert(unloadingYMDatum.getUseCutoff(), True)
    assert(unloadingYMDatum.getCutoff(),1.3)

def test8():
    mat = mat8

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    unloadingYMDatum = mat.Datum.getDatumUnloadingYoungsModulus()

    unloadingYMDatum.setUsing(True)
    unloadingYMDatum.setType(DatumType.DATUM_TYPE_RADIAL)
    unloadingYMDatum.setCenter(1.4,1.5)
    unloadingYMDatum.setChange(1.2)
    unloadingYMDatum.setUseCutoff(False)

    assert(unloadingYMDatum.getUsing(),True)
    assert(unloadingYMDatum.getType(), DatumType.DATUM_TYPE_DEPTH)
    assert(unloadingYMDatum.getCenter(),(1.4,1.5))
    assert(unloadingYMDatum.getChange(),1.2)
    assert(unloadingYMDatum.getUseCutoff(), False)

def test9():
    mat = mat9

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    cohesionDatum = mat.Datum.getDatumCohesion()
    
    cohesionDatum.setUsing(True)
    cohesionDatum.setType(DatumType.DATUM_TYPE_DEPTH)
    cohesionDatum.setDatum(1.1)
    cohesionDatum.setPeakChange(1.2)
    cohesionDatum.setUsePeakCutoff(True)
    cohesionDatum.setPeakCutoffValue(1.3)
    cohesionDatum.setResidualChange(1.4)
    cohesionDatum.setUseResidualCutoff(True)
    cohesionDatum.setResidualCutoffValue(1.5)

    assert(cohesionDatum.getUsing(),True)
    assert(cohesionDatum.getType(), DatumType.DATUM_TYPE_DEPTH)
    assert(cohesionDatum.getDatum(),1.1)
    assert(cohesionDatum.getPeakChange(),1.2)
    assert(cohesionDatum.getUsePeakCutoff(), True)
    assert(cohesionDatum.getPeakCutoffValue(),1.3)
    assert(cohesionDatum.getResidualChange(),1.4)
    assert(cohesionDatum.getUseResidualCutoff(), True)
    assert(cohesionDatum.getResidualCutoffValue(),1.5)

def test10():
    mat = mat10

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    cohesionDatum = mat.Datum.getDatumCohesion()
    
    cohesionDatum.setUsing(True)
    cohesionDatum.setType(DatumType.DATUM_TYPE_DEPTH)
    cohesionDatum.setDatum(1.1)
    cohesionDatum.setPeakChange(1.2)
    cohesionDatum.setUsePeakCutoff(False)
    cohesionDatum.setResidualChange(1.4)
    cohesionDatum.setUseResidualCutoff(False)

    assert(cohesionDatum.getUsing(),True)
    assert(cohesionDatum.getType(), DatumType.DATUM_TYPE_DEPTH)
    assert(cohesionDatum.getDatum(),1.1)
    assert(cohesionDatum.getPeakChange(),1.2)
    assert(cohesionDatum.getUsePeakCutoff(), False)
    assert(cohesionDatum.getResidualChange(),1.4)
    assert(cohesionDatum.getUseResidualCutoff(), False)

def test11():
    mat = mat11

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    cohesionDatum = mat.Datum.getDatumCohesion()
    
    cohesionDatum.setUsing(True)
    cohesionDatum.setType(DatumType.DATUM_TYPE_DEPTH)
    cohesionDatum.setDatum(1.1)
    cohesionDatum.setPeakChange(1.2)
    cohesionDatum.setUsePeakCutoff(True)
    cohesionDatum.setPeakCutoffValue(1.3)
    cohesionDatum.setResidualChange(1.4)
    cohesionDatum.setUseResidualCutoff(False)

    assert(cohesionDatum.getUsing(),True)
    assert(cohesionDatum.getType(), DatumType.DATUM_TYPE_DEPTH)
    assert(cohesionDatum.getDatum(),1.1)
    assert(cohesionDatum.getPeakChange(),1.2)
    assert(cohesionDatum.getUsePeakCutoff(), True)
    assert(cohesionDatum.getPeakCutoffValue(),1.3)
    assert(cohesionDatum.getResidualChange(),1.4)
    assert(cohesionDatum.getUseResidualCutoff(), False)

def test12():
    mat = mat12

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    cohesionDatum = mat.Datum.getDatumCohesion()
    
    cohesionDatum.setUsing(True)
    cohesionDatum.setType(DatumType.DATUM_TYPE_DEPTH)
    cohesionDatum.setDatum(1.1)
    cohesionDatum.setPeakChange(1.2)
    cohesionDatum.setUsePeakCutoff(False)
    cohesionDatum.setResidualChange(1.4)
    cohesionDatum.setUseResidualCutoff(True)
    cohesionDatum.setResidualCutoffValue(1.5)

    assert(cohesionDatum.getUsing(),True)
    assert(cohesionDatum.getType(), DatumType.DATUM_TYPE_DEPTH)
    assert(cohesionDatum.getDatum(),1.1)
    assert(cohesionDatum.getPeakChange(),1.2)
    assert(cohesionDatum.getUsePeakCutoff(), False)
    assert(cohesionDatum.getResidualChange(),1.4)
    assert(cohesionDatum.getUseResidualCutoff(), True)
    assert(cohesionDatum.getResidualCutoffValue(),1.5)

def test13():
    mat = mat13

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    cohesionDatum = mat.Datum.getDatumCohesion()
    
    cohesionDatum.setUsing(True)
    cohesionDatum.setType(DatumType.DATUM_TYPE_RADIAL)
    cohesionDatum.setCenter(1.6, 1.7)
    cohesionDatum.setPeakChange(1.2)
    cohesionDatum.setUsePeakCutoff(True)
    cohesionDatum.setPeakCutoffValue(1.3)
    cohesionDatum.setResidualChange(1.4)
    cohesionDatum.setUseResidualCutoff(True)
    cohesionDatum.setResidualCutoffValue(1.5)

    assert(cohesionDatum.getUsing(),True)
    assert(cohesionDatum.getType(), DatumType.DATUM_TYPE_RADIAL)
    assert(cohesionDatum.getCenter(),(1.6,1.7))
    assert(cohesionDatum.getPeakChange(),1.2)
    assert(cohesionDatum.getUsePeakCutoff(), True)
    assert(cohesionDatum.getPeakCutoffValue(),1.3)
    assert(cohesionDatum.getResidualChange(),1.4)
    assert(cohesionDatum.getUseResidualCutoff(), True)
    assert(cohesionDatum.getResidualCutoffValue(),1.5)

def test14():
    mat = mat14

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    cohesionDatum = mat.Datum.getDatumCohesion()
    
    cohesionDatum.setUsing(True)
    cohesionDatum.setType(DatumType.DATUM_TYPE_RADIAL)
    cohesionDatum.setCenter(1.6, 1.7)
    cohesionDatum.setPeakChange(1.2)
    cohesionDatum.setUsePeakCutoff(False)
    cohesionDatum.setResidualChange(1.4)
    cohesionDatum.setUseResidualCutoff(False)

    assert(cohesionDatum.getUsing(),True)
    assert(cohesionDatum.getType(), DatumType.DATUM_TYPE_RADIAL)
    assert(cohesionDatum.getCenter(),(1.6,1.7))
    assert(cohesionDatum.getPeakChange(),1.2)
    assert(cohesionDatum.getUsePeakCutoff(), False)
    assert(cohesionDatum.getResidualChange(),1.4)
    assert(cohesionDatum.getUseResidualCutoff(), False)

def test15():
    mat = mat15

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    cohesionDatum = mat.Datum.getDatumCohesion()
    
    cohesionDatum.setUsing(True)
    cohesionDatum.setType(DatumType.DATUM_TYPE_RADIAL)
    cohesionDatum.setCenter(1.6, 1.7)
    cohesionDatum.setPeakChange(1.2)
    cohesionDatum.setUsePeakCutoff(True)
    cohesionDatum.setPeakCutoffValue(1.3)
    cohesionDatum.setResidualChange(1.4)
    cohesionDatum.setUseResidualCutoff(False)

    assert(cohesionDatum.getUsing(),True)
    assert(cohesionDatum.getType(), DatumType.DATUM_TYPE_RADIAL)
    assert(cohesionDatum.getCenter(),(1.6,1.7))
    assert(cohesionDatum.getPeakChange(),1.2)
    assert(cohesionDatum.getUsePeakCutoff(), True)
    assert(cohesionDatum.getPeakCutoffValue(),1.3)
    assert(cohesionDatum.getResidualChange(),1.4)
    assert(cohesionDatum.getUseResidualCutoff(), False)

def test16():
    mat = mat16

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    cohesionDatum = mat.Datum.getDatumCohesion()
    
    cohesionDatum.setUsing(True)
    cohesionDatum.setType(DatumType.DATUM_TYPE_RADIAL)
    cohesionDatum.setCenter(1.6, 1.7)
    cohesionDatum.setPeakChange(1.2)
    cohesionDatum.setUsePeakCutoff(False)
    cohesionDatum.setResidualChange(1.4)
    cohesionDatum.setUseResidualCutoff(True)
    cohesionDatum.setResidualCutoffValue(1.5)

    assert(cohesionDatum.getUsing(),True)
    assert(cohesionDatum.getType(), DatumType.DATUM_TYPE_RADIAL)
    assert(cohesionDatum.getCenter(),(1.6,1.7))
    assert(cohesionDatum.getPeakChange(),1.2)
    assert(cohesionDatum.getUsePeakCutoff(), False)
    assert(cohesionDatum.getResidualChange(),1.4)
    assert(cohesionDatum.getUseResidualCutoff(), True)
    assert(cohesionDatum.getResidualCutoffValue(),1.5)

def test17():
    mat = mat17

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    phiDatum = mat.Datum.getDatumFrictionAngle()
    
    phiDatum.setUsing(True)
    phiDatum.setType(DatumType.DATUM_TYPE_DEPTH)
    phiDatum.setDatum(1.1)
    phiDatum.setPeakChange(1.2)
    phiDatum.setUsePeakCutoff(True)
    phiDatum.setPeakCutoffValue(1.3)
    phiDatum.setResidualChange(1.4)
    phiDatum.setUseResidualCutoff(True)
    phiDatum.setResidualCutoffValue(1.5)

    assert(phiDatum.getUsing(),True)
    assert(phiDatum.getType(), DatumType.DATUM_TYPE_DEPTH)
    assert(phiDatum.getDatum(),1.1)
    assert(phiDatum.getPeakChange(),1.2)
    assert(phiDatum.getUsePeakCutoff(), True)
    assert(phiDatum.getPeakCutoffValue(),1.3)
    assert(phiDatum.getResidualChange(),1.4)
    assert(phiDatum.getUseResidualCutoff(), True)
    assert(phiDatum.getResidualCutoffValue(),1.5)

def test18(): 
    mat = mat18

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    phiDatum = mat.Datum.getDatumFrictionAngle()

    phiDatum.setUsing(True)
    phiDatum.setType(DatumType.DATUM_TYPE_DEPTH)
    phiDatum.setDatum(1.1)
    phiDatum.setPeakChange(1.2)
    phiDatum.setUsePeakCutoff(False)
    phiDatum.setResidualChange(1.4)
    phiDatum.setUseResidualCutoff(False)

    assert(phiDatum.getUsing(),True)
    assert(phiDatum.getType(), DatumType.DATUM_TYPE_DEPTH)
    assert(phiDatum.getDatum(),1.1)
    assert(phiDatum.getPeakChange(),1.2)
    assert(phiDatum.getUsePeakCutoff(), False)
    assert(phiDatum.getResidualChange(),1.4)
    assert(phiDatum.getUseResidualCutoff(), False)
    
def test19(): 
    mat = mat19

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    phiDatum = mat.Datum.getDatumFrictionAngle()

    phiDatum.setUsing(True)
    phiDatum.setType(DatumType.DATUM_TYPE_DEPTH)
    phiDatum.setDatum(1.1)
    phiDatum.setPeakChange(1.2)
    phiDatum.setUsePeakCutoff(True)
    phiDatum.setPeakCutoffValue(1.3)
    phiDatum.setResidualChange(1.4)
    phiDatum.setUseResidualCutoff(False)

    assert(phiDatum.getUsing(),True)
    assert(phiDatum.getType(), DatumType.DATUM_TYPE_DEPTH)
    assert(phiDatum.getDatum(),1.1)
    assert(phiDatum.getPeakChange(),1.2)
    assert(phiDatum.getUsePeakCutoff(), True)
    assert(phiDatum.getPeakCutoffValue(),1.3)
    assert(phiDatum.getResidualChange(),1.4)
    assert(phiDatum.getUseResidualCutoff(), False)

def test20(): 
    mat = mat20

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    phiDatum = mat.Datum.getDatumFrictionAngle()

    phiDatum.setUsing(True)
    phiDatum.setType(DatumType.DATUM_TYPE_DEPTH)
    phiDatum.setDatum(1.1)
    phiDatum.setPeakChange(1.2)
    phiDatum.setUsePeakCutoff(False)
    phiDatum.setResidualChange(1.4)
    phiDatum.setUseResidualCutoff(True)
    phiDatum.setResidualCutoffValue(1.5)

    assert(phiDatum.getUsing(),True)
    assert(phiDatum.getType(), DatumType.DATUM_TYPE_DEPTH)
    assert(phiDatum.getDatum(),1.1)
    assert(phiDatum.getPeakChange(),1.2)
    assert(phiDatum.getUsePeakCutoff(), False)
    assert(phiDatum.getResidualChange(),1.4)
    assert(phiDatum.getUseResidualCutoff(), True)
    assert(phiDatum.getResidualCutoffValue(),1.5)

def test21(): 
    mat = mat21

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    phiDatum = mat.Datum.getDatumFrictionAngle()

    phiDatum.setUsing(True)
    phiDatum.setType(DatumType.DATUM_TYPE_RADIAL)
    phiDatum.setCenter(1.6, 1.7) 
    phiDatum.setPeakChange(1.2)
    phiDatum.setUsePeakCutoff(True)
    phiDatum.setPeakCutoffValue(1.3)
    phiDatum.setResidualChange(1.4)
    phiDatum.setUseResidualCutoff(True)
    phiDatum.setResidualCutoffValue(1.5)

    assert(phiDatum.getUsing(),True)
    assert(phiDatum.getType(), DatumType.DATUM_TYPE_RADIAL)
    assert(phiDatum.getCenter(),(1.6,1.7))
    assert(phiDatum.getPeakChange(),1.2)
    assert(phiDatum.getUsePeakCutoff(), True)
    assert(phiDatum.getPeakCutoffValue(),1.3)
    assert(phiDatum.getResidualChange(),1.4)
    assert(phiDatum.getUseResidualCutoff(), True)
    assert(phiDatum.getResidualCutoffValue(),1.5)

def test22(): 
    mat = mat22

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    phiDatum = mat.Datum.getDatumFrictionAngle()

    phiDatum.setUsing(True)
    phiDatum.setType(DatumType.DATUM_TYPE_RADIAL)
    phiDatum.setCenter(1.6, 1.7)
    phiDatum.setPeakChange(1.2)
    phiDatum.setUsePeakCutoff(False)
    phiDatum.setResidualChange(1.4)
    phiDatum.setUseResidualCutoff(False)

    assert(phiDatum.getUsing(),True)
    assert(phiDatum.getType(), DatumType.DATUM_TYPE_RADIAL)
    assert(phiDatum.getCenter(),(1.6,1.7))
    assert(phiDatum.getPeakChange(),1.2)
    assert(phiDatum.getUsePeakCutoff(), False)
    assert(phiDatum.getResidualChange(),1.4)
    assert(phiDatum.getUseResidualCutoff(), False)

def test23(): 
    mat = mat23

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    phiDatum = mat.Datum.getDatumFrictionAngle()

    phiDatum.setUsing(True)
    phiDatum.setType(DatumType.DATUM_TYPE_RADIAL)
    phiDatum.setCenter(1.6, 1.7)
    phiDatum.setPeakChange(1.2)
    phiDatum.setUsePeakCutoff(True)
    phiDatum.setPeakCutoffValue(1.3)
    phiDatum.setResidualChange(1.4)
    phiDatum.setUseResidualCutoff(False)

    assert(phiDatum.getUsing(),True)
    assert(phiDatum.getType(), DatumType.DATUM_TYPE_RADIAL)
    assert(phiDatum.getCenter(),(1.6,1.7))
    assert(phiDatum.getPeakChange(),1.2)
    assert(phiDatum.getUsePeakCutoff(), True)
    assert(phiDatum.getPeakCutoffValue(),1.3)
    assert(phiDatum.getResidualChange(),1.4)
    assert(phiDatum.getUseResidualCutoff(), False)

def test24(): 
    mat = mat24

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MOHR_COULOMB)
    mat.Strength.MohrCoulombStrength.setMaterialType(MaterialType.PLASTIC)
    mat.Stiffness.Isotropic.setUseUnloadingCondition(True)

    mat.Datum.setUsingDatum(True)
    phiDatum = mat.Datum.getDatumFrictionAngle()

    phiDatum.setUsing(True)
    phiDatum.setType(DatumType.DATUM_TYPE_RADIAL)
    phiDatum.setCenter(1.6, 1.7)
    phiDatum.setPeakChange(1.2)
    phiDatum.setUsePeakCutoff(False)
    phiDatum.setResidualChange(1.4)
    phiDatum.setUseResidualCutoff(True)
    phiDatum.setResidualCutoffValue(1.5)

    assert(phiDatum.getUsing(),True)
    assert(phiDatum.getType(), DatumType.DATUM_TYPE_RADIAL)
    assert(phiDatum.getCenter(),(1.6,1.7))
    assert(phiDatum.getPeakChange(),1.2)
    assert(phiDatum.getUsePeakCutoff(), False)
    assert(phiDatum.getResidualChange(),1.4)
    assert(phiDatum.getUseResidualCutoff(), True)
    assert(phiDatum.getResidualCutoffValue(),1.5)

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

model.save()

pass