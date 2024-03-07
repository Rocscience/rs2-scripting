from xml.etree.ElementTree import TreeBuilder
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_piezo.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\initConditionsPiezo_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\initConditionsPiezo_python.fez'

modeler = RS2Modeler()

model = modeler.openFile(base_model)

matList = model.getAllMaterialProperties()
mat1 = matList[0]
mat2 = matList[1]
mat3 = matList[2]
mat4 = matList[3]
mat5 = matList[4]

def test1():
    mat1.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__BOTH_FIELD_AND_BODY)
    mat1.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat1.InitialConditions.setUnitWeight(1.4)
    mat1.InitialConditions.setPorosityValue(0.5)
    mat1.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_PIEZO)
    mat1.InitialConditions.setInitialPiezoByName("None")
    mat1.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat1.InitialConditions.setInitialTemperature(1.9)

    assert(mat1.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__BOTH_FIELD_AND_BODY)
    assert(mat1.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat1.InitialConditions.getUnitWeight(), 1.4)  
    assert(mat1.InitialConditions.getPorosityValue(), 0.5)
    assert(mat1.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_PIEZO)
    assert(mat1.InitialConditions.getInitialPiezoName(), "None")
    assert(mat1.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat1.InitialConditions.getInitialTemperature(), 1.9)

def test2():
    mat2.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__BOTH_FIELD_AND_BODY)
    mat2.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat2.InitialConditions.setUnitWeight(1.4)
    mat2.InitialConditions.setPorosityValue(0.5)
    mat2.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_PIEZO)
    mat2.InitialConditions.setInitialPiezoByName("1")
    mat2.InitialConditions.setInitialHuType(HuTypes.HT_CUSTOM)
    mat2.InitialConditions.setInitialHu(1.8)
    mat2.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat2.InitialConditions.setInitialTemperature(1.9)

    assert(mat2.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__BOTH_FIELD_AND_BODY)
    assert(mat2.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat2.InitialConditions.getUnitWeight(), 1.4)  
    assert(mat2.InitialConditions.getPorosityValue(), 0.5)
    assert(mat2.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_PIEZO)
    assert(mat2.InitialConditions.getInitialPiezoName(), "1")
    assert(mat2.InitialConditions.getInitialHuType(), HuTypes.HT_CUSTOM)
    assert(mat2.InitialConditions.getInitialHu(),1.8)
    assert(mat2.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat2.InitialConditions.getInitialTemperature(), 1.9)

def test3():
    mat3.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__BOTH_FIELD_AND_BODY)
    mat3.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat3.InitialConditions.setUnitWeight(1.4)
    mat3.InitialConditions.setPorosityValue(0.5)
    mat3.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_PIEZO)
    mat3.InitialConditions.setInitialPiezoByName("1")
    mat3.InitialConditions.setInitialHuType(HuTypes.HT_AUTO)
    mat3.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat3.InitialConditions.setInitialTemperature(1.9)

    assert(mat3.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__BOTH_FIELD_AND_BODY)
    assert(mat3.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat3.InitialConditions.getUnitWeight(), 1.4)  
    assert(mat3.InitialConditions.getPorosityValue(), 0.5)
    assert(mat3.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_PIEZO)
    assert(mat3.InitialConditions.getInitialPiezoName(), "1")
    assert(mat3.InitialConditions.getInitialHuType(), HuTypes.HT_AUTO)
    assert(mat3.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat3.InitialConditions.getInitialTemperature(), 1.9)

def test4():
    mat4.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__BOTH_FIELD_AND_BODY)
    mat4.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat4.InitialConditions.setUnitWeight(1.4)
    mat4.InitialConditions.setPorosityValue(0.5)
    mat4.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_PIEZO)
    mat4.InitialConditions.setInitialPiezoByName("3")
    mat4.InitialConditions.setInitialHuType(HuTypes.HT_CUSTOM)
    mat4.InitialConditions.setInitialHu(1.8)
    mat4.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat4.InitialConditions.setInitialTemperature(1.9)

    assert(mat4.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__BOTH_FIELD_AND_BODY)
    assert(mat4.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat4.InitialConditions.getUnitWeight(), 1.4)  
    assert(mat4.InitialConditions.getPorosityValue(), 0.5)
    assert(mat4.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_PIEZO)
    assert(mat4.InitialConditions.getInitialPiezoName(), "3")
    assert(mat4.InitialConditions.getInitialHuType(), HuTypes.HT_CUSTOM)
    assert(mat4.InitialConditions.getInitialHu(),1.8)
    assert(mat4.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat4.InitialConditions.getInitialTemperature(), 1.9)

def test5():
    mat5.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__BOTH_FIELD_AND_BODY)
    mat5.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat5.InitialConditions.setUnitWeight(1.4)
    mat5.InitialConditions.setPorosityValue(0.5)
    mat5.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_PIEZO)
    mat5.InitialConditions.setInitialPiezoByName("3")
    mat5.InitialConditions.setInitialHuType(HuTypes.HT_AUTO)
    mat5.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_PWP)
    mat5.InitialConditions.setInitialTemperature(1.9)

    assert(mat5.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__BOTH_FIELD_AND_BODY)
    assert(mat5.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat5.InitialConditions.getUnitWeight(), 1.4)  
    assert(mat5.InitialConditions.getPorosityValue(), 0.5)
    assert(mat5.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_PIEZO)
    assert(mat5.InitialConditions.getInitialPiezoName(), "3")
    assert(mat5.InitialConditions.getInitialHuType(), HuTypes.HT_AUTO)
    assert(mat5.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_PWP)
    assert(mat5.InitialConditions.getInitialTemperature(), 1.9)

test1()
test2()
test3()
test4()
test5()

model.saveAs(final_python_model)

pass