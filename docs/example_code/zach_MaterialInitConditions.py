from xml.etree.ElementTree import TreeBuilder
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\initConditions_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\initConditions_python.fez'

modeler = RS2Modeler()

model = modeler.openFile(base_model)

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

def test1():
    mat1.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    mat1.InitialConditions.setAccountForMoistureContentInUnitWeight(True)
    mat1.InitialConditions.setSaturatedUnitWeight(1.3)
    mat1.InitialConditions.setMoistUnitWeight(1.2)
    mat1.InitialConditions.setDryUnitWeight(1.1)
    mat1.InitialConditions.setPorosityValue(0.5)
    mat1.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_DRY)
    mat1.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat1.InitialConditions.setInitialTemperature(1.9)

    assert(mat1.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    assert(mat1.InitialConditions.getAccountForMoistureContentInUnitWeight(), True)
    assert(mat1.InitialConditions.getDryUnitWeight(), 1.1)
    assert(mat1.InitialConditions.getMoistUnitWeight(), 1.2)
    assert(mat1.InitialConditions.getSaturatedUnitWeight(), 1.3)
    assert(mat1.InitialConditions.getPorosityValue(), 0.5)
    assert(mat1.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_DRY)
    assert(mat1.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat1.InitialConditions.getInitialTemperature(), 1.9)

def test2():
    mat2.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    mat2.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat2.InitialConditions.setUnitWeight(1.4)
    mat2.InitialConditions.setPorosityValue(0.5)
    mat2.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_DRY)
    mat2.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat2.InitialConditions.setInitialTemperature(1.9)

    assert(mat2.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    assert(mat2.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)  
    assert(mat2.InitialConditions.getUnitWeight(), 1.4)
    assert(mat2.InitialConditions.getPorosityValue(), 0.5)
    assert(mat2.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_DRY)
    assert(mat2.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat2.InitialConditions.getInitialTemperature(), 1.9)

def test3():
    mat3.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    mat3.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat3.InitialConditions.setUnitWeight(1.4)
    mat3.InitialConditions.setPorosityValue(0.5)
    mat3.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_PWP)
    mat3.InitialConditions.setInitialPoreWaterPressure(1.6)
    mat3.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat3.InitialConditions.setInitialTemperature(1.9)

    assert(mat3.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    assert(mat3.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat3.InitialConditions.getUnitWeight(), 1.4)
    assert(mat3.InitialConditions.getPorosityValue(), 0.5)  
    assert(mat3.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_PWP)
    assert(mat3.InitialConditions.getInitialPoreWaterPressure(), 1.6)
    assert(mat3.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat3.InitialConditions.getInitialTemperature(), 1.9)

def test4():
    mat4.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    mat4.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat4.InitialConditions.setUnitWeight(1.4)
    mat4.InitialConditions.setPorosityValue(0.5)
    mat4.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_RU)
    mat4.InitialConditions.setInitialRu(1.7)
    mat4.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat4.InitialConditions.setInitialTemperature(1.9)

    assert(mat4.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    assert(mat4.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat4.InitialConditions.getUnitWeight(), 1.4)
    assert(mat4.InitialConditions.getPorosityValue(), 0.5)
    assert(mat4.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_RU)
    assert(mat4.InitialConditions.getInitialRu(), 1.7)
    assert(mat4.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat4.InitialConditions.getInitialTemperature(), 1.9)

def test5():
    mat5.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    mat5.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat5.InitialConditions.setUnitWeight(1.4)
    mat5.InitialConditions.setPorosityValue(0.5)
    mat5.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_PIEZO)
    mat5.InitialConditions.setInitialPiezoByName("1")
    mat5.InitialConditions.setInitialHuType(HuTypes.HT_CUSTOM)
    mat5.InitialConditions.setInitialHu(1.8)
    mat5.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat5.InitialConditions.setInitialTemperature(1.9)

    assert(mat5.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    assert(mat5.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat5.InitialConditions.getUnitWeight(), 1.4)  
    assert(mat5.InitialConditions.getPorosityValue(), 0.5)
    assert(mat5.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_PIEZO)
    assert(mat5.InitialConditions.getInitialPiezoName(), "1")
    assert(mat5.InitialConditions.getInitialHuType(), HuTypes.HT_CUSTOM)
    assert(mat5.InitialConditions.getInitialHu(), 1.8)
    assert(mat5.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat5.InitialConditions.getInitialTemperature(), 1.9)

def test6():
    mat6.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    mat6.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat6.InitialConditions.setUnitWeight(1.4)
    mat6.InitialConditions.setPorosityValue(0.5)
    mat6.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_PIEZO)
    mat6.InitialConditions.setInitialPiezoByName("1")
    mat6.InitialConditions.setInitialHuType(HuTypes.HT_AUTO)
    mat6.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat6.InitialConditions.setInitialTemperature(1.9)

    assert(mat6.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    assert(mat6.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat6.InitialConditions.getUnitWeight(), 1.4)
    assert(mat6.InitialConditions.getPorosityValue(), 0.5)
    assert(mat6.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_PIEZO)  
    assert(mat6.InitialConditions.getInitialPiezoName(), "1")
    assert(mat6.InitialConditions.getInitialHuType(), HuTypes.HT_AUTO)
    assert(mat6.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat6.InitialConditions.getInitialTemperature(), 1.9)

def test7():
    mat7.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    mat7.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat7.InitialConditions.setUnitWeight(1.4)
    mat7.InitialConditions.setPorosityValue(0.5)
    mat7.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_GRID)
    mat7.InitialConditions.setInitialGridByName("Default Grid")
    mat7.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat7.InitialConditions.setInitialTemperature(1.9)

    assert(mat7.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    assert(mat7.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat7.InitialConditions.getUnitWeight(), 1.4)
    assert(mat7.InitialConditions.getPorosityValue(), 0.5)
    assert(mat7.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_GRID)
    assert(mat7.InitialConditions.getInitialGridName(), "Default Grid")
    assert(mat7.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat7.InitialConditions.getInitialTemperature(), 1.9)

''' This case currently doesn't work since SWM_INTERPOLATED does not exist
def test8():
    mat8.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    mat8.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat8.InitialConditions.setUnitWeight(1.4)
    mat8.InitialConditions.setPorosityValue(0.5)
    mat8.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_INTERPOLATED) 
    mat8.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat8.InitialConditions.setInitialTemperature(1.9)

    assert(mat8.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    assert(mat8.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat8.InitialConditions.getUnitWeight(), 1.4)
    assert(mat8.InitialConditions.getPorosityValue(), 0.5)  
    assert(mat8.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_INTERPOLATED)
    assert(mat8.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat8.InitialConditions.getInitialTemperature(), 1.9)

''' 

def test9():
    mat9.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    mat9.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat9.InitialConditions.setUnitWeight(1.4)
    mat9.InitialConditions.setPorosityValue(0.5)
    mat9.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_DRY)
    mat9.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_GRID)
    mat9.InitialConditions.setInitialTemperatureGridByName('Default Grid')

    
    assert(mat9.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    assert(mat9.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat9.InitialConditions.getUnitWeight(), 1.4)
    assert(mat9.InitialConditions.getPorosityValue(), 0.5)
    assert(mat9.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_DRY)
    assert(mat9.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_GRID) 
    assert(mat9.InitialConditions.getInitialTemperatureGridName(), 'Default Grid')

def test10():
    mat10.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__BOTH_FIELD_AND_BODY)
    mat10.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat10.InitialConditions.setUnitWeight(1.4)
    mat10.InitialConditions.setPorosityValue(0.5)
    mat10.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_DRY)
    mat10.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat10.InitialConditions.setInitialTemperature(1.9)

    assert(mat10.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__BOTH_FIELD_AND_BODY)
    assert(mat10.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat10.InitialConditions.getUnitWeight(), 1.4)
    assert(mat10.InitialConditions.getPorosityValue(), 0.5)
    assert(mat10.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_DRY)
    assert(mat10.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat10.InitialConditions.getInitialTemperature(), 1.9)

def test11():
    mat11.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__BODY_FORCE_ONLY)
    mat11.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat11.InitialConditions.setUnitWeight(1.4)
    mat11.InitialConditions.setPorosityValue(0.5)
    mat11.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_DRY)
    mat11.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat11.InitialConditions.setInitialTemperature(1.9)

    assert(mat11.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__BODY_FORCE_ONLY)
    assert(mat11.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat11.InitialConditions.getUnitWeight(), 1.4) 
    assert(mat11.InitialConditions.getPorosityValue(), 0.5)
    assert(mat11.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_DRY)
    assert(mat11.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat11.InitialConditions.getInitialTemperature(), 1.9)

def test12():
    mat12.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__NONE)
    mat12.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat12.InitialConditions.setUnitWeight(1.4)
    mat12.InitialConditions.setPorosityValue(0.5)
    mat12.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_DRY)
    mat12.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat12.InitialConditions.setInitialTemperature(1.9)

    assert(mat12.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__NONE)
    assert(mat12.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat12.InitialConditions.getUnitWeight(), 1.4)
    assert(mat12.InitialConditions.getPorosityValue(), 0.5)  
    assert(mat12.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_DRY)
    assert(mat12.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat12.InitialConditions.getInitialTemperature(), 1.9)

def test13():
    mat13.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    mat13.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat13.InitialConditions.setUnitWeight(1.4)
    mat13.InitialConditions.setPorosityValue(0.5)
    mat13.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_GRID)
    mat13.InitialConditions.setInitialGridByName("None")
    mat13.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat13.InitialConditions.setInitialTemperature(1.9)

    assert(mat13.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    assert(mat13.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat13.InitialConditions.getUnitWeight(), 1.4)
    assert(mat13.InitialConditions.getPorosityValue(), 0.5)
    assert(mat13.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_GRID)
    assert(mat13.InitialConditions.getInitialGridName(), "None")
    assert(mat13.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat13.InitialConditions.getInitialTemperature(), 1.9)

def test14():
    mat14.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    mat14.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat14.InitialConditions.setUnitWeight(1.4)
    mat14.InitialConditions.setPorosityValue(0.5)
    mat14.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_DRY)
    mat14.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_GRID)
    mat14.InitialConditions.setInitialTemperatureGridByName('None')

    
    assert(mat14.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    assert(mat14.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat14.InitialConditions.getUnitWeight(), 1.4)
    assert(mat14.InitialConditions.getPorosityValue(), 0.5)
    assert(mat14.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_DRY)
    assert(mat14.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_GRID) 
    assert(mat14.InitialConditions.getInitialTemperatureGridName(), 'None')

test1()
test2()
test3()
test4()
test5()
test6()
test7()
test9()
test10()
test11()
test12()
test13()
test14()

model.saveAs(final_python_model)

pass