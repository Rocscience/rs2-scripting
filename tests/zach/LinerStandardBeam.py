from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Liner\standardBeam_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Liner\standardBeam_python.fez'

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
liner15 = linerList[14]
liner16 = linerList[15]
liner17 = linerList[16]


def test1():
    liner = liner1

    liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)

    liner.StandardBeam.setActivateThermal(True) #Makes set initial temperature available

    liner.StandardBeam.setUnitWeight(1.1)
    liner.StandardBeam.setIncludeWeightInStressAnalysis(True)
    liner.StandardBeam.setInitialTemperature(1.2)

    assert(liner.getLinerType(), LinerTypes.P2_LINER_STANDARD_BEAM)
    assert(liner.StandardBeam.getUnitWeight(), 1.1)
    assert(liner.StandardBeam.getIncludeWeightInStressAnalysis(), True)
    assert(liner.StandardBeam.getInitialTemperature(), 1.2)

def test2():
    liner = liner2

    liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)

    liner.StandardBeam.setIncludeWeightInStressAnalysis(False)

    assert(liner.StandardBeam.getIncludeWeightInStressAnalysis(), False)

def test3():
    liner = liner3

    liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)

    liner.StandardBeam.setMethod(GeometryChoice.LNP_USE_THICKNESS)
    liner.StandardBeam.setThickness(1.3)

    assert(liner.StandardBeam.getMethod(), GeometryChoice.LNP_USE_THICKNESS)
    assert(liner.StandardBeam.getThickness(), 1.3)

def test4():
    liner = liner4

    liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)

    liner.StandardBeam.setMethod(GeometryChoice.LNP_USE_AREA)
    liner.StandardBeam.setArea(1.4)
    liner.StandardBeam.setMomentOfInertia(1.5)

    assert(liner.StandardBeam.getMethod(), GeometryChoice.LNP_USE_AREA)
    assert(liner.StandardBeam.getArea(), 1.4)
    assert(liner.StandardBeam.getMomentOfInertia(), 1.5)

def test5():
    liner = liner5

    liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)

    liner.StandardBeam.setYoungsModulus(1.6)
    liner.StandardBeam.setPoissonsRatio(0.07)

    assert(liner.StandardBeam.getYoungsModulus(), 1.6)
    assert(liner.StandardBeam.getPoissonsRatio(), 0.07)

def test6():
    liner = liner6

    liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)

    liner.StandardBeam.setMaterialType(MaterialType.ELASTIC)

    assert(liner.StandardBeam.getMaterialType(), MaterialType.ELASTIC)

def test7():
    liner = liner7

    liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)

    liner.StandardBeam.setMaterialType(MaterialType.PLASTIC)
    liner.StandardBeam.setCompressiveStrengthPeak(1.9)
    liner.StandardBeam.setCompressiveStrengthResidual(1.8)
    liner.StandardBeam.setTensileStrengthPeak(1.12)
    liner.StandardBeam.setTensileStrengthResidual(1.11)

    assert(liner.StandardBeam.getMaterialType(), MaterialType.PLASTIC)
    assert(liner.StandardBeam.getCompressiveStrengthPeak(), 1.9)
    assert(liner.StandardBeam.getCompressiveStrengthResidual(), 1.8)  
    assert(liner.StandardBeam.getTensileStrengthPeak(), 1.12)
    assert(liner.StandardBeam.getTensileStrengthResidual(), 1.11)

def test8():
    liner = liner8

    liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)

    liner.StandardBeam.setSlidingGap(True)
    liner.StandardBeam.setStrainAtLocking(1.13)
    liner.StandardBeam.setBeamElementFormulation(LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
    liner.StandardBeam.setAxialStrainExpansion(1.14)

    assert(liner.StandardBeam.getSlidingGap(), True)
    assert(liner.StandardBeam.getStrainAtLocking(), 1.13)
    assert(liner.StandardBeam.getBeamElementFormulation(), LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
    assert(liner.StandardBeam.getAxialStrainExpansion(), 1.14)

def test9():
    liner = liner9

    liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)

    liner.StandardBeam.setSlidingGap(True)
    liner.StandardBeam.setStrainAtLocking(1.13)
    liner.StandardBeam.setBeamElementFormulation(LinerFormulation.P2_LINER_FORMULATION_BERNOULLI)
    liner.StandardBeam.setAxialStrainExpansion(1.14)

    assert(liner.StandardBeam.getSlidingGap(), True)
    assert(liner.StandardBeam.getStrainAtLocking(), 1.13)
    assert(liner.StandardBeam.getBeamElementFormulation(), LinerFormulation.P2_LINER_FORMULATION_BERNOULLI)
    assert(liner.StandardBeam.getAxialStrainExpansion(), 1.14)

def test10():
    liner = liner10

    liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)

    liner.StandardBeam.setSlidingGap(False)
    liner.StandardBeam.setBeamElementFormulation(LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
    liner.StandardBeam.setAxialStrainExpansion(1.14)

    assert(liner.StandardBeam.getSlidingGap(), False)
    assert(liner.StandardBeam.getBeamElementFormulation(), LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
    assert(liner.StandardBeam.getAxialStrainExpansion(), 1.14)

def test11():
    liner = liner11

    liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)

    liner.StandardBeam.setSlidingGap(False)
    liner.StandardBeam.setBeamElementFormulation(LinerFormulation.P2_LINER_FORMULATION_BERNOULLI)
    liner.StandardBeam.setAxialStrainExpansion(1.14)

    assert(liner.StandardBeam.getSlidingGap(), False)
    assert(liner.StandardBeam.getBeamElementFormulation(), LinerFormulation.P2_LINER_FORMULATION_BERNOULLI)
    assert(liner.StandardBeam.getAxialStrainExpansion(), 1.14)

def test12():
    liner = liner12

    liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)

    liner.StandardBeam.setActivateThermal(True)
    liner.StandardBeam.setStaticTemperatureMode(StaticWaterModes.SWM_PWP)
    liner.StandardBeam.setStaticTemperature(1.15)
    liner.StandardBeam.setSpecificHeatCapacity(1.16)
    liner.StandardBeam.setThermalExpansion(True)
    liner.StandardBeam.setExpansionCoefficient(1.17)

    assert(liner.StandardBeam.getActivateThermal(), True)
    assert(liner.StandardBeam.getStaticTemperatureMode(), StaticWaterModes.SWM_PWP)
    assert(liner.StandardBeam.getStaticTemperature(), 1.15)
    assert(liner.StandardBeam.getSpecificHeatCapacity(), 1.16)
    assert(liner.StandardBeam.getThermalExpansion(), True)
    assert(liner.StandardBeam.getExpansionCoefficient(), 1.17)

def test13():
    liner = liner13

    liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)

    liner.StandardBeam.setActivateThermal(True)
    liner.StandardBeam.setStaticTemperatureMode(StaticWaterModes.SWM_PWP)
    liner.StandardBeam.setStaticTemperature(1.15)
    liner.StandardBeam.setSpecificHeatCapacity(1.16)
    liner.StandardBeam.setThermalExpansion(False)

    assert(liner.StandardBeam.getActivateThermal(), True)
    assert(liner.StandardBeam.getStaticTemperatureMode(), StaticWaterModes.SWM_PWP)
    assert(liner.StandardBeam.getStaticTemperature(), 1.15)
    assert(liner.StandardBeam.getSpecificHeatCapacity(), 1.16)
    assert(liner.StandardBeam.getThermalExpansion(), False)

def test14():
    liner = liner14

    liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)

    liner.StandardBeam.setActivateThermal(True)
    liner.StandardBeam.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    liner.StandardBeam.setStaticTemperatureGridToUse('None')
    liner.StandardBeam.setSpecificHeatCapacity(1.16)
    liner.StandardBeam.setThermalExpansion(True)
    liner.StandardBeam.setExpansionCoefficient(1.17)

    assert(liner.StandardBeam.getActivateThermal(), True)
    assert(liner.StandardBeam.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(liner.StandardBeam.getStaticTemperatureGridToUse(), 'None')
    assert(liner.StandardBeam.getSpecificHeatCapacity(), 1.16)
    assert(liner.StandardBeam.getThermalExpansion(), True)
    assert(liner.StandardBeam.getExpansionCoefficient(), 1.17)

def test15():
    liner = liner15

    liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)

    liner.StandardBeam.setActivateThermal(True)
    liner.StandardBeam.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    liner.StandardBeam.setStaticTemperatureGridToUse('Default Grid')
    liner.StandardBeam.setSpecificHeatCapacity(1.16)
    liner.StandardBeam.setThermalExpansion(True)
    liner.StandardBeam.setExpansionCoefficient(1.17)

    assert(liner.StandardBeam.getActivateThermal(), True)
    assert(liner.StandardBeam.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(liner.StandardBeam.getStaticTemperatureGridToUse(), 'Default Grid')
    assert(liner.StandardBeam.getSpecificHeatCapacity(), 1.16)
    assert(liner.StandardBeam.getThermalExpansion(), True)
    assert(liner.StandardBeam.getExpansionCoefficient(), 1.17)

def test16():
    liner = liner16

    liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)

    liner.StandardBeam.setActivateThermal(True)
    liner.StandardBeam.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    liner.StandardBeam.setStaticTemperatureGridToUse('Grid 3')
    liner.StandardBeam.setSpecificHeatCapacity(1.16)
    liner.StandardBeam.setThermalExpansion(True)
    liner.StandardBeam.setExpansionCoefficient(1.17)

    assert(liner.StandardBeam.getActivateThermal(), True)
    assert(liner.StandardBeam.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(liner.StandardBeam.getStaticTemperatureGridToUse(), 'Grid 3')
    assert(liner.StandardBeam.getSpecificHeatCapacity(), 1.16)
    assert(liner.StandardBeam.getThermalExpansion(), True)
    assert(liner.StandardBeam.getExpansionCoefficient(), 1.17)

def test17():
    liner = liner17

    liner.setLinerType(LinerTypes.P2_LINER_STANDARD_BEAM)

    liner.StandardBeam.setActivateThermal(True)
    liner.StandardBeam.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    liner.StandardBeam.setStaticTemperatureGridToUse('Default Grid')
    liner.StandardBeam.setSpecificHeatCapacity(1.16)
    liner.StandardBeam.setThermalExpansion(False)

    assert(liner.StandardBeam.getActivateThermal(), True)
    assert(liner.StandardBeam.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(liner.StandardBeam.getStaticTemperatureGridToUse(), 'Default Grid')
    assert(liner.StandardBeam.getSpecificHeatCapacity(), 1.16)
    assert(liner.StandardBeam.getThermalExpansion(), False)

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
test15()
test16()
test17()

model.save()
pass