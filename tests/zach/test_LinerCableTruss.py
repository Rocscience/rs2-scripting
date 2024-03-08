from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Liner\cableTruss_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Liner\cableTruss_python.fez'

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

    liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)

    liner.CableTruss.setActivateThermal(True) #Makes set initial temperature and set unit weight available

    liner.CableTruss.setUnitWeight(1.1)
    liner.CableTruss.setInitialTemperature(1.2)

    assert(liner.getLinerType(), LinerTypes.P2_LINER_CABLE_TRUSS)
    assert(liner.CableTruss.getUnitWeight(), 1.1)
    assert(liner.CableTruss.getInitialTemperature(), 1.2)

def test2():
    liner = liner2

    liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)

    liner.CableTruss.setCableDiameter(1.3)
    liner.CableTruss.setOutofplaneSpacing(1.4)

    assert(liner.CableTruss.getCableDiameter(), 1.3)
    assert(liner.CableTruss.getOutofplaneSpacing(), 1.4)

def test3():
    liner = liner3

    liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)

    liner.CableTruss.setYoungsModulus(1.5)

    assert(liner.CableTruss.getYoungsModulus(), 1.5)

def test4():
    liner = liner4

    liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)

    liner.CableTruss.setMaterialType(MaterialType.ELASTIC)

    assert(liner.CableTruss.getMaterialType(), MaterialType.ELASTIC)

def test5():
    liner = liner5

    liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)

    liner.CableTruss.setMaterialType(MaterialType.PLASTIC)
    liner.CableTruss.setTensileStrengthPeak(1.7)
    liner.CableTruss.setTensileStrengthResidual(1.6)


    assert(liner.CableTruss.getMaterialType(), MaterialType.PLASTIC)
    assert(liner.CableTruss.getTensileStrengthPeak(), 1.7)
    assert(liner.CableTruss.getTensileStrengthResidual(), 1.6)

def test6():
    liner = liner6

    liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)

    liner.CableTruss.setPreTensioning(False)

    assert(liner.CableTruss.getPreTensioning(), False)

def test7():
    liner = liner7

    liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)

    liner.CableTruss.setPreTensioning(True)
    liner.CableTruss.setPreTensioningForce(1.8)

    assert(liner.CableTruss.getPreTensioning(), True)
    assert(liner.CableTruss.getPreTensioningForce(),1.8)

def test8():
    liner = liner8

    liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)

    liner.CableTruss.setAxialStrainExpansion(1.9)

    assert(liner.CableTruss.getAxialStrainExpansion(), 1.9)

def test9():
    liner = liner9

    liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)

    liner.CableTruss.setActivateThermal(True)
    liner.CableTruss.setStaticTemperatureMode(StaticWaterModes.SWM_PWP)
    liner.CableTruss.setStaticTemperature(1.7)
    liner.CableTruss.setSpecificHeatCapacity(1.8)
    liner.CableTruss.setThermalExpansion(True)
    liner.CableTruss.setExpansionCoefficient(1.13)

    assert(liner.CableTruss.getActivateThermal(), True)
    assert(liner.CableTruss.getStaticTemperatureMode(), StaticWaterModes.SWM_PWP)
    assert(liner.CableTruss.getStaticTemperature(), 1.7)
    assert(liner.CableTruss.getSpecificHeatCapacity(), 1.8)
    assert(liner.CableTruss.getThermalExpansion(), True)
    assert(liner.CableTruss.getExpansionCoefficient(), 1.13)

def test10():
    liner = liner10

    liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)

    liner.CableTruss.setActivateThermal(True)
    liner.CableTruss.setStaticTemperatureMode(StaticWaterModes.SWM_PWP)
    liner.CableTruss.setStaticTemperature(1.7)
    liner.CableTruss.setSpecificHeatCapacity(1.8)
    liner.CableTruss.setThermalExpansion(False)

    assert(liner.CableTruss.getActivateThermal(), True)
    assert(liner.CableTruss.getStaticTemperatureMode(), StaticWaterModes.SWM_PWP)
    assert(liner.CableTruss.getStaticTemperature(), 1.7)
    assert(liner.CableTruss.getSpecificHeatCapacity(), 1.8)
    assert(liner.CableTruss.getThermalExpansion(), False)

def test11():
    liner = liner11

    liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)

    liner.CableTruss.setActivateThermal(True)
    liner.CableTruss.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    liner.CableTruss.setStaticTemperatureGridToUse('None')
    liner.CableTruss.setSpecificHeatCapacity(1.8)
    liner.CableTruss.setThermalExpansion(True)
    liner.CableTruss.setExpansionCoefficient(1.13)

    assert(liner.CableTruss.getActivateThermal(), True)
    assert(liner.CableTruss.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(liner.CableTruss.getStaticTemperatureGridToUse(), 'None')
    assert(liner.CableTruss.getSpecificHeatCapacity(), 1.8)
    assert(liner.CableTruss.getThermalExpansion(), True)
    assert(liner.CableTruss.getExpansionCoefficient(), 1.13)

def test12():
    liner = liner12

    liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)

    liner.CableTruss.setActivateThermal(True)
    liner.CableTruss.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    liner.CableTruss.setStaticTemperatureGridToUse('Default Grid')
    liner.CableTruss.setSpecificHeatCapacity(1.8)
    liner.CableTruss.setThermalExpansion(True)
    liner.CableTruss.setExpansionCoefficient(1.13)

    assert(liner.CableTruss.getActivateThermal(), True)
    assert(liner.CableTruss.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(liner.CableTruss.getStaticTemperatureGridToUse(), 'Default Grid')
    assert(liner.CableTruss.getSpecificHeatCapacity(), 1.8)
    assert(liner.CableTruss.getThermalExpansion(), True)
    assert(liner.CableTruss.getExpansionCoefficient(), 1.13)

def test13():
    liner = liner13

    liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)

    liner.CableTruss.setActivateThermal(True)
    liner.CableTruss.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    liner.CableTruss.setStaticTemperatureGridToUse('Grid 3')
    liner.CableTruss.setSpecificHeatCapacity(1.8)
    liner.CableTruss.setThermalExpansion(True)
    liner.CableTruss.setExpansionCoefficient(1.13)

    assert(liner.CableTruss.getActivateThermal(), True)
    assert(liner.CableTruss.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(liner.CableTruss.getStaticTemperatureGridToUse(), 'Grid 3')
    assert(liner.CableTruss.getSpecificHeatCapacity(), 1.8)
    assert(liner.CableTruss.getThermalExpansion(), True)
    assert(liner.CableTruss.getExpansionCoefficient(), 1.13)

def test14():
    liner = liner14

    liner.setLinerType(LinerTypes.P2_LINER_CABLE_TRUSS)

    liner.CableTruss.setActivateThermal(True)
    liner.CableTruss.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    liner.CableTruss.setStaticTemperatureGridToUse('Default Grid')
    liner.CableTruss.setSpecificHeatCapacity(1.8)
    liner.CableTruss.setThermalExpansion(False)

    assert(liner.CableTruss.getActivateThermal(), True)
    assert(liner.CableTruss.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(liner.CableTruss.getStaticTemperatureGridToUse(), 'Default Grid')
    assert(liner.CableTruss.getSpecificHeatCapacity(), 1.8)
    assert(liner.CableTruss.getThermalExpansion(), False)


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