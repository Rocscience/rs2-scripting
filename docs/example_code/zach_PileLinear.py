from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\linear_final.fez")

pileList = model.getAllPileProperties()
pile1 = pileList[0]
pile2 = pileList[1]

def test1():
    pile1.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_LINEAR)
    pile1.Linear.setShearStiffness(1.1)
    pile1.Linear.setNormalStiffness(1.2)
    pile1.Linear.setMaxTractionAtTheTop(1.3)
    pile1.Linear.setMaxTractionAtTheBottom(1.4)
    pile1.Linear.setUseBaseResistance(True)
    pile1.Linear.setBaseNormalStiffness(1.5)
    pile1.Linear.setBaseForceResistance(1.6)

    assert(pile1.Linear.getShearStiffness(), 1.1)
    assert(pile1.Linear.getNormalStiffness(), 1.2)
    assert(pile1.Linear.getMaxTractionAtTheTop(), 1.3)
    assert(pile1.Linear.getMaxTractionAtTheBottom(), 1.4)
    assert(pile1.Linear.getUseBaseResistance(), True)
    assert(pile1.Linear.getBaseNormalStiffness(), 1.5)  
    assert(pile1.Linear.getBaseForceResistance(), 1.6)

def test2():
    pile2.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_LINEAR)
    pile2.Linear.setShearStiffness(1.1)
    pile2.Linear.setNormalStiffness(1.2)
    pile2.Linear.setMaxTractionAtTheTop(1.3)
    pile2.Linear.setMaxTractionAtTheBottom(1.4)
    pile2.Linear.setUseBaseResistance(False)

    assert(pile2.Linear.getShearStiffness(), 1.1)  
    assert(pile2.Linear.getNormalStiffness(), 1.2)
    assert(pile2.Linear.getMaxTractionAtTheTop(), 1.3)
    assert(pile2.Linear.getMaxTractionAtTheBottom(), 1.4)
    assert(pile2.Linear.getUseBaseResistance(), False)

test1()
test2()

model.save()

pass