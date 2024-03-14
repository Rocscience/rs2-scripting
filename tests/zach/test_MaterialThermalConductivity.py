from xml.etree.ElementTree import TreeBuilder
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\thermalConductivity_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\thermalConductivity_python.fez'

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

def test1():
    mat1.Thermal.Conductivity.setMethod(ThermalType.THERMAL_CONSTANT)
    mat1.Thermal.Conductivity.ConstantConductivity.setUnfrozenConductivity(1.1)
    mat1.Thermal.Conductivity.ConstantConductivity.setFrozenConductivity(1.2)
    mat1.Thermal.Conductivity.ConstantConductivity.setFrozenTemperature(1.3)

    assert(mat1.Thermal.Conductivity.getMethod(), ThermalType.THERMAL_CONSTANT)
    assert(mat1.Thermal.Conductivity.ConstantConductivity.getUnfrozenConductivity(), 1.1)
    assert(mat1.Thermal.Conductivity.ConstantConductivity.getFrozenConductivity(), 1.2)
    assert(mat1.Thermal.Conductivity.ConstantConductivity.getFrozenTemperature(), 1.3)

def test2():
    mat2.Thermal.Conductivity.setMethod(ThermalType.THERMAL_JOHANSEN)
    mat2.Thermal.Conductivity.Johansen.setSoilType(ThermalSoilType.THERMAL_SOIL_FINE)
    mat2.Thermal.Conductivity.Johansen.setQuartzContent(0.4)

    assert(mat2.Thermal.Conductivity.getMethod(), ThermalType.THERMAL_JOHANSEN)
    assert(mat2.Thermal.Conductivity.Johansen.getSoilType(), ThermalSoilType.THERMAL_SOIL_FINE)
    assert(mat2.Thermal.Conductivity.Johansen.getQuartzContent(), 0.4)

def test3():
    mat3.Thermal.Conductivity.setMethod(ThermalType.THERMAL_JOHANSEN)
    mat3.Thermal.Conductivity.Johansen.setSoilType(ThermalSoilType.THERMAL_SOIL_COARSE)
    mat3.Thermal.Conductivity.Johansen.setQuartzContent(0.4)

    assert(mat3.Thermal.Conductivity.getMethod(), ThermalType.THERMAL_JOHANSEN)
    assert(mat3.Thermal.Conductivity.Johansen.getSoilType(), ThermalSoilType.THERMAL_SOIL_COARSE)
    assert(mat3.Thermal.Conductivity.Johansen.getQuartzContent(), 0.4)

def test4():
    mat4.Thermal.Conductivity.setMethod(ThermalType.THERMAL_JOHANSEN)
    mat4.Thermal.Conductivity.Johansen.setSoilType(ThermalSoilType.THERMAL_SOIL_CRUSHED_ROCK)
    mat4.Thermal.Conductivity.Johansen.setQuartzContent(0.4)
    
    assert(mat4.Thermal.Conductivity.getMethod(), ThermalType.THERMAL_JOHANSEN)
    assert(mat4.Thermal.Conductivity.Johansen.getSoilType(), ThermalSoilType.THERMAL_SOIL_CRUSHED_ROCK)
    assert(mat4.Thermal.Conductivity.Johansen.getQuartzContent(), 0.4)

def test5():
    mat5.Thermal.Conductivity.setMethod(ThermalType.THERMAL_JOHANSEN)
    mat5.Thermal.Conductivity.Johansen.setSoilType(ThermalSoilType.THERMAL_SOIL_PEAT)
    mat5.Thermal.Conductivity.Johansen.setQuartzContent(0.4)
    mat5.Thermal.Conductivity.Johansen.setDryConductivity(1.5)
    mat5.Thermal.Conductivity.Johansen.setSaturatedUnfrozenConductivity(1.6)
    mat5.Thermal.Conductivity.Johansen.setSaturatedFrozenConductivity(1.7)

    assert(mat5.Thermal.Conductivity.getMethod(), ThermalType.THERMAL_JOHANSEN)
    assert(mat5.Thermal.Conductivity.Johansen.getSoilType(), ThermalSoilType.THERMAL_SOIL_PEAT)
    assert(mat5.Thermal.Conductivity.Johansen.getQuartzContent(), 0.4)
    assert(mat5.Thermal.Conductivity.Johansen.getDryConductivity(), 1.5)
    assert(mat5.Thermal.Conductivity.Johansen.getSaturatedUnfrozenConductivity(), 1.6)
    assert(mat5.Thermal.Conductivity.Johansen.getSaturatedFrozenConductivity(), 1.7)

def test6():
    mat6.Thermal.Conductivity.setMethod(ThermalType.THERMAL_JOHANSEN_LU)
    mat6.Thermal.Conductivity.JohansenLu.setSoilType(ThermalSoilType.THERMAL_SOIL_FINE)
    mat6.Thermal.Conductivity.JohansenLu.setQuartzContent(0.4)

    assert(mat6.Thermal.Conductivity.getMethod(), ThermalType.THERMAL_JOHANSEN_LU)
    assert(mat6.Thermal.Conductivity.JohansenLu.getSoilType(), ThermalSoilType.THERMAL_SOIL_FINE)
    assert(mat6.Thermal.Conductivity.JohansenLu.getQuartzContent(), 0.4)

def test7():
    mat7.Thermal.Conductivity.setMethod(ThermalType.THERMAL_JOHANSEN_LU)
    mat7.Thermal.Conductivity.JohansenLu.setSoilType(ThermalSoilType.THERMAL_SOIL_COARSE)
    mat7.Thermal.Conductivity.JohansenLu.setQuartzContent(0.4)

    assert(mat7.Thermal.Conductivity.getMethod(), ThermalType.THERMAL_JOHANSEN_LU)
    assert(mat7.Thermal.Conductivity.JohansenLu.getSoilType(), ThermalSoilType.THERMAL_SOIL_COARSE)
    assert(mat7.Thermal.Conductivity.JohansenLu.getQuartzContent(), 0.4)

def test8():
    mat8.Thermal.Conductivity.setMethod(ThermalType.THERMAL_DEVRIES)
    mat8.Thermal.Conductivity.Derives.setParticleConductivity(1.8)

    assert(mat8.Thermal.Conductivity.getMethod(), ThermalType.THERMAL_DEVRIES)
    assert(mat8.Thermal.Conductivity.Derives.getParticleConductivity(), 1.8)

def test9():
    mat9.Thermal.Conductivity.setMethod(ThermalType.THERMAL_COTE_AND_KONRAD)
    mat9.Thermal.Conductivity.CoteAndKonrad.setParticleConductivity(1.8)
    mat9.Thermal.Conductivity.CoteAndKonrad.setUnfrozenKappa(1.9)
    mat9.Thermal.Conductivity.CoteAndKonrad.setFrozenKappa(1.11)
    mat9.Thermal.Conductivity.CoteAndKonrad.setChi(1.12)
    mat9.Thermal.Conductivity.CoteAndKonrad.setEta(1.13)

    assert(mat9.Thermal.Conductivity.getMethod(), ThermalType.THERMAL_COTE_AND_KONRAD)
    assert(mat9.Thermal.Conductivity.CoteAndKonrad.getParticleConductivity(), 1.8)
    assert(mat9.Thermal.Conductivity.CoteAndKonrad.getUnfrozenKappa(), 1.9)
    assert(mat9.Thermal.Conductivity.CoteAndKonrad.getFrozenKappa(), 1.11)
    assert(mat9.Thermal.Conductivity.CoteAndKonrad.getChi(), 1.12)
    assert(mat9.Thermal.Conductivity.CoteAndKonrad.getEta(), 1.13)

def test10():
    mat10.Thermal.Conductivity.setMethod(ThermalType.THERMAL_TABULAR)
    mat10.Thermal.Conductivity.Tabular.setDependence(ThermalVolumetricDepencenceType.THERMAL_VOLUMETRIC_DEPENDENCE_TEMPERATURE)
    mat10.Thermal.Conductivity.Tabular.setThermalConductivityTemperatureFunction([1.1,1.3],[1.2,1.4])

    assert(mat10.Thermal.Conductivity.getMethod(), ThermalType.THERMAL_TABULAR)
    assert(mat10.Thermal.Conductivity.Tabular.getDependence(), ThermalVolumetricDepencenceType.THERMAL_VOLUMETRIC_DEPENDENCE_TEMPERATURE)
    assert(mat10.Thermal.Conductivity.Tabular.getThermalConductivityTemperatureFunction(), ([1.1,1.3],[1.2,1.4]))

def test11():
    mat11.Thermal.Conductivity.setMethod(ThermalType.THERMAL_TABULAR)
    mat11.Thermal.Conductivity.Tabular.setDependence(ThermalVolumetricDepencenceType.THERMAL_VOLUMETRIC_DEPENDENCE_WATER_CONTENT)
    mat11.Thermal.Conductivity.Tabular.setThermalConductivityWaterContentFunction([0.1,0.3],[1.2,1.4])

    assert(mat11.Thermal.Conductivity.getMethod(), ThermalType.THERMAL_TABULAR)
    assert(mat11.Thermal.Conductivity.Tabular.getDependence(), ThermalVolumetricDepencenceType.THERMAL_VOLUMETRIC_DEPENDENCE_WATER_CONTENT)
    assert(mat11.Thermal.Conductivity.Tabular.getThermalConductivityWaterContentFunction(), ([0.1,0.3],[1.2,1.4]))

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

model.save()

pass