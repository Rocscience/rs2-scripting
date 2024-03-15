from xml.etree.ElementTree import TreeBuilder
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\thermalType_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\thermalType_python.fez'

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

def test1():
    mat1.Thermal.setStaticTemperatureMode(StaticWaterModes.SWM_PWP)
    mat1.Thermal.setStaticTemperature(1.1)
    mat1.Thermal.setWaterContent(ThermalWaterContentMethodType.THERMAL_WATER_CONTENT_FROM_GROUNDWATER)

    assert(mat1.Thermal.getStaticTemperatureMode(), StaticWaterModes.SWM_PWP)
    assert(mat1.Thermal.getStaticTemperature(), 1.1)
    assert(mat1.Thermal.getWaterContent(), ThermalWaterContentMethodType.THERMAL_WATER_CONTENT_FROM_GROUNDWATER)

def test2():
    mat2.Thermal.setStaticTemperatureMode(StaticWaterModes.SWM_PWP)
    mat2.Thermal.setStaticTemperature(1.1)
    mat2.Thermal.setWaterContent(ThermalWaterContentMethodType.THERMAL_WATER_CONTENT_DEFINE)
    mat2.Thermal.setWaterContentValue(0.2)

    assert(mat2.Thermal.getStaticTemperatureMode(), StaticWaterModes.SWM_PWP)
    assert(mat2.Thermal.getStaticTemperature(), 1.1)  
    assert(mat2.Thermal.getWaterContent(), ThermalWaterContentMethodType.THERMAL_WATER_CONTENT_DEFINE)
    assert(mat2.Thermal.getWaterContentValue(), 0.2)


def test3():
    mat3.Thermal.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    mat3.Thermal.setStaticTemperatureGridToUseByName('None')
    mat3.Thermal.setWaterContent(ThermalWaterContentMethodType.THERMAL_WATER_CONTENT_FROM_GROUNDWATER)

    assert(mat3.Thermal.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(mat3.Thermal.getStaticTemperatureGridToUse(), 'None')
    assert(mat3.Thermal.getWaterContent(), ThermalWaterContentMethodType.THERMAL_WATER_CONTENT_FROM_GROUNDWATER)



def test4():
    mat4.Thermal.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    mat4.Thermal.setStaticTemperatureGridToUseByName('Default Grid')
    mat4.Thermal.setWaterContent(ThermalWaterContentMethodType.THERMAL_WATER_CONTENT_FROM_GROUNDWATER)

    assert(mat4.Thermal.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(mat4.Thermal.getStaticTemperatureGridToUse(), 'Default Grid')
    assert(mat4.Thermal.getWaterContent(), ThermalWaterContentMethodType.THERMAL_WATER_CONTENT_FROM_GROUNDWATER)

def test5():
    mat5.Thermal.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    mat5.Thermal.setStaticTemperatureGridToUseByName('Grid 3')
    mat5.Thermal.setWaterContent(ThermalWaterContentMethodType.THERMAL_WATER_CONTENT_FROM_GROUNDWATER)

    assert(mat5.Thermal.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(mat5.Thermal.getStaticTemperatureGridToUse(), 'Grid 3')
    assert(mat5.Thermal.getWaterContent(), ThermalWaterContentMethodType.THERMAL_WATER_CONTENT_FROM_GROUNDWATER)

def test6():
    mat6.Thermal.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    mat6.Thermal.setStaticTemperatureGridToUseByName('None')
    mat6.Thermal.setWaterContent(ThermalWaterContentMethodType.THERMAL_WATER_CONTENT_DEFINE)
    mat6.Thermal.setWaterContentValue(0.2)
    
    assert(mat6.Thermal.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(mat6.Thermal.getStaticTemperatureGridToUse(), 'None')
    assert(mat6.Thermal.getWaterContent(), ThermalWaterContentMethodType.THERMAL_WATER_CONTENT_DEFINE)
    assert(mat6.Thermal.getWaterContentValue(), 0.2)

def test7():
    mat7.Thermal.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    mat7.Thermal.setStaticTemperatureGridToUseByName('Default Grid')
    mat7.Thermal.setWaterContent(ThermalWaterContentMethodType.THERMAL_WATER_CONTENT_DEFINE)
    mat7.Thermal.setWaterContentValue(0.2)

    assert(mat7.Thermal.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(mat7.Thermal.getStaticTemperatureGridToUse(), 'Default Grid')
    assert(mat7.Thermal.getWaterContent(), ThermalWaterContentMethodType.THERMAL_WATER_CONTENT_DEFINE)
    assert(mat7.Thermal.getWaterContentValue(), 0.2)

def test8():
    mat8.Thermal.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    mat8.Thermal.setStaticTemperatureGridToUseByName('Grid 3')
    mat8.Thermal.setWaterContent(ThermalWaterContentMethodType.THERMAL_WATER_CONTENT_DEFINE)
    mat8.Thermal.setWaterContentValue(0.2)

    assert(mat8.Thermal.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(mat8.Thermal.getStaticTemperatureGridToUse(), 'Grid 3')
    assert(mat8.Thermal.getWaterContent(), ThermalWaterContentMethodType.THERMAL_WATER_CONTENT_DEFINE)
    assert(mat8.Thermal.getWaterContentValue(), 0.2)

test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()

model.save()

pass