from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Liner\geosynthetic_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Liner\geosynthetic_python.fez'

model = modeler.openFile(base_model)

model.saveAs(final_python_model)

linerList = model.getAllLinerProperties()

liner1 = linerList[0]
liner2 = linerList[1]
liner3 = linerList[2]
liner4 = linerList[3]
liner5 = linerList[4]
liner6 = linerList[5]
liner7 = linerList[6]
liner8 = linerList[7]
liner9 = linerList[8]
liner10 = linerList[9]
liner11 = linerList[10]
liner12 = linerList[11]
liner13 = linerList[12]
liner14 = linerList[13]

def test1():
    liner = liner1

    liner.setLinerType(LinerTypes.P2_LINER_GEOSYNTHETIC)

    liner.Geosynthetic.setActivateThermal(True) #Makes set initial temperature and set unit weight available

    liner.Geosynthetic.setGeosyntheticUnitWeight(1.1)
    liner.Geosynthetic.setInitialTemperature(1.2)

    assert(liner.getLinerType(), LinerTypes.P2_LINER_GEOSYNTHETIC)
    assert(liner.Geosynthetic.getGeosyntheticUnitWeight(), 1.1)
    assert(liner.Geosynthetic.getInitialTemperature(), 1.2)

def test2():
    liner = liner2

    liner.setLinerType(LinerTypes.P2_LINER_GEOSYNTHETIC)

    liner.Geosynthetic.setTensileModulus(1.3)

    assert(liner.Geosynthetic.getTensileModulus(), 1.3)

def test3():
    liner = liner3

    liner.setLinerType(LinerTypes.P2_LINER_GEOSYNTHETIC)

    liner.Geosynthetic.setMaterialType(MaterialType.ELASTIC)

    assert(liner.Geosynthetic.getMaterialType(), MaterialType.ELASTIC)

def test4():
    liner = liner4

    liner.setLinerType(LinerTypes.P2_LINER_GEOSYNTHETIC)

    liner.Geosynthetic.setMaterialType(MaterialType.PLASTIC)
    liner.Geosynthetic.setTensileStrengthPeak(1.5)
    liner.Geosynthetic.setTensileStrengthResidual(1.4)


    assert(liner.Geosynthetic.getMaterialType(), MaterialType.PLASTIC)
    assert(liner.Geosynthetic.getTensileStrengthPeak(), 1.5)
    assert(liner.Geosynthetic.getTensileStrengthResidual(), 1.4)

def test5():
    liner = liner5

    liner.setLinerType(LinerTypes.P2_LINER_GEOSYNTHETIC)

    liner.Geosynthetic.setAxialStrainExpansion(1.6)

    assert(liner.Geosynthetic.getAxialStrainExpansion(), 1.6)

def test6():
    liner = liner6

    liner.setLinerType(LinerTypes.P2_LINER_GEOSYNTHETIC)

    liner.Geosynthetic.setActivateThermal(True)
    liner.Geosynthetic.setStaticTemperatureMode(StaticWaterModes.SWM_PWP)
    liner.Geosynthetic.setStaticTemperature(1.7)
    liner.Geosynthetic.setSpecificHeatCapacity(1.8)
    liner.Geosynthetic.setThermalExpansion(True)
    liner.Geosynthetic.setExpansionCoefficient(1.9)

    assert(liner.Geosynthetic.getActivateThermal(), True)
    assert(liner.Geosynthetic.getStaticTemperatureMode(), StaticWaterModes.SWM_PWP)
    assert(liner.Geosynthetic.getStaticTemperature(), 1.7)
    assert(liner.Geosynthetic.getSpecificHeatCapacity(), 1.8)
    assert(liner.Geosynthetic.getThermalExpansion(), True)
    assert(liner.Geosynthetic.getExpansionCoefficient(), 1.9)

def test7():
    liner = liner7

    liner.setLinerType(LinerTypes.P2_LINER_GEOSYNTHETIC)

    liner.Geosynthetic.setActivateThermal(True)
    liner.Geosynthetic.setStaticTemperatureMode(StaticWaterModes.SWM_PWP)
    liner.Geosynthetic.setStaticTemperature(1.7)
    liner.Geosynthetic.setSpecificHeatCapacity(1.8)
    liner.Geosynthetic.setThermalExpansion(False)

    assert(liner.Geosynthetic.getActivateThermal(), True)
    assert(liner.Geosynthetic.getStaticTemperatureMode(), StaticWaterModes.SWM_PWP)
    assert(liner.Geosynthetic.getStaticTemperature(), 1.7)
    assert(liner.Geosynthetic.getSpecificHeatCapacity(), 1.8)
    assert(liner.Geosynthetic.getThermalExpansion(), False)

def test8():
    liner = liner8

    liner.setLinerType(LinerTypes.P2_LINER_GEOSYNTHETIC)

    liner.Geosynthetic.setActivateThermal(True)
    liner.Geosynthetic.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    liner.Geosynthetic.setStaticTemperatureGridToUse('None')
    liner.Geosynthetic.setSpecificHeatCapacity(1.8)
    liner.Geosynthetic.setThermalExpansion(True)
    liner.Geosynthetic.setExpansionCoefficient(1.9)

    assert(liner.Geosynthetic.getActivateThermal(), True)
    assert(liner.Geosynthetic.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(liner.Geosynthetic.getStaticTemperatureGridToUse(), 'None')
    assert(liner.Geosynthetic.getSpecificHeatCapacity(), 1.8)
    assert(liner.Geosynthetic.getThermalExpansion(), True)
    assert(liner.Geosynthetic.getExpansionCoefficient(), 1.9)

def test9():
    liner = liner9

    liner.setLinerType(LinerTypes.P2_LINER_GEOSYNTHETIC)

    liner.Geosynthetic.setActivateThermal(True)
    liner.Geosynthetic.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    liner.Geosynthetic.setStaticTemperatureGridToUse('Default Grid')
    liner.Geosynthetic.setSpecificHeatCapacity(1.8)
    liner.Geosynthetic.setThermalExpansion(True)
    liner.Geosynthetic.setExpansionCoefficient(1.9)

    assert(liner.Geosynthetic.getActivateThermal(), True)
    assert(liner.Geosynthetic.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(liner.Geosynthetic.getStaticTemperatureGridToUse(), 'Default Grid')
    assert(liner.Geosynthetic.getSpecificHeatCapacity(), 1.8)
    assert(liner.Geosynthetic.getThermalExpansion(), True)
    assert(liner.Geosynthetic.getExpansionCoefficient(), 1.9)

def test10():
    liner = liner10

    liner.setLinerType(LinerTypes.P2_LINER_GEOSYNTHETIC)

    liner.Geosynthetic.setActivateThermal(True)
    liner.Geosynthetic.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    liner.Geosynthetic.setStaticTemperatureGridToUse('Grid 3')
    liner.Geosynthetic.setSpecificHeatCapacity(1.8)
    liner.Geosynthetic.setThermalExpansion(True)
    liner.Geosynthetic.setExpansionCoefficient(1.9)

    assert(liner.Geosynthetic.getActivateThermal(), True)
    assert(liner.Geosynthetic.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(liner.Geosynthetic.getStaticTemperatureGridToUse(), 'Grid 3')
    assert(liner.Geosynthetic.getSpecificHeatCapacity(), 1.8)
    assert(liner.Geosynthetic.getThermalExpansion(), True)
    assert(liner.Geosynthetic.getExpansionCoefficient(), 1.9)

def test11():
    liner = liner11

    liner.setLinerType(LinerTypes.P2_LINER_GEOSYNTHETIC)

    liner.Geosynthetic.setActivateThermal(True)
    liner.Geosynthetic.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    liner.Geosynthetic.setStaticTemperatureGridToUse('Default Grid')
    liner.Geosynthetic.setSpecificHeatCapacity(1.8)
    liner.Geosynthetic.setThermalExpansion(False)

    assert(liner.Geosynthetic.getActivateThermal(), True)
    assert(liner.Geosynthetic.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(liner.Geosynthetic.getStaticTemperatureGridToUse(), 'Default Grid')
    assert(liner.Geosynthetic.getSpecificHeatCapacity(), 1.8)
    assert(liner.Geosynthetic.getThermalExpansion(), False)    


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