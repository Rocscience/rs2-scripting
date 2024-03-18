from xml.etree.ElementTree import TreeBuilder
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\thermalCapacity_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\thermalCapacity_python.fez'

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
    mat1.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    mat1.Thermal.HeatCapacity.ConstantHeatCapacity.setIncludeLatentHeat(True)
    mat1.Thermal.HeatCapacity.ConstantHeatCapacity.setUnfrozenVolumetricHeatCapacity(1.1)
    mat1.Thermal.HeatCapacity.ConstantHeatCapacity.setFrozenVolumetricHeatCapacity(1.2)
    mat1.Thermal.HeatCapacity.ConstantHeatCapacity.setFrozenTemperature(1.3)

    assert(mat1.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    assert(mat1.Thermal.HeatCapacity.ConstantHeatCapacity.getIncludeLatentHeat(), True)
    assert(mat1.Thermal.HeatCapacity.ConstantHeatCapacity.getUnfrozenVolumetricHeatCapacity(), 1.1)
    assert(mat1.Thermal.HeatCapacity.ConstantHeatCapacity.getFrozenVolumetricHeatCapacity(), 1.2)
    assert(mat1.Thermal.HeatCapacity.ConstantHeatCapacity.getFrozenTemperature(), 1.3)


def test2():
    mat2.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    mat2.Thermal.HeatCapacity.ConstantHeatCapacity.setIncludeLatentHeat(False)
    mat2.Thermal.HeatCapacity.ConstantHeatCapacity.setUnfrozenVolumetricHeatCapacity(1.1)
    mat2.Thermal.HeatCapacity.ConstantHeatCapacity.setFrozenVolumetricHeatCapacity(1.2)
    mat2.Thermal.HeatCapacity.ConstantHeatCapacity.setFrozenTemperature(1.3)

    assert(mat2.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    assert(mat2.Thermal.HeatCapacity.ConstantHeatCapacity.getIncludeLatentHeat(), False)
    assert(mat2.Thermal.HeatCapacity.ConstantHeatCapacity.getUnfrozenVolumetricHeatCapacity(), 1.1)
    assert(mat2.Thermal.HeatCapacity.ConstantHeatCapacity.getFrozenVolumetricHeatCapacity(), 1.2)
    assert(mat2.Thermal.HeatCapacity.ConstantHeatCapacity.getFrozenTemperature(), 1.3)

def test3():
    mat3.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_JAMENEWMAN)
    mat3.Thermal.HeatCapacity.JameNewman.setIncludeLatentHeat(True)
    mat3.Thermal.HeatCapacity.JameNewman.setSoilSpecificHeatCapacity(1.4)

    assert(mat3.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_JAMENEWMAN)
    assert(mat3.Thermal.HeatCapacity.JameNewman.getIncludeLatentHeat(), True)
    assert(mat3.Thermal.HeatCapacity.JameNewman.getSoilSpecificHeatCapacity(), 1.4)

def test4():
    mat4.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_JAMENEWMAN)
    mat4.Thermal.HeatCapacity.JameNewman.setIncludeLatentHeat(False)
    mat4.Thermal.HeatCapacity.JameNewman.setSoilSpecificHeatCapacity(1.4)

    assert(mat4.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_JAMENEWMAN)
    assert(mat4.Thermal.HeatCapacity.JameNewman.getIncludeLatentHeat(), False)
    assert(mat4.Thermal.HeatCapacity.JameNewman.getSoilSpecificHeatCapacity(), 1.4)

def test5():
    mat5.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CUSTOM)
    mat5.Thermal.HeatCapacity.CustomHeatCapacity.setIncludeLatentHeat(True)
    mat5.Thermal.HeatCapacity.CustomHeatCapacity.setDependence(ThermalVolumetricDepencenceType.THERMAL_VOLUMETRIC_DEPENDENCE_TEMPERATURE)
    mat5.Thermal.HeatCapacity.CustomHeatCapacity.setVolumetricHeatCapacityVsTemperatureTable([1.1,1.3],[1.2,1.4])
    
    assert(mat5.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CUSTOM)
    assert(mat5.Thermal.HeatCapacity.CustomHeatCapacity.getIncludeLatentHeat(), True)
    assert(mat5.Thermal.HeatCapacity.CustomHeatCapacity.getDependence(), ThermalVolumetricDepencenceType.THERMAL_VOLUMETRIC_DEPENDENCE_TEMPERATURE)
    assert(mat5.Thermal.HeatCapacity.CustomHeatCapacity.getVolumetricHeatCapacityVsTemperatureTable(), ([1.1,1.3],[1.2,1.4]))

def test6():
    mat6.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CUSTOM)
    mat6.Thermal.HeatCapacity.CustomHeatCapacity.setIncludeLatentHeat(False)
    mat6.Thermal.HeatCapacity.CustomHeatCapacity.setDependence(ThermalVolumetricDepencenceType.THERMAL_VOLUMETRIC_DEPENDENCE_TEMPERATURE)
    mat6.Thermal.HeatCapacity.CustomHeatCapacity.setVolumetricHeatCapacityVsTemperatureTable([1.1,1.3],[1.2,1.4])

    assert(mat6.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CUSTOM)
    assert(mat6.Thermal.HeatCapacity.CustomHeatCapacity.getIncludeLatentHeat(), False)
    assert(mat6.Thermal.HeatCapacity.CustomHeatCapacity.getDependence(), ThermalVolumetricDepencenceType.THERMAL_VOLUMETRIC_DEPENDENCE_TEMPERATURE)
    assert(mat6.Thermal.HeatCapacity.CustomHeatCapacity.getVolumetricHeatCapacityVsTemperatureTable(), ([1.1,1.3],[1.2,1.4]))

def test7():
    mat7.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CUSTOM)
    mat7.Thermal.HeatCapacity.CustomHeatCapacity.setIncludeLatentHeat(True)
    mat7.Thermal.HeatCapacity.CustomHeatCapacity.setDependence(ThermalVolumetricDepencenceType.THERMAL_VOLUMETRIC_DEPENDENCE_WATER_CONTENT)
    mat7.Thermal.HeatCapacity.CustomHeatCapacity.setVolumetricHeatCapacityVsWaterContentTable([1.1,1.3],[0.2,0.4])

    assert(mat7.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CUSTOM)
    assert(mat7.Thermal.HeatCapacity.CustomHeatCapacity.getIncludeLatentHeat(), True)
    assert(mat7.Thermal.HeatCapacity.CustomHeatCapacity.getDependence(), ThermalVolumetricDepencenceType.THERMAL_VOLUMETRIC_DEPENDENCE_WATER_CONTENT)
    assert(mat7.Thermal.HeatCapacity.CustomHeatCapacity.getVolumetricHeatCapacityVsWaterContentTable(), ([1.1,1.3],[0.2,0.4]))

def test8():
    mat8.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CUSTOM)
    mat8.Thermal.HeatCapacity.CustomHeatCapacity.setIncludeLatentHeat(False)
    mat8.Thermal.HeatCapacity.CustomHeatCapacity.setDependence(ThermalVolumetricDepencenceType.THERMAL_VOLUMETRIC_DEPENDENCE_WATER_CONTENT)
    mat8.Thermal.HeatCapacity.CustomHeatCapacity.setVolumetricHeatCapacityVsWaterContentTable([1.1,1.3],[0.2,0.4])

    assert(mat8.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CUSTOM)
    assert(mat8.Thermal.HeatCapacity.CustomHeatCapacity.getIncludeLatentHeat(), False)
    assert(mat8.Thermal.HeatCapacity.CustomHeatCapacity.getDependence(), ThermalVolumetricDepencenceType.THERMAL_VOLUMETRIC_DEPENDENCE_WATER_CONTENT)
    assert(mat8.Thermal.HeatCapacity.CustomHeatCapacity.getVolumetricHeatCapacityVsWaterContentTable(), ([1.1,1.3],[0.2,0.4]))


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