from xml.etree.ElementTree import TreeBuilder
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_thermalGrid.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\initConditionsThermalGrid_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\initConditionsThermalGrid_python.fez'

modeler = RS2Modeler()

model = modeler.openFile(base_model)

matList = model.getAllMaterialProperties()
mat1 = matList[0]
mat2 = matList[1]
mat3 = matList[2]



def test1():
    mat1.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    mat1.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat1.InitialConditions.setUnitWeight(1.4)
    mat1.InitialConditions.setPorosityValue(0.5)
    mat1.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_DRY)
    mat1.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_GRID)
    mat1.InitialConditions.setInitialTemperatureGridByName('None')

    
    assert(mat1.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    assert(mat1.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat1.InitialConditions.getUnitWeight(), 1.4)
    assert(mat1.InitialConditions.getPorosityValue(), 0.5)
    assert(mat1.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_DRY)
    assert(mat1.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_GRID) 
    assert(mat1.InitialConditions.getInitialTemperatureGridName(), 'None')

def test2():
    mat2.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    mat2.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat2.InitialConditions.setUnitWeight(1.4)
    mat2.InitialConditions.setPorosityValue(0.5)
    mat2.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_DRY)
    mat2.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_GRID)
    mat2.InitialConditions.setInitialTemperatureGridByName('Default Grid')

    
    assert(mat2.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    assert(mat2.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat2.InitialConditions.getUnitWeight(), 1.4)
    assert(mat2.InitialConditions.getPorosityValue(), 0.5)
    assert(mat2.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_DRY)
    assert(mat2.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_GRID) 
    assert(mat2.InitialConditions.getInitialTemperatureGridName(), 'Default Grid')

def test3():
    mat3.InitialConditions.setInitialElementLoading(InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    mat3.InitialConditions.setAccountForMoistureContentInUnitWeight(False)
    mat3.InitialConditions.setUnitWeight(1.4)
    mat3.InitialConditions.setPorosityValue(0.5)
    mat3.InitialConditions.setInitialWaterCondition(StaticWaterModes.SWM_DRY)
    mat3.InitialConditions.setInitialTemperatureCondition(StaticWaterModes.SWM_GRID)
    mat3.InitialConditions.setInitialTemperatureGridByName('Grid 3')

    
    assert(mat3.InitialConditions.getInitialElementLoading(), InitialElementLoadingType.INITIAL_MAT_LOADING__FIELD_STRESS_ONLY)
    assert(mat3.InitialConditions.getAccountForMoistureContentInUnitWeight(), False)
    assert(mat3.InitialConditions.getUnitWeight(), 1.4)
    assert(mat3.InitialConditions.getPorosityValue(), 0.5)
    assert(mat3.InitialConditions.getInitialWaterCondition(), StaticWaterModes.SWM_DRY)
    assert(mat3.InitialConditions.getInitialTemperatureCondition(), StaticWaterModes.SWM_GRID) 
    assert(mat3.InitialConditions.getInitialTemperatureGridName(), 'Grid 3')

test1()
test2()
test3()

model.saveAs(final_python_model)

pass