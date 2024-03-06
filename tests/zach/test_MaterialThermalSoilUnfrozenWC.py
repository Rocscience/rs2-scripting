from xml.etree.ElementTree import TreeBuilder
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\thermalSoilUnfrozenWC_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\thermalSoilUnfrozenWC_python.fez'

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

def test1():
    mat1.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    mat1.Thermal.HeatCapacity.ConstantHeatCapacity.setIncludeLatentHeat(True)
    mat1.Thermal.SoilUnfrozenWaterContent.setType(ThermalWaterContentType.THERMAL_WATER_CONTENT_KONRAD)
    mat1.Thermal.SoilUnfrozenWaterContent.Konrad.setResidualWaterContent(0.1)
    mat1.Thermal.SoilUnfrozenWaterContent.Konrad.setFrozenTemperature(1.2)
    mat1.Thermal.SoilUnfrozenWaterContent.Konrad.setSolidusTemperature(1.3)

    assert(mat1.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    assert(mat1.Thermal.HeatCapacity.ConstantHeatCapacity.getIncludeLatentHeat(), True)
    assert(mat1.Thermal.SoilUnfrozenWaterContent.getType(), ThermalWaterContentType.THERMAL_WATER_CONTENT_KONRAD)
    assert(mat1.Thermal.SoilUnfrozenWaterContent.Konrad.getResidualWaterContent(), 0.1)
    assert(mat1.Thermal.SoilUnfrozenWaterContent.Konrad.getFrozenTemperature(), 1.2)
    assert(mat1.Thermal.SoilUnfrozenWaterContent.Konrad.getSolidusTemperature(), 1.3)

def test2():
    mat2.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    mat2.Thermal.HeatCapacity.ConstantHeatCapacity.setIncludeLatentHeat(True)
    mat2.Thermal.SoilUnfrozenWaterContent.setType(ThermalWaterContentType.THERMAL_WATER_CONTENT_TICE_ANDERSON)
    mat2.Thermal.SoilUnfrozenWaterContent.TiceAnderson.setInputAlpha(1.4)
    mat2.Thermal.SoilUnfrozenWaterContent.TiceAnderson.setInputBeta(1.5)
    mat2.Thermal.SoilUnfrozenWaterContent.TiceAnderson.setFrozenTemperature(1.2)

    assert(mat2.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)  
    assert(mat2.Thermal.HeatCapacity.ConstantHeatCapacity.getIncludeLatentHeat(), True)
    assert(mat2.Thermal.SoilUnfrozenWaterContent.getType(), ThermalWaterContentType.THERMAL_WATER_CONTENT_TICE_ANDERSON)
    assert(mat2.Thermal.SoilUnfrozenWaterContent.TiceAnderson.getInputAlpha(), 1.4)
    assert(mat2.Thermal.SoilUnfrozenWaterContent.TiceAnderson.getInputBeta(), 1.5)
    assert(mat2.Thermal.SoilUnfrozenWaterContent.TiceAnderson.getFrozenTemperature(), 1.2)

def test3():
    mat3.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    mat3.Thermal.HeatCapacity.ConstantHeatCapacity.setIncludeLatentHeat(True)
    mat3.Thermal.SoilUnfrozenWaterContent.setType(ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)
    mat3.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setFrozenTemperature(1.2)
    mat3.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setSelectHydraulicModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat3.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCSat(0.06)
    mat3.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCRes(0.07)
    mat3.Thermal.SoilUnfrozenWaterContent.HydraulicModel.SimpleWaterContent.setSoilType(EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_GENERAL)

    assert(mat3.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    assert(mat3.Thermal.HeatCapacity.ConstantHeatCapacity.getIncludeLatentHeat(), True)
    assert(mat3.Thermal.SoilUnfrozenWaterContent.getType(), ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)  
    assert(mat3.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getFrozenTemperature(), 1.2)
    assert(mat3.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getSelectHydraulicModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)
    assert(mat3.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCSat(), 0.06) 
    assert(mat3.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCRes(), 0.07)
    assert(mat3.Thermal.SoilUnfrozenWaterContent.HydraulicModel.SimpleWaterContent.getSoilType(), EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_GENERAL)

def test4():
    mat4.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    mat4.Thermal.HeatCapacity.ConstantHeatCapacity.setIncludeLatentHeat(True)
    mat4.Thermal.SoilUnfrozenWaterContent.setType(ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)
    mat4.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setFrozenTemperature(1.2)
    mat4.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setSelectHydraulicModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat4.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCSat(0.06)
    mat4.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCRes(0.07)
    mat4.Thermal.SoilUnfrozenWaterContent.HydraulicModel.SimpleWaterContent.setSoilType(EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_SAND)

    assert(mat4.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    assert(mat4.Thermal.HeatCapacity.ConstantHeatCapacity.getIncludeLatentHeat(), True) 
    assert(mat4.Thermal.SoilUnfrozenWaterContent.getType(), ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)
    assert(mat4.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getFrozenTemperature(), 1.2)
    assert(mat4.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getSelectHydraulicModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)  
    assert(mat4.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCSat(), 0.06)
    assert(mat4.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCRes(), 0.07) 
    assert(mat4.Thermal.SoilUnfrozenWaterContent.HydraulicModel.SimpleWaterContent.getSoilType(), EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_SAND)

def test5():
    mat5.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    mat5.Thermal.HeatCapacity.ConstantHeatCapacity.setIncludeLatentHeat(True)
    mat5.Thermal.SoilUnfrozenWaterContent.setType(ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)
    mat5.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setFrozenTemperature(1.2)
    mat5.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setSelectHydraulicModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat5.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCSat(0.06)
    mat5.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCRes(0.07)
    mat5.Thermal.SoilUnfrozenWaterContent.HydraulicModel.SimpleWaterContent.setSoilType(EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_SILT)

    assert(mat5.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    assert(mat5.Thermal.HeatCapacity.ConstantHeatCapacity.getIncludeLatentHeat(), True)
    assert(mat5.Thermal.SoilUnfrozenWaterContent.getType(), ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL) 
    assert(mat5.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getFrozenTemperature(), 1.2)
    assert(mat5.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getSelectHydraulicModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)
    assert(mat5.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCSat(), 0.06)
    assert(mat5.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCRes(), 0.07)
    assert(mat5.Thermal.SoilUnfrozenWaterContent.HydraulicModel.SimpleWaterContent.getSoilType(), EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_SILT)

def test6():
    mat6.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    mat6.Thermal.HeatCapacity.ConstantHeatCapacity.setIncludeLatentHeat(True)
    mat6.Thermal.SoilUnfrozenWaterContent.setType(ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)
    mat6.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setFrozenTemperature(1.2)
    mat6.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setSelectHydraulicModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat6.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCSat(0.06)
    mat6.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCRes(0.07)
    mat6.Thermal.SoilUnfrozenWaterContent.HydraulicModel.SimpleWaterContent.setSoilType(EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_CLAY)

    assert(mat6.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)  
    assert(mat6.Thermal.HeatCapacity.ConstantHeatCapacity.getIncludeLatentHeat(), True)
    assert(mat6.Thermal.SoilUnfrozenWaterContent.getType(), ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)
    assert(mat6.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getFrozenTemperature(), 1.2) 
    assert(mat6.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getSelectHydraulicModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)
    assert(mat6.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCSat(), 0.06)
    assert(mat6.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCRes(), 0.07)
    assert(mat6.Thermal.SoilUnfrozenWaterContent.HydraulicModel.SimpleWaterContent.getSoilType(), EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_CLAY)


def test7():
    mat7.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    mat7.Thermal.HeatCapacity.ConstantHeatCapacity.setIncludeLatentHeat(True)
    mat7.Thermal.SoilUnfrozenWaterContent.setType(ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)
    mat7.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setFrozenTemperature(1.2)
    mat7.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setSelectHydraulicModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat7.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCSat(0.06)
    mat7.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCRes(0.07)
    mat7.Thermal.SoilUnfrozenWaterContent.HydraulicModel.SimpleWaterContent.setSoilType(EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_LOAM)

    assert(mat7.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    assert(mat7.Thermal.HeatCapacity.ConstantHeatCapacity.getIncludeLatentHeat(), True)  
    assert(mat7.Thermal.SoilUnfrozenWaterContent.getType(), ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)
    assert(mat7.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getFrozenTemperature(), 1.2)
    assert(mat7.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getSelectHydraulicModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)
    assert(mat7.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCSat(), 0.06)
    assert(mat7.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCRes(), 0.07) 
    assert(mat7.Thermal.SoilUnfrozenWaterContent.HydraulicModel.SimpleWaterContent.getSoilType(), EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_LOAM)

def test8():
    mat8.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    mat8.Thermal.HeatCapacity.ConstantHeatCapacity.setIncludeLatentHeat(True)
    mat8.Thermal.SoilUnfrozenWaterContent.setType(ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)
    mat8.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setFrozenTemperature(1.2)
    mat8.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setSelectHydraulicModel(GroundWaterModes.SL_WATER_MODE_FREDLUND)
    mat8.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCSat(0.06)
    mat8.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCRes(0.07)
    mat8.Thermal.SoilUnfrozenWaterContent.HydraulicModel.FredlundWaterContent.setA(1.8)
    mat8.Thermal.SoilUnfrozenWaterContent.HydraulicModel.FredlundWaterContent.setB(1.9)
    mat8.Thermal.SoilUnfrozenWaterContent.HydraulicModel.FredlundWaterContent.setC(1.11)

    assert(mat8.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    assert(mat8.Thermal.HeatCapacity.ConstantHeatCapacity.getIncludeLatentHeat(), True)
    assert(mat8.Thermal.SoilUnfrozenWaterContent.getType(), ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)
    assert(mat8.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getFrozenTemperature(), 1.2)
    assert(mat8.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getSelectHydraulicModel(), GroundWaterModes.SL_WATER_MODE_FREDLUND) 
    assert(mat8.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCSat(), 0.06)
    assert(mat8.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCRes(), 0.07)
    assert(mat8.Thermal.SoilUnfrozenWaterContent.HydraulicModel.FredlundWaterContent.getA(), 1.8)
    assert(mat8.Thermal.SoilUnfrozenWaterContent.HydraulicModel.FredlundWaterContent.getB(), 1.9)
    assert(mat8.Thermal.SoilUnfrozenWaterContent.HydraulicModel.FredlundWaterContent.getC(), 1.11)

def test9():
    mat9.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    mat9.Thermal.HeatCapacity.ConstantHeatCapacity.setIncludeLatentHeat(True)
    mat9.Thermal.SoilUnfrozenWaterContent.setType(ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)
    mat9.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setFrozenTemperature(1.2)
    mat9.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setSelectHydraulicModel(GroundWaterModes.SL_WATER_MODE_VAN_GENUCHTEN)
    mat9.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCSat(0.06)
    mat9.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCRes(0.07)
    mat9.Thermal.SoilUnfrozenWaterContent.HydraulicModel.GenuchtenWaterContent.setAlpha(1.12)
    mat9.Thermal.SoilUnfrozenWaterContent.HydraulicModel.GenuchtenWaterContent.setN(1.13)
    mat9.Thermal.SoilUnfrozenWaterContent.HydraulicModel.GenuchtenWaterContent.setCustomM(True)
    mat9.Thermal.SoilUnfrozenWaterContent.HydraulicModel.GenuchtenWaterContent.setM(1.14)

    assert(mat9.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    assert(mat9.Thermal.HeatCapacity.ConstantHeatCapacity.getIncludeLatentHeat(), True)  
    assert(mat9.Thermal.SoilUnfrozenWaterContent.getType(), ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)
    assert(mat9.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getFrozenTemperature(), 1.2)
    assert(mat9.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getSelectHydraulicModel(), GroundWaterModes.SL_WATER_MODE_VAN_GENUCHTEN)
    assert(mat9.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCSat(), 0.06)
    assert(mat9.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCRes(), 0.07)  
    assert(mat9.Thermal.SoilUnfrozenWaterContent.HydraulicModel.GenuchtenWaterContent.getAlpha(), 1.12)
    assert(mat9.Thermal.SoilUnfrozenWaterContent.HydraulicModel.GenuchtenWaterContent.getN(), 1.13)
    assert(mat9.Thermal.SoilUnfrozenWaterContent.HydraulicModel.GenuchtenWaterContent.getCustomM(), True)
    assert(mat9.Thermal.SoilUnfrozenWaterContent.HydraulicModel.GenuchtenWaterContent.getM(), 1.14)

def test10():
    mat10.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    mat10.Thermal.HeatCapacity.ConstantHeatCapacity.setIncludeLatentHeat(True)
    mat10.Thermal.SoilUnfrozenWaterContent.setType(ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)
    mat10.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setFrozenTemperature(1.2)
    mat10.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setSelectHydraulicModel(GroundWaterModes.SL_WATER_MODE_VAN_GENUCHTEN)
    mat10.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCSat(0.06)
    mat10.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCRes(0.07)
    mat10.Thermal.SoilUnfrozenWaterContent.HydraulicModel.GenuchtenWaterContent.setAlpha(1.12)
    mat10.Thermal.SoilUnfrozenWaterContent.HydraulicModel.GenuchtenWaterContent.setN(1.13)
    mat10.Thermal.SoilUnfrozenWaterContent.HydraulicModel.GenuchtenWaterContent.setCustomM(False)

    assert(mat10.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    assert(mat10.Thermal.HeatCapacity.ConstantHeatCapacity.getIncludeLatentHeat(), True)
    assert(mat10.Thermal.SoilUnfrozenWaterContent.getType(), ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)
    assert(mat10.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getFrozenTemperature(), 1.2)
    assert(mat10.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getSelectHydraulicModel(), GroundWaterModes.SL_WATER_MODE_VAN_GENUCHTEN)
    assert(mat10.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCSat(), 0.06)
    assert(mat10.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCRes(), 0.07)
    assert(mat10.Thermal.SoilUnfrozenWaterContent.HydraulicModel.GenuchtenWaterContent.getAlpha(), 1.12)
    assert(mat10.Thermal.SoilUnfrozenWaterContent.HydraulicModel.GenuchtenWaterContent.getN(), 1.13)
    assert(mat10.Thermal.SoilUnfrozenWaterContent.HydraulicModel.GenuchtenWaterContent.getCustomM(), False)

def test11():
    mat11.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    mat11.Thermal.HeatCapacity.ConstantHeatCapacity.setIncludeLatentHeat(True)
    mat11.Thermal.SoilUnfrozenWaterContent.setType(ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)
    mat11.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setFrozenTemperature(1.2)
    mat11.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setSelectHydraulicModel(GroundWaterModes.SL_WATER_MODE_BROOK)
    mat11.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCSat(0.06)
    mat11.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCRes(0.07)
    mat11.Thermal.SoilUnfrozenWaterContent.HydraulicModel.BrooksWaterContent.setPoreSizeIndex(1.15)
    mat11.Thermal.SoilUnfrozenWaterContent.HydraulicModel.BrooksWaterContent.setBubblingPressure(1.16)

    assert(mat11.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)  
    assert(mat11.Thermal.HeatCapacity.ConstantHeatCapacity.getIncludeLatentHeat(), True)
    assert(mat11.Thermal.SoilUnfrozenWaterContent.getType(), ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)
    assert(mat11.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getFrozenTemperature(), 1.2)
    assert(mat11.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getSelectHydraulicModel(), GroundWaterModes.SL_WATER_MODE_BROOK)
    assert(mat11.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCSat(), 0.06)
    assert(mat11.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCRes(), 0.07)
    assert(mat11.Thermal.SoilUnfrozenWaterContent.HydraulicModel.BrooksWaterContent.getPoreSizeIndex(), 1.15) 
    assert(mat11.Thermal.SoilUnfrozenWaterContent.HydraulicModel.BrooksWaterContent.getBubblingPressure(), 1.16)

def test12():
    mat12.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    mat12.Thermal.HeatCapacity.ConstantHeatCapacity.setIncludeLatentHeat(True)
    mat12.Thermal.SoilUnfrozenWaterContent.setType(ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)
    mat12.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setFrozenTemperature(1.2)
    mat12.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setSelectHydraulicModel(GroundWaterModes.SL_WATER_MODE_GARDNER)
    mat12.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCSat(0.06)
    mat12.Thermal.SoilUnfrozenWaterContent.HydraulicModel.setWCRes(0.07)
    mat12.Thermal.SoilUnfrozenWaterContent.HydraulicModel.GardnerWaterContent.setA(1.17)
    mat12.Thermal.SoilUnfrozenWaterContent.HydraulicModel.GardnerWaterContent.setN(1.18)

    assert(mat12.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    assert(mat12.Thermal.HeatCapacity.ConstantHeatCapacity.getIncludeLatentHeat(), True)
    assert(mat12.Thermal.SoilUnfrozenWaterContent.getType(), ThermalWaterContentType.THERMAL_WATER_CONTENT_HYDRO_MODEL)
    assert(mat12.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getFrozenTemperature(), 1.2)
    assert(mat12.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getSelectHydraulicModel(), GroundWaterModes.SL_WATER_MODE_GARDNER)
    assert(mat12.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCSat(), 0.06) 
    assert(mat12.Thermal.SoilUnfrozenWaterContent.HydraulicModel.getWCRes(), 0.07)
    assert(mat12.Thermal.SoilUnfrozenWaterContent.HydraulicModel.GardnerWaterContent.getA(), 1.17)
    assert(mat12.Thermal.SoilUnfrozenWaterContent.HydraulicModel.GardnerWaterContent.getN(), 1.18)

def test13():
    mat13.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    mat13.Thermal.HeatCapacity.ConstantHeatCapacity.setIncludeLatentHeat(True)
    mat13.Thermal.SoilUnfrozenWaterContent.setType(ThermalWaterContentType.THERMAL_WATER_CONTENT_CUSTOM)
    mat13.Thermal.SoilUnfrozenWaterContent.CustomWaterContent.setTemperatureVsUnfrozenWaterContentValues([1.1,1.3],[0.2,0.4])

    assert(mat13.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    assert(mat13.Thermal.HeatCapacity.ConstantHeatCapacity.getIncludeLatentHeat(), True)
    assert(mat13.Thermal.SoilUnfrozenWaterContent.getType(), ThermalWaterContentType.THERMAL_WATER_CONTENT_CUSTOM)
    assert(mat13.Thermal.SoilUnfrozenWaterContent.CustomWaterContent.getTemperatureVsUnfrozenWaterContentValues(), [[1.1,1.3],[0.2,0.4]])

def test14():
    mat14.Thermal.HeatCapacity.setType(ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT)
    mat14.Thermal.HeatCapacity.ConstantHeatCapacity.setIncludeLatentHeat(True)
    mat14.Thermal.SoilUnfrozenWaterContent.setType(ThermalWaterContentType.THERMAL_WATER_CONTENT_DEFAULT)

    assert(mat14.Thermal.HeatCapacity.getType(), ThermalHeatCapacityType.THERMAL_HEAT_CAPACITY_CONSTANT) 
    assert(mat14.Thermal.HeatCapacity.ConstantHeatCapacity.getIncludeLatentHeat(), True)
    assert(mat14.Thermal.SoilUnfrozenWaterContent.getType(), ThermalWaterContentType.THERMAL_WATER_CONTENT_DEFAULT)

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

model.save()

pass