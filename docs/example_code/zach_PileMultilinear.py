from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\multiLinear_final.fez")

pileList = model.getAllPileProperties()
pile1 = pileList[0]
pile2 = pileList[1]
pile3 = pileList[2]
pile4 = pileList[3]

def test1():
    pile1.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_MULTI_LINEAR)
    pile1.MultiLinear.setShearStiffness(1.1)
    pile1.MultiLinear.setNormalStiffness(1.2)
    pile1.MultiLinear.setDefinitionMethod(PileDefinitionMethod.DISTANCE_FROM_TOP)
    pile1.MultiLinear.setCoordinates([1.1,1.3],[1.2,1.4])
    pile1.MultiLinear.setUseBaseResistance(True)
    pile1.MultiLinear.setBaseNormalStiffness(1.3)
    pile1.MultiLinear.setBaseForceResistance(1.4)

    
    assert(pile1.MultiLinear.getShearStiffness(), 1.1)
    assert(pile1.MultiLinear.getNormalStiffness(), 1.2)
    assert(pile1.MultiLinear.getDefinitionMethod(), PileDefinitionMethod.DISTANCE_FROM_TOP)
    assert(pile1.MultiLinear.getCoordinates(), [(1.1,1.3),(1.2,1.4)])
    assert(pile1.MultiLinear.getUseBaseResistance(), True)
    assert(pile1.MultiLinear.getBaseNormalStiffness(), 1.3)
    assert(pile1.MultiLinear.getBaseForceResistance(), 1.4)

def test2():
    pile2.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_MULTI_LINEAR)
    pile2.MultiLinear.setShearStiffness(1.1)
    pile2.MultiLinear.setNormalStiffness(1.2)
    pile2.MultiLinear.setDefinitionMethod(PileDefinitionMethod.ELEVATION)
    pile2.MultiLinear.setCoordinates([1.1,1.3],[1.2,1.4])
    pile2.MultiLinear.setUseBaseResistance(True)
    pile2.MultiLinear.setBaseNormalStiffness(1.3)
    pile2.MultiLinear.setBaseForceResistance(1.4)

    assert(pile2.MultiLinear.getShearStiffness(), 1.1)
    assert(pile2.MultiLinear.getNormalStiffness(), 1.2)
    assert(pile2.MultiLinear.getDefinitionMethod(), PileDefinitionMethod.ELEVATION)
    assert(pile2.MultiLinear.getCoordinates(), [(1.1,1.3),(1.2,1.4)])
    assert(pile2.MultiLinear.getUseBaseResistance(), True)
    assert(pile2.MultiLinear.getBaseNormalStiffness(), 1.3)
    assert(pile2.MultiLinear.getBaseForceResistance(), 1.4)

def test3():
    pile3.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_MULTI_LINEAR)
    pile3.MultiLinear.setShearStiffness(1.1)
    pile3.MultiLinear.setNormalStiffness(1.2)
    pile3.MultiLinear.setDefinitionMethod(PileDefinitionMethod.DISTANCE_FROM_TOP)
    pile3.MultiLinear.setCoordinates([1.1,1.3],[1.2,1.4])
    pile3.MultiLinear.setUseBaseResistance(False)

    assert(pile3.MultiLinear.getShearStiffness(), 1.1)
    assert(pile3.MultiLinear.getNormalStiffness(), 1.2)
    assert(pile3.MultiLinear.getDefinitionMethod(), PileDefinitionMethod.DISTANCE_FROM_TOP)
    assert(pile3.MultiLinear.getCoordinates(), [(1.1,1.3),(1.2,1.4)])
    assert(pile3.MultiLinear.getUseBaseResistance(), False)

def test4():
    pile4.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_MULTI_LINEAR)
    pile4.MultiLinear.setShearStiffness(1.1)
    pile4.MultiLinear.setNormalStiffness(1.2)
    pile4.MultiLinear.setDefinitionMethod(PileDefinitionMethod.ELEVATION)
    pile4.MultiLinear.setCoordinates([1.1,1.3],[1.2,1.4])
    pile4.MultiLinear.setUseBaseResistance(False)

    assert(pile4.MultiLinear.getShearStiffness(), 1.1)
    assert(pile4.MultiLinear.getNormalStiffness(), 1.2)
    assert(pile4.MultiLinear.getDefinitionMethod(), PileDefinitionMethod.ELEVATION)
    assert(pile4.MultiLinear.getCoordinates(), [(1.1,1.3),(1.2,1.4)])
    assert(pile4.MultiLinear.getUseBaseResistance(), False)

test1()
test2()
test3()
test4()

model.save()

pass