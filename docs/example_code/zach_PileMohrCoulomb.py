from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\mohrCoulomb_final.fez")

pileList = model.getAllPileProperties()
pile1 = pileList[0]
pile2 = pileList[1]
pile3 = pileList[2]
pile4 = pileList[3]

def test1():
    pile1.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_C_PHI)
    pile1.MohrCoulombPile.setShearStiffness(1.1)
    pile1.MohrCoulombPile.setNormalStiffness(1.2)
    pile1.MohrCoulombPile.setFrictionAngle(1.3)
    pile1.MohrCoulombPile.setResidualFrictionAngle(1.4)
    pile1.MohrCoulombPile.setCohesion(1.5)
    pile1.MohrCoulombPile.setResidualCohesion(1.6)
    pile1.MohrCoulombPile.setUseShearResistanceCutoff(True)
    pile1.MohrCoulombPile.setShearResistanceCutoff(1.7)
    pile1.MohrCoulombPile.setPerimeter(1.8)
    pile1.MohrCoulombPile.setUseBaseResistance(True)
    pile1.MohrCoulombPile.setBaseNormalStiffness(1.9)
    pile1.MohrCoulombPile.setBaseForceResistance(1.11)

    
    assert(pile1.MohrCoulombPile.getShearStiffness(), 1.1)
    assert(pile1.MohrCoulombPile.getNormalStiffness(), 1.2)  
    assert(pile1.MohrCoulombPile.getFrictionAngle(), 1.3)
    assert(pile1.MohrCoulombPile.getResidualFrictionAngle(), 1.4)
    assert(pile1.MohrCoulombPile.getCohesion(), 1.5)
    assert(pile1.MohrCoulombPile.getResidualCohesion(), 1.6)
    assert(pile1.MohrCoulombPile.getUseShearResistanceCutoff(), True)
    assert(pile1.MohrCoulombPile.getShearResistanceCutoff(), 1.7)
    assert(pile1.MohrCoulombPile.getPerimeter(), 1.8)
    assert(pile1.MohrCoulombPile.getUseBaseResistance(), True)
    assert(pile1.MohrCoulombPile.getBaseNormalStiffness(), 1.9)
    assert(pile1.MohrCoulombPile.getBaseForceResistance(), 1.11)

def test2():
    pile2.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_C_PHI)
    pile2.MohrCoulombPile.setShearStiffness(1.1)
    pile2.MohrCoulombPile.setNormalStiffness(1.2)
    pile2.MohrCoulombPile.setFrictionAngle(1.3)
    pile2.MohrCoulombPile.setResidualFrictionAngle(1.4)
    pile2.MohrCoulombPile.setCohesion(1.5)
    pile2.MohrCoulombPile.setResidualCohesion(1.6)
    pile2.MohrCoulombPile.setUseShearResistanceCutoff(False)
    pile2.MohrCoulombPile.setPerimeter(1.8)
    pile2.MohrCoulombPile.setUseBaseResistance(False)

    assert(pile2.MohrCoulombPile.getShearStiffness(), 1.1)  
    assert(pile2.MohrCoulombPile.getNormalStiffness(), 1.2)
    assert(pile2.MohrCoulombPile.getFrictionAngle(), 1.3)
    assert(pile2.MohrCoulombPile.getResidualFrictionAngle(), 1.4)
    assert(pile2.MohrCoulombPile.getCohesion(), 1.5)
    assert(pile2.MohrCoulombPile.getResidualCohesion(), 1.6)
    assert(pile2.MohrCoulombPile.getUseShearResistanceCutoff(), False) 
    assert(pile2.MohrCoulombPile.getPerimeter(), 1.8)
    assert(pile2.MohrCoulombPile.getUseBaseResistance(), False)

def test3():
    pile3.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_C_PHI)
    pile3.MohrCoulombPile.setShearStiffness(1.1)
    pile3.MohrCoulombPile.setNormalStiffness(1.2)
    pile3.MohrCoulombPile.setFrictionAngle(1.3)
    pile3.MohrCoulombPile.setResidualFrictionAngle(1.4)
    pile3.MohrCoulombPile.setCohesion(1.5)
    pile3.MohrCoulombPile.setResidualCohesion(1.6)
    pile3.MohrCoulombPile.setUseShearResistanceCutoff(True)
    pile3.MohrCoulombPile.setShearResistanceCutoff(1.7)
    pile3.MohrCoulombPile.setPerimeter(1.8)
    pile3.MohrCoulombPile.setUseBaseResistance(False)

    assert(pile3.MohrCoulombPile.getShearStiffness(), 1.1)
    assert(pile3.MohrCoulombPile.getNormalStiffness(), 1.2)
    assert(pile3.MohrCoulombPile.getFrictionAngle(), 1.3)
    assert(pile3.MohrCoulombPile.getResidualFrictionAngle(), 1.4)
    assert(pile3.MohrCoulombPile.getCohesion(), 1.5)
    assert(pile3.MohrCoulombPile.getResidualCohesion(), 1.6)
    assert(pile3.MohrCoulombPile.getUseShearResistanceCutoff(), True)
    assert(pile3.MohrCoulombPile.getShearResistanceCutoff(), 1.7)
    assert(pile3.MohrCoulombPile.getPerimeter(), 1.8)
    assert(pile3.MohrCoulombPile.getUseBaseResistance(), False)

def test4():
    pile4.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_C_PHI)
    pile4.MohrCoulombPile.setShearStiffness(1.1)
    pile4.MohrCoulombPile.setNormalStiffness(1.2)
    pile4.MohrCoulombPile.setFrictionAngle(1.3)
    pile4.MohrCoulombPile.setResidualFrictionAngle(1.4)
    pile4.MohrCoulombPile.setCohesion(1.5)
    pile4.MohrCoulombPile.setResidualCohesion(1.6)
    pile4.MohrCoulombPile.setUseShearResistanceCutoff(False)
    pile4.MohrCoulombPile.setPerimeter(1.8)
    pile4.MohrCoulombPile.setUseBaseResistance(True)
    pile4.MohrCoulombPile.setBaseNormalStiffness(1.9)
    pile4.MohrCoulombPile.setBaseForceResistance(1.11)

    assert(pile4.MohrCoulombPile.getShearStiffness(), 1.1)
    assert(pile4.MohrCoulombPile.getNormalStiffness(), 1.2)
    assert(pile4.MohrCoulombPile.getFrictionAngle(), 1.3)
    assert(pile4.MohrCoulombPile.getResidualFrictionAngle(), 1.4)
    assert(pile4.MohrCoulombPile.getCohesion(), 1.5)
    assert(pile4.MohrCoulombPile.getResidualCohesion(), 1.6)
    assert(pile4.MohrCoulombPile.getUseShearResistanceCutoff(), False)
    assert(pile4.MohrCoulombPile.getPerimeter(), 1.8)
    assert(pile4.MohrCoulombPile.getUseBaseResistance(), True)
    assert(pile4.MohrCoulombPile.getBaseNormalStiffness(), 1.9)
    assert(pile4.MohrCoulombPile.getBaseForceResistance(), 1.11)

test1()
test2()
test3()
test4()

model.save()

pass