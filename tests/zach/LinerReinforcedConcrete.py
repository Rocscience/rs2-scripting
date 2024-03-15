from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Liner\reinforcedConcrete_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Liner\reinforcedConcrete_python.fez'

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

    liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)

    liner.ReinforcedConcrete.setActivateThermal(True) #Makes set initial temperature and set unit weight available
    liner.ReinforcedConcrete.setConcrete(True) #Makes concrete unit weight available
    liner.ReinforcedConcrete.setIncludeWeightInStressAnalysis(True)

    liner.ReinforcedConcrete.setConcreteUnitWeight(1.1)
    liner.ReinforcedConcrete.setInitialTemperature(1.2)

    assert(liner.getLinerType(), LinerTypes.P2_LINER_REINFORCED_CONCRETE)
    assert(liner.ReinforcedConcrete.getConcreteUnitWeight(), 1.1)
    assert(liner.ReinforcedConcrete.getInitialTemperature(), 1.2)

def test2():
    liner = liner2

    liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)
    
    liner.ReinforcedConcrete.setReinforcement(False)

    assert(liner.ReinforcedConcrete.getReinforcement(), False)

def test3():
    liner = liner3

    liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)
    liner.ReinforcedConcrete.setIncludeWeightInStressAnalysis(True) # Makes set weight available
    
    liner.ReinforcedConcrete.setReinforcement(True)
    liner.ReinforcedConcrete.setSpacing(1.3)
    liner.ReinforcedConcrete.setSectionDepth(1.4)
    liner.ReinforcedConcrete.setArea(1.5)
    liner.ReinforcedConcrete.setMomentOfInertia(1.6)
    #liner.ReinforcedConcrete.setYoungsModulus(1.7)         Reinforcement methods are switched with concrete methods
    #liner.ReinforcedConcrete.setCompressiveStrength(1.8)
    #liner.ReinforcedConcrete.setTensileStrength(1.9)
    liner.ReinforcedConcrete.setWeight(1.11)

    assert(liner.ReinforcedConcrete.getReinforcement(), True)
    assert(liner.ReinforcedConcrete.getSpacing(), 1.3)
    assert(liner.ReinforcedConcrete.getSectionDepth(), 1.4)
    assert(liner.ReinforcedConcrete.getArea(), 1.5)
    assert(liner.ReinforcedConcrete.getMomentOfInertia(), 1.6)
    #assert(liner.ReinforcedConcrete.getYoungsModulus(), 1.7)
    #assert(liner.ReinforcedConcrete.getCompressiveStrength(), 1.8)
    #assert(liner.ReinforcedConcrete.getTensileStrength(), 1.9)
    assert(liner.ReinforcedConcrete.getWeight(), 1.11)

def test4():
    liner = liner4

    liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)

    liner.ReinforcedConcrete.setConcrete(False)

    assert(liner.ReinforcedConcrete.getConcrete(), False)

def test5():
    liner = liner5

    liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)

    liner.ReinforcedConcrete.setConcrete(True)
    liner.ReinforcedConcrete.setThickness(1.12)
    #liner.ReinforcedConcrete.setConcreteYoungsModulus(1.13)            Reinforcement methods are switched with concrete methods
    liner.ReinforcedConcrete.setPoissonRatio(0.14)
    #liner.ReinforcedConcrete.setConcreteCompressiveStrength(1.15)
    #liner.ReinforcedConcrete.setConcreteTensileStrength(1.16)

    assert(liner.ReinforcedConcrete.getConcrete(), True)
    assert(liner.ReinforcedConcrete.getThickness(), 1.12)
    #assert(liner.ReinforcedConcrete.getConcreteYoungsModulus(), 1.13)
    assert(liner.ReinforcedConcrete.getPoissonRatio(), 0.14)
    #assert(liner.ReinforcedConcrete.getConcreteCompressiveStrength(), 1.15) 
    #assert(liner.ReinforcedConcrete.getConcreteTensileStrength(), 1.16)

def test6():
    liner = liner6

    liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)

    liner.ReinforcedConcrete.setMaterialType(MaterialType.PLASTIC)
    liner.ReinforcedConcrete.setSlidingGap(False)
    liner.ReinforcedConcrete.setBeamElementFormulation(LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
    liner.ReinforcedConcrete.setAxialStrainExpansion(1.18)

    assert(liner.ReinforcedConcrete.getMaterialType(), MaterialType.PLASTIC)
    assert(liner.ReinforcedConcrete.getSlidingGap(), False)
    assert(liner.ReinforcedConcrete.getBeamElementFormulation(), LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
    assert(liner.ReinforcedConcrete.getAxialStrainExpansion(), 1.18)

def test7():
    liner = liner7

    liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)

    liner.ReinforcedConcrete.setMaterialType(MaterialType.ELASTIC)
    liner.ReinforcedConcrete.setSlidingGap(True)
    liner.ReinforcedConcrete.setStrainAtLocking(1.17)
    liner.ReinforcedConcrete.setBeamElementFormulation(LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
    liner.ReinforcedConcrete.setAxialStrainExpansion(1.18)

    assert(liner.ReinforcedConcrete.getMaterialType(), MaterialType.ELASTIC)
    assert(liner.ReinforcedConcrete.getSlidingGap(), True)
    assert(liner.ReinforcedConcrete.getStrainAtLocking(),1.17)
    assert(liner.ReinforcedConcrete.getBeamElementFormulation(), LinerFormulation.P2_LINER_FORMULATION_TIMOSHENKO)
    assert(liner.ReinforcedConcrete.getAxialStrainExpansion(), 1.18)

def test8():
    liner = liner8

    liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)

    liner.ReinforcedConcrete.setMaterialType(MaterialType.ELASTIC)
    liner.ReinforcedConcrete.setSlidingGap(False)
    liner.ReinforcedConcrete.setBeamElementFormulation(LinerFormulation.P2_LINER_FORMULATION_BERNOULLI)
    liner.ReinforcedConcrete.setAxialStrainExpansion(1.18)

    assert(liner.ReinforcedConcrete.getMaterialType(), MaterialType.ELASTIC)
    assert(liner.ReinforcedConcrete.getSlidingGap(), False)
    assert(liner.ReinforcedConcrete.getBeamElementFormulation(), LinerFormulation.P2_LINER_FORMULATION_BERNOULLI)
    assert(liner.ReinforcedConcrete.getAxialStrainExpansion(), 1.18)

def test9():
    liner = liner9

    liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)

    liner.ReinforcedConcrete.setActivateThermal(True)
    liner.ReinforcedConcrete.setStaticTemperatureMode(StaticWaterModes.SWM_PWP)
    liner.ReinforcedConcrete.setStaticTemperature(1.19)
    liner.ReinforcedConcrete.setSpecificHeatCapacity(1.21)
    liner.ReinforcedConcrete.setThermalExpansion(True)
    liner.ReinforcedConcrete.setExpansionCoefficient(1.22)

    assert(liner.ReinforcedConcrete.getActivateThermal(), True)
    assert(liner.ReinforcedConcrete.getStaticTemperatureMode(), StaticWaterModes.SWM_PWP)
    assert(liner.ReinforcedConcrete.getStaticTemperature(), 1.19)
    assert(liner.ReinforcedConcrete.getSpecificHeatCapacity(), 1.21)
    assert(liner.ReinforcedConcrete.getThermalExpansion(), True)
    assert(liner.ReinforcedConcrete.getExpansionCoefficient(), 1.22)

def test10():
    liner = liner10

    liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)

    liner.ReinforcedConcrete.setActivateThermal(True)
    liner.ReinforcedConcrete.setStaticTemperatureMode(StaticWaterModes.SWM_PWP)
    liner.ReinforcedConcrete.setStaticTemperature(1.19)
    liner.ReinforcedConcrete.setSpecificHeatCapacity(1.21)
    liner.ReinforcedConcrete.setThermalExpansion(False)

    assert(liner.ReinforcedConcrete.getActivateThermal(), True)
    assert(liner.ReinforcedConcrete.getStaticTemperatureMode(), StaticWaterModes.SWM_PWP)
    assert(liner.ReinforcedConcrete.getStaticTemperature(), 1.19)
    assert(liner.ReinforcedConcrete.getSpecificHeatCapacity(), 1.21)
    assert(liner.ReinforcedConcrete.getThermalExpansion(), False)

def test11():
    liner = liner11

    liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)

    liner.ReinforcedConcrete.setActivateThermal(True)
    liner.ReinforcedConcrete.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    liner.ReinforcedConcrete.setStaticTemperatureGridToUse('None')
    liner.ReinforcedConcrete.setSpecificHeatCapacity(1.21)
    liner.ReinforcedConcrete.setThermalExpansion(True)
    liner.ReinforcedConcrete.setExpansionCoefficient(1.22)

    assert(liner.ReinforcedConcrete.getActivateThermal(), True)
    assert(liner.ReinforcedConcrete.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(liner.ReinforcedConcrete.getStaticTemperatureGridToUse(), 'None')
    assert(liner.ReinforcedConcrete.getSpecificHeatCapacity(), 1.21)
    assert(liner.ReinforcedConcrete.getThermalExpansion(), True)
    assert(liner.ReinforcedConcrete.getExpansionCoefficient(), 1.22)

def test12():
    liner = liner12

    liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)

    liner.ReinforcedConcrete.setActivateThermal(True)
    liner.ReinforcedConcrete.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    liner.ReinforcedConcrete.setStaticTemperatureGridToUse('Default Grid')
    liner.ReinforcedConcrete.setSpecificHeatCapacity(1.21)
    liner.ReinforcedConcrete.setThermalExpansion(True)
    liner.ReinforcedConcrete.setExpansionCoefficient(1.22)

    assert(liner.ReinforcedConcrete.getActivateThermal(), True)
    assert(liner.ReinforcedConcrete.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(liner.ReinforcedConcrete.getStaticTemperatureGridToUse(), 'Default Grid')
    assert(liner.ReinforcedConcrete.getSpecificHeatCapacity(), 1.21)
    assert(liner.ReinforcedConcrete.getThermalExpansion(), True)
    assert(liner.ReinforcedConcrete.getExpansionCoefficient(), 1.22)

def test13():
    liner = liner13

    liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)

    liner.ReinforcedConcrete.setActivateThermal(True)
    liner.ReinforcedConcrete.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    liner.ReinforcedConcrete.setStaticTemperatureGridToUse('Grid 3')
    liner.ReinforcedConcrete.setSpecificHeatCapacity(1.21)
    liner.ReinforcedConcrete.setThermalExpansion(True)
    liner.ReinforcedConcrete.setExpansionCoefficient(1.22)

    assert(liner.ReinforcedConcrete.getActivateThermal(), True)
    assert(liner.ReinforcedConcrete.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(liner.ReinforcedConcrete.getStaticTemperatureGridToUse(), 'Grid 3')
    assert(liner.ReinforcedConcrete.getSpecificHeatCapacity(), 1.21)
    assert(liner.ReinforcedConcrete.getThermalExpansion(), True)
    assert(liner.ReinforcedConcrete.getExpansionCoefficient(), 1.22)

def test14():
    liner = liner14

    liner.setLinerType(LinerTypes.P2_LINER_REINFORCED_CONCRETE)

    liner.ReinforcedConcrete.setActivateThermal(True)
    liner.ReinforcedConcrete.setStaticTemperatureMode(StaticWaterModes.SWM_GRID)
    liner.ReinforcedConcrete.setStaticTemperatureGridToUse('Default Grid')
    liner.ReinforcedConcrete.setSpecificHeatCapacity(1.21)
    liner.ReinforcedConcrete.setThermalExpansion(False)

    assert(liner.ReinforcedConcrete.getActivateThermal(), True)
    assert(liner.ReinforcedConcrete.getStaticTemperatureMode(), StaticWaterModes.SWM_GRID)
    assert(liner.ReinforcedConcrete.getStaticTemperatureGridToUse(), 'Default Grid')
    assert(liner.ReinforcedConcrete.getSpecificHeatCapacity(), 1.21)
    assert(liner.ReinforcedConcrete.getThermalExpansion(), False)



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