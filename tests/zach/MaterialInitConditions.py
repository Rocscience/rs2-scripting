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

''' This case currently doesn't work since SWM_INTERPOLATED does not exist
def test5():
    mat5.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    mat5.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat5.InitialConditions.setUnitWeight(1.4)
    mat5.InitialConditions.setPorosityValue(0.5)
    mat5.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_INTERPOLATED) 
    mat5.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat5.InitialConditions.setInitialTemperature(1.9)

    assert(mat5.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    assert(mat5.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat5.InitialConditions.getUnitWeight(), 1.4)
    assert(mat5.InitialConditions.getPorosityValue(), 0.5)  
    assert(mat5.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_INTERPOLATED)
    assert(mat5.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat5.InitialConditions.getInitialTemperature(), 1.9)

''' 

def test6():
    mat6.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__BOTH_FIELD_AND_BODY)
    mat6.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat6.InitialConditions.setUnitWeight(1.4)
    mat6.InitialConditions.setPorosityValue(0.5)
    mat6.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_DRY)
    mat6.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat6.InitialConditions.setInitialTemperature(1.9)

    assert(mat6.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__BOTH_FIELD_AND_BODY)
    assert(mat6.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat6.InitialConditions.getUnitWeight(), 1.4)
    assert(mat6.InitialConditions.getPorosityValue(), 0.5)
    assert(mat6.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_DRY)
    assert(mat6.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat6.InitialConditions.getInitialTemperature(), 1.9)

def test7():
    mat7.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__BODY_FORCE_ONLY)
    mat7.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat7.InitialConditions.setUnitWeight(1.4)
    mat7.InitialConditions.setPorosityValue(0.5)
    mat7.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_DRY)
    mat7.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat7.InitialConditions.setInitialTemperature(1.9)

    assert(mat7.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__BODY_FORCE_ONLY)
    assert(mat7.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat7.InitialConditions.getUnitWeight(), 1.4) 
    assert(mat7.InitialConditions.getPorosityValue(), 0.5)
    assert(mat7.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_DRY)
    assert(mat7.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat7.InitialConditions.getInitialTemperature(), 1.9)

def test8():
    mat8.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__NONE)
    mat8.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat8.InitialConditions.setUnitWeight(1.4)
    mat8.InitialConditions.setPorosityValue(0.5)
    mat8.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_DRY)
    mat8.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat8.InitialConditions.setInitialTemperature(1.9)

    assert(mat8.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__NONE)
    assert(mat8.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat8.InitialConditions.getUnitWeight(), 1.4)
    assert(mat8.InitialConditions.getPorosityValue(), 0.5)  
    assert(mat8.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_DRY)
    assert(mat8.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat8.InitialConditions.getInitialTemperature(), 1.9)


test1()
test2()
test3()
test4()
#test6()
test7()
test8()


model.saveAs(final_python_model)

pass