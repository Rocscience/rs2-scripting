from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_Stiffness.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\stiffnessDynamicSoils_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\stiffnessDynamicSoils_python.fez'

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

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.MANZARI_AND_DAFALIAS)
    
    mat.Stiffness.ManzariAndDafalias.setG0Parameter(1.1)
    mat.Stiffness.ManzariAndDafalias.setVParameter(1.2)
    mat.Stiffness.ManzariAndDafalias.setPatmParameter(1.3)
    mat.Stiffness.ManzariAndDafalias.setInitialVoidRatio(1.4)

    assert(mat.Stiffness.ManzariAndDafalias.getG0Parameter(), 1.1)
    assert(mat.Stiffness.ManzariAndDafalias.getVParameter(), 1.2)
    assert(mat.Stiffness.ManzariAndDafalias.getPatmParameter(), 1.3)
    assert(mat.Stiffness.ManzariAndDafalias.getInitialVoidRatio(), 1.4)

def test2():
    mat = mat2

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SAND)
    
    mat.Stiffness.Pm4Sand.setG0Parameter(1.1)
    mat.Stiffness.Pm4Sand.setVParameter(0.2)
    mat.Stiffness.Pm4Sand.setPatmParameter(1.3)
    mat.Stiffness.Pm4Sand.setAutoCalculateCGDParameter(False)
    mat.Stiffness.Pm4Sand.setCGDParameter(1.4)
    mat.Stiffness.Pm4Sand.setAutoCalculatePSedParameter(False)
    mat.Stiffness.Pm4Sand.setPSedParameter(1.5)
    mat.Stiffness.Pm4Sand.setPostShake(False)
    mat.Stiffness.Pm4Sand.setAutoCalculateFSedMin(False)
    mat.Stiffness.Pm4Sand.setFSedMin(0.6)

    assert(mat.Stiffness.Pm4Sand.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Sand.getVParameter(), 0.2)
    assert(mat.Stiffness.Pm4Sand.getPatmParameter(), 1.3)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateCGDParameter(), False)
    assert(mat.Stiffness.Pm4Sand.getCGDParameter(), 1.4)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculatePSedParameter(), False)
    assert(mat.Stiffness.Pm4Sand.getPSedParameter(), 1.5)
    assert(mat.Stiffness.Pm4Sand.getPostShake(), False)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateFSedMin(), False)
    assert(mat.Stiffness.Pm4Sand.getFSedMin(), 0.6)

def test3():
    mat = mat3

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SAND)
    
    mat.Stiffness.Pm4Sand.setG0Parameter(1.1)
    mat.Stiffness.Pm4Sand.setVParameter(0.2)
    mat.Stiffness.Pm4Sand.setPatmParameter(1.3)
    mat.Stiffness.Pm4Sand.setAutoCalculateCGDParameter(True)
    mat.Stiffness.Pm4Sand.setAutoCalculatePSedParameter(True)
    mat.Stiffness.Pm4Sand.setPostShake(True)
    mat.Stiffness.Pm4Sand.setAutoCalculateFSedMin(True)

    assert(mat.Stiffness.Pm4Sand.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Sand.getVParameter(), 0.2)
    assert(mat.Stiffness.Pm4Sand.getPatmParameter(), 1.3)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateCGDParameter(), True)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculatePSedParameter(), True)
    assert(mat.Stiffness.Pm4Sand.getPostShake(), True)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateFSedMin(), True)

def test4():
    mat = mat4

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SAND)
    
    mat.Stiffness.Pm4Sand.setG0Parameter(1.1)
    mat.Stiffness.Pm4Sand.setVParameter(0.2)
    mat.Stiffness.Pm4Sand.setPatmParameter(1.3)
    mat.Stiffness.Pm4Sand.setAutoCalculateCGDParameter(True)
    mat.Stiffness.Pm4Sand.setAutoCalculatePSedParameter(False)
    mat.Stiffness.Pm4Sand.setPSedParameter(1.5)
    mat.Stiffness.Pm4Sand.setPostShake(False)
    mat.Stiffness.Pm4Sand.setAutoCalculateFSedMin(False)
    mat.Stiffness.Pm4Sand.setFSedMin(0.6)

    assert(mat.Stiffness.Pm4Sand.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Sand.getVParameter(), 0.2)
    assert(mat.Stiffness.Pm4Sand.getPatmParameter(), 1.3)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateCGDParameter(), True)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculatePSedParameter(), False)
    assert(mat.Stiffness.Pm4Sand.getPSedParameter(), 1.5)
    assert(mat.Stiffness.Pm4Sand.getPostShake(), False)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateFSedMin(), False)
    assert(mat.Stiffness.Pm4Sand.getFSedMin(), 0.6)

def test5():
    mat = mat5

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SAND)
    
    mat.Stiffness.Pm4Sand.setG0Parameter(1.1)
    mat.Stiffness.Pm4Sand.setVParameter(0.2)
    mat.Stiffness.Pm4Sand.setPatmParameter(1.3)
    mat.Stiffness.Pm4Sand.setAutoCalculateCGDParameter(False)
    mat.Stiffness.Pm4Sand.setCGDParameter(1.4)
    mat.Stiffness.Pm4Sand.setAutoCalculatePSedParameter(True)
    mat.Stiffness.Pm4Sand.setPostShake(False)
    mat.Stiffness.Pm4Sand.setAutoCalculateFSedMin(False)
    mat.Stiffness.Pm4Sand.setFSedMin(0.6)

    assert(mat.Stiffness.Pm4Sand.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Sand.getVParameter(), 0.2)
    assert(mat.Stiffness.Pm4Sand.getPatmParameter(), 1.3)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateCGDParameter(), False)
    assert(mat.Stiffness.Pm4Sand.getCGDParameter(), 1.4)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculatePSedParameter(), True)
    assert(mat.Stiffness.Pm4Sand.getPostShake(), False)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateFSedMin(), False)
    assert(mat.Stiffness.Pm4Sand.getFSedMin(), 0.6)

def test6():
    mat = mat6

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SAND)
    
    mat.Stiffness.Pm4Sand.setG0Parameter(1.1)
    mat.Stiffness.Pm4Sand.setVParameter(0.2)
    mat.Stiffness.Pm4Sand.setPatmParameter(1.3)
    mat.Stiffness.Pm4Sand.setAutoCalculateCGDParameter(False)
    mat.Stiffness.Pm4Sand.setCGDParameter(1.4)
    mat.Stiffness.Pm4Sand.setAutoCalculatePSedParameter(False)
    mat.Stiffness.Pm4Sand.setPSedParameter(1.5)
    mat.Stiffness.Pm4Sand.setPostShake(True)
    mat.Stiffness.Pm4Sand.setAutoCalculateFSedMin(False)
    mat.Stiffness.Pm4Sand.setFSedMin(0.6)

    assert(mat.Stiffness.Pm4Sand.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Sand.getVParameter(), 0.2)
    assert(mat.Stiffness.Pm4Sand.getPatmParameter(), 1.3)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateCGDParameter(), False)
    assert(mat.Stiffness.Pm4Sand.getCGDParameter(), 1.4)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculatePSedParameter(), False)
    assert(mat.Stiffness.Pm4Sand.getPSedParameter(), 1.5)
    assert(mat.Stiffness.Pm4Sand.getPostShake(), True)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateFSedMin(), False)
    assert(mat.Stiffness.Pm4Sand.getFSedMin(), 0.6)

def test7():
    mat = mat7

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SAND)
    
    mat.Stiffness.Pm4Sand.setG0Parameter(1.1)
    mat.Stiffness.Pm4Sand.setVParameter(0.2)
    mat.Stiffness.Pm4Sand.setPatmParameter(1.3)
    mat.Stiffness.Pm4Sand.setAutoCalculateCGDParameter(False)
    mat.Stiffness.Pm4Sand.setCGDParameter(1.4)
    mat.Stiffness.Pm4Sand.setAutoCalculatePSedParameter(False)
    mat.Stiffness.Pm4Sand.setPSedParameter(1.5)
    mat.Stiffness.Pm4Sand.setPostShake(False)
    mat.Stiffness.Pm4Sand.setAutoCalculateFSedMin(True)

    assert(mat.Stiffness.Pm4Sand.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Sand.getVParameter(), 0.2)
    assert(mat.Stiffness.Pm4Sand.getPatmParameter(), 1.3)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateCGDParameter(), False)
    assert(mat.Stiffness.Pm4Sand.getCGDParameter(), 1.4)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculatePSedParameter(), False)
    assert(mat.Stiffness.Pm4Sand.getPSedParameter(), 1.5)
    assert(mat.Stiffness.Pm4Sand.getPostShake(), False)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateFSedMin(), True)

def test8():
    mat = mat8

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SAND)
    
    mat.Stiffness.Pm4Sand.setG0Parameter(1.1)
    mat.Stiffness.Pm4Sand.setVParameter(0.2)
    mat.Stiffness.Pm4Sand.setPatmParameter(1.3)
    mat.Stiffness.Pm4Sand.setAutoCalculateCGDParameter(True)
    mat.Stiffness.Pm4Sand.setAutoCalculatePSedParameter(False)
    mat.Stiffness.Pm4Sand.setPSedParameter(1.5)
    mat.Stiffness.Pm4Sand.setPostShake(True)
    mat.Stiffness.Pm4Sand.setAutoCalculateFSedMin(False)
    mat.Stiffness.Pm4Sand.setFSedMin(0.6)

    assert(mat.Stiffness.Pm4Sand.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Sand.getVParameter(), 0.2)
    assert(mat.Stiffness.Pm4Sand.getPatmParameter(), 1.3)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateCGDParameter(), True)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculatePSedParameter(), False)
    assert(mat.Stiffness.Pm4Sand.getPSedParameter(), 1.5)
    assert(mat.Stiffness.Pm4Sand.getPostShake(), True)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateFSedMin(), False)
    assert(mat.Stiffness.Pm4Sand.getFSedMin(), 0.6)

def test9():
    mat = mat9

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SAND)
    
    mat.Stiffness.Pm4Sand.setG0Parameter(1.1)
    mat.Stiffness.Pm4Sand.setVParameter(0.2)
    mat.Stiffness.Pm4Sand.setPatmParameter(1.3)
    mat.Stiffness.Pm4Sand.setAutoCalculateCGDParameter(False)
    mat.Stiffness.Pm4Sand.setCGDParameter(1.4)
    mat.Stiffness.Pm4Sand.setAutoCalculatePSedParameter(True)
    mat.Stiffness.Pm4Sand.setPostShake(False)
    mat.Stiffness.Pm4Sand.setAutoCalculateFSedMin(True)

    assert(mat.Stiffness.Pm4Sand.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Sand.getVParameter(), 0.2)
    assert(mat.Stiffness.Pm4Sand.getPatmParameter(), 1.3)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateCGDParameter(), False)
    assert(mat.Stiffness.Pm4Sand.getCGDParameter(), 1.4)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculatePSedParameter(), True)
    assert(mat.Stiffness.Pm4Sand.getPostShake(), False)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateFSedMin(), True)

def test10():
    mat = mat10

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SAND)
    
    mat.Stiffness.Pm4Sand.setG0Parameter(1.1)
    mat.Stiffness.Pm4Sand.setVParameter(0.2)
    mat.Stiffness.Pm4Sand.setPatmParameter(1.3)
    mat.Stiffness.Pm4Sand.setAutoCalculateCGDParameter(True)
    mat.Stiffness.Pm4Sand.setAutoCalculatePSedParameter(True)
    mat.Stiffness.Pm4Sand.setPostShake(False)
    mat.Stiffness.Pm4Sand.setAutoCalculateFSedMin(False)
    mat.Stiffness.Pm4Sand.setFSedMin(0.6)

    assert(mat.Stiffness.Pm4Sand.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Sand.getVParameter(), 0.2)
    assert(mat.Stiffness.Pm4Sand.getPatmParameter(), 1.3)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateCGDParameter(), True)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculatePSedParameter(), True)
    assert(mat.Stiffness.Pm4Sand.getPostShake(), False)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateFSedMin(), False)
    assert(mat.Stiffness.Pm4Sand.getFSedMin(), 0.6)

def test11():
    mat = mat11

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SAND)
    
    mat.Stiffness.Pm4Sand.setG0Parameter(1.1)
    mat.Stiffness.Pm4Sand.setVParameter(0.2)
    mat.Stiffness.Pm4Sand.setPatmParameter(1.3)
    mat.Stiffness.Pm4Sand.setAutoCalculateCGDParameter(False)
    mat.Stiffness.Pm4Sand.setCGDParameter(1.4)
    mat.Stiffness.Pm4Sand.setAutoCalculatePSedParameter(False)
    mat.Stiffness.Pm4Sand.setPSedParameter(1.5)
    mat.Stiffness.Pm4Sand.setPostShake(True)
    mat.Stiffness.Pm4Sand.setAutoCalculateFSedMin(True)

    assert(mat.Stiffness.Pm4Sand.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Sand.getVParameter(), 0.2)
    assert(mat.Stiffness.Pm4Sand.getPatmParameter(), 1.3)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateCGDParameter(), False)
    assert(mat.Stiffness.Pm4Sand.getCGDParameter(), 1.4)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculatePSedParameter(), False)
    assert(mat.Stiffness.Pm4Sand.getPSedParameter(), 1.5)
    assert(mat.Stiffness.Pm4Sand.getPostShake(), True)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateFSedMin(), True)

def test12():
    mat = mat12

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SAND)
    
    mat.Stiffness.Pm4Sand.setG0Parameter(1.1)
    mat.Stiffness.Pm4Sand.setVParameter(0.2)
    mat.Stiffness.Pm4Sand.setPatmParameter(1.3)
    mat.Stiffness.Pm4Sand.setAutoCalculateCGDParameter(True)
    mat.Stiffness.Pm4Sand.setAutoCalculatePSedParameter(False)
    mat.Stiffness.Pm4Sand.setPSedParameter(1.5)
    mat.Stiffness.Pm4Sand.setPostShake(False)
    mat.Stiffness.Pm4Sand.setAutoCalculateFSedMin(True)

    assert(mat.Stiffness.Pm4Sand.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Sand.getVParameter(), 0.2)
    assert(mat.Stiffness.Pm4Sand.getPatmParameter(), 1.3)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateCGDParameter(), True)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculatePSedParameter(), False)
    assert(mat.Stiffness.Pm4Sand.getPSedParameter(), 1.5)
    assert(mat.Stiffness.Pm4Sand.getPostShake(), False)
    assert(mat.Stiffness.Pm4Sand.getAutoCalculateFSedMin(), True)

def test13():
    mat = mat13

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SILT)
    
    mat.Stiffness.Pm4Silt.setG0Parameter(1.1)
    mat.Stiffness.Pm4Silt.setAutoCalculateNGParameter(False)
    mat.Stiffness.Pm4Silt.setNGParameter(1.2)
    mat.Stiffness.Pm4Silt.setAutoCalculateVParameter(False)
    mat.Stiffness.Pm4Silt.setVParameter(0.3)
    mat.Stiffness.Pm4Silt.setPatmParameter(1.4)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGDParameter(False)
    mat.Stiffness.Pm4Silt.setCGDParameter(1.5)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGCParameter(False)
    mat.Stiffness.Pm4Silt.setCGCParameter(1.6)
    mat.Stiffness.Pm4Silt.setPostShake(False)

    assert(mat.Stiffness.Pm4Silt.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateNGParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getNGParameter(), 1.2)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateVParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getVParameter(), 0.3)
    assert(mat.Stiffness.Pm4Silt.getPatmParameter(), 1.4)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGDParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getCGDParameter(), 1.5)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGCParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getCGCParameter(), 1.6)
    assert(mat.Stiffness.Pm4Silt.getPostShake(), False)

def test14():
    mat = mat14

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SILT)
    
    mat.Stiffness.Pm4Silt.setG0Parameter(1.1)
    mat.Stiffness.Pm4Silt.setAutoCalculateNGParameter(True)
    mat.Stiffness.Pm4Silt.setAutoCalculateVParameter(True)
    mat.Stiffness.Pm4Silt.setPatmParameter(1.4)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGDParameter(True)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGCParameter(True)
    mat.Stiffness.Pm4Silt.setPostShake(True)

    assert(mat.Stiffness.Pm4Silt.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateNGParameter(), True)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateVParameter(), True)
    assert(mat.Stiffness.Pm4Silt.getPatmParameter(), 1.4)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGDParameter(), True)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGCParameter(), True)
    assert(mat.Stiffness.Pm4Silt.getPostShake(), True)

def test15():
    mat = mat15

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SILT)
    
    mat.Stiffness.Pm4Silt.setG0Parameter(1.1)
    mat.Stiffness.Pm4Silt.setAutoCalculateNGParameter(True)
    mat.Stiffness.Pm4Silt.setAutoCalculateVParameter(False)
    mat.Stiffness.Pm4Silt.setVParameter(0.3)
    mat.Stiffness.Pm4Silt.setPatmParameter(1.4)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGDParameter(False)
    mat.Stiffness.Pm4Silt.setCGDParameter(1.5)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGCParameter(False)
    mat.Stiffness.Pm4Silt.setCGCParameter(1.6)
    mat.Stiffness.Pm4Silt.setPostShake(False)

    assert(mat.Stiffness.Pm4Silt.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateNGParameter(), True)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateVParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getVParameter(), 0.3)
    assert(mat.Stiffness.Pm4Silt.getPatmParameter(), 1.4)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGDParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getCGDParameter(), 1.5)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGCParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getCGCParameter(), 1.6)
    assert(mat.Stiffness.Pm4Silt.getPostShake(), False)

def test16():
    mat = mat16

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SILT)
    
    mat.Stiffness.Pm4Silt.setG0Parameter(1.1)
    mat.Stiffness.Pm4Silt.setAutoCalculateNGParameter(False)
    mat.Stiffness.Pm4Silt.setNGParameter(1.2)
    mat.Stiffness.Pm4Silt.setAutoCalculateVParameter(True)
    mat.Stiffness.Pm4Silt.setPatmParameter(1.4)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGDParameter(False)
    mat.Stiffness.Pm4Silt.setCGDParameter(1.5)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGCParameter(False)
    mat.Stiffness.Pm4Silt.setCGCParameter(1.6)
    mat.Stiffness.Pm4Silt.setPostShake(False)

    assert(mat.Stiffness.Pm4Silt.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateNGParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getNGParameter(), 1.2)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateVParameter(), True)
    assert(mat.Stiffness.Pm4Silt.getPatmParameter(), 1.4)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGDParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getCGDParameter(), 1.5)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGCParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getCGCParameter(), 1.6)
    assert(mat.Stiffness.Pm4Silt.getPostShake(), False)

def test17():
    mat = mat17

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SILT)
    
    mat.Stiffness.Pm4Silt.setG0Parameter(1.1)
    mat.Stiffness.Pm4Silt.setAutoCalculateNGParameter(False)
    mat.Stiffness.Pm4Silt.setNGParameter(1.2)
    mat.Stiffness.Pm4Silt.setAutoCalculateVParameter(False)
    mat.Stiffness.Pm4Silt.setVParameter(0.3)
    mat.Stiffness.Pm4Silt.setPatmParameter(1.4)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGDParameter(True)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGCParameter(False)
    mat.Stiffness.Pm4Silt.setCGCParameter(1.6)
    mat.Stiffness.Pm4Silt.setPostShake(False)

    assert(mat.Stiffness.Pm4Silt.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateNGParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getNGParameter(), 1.2)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateVParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getVParameter(), 0.3)
    assert(mat.Stiffness.Pm4Silt.getPatmParameter(), 1.4)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGDParameter(), True)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGCParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getCGCParameter(), 1.6)
    assert(mat.Stiffness.Pm4Silt.getPostShake(), False)

def test18():
    mat = mat18

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SILT)
    
    mat.Stiffness.Pm4Silt.setG0Parameter(1.1)
    mat.Stiffness.Pm4Silt.setAutoCalculateNGParameter(False)
    mat.Stiffness.Pm4Silt.setNGParameter(1.2)
    mat.Stiffness.Pm4Silt.setAutoCalculateVParameter(False)
    mat.Stiffness.Pm4Silt.setVParameter(0.3)
    mat.Stiffness.Pm4Silt.setPatmParameter(1.4)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGDParameter(False)
    mat.Stiffness.Pm4Silt.setCGDParameter(1.5)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGCParameter(True)
    mat.Stiffness.Pm4Silt.setPostShake(False)

    assert(mat.Stiffness.Pm4Silt.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateNGParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getNGParameter(), 1.2)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateVParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getVParameter(), 0.3)
    assert(mat.Stiffness.Pm4Silt.getPatmParameter(), 1.4)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGDParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getCGDParameter(), 1.5)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGCParameter(), True)
    assert(mat.Stiffness.Pm4Silt.getPostShake(), False)

def test19():
    mat = mat19

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SILT)
    
    mat.Stiffness.Pm4Silt.setG0Parameter(1.1)
    mat.Stiffness.Pm4Silt.setAutoCalculateNGParameter(False)
    mat.Stiffness.Pm4Silt.setNGParameter(1.2)
    mat.Stiffness.Pm4Silt.setAutoCalculateVParameter(False)
    mat.Stiffness.Pm4Silt.setVParameter(0.3)
    mat.Stiffness.Pm4Silt.setPatmParameter(1.4)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGDParameter(False)
    mat.Stiffness.Pm4Silt.setCGDParameter(1.5)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGCParameter(False)
    mat.Stiffness.Pm4Silt.setCGCParameter(1.6)
    mat.Stiffness.Pm4Silt.setPostShake(True)

    assert(mat.Stiffness.Pm4Silt.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateNGParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getNGParameter(), 1.2)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateVParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getVParameter(), 0.3)
    assert(mat.Stiffness.Pm4Silt.getPatmParameter(), 1.4)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGDParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getCGDParameter(), 1.5)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGCParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getCGCParameter(), 1.6)
    assert(mat.Stiffness.Pm4Silt.getPostShake(), True)

def test20():
    mat = mat20

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SILT)
    
    mat.Stiffness.Pm4Silt.setG0Parameter(1.1)
    mat.Stiffness.Pm4Silt.setAutoCalculateNGParameter(True)
    mat.Stiffness.Pm4Silt.setAutoCalculateVParameter(False)
    mat.Stiffness.Pm4Silt.setVParameter(0.3)
    mat.Stiffness.Pm4Silt.setPatmParameter(1.4)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGDParameter(True)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGCParameter(False)
    mat.Stiffness.Pm4Silt.setCGCParameter(1.6)
    mat.Stiffness.Pm4Silt.setPostShake(True)

    assert(mat.Stiffness.Pm4Silt.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateNGParameter(), True)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateVParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getVParameter(), 0.3)
    assert(mat.Stiffness.Pm4Silt.getPatmParameter(), 1.4)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGDParameter(), True)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGCParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getCGCParameter(), 1.6)
    assert(mat.Stiffness.Pm4Silt.getPostShake(), True)

def test21():
    mat = mat21

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SILT)
    
    mat.Stiffness.Pm4Silt.setG0Parameter(1.1)
    mat.Stiffness.Pm4Silt.setAutoCalculateNGParameter(False)
    mat.Stiffness.Pm4Silt.setNGParameter(1.2)
    mat.Stiffness.Pm4Silt.setAutoCalculateVParameter(True)
    mat.Stiffness.Pm4Silt.setPatmParameter(1.4)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGDParameter(False)
    mat.Stiffness.Pm4Silt.setCGDParameter(1.5)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGCParameter(True)
    mat.Stiffness.Pm4Silt.setPostShake(False)

    assert(mat.Stiffness.Pm4Silt.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateNGParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getNGParameter(), 1.2)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateVParameter(), True)
    assert(mat.Stiffness.Pm4Silt.getPatmParameter(), 1.4)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGDParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getCGDParameter(), 1.5)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGCParameter(), True)
    assert(mat.Stiffness.Pm4Silt.getPostShake(), False)

def test22():
    mat = mat22

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SILT)
    
    mat.Stiffness.Pm4Silt.setG0Parameter(1.1)
    mat.Stiffness.Pm4Silt.setAutoCalculateNGParameter(True)
    mat.Stiffness.Pm4Silt.setAutoCalculateVParameter(True)
    mat.Stiffness.Pm4Silt.setPatmParameter(1.4)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGDParameter(False)
    mat.Stiffness.Pm4Silt.setCGDParameter(1.5)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGCParameter(False)
    mat.Stiffness.Pm4Silt.setCGCParameter(1.6)
    mat.Stiffness.Pm4Silt.setPostShake(False)

    assert(mat.Stiffness.Pm4Silt.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateNGParameter(), True)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateVParameter(), True)
    assert(mat.Stiffness.Pm4Silt.getPatmParameter(), 1.4)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGDParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getCGDParameter(), 1.5)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGCParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getCGCParameter(), 1.6)
    assert(mat.Stiffness.Pm4Silt.getPostShake(), False)

def test23():
    mat = mat23

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SILT)
    
    mat.Stiffness.Pm4Silt.setG0Parameter(1.1)
    mat.Stiffness.Pm4Silt.setAutoCalculateNGParameter(False)
    mat.Stiffness.Pm4Silt.setNGParameter(1.2)
    mat.Stiffness.Pm4Silt.setAutoCalculateVParameter(False)
    mat.Stiffness.Pm4Silt.setVParameter(0.3)
    mat.Stiffness.Pm4Silt.setPatmParameter(1.4)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGDParameter(True)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGCParameter(True)
    mat.Stiffness.Pm4Silt.setPostShake(True)

    assert(mat.Stiffness.Pm4Silt.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateNGParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getNGParameter(), 1.2)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateVParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getVParameter(), 0.3)
    assert(mat.Stiffness.Pm4Silt.getPatmParameter(), 1.4)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGDParameter(), True)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGCParameter(), True)
    assert(mat.Stiffness.Pm4Silt.getPostShake(), True)

def test24():
    mat = mat24

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.PM4_SILT)
    
    mat.Stiffness.Pm4Silt.setG0Parameter(1.1)
    mat.Stiffness.Pm4Silt.setAutoCalculateNGParameter(True)
    mat.Stiffness.Pm4Silt.setAutoCalculateVParameter(True)
    mat.Stiffness.Pm4Silt.setPatmParameter(1.4)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGDParameter(False)
    mat.Stiffness.Pm4Silt.setCGDParameter(1.5)
    mat.Stiffness.Pm4Silt.setAutoCalculateCGCParameter(True)
    mat.Stiffness.Pm4Silt.setPostShake(False)

    assert(mat.Stiffness.Pm4Silt.getG0Parameter(), 1.1)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateNGParameter(), True)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateVParameter(), True)
    assert(mat.Stiffness.Pm4Silt.getPatmParameter(), 1.4)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGDParameter(), False)
    assert(mat.Stiffness.Pm4Silt.getCGDParameter(), 1.5)
    assert(mat.Stiffness.Pm4Silt.getAutoCalculateCGCParameter(), True)
    assert(mat.Stiffness.Pm4Silt.getPostShake(), False)



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