from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_BoltAndPile.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Pile\materialDependent_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Pile\materialDependent_python.fez'

model = modeler.openFile(base_model)

pileList = model.getAllPileProperties()
pile1 = pileList[0]
pile2 = pileList[1]
pile3 = pileList[2]
pile4 = pileList[3]
pile5 = pileList[4]
pile6 = pileList[5]
pile7 = pileList[6]
pile8 = pileList[7]

def test1():
    pile1.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_MATERIAL_DEPENDENT)
    pile1.MaterialDependentPile.setInterfaceCoefficient(1.1)
    pile1.MaterialDependentPile.setUseStiffnessMaterialDependent(True)
    pile1.MaterialDependentPile.setStiffnessCoefficient(1.2)
    pile1.MaterialDependentPile.setUseShearResistanceCutoff(True)
    pile1.MaterialDependentPile.setShearResistanceCutoff(1.5)
    pile1.MaterialDependentPile.setPerimeter(1.6)
    pile1.MaterialDependentPile.setUseBaseResistance(True)
    pile1.MaterialDependentPile.setBaseNormalStiffness(1.7)
    pile1.MaterialDependentPile.setBaseForceResistance(1.8)

    assert(pile1.MaterialDependentPile.getInterfaceCoefficient(), 1.1)
    assert(pile1.MaterialDependentPile.getUseStiffnessMaterialDependent(), True)
    assert(pile1.MaterialDependentPile.getStiffnessCoefficient(), 1.2) 
    assert(pile1.MaterialDependentPile.getUseShearResistanceCutoff(), True)
    assert(pile1.MaterialDependentPile.getShearResistanceCutoff(), 1.5)
    assert(pile1.MaterialDependentPile.getPerimeter(), 1.6)
    assert(pile1.MaterialDependentPile.getUseBaseResistance(), True)
    assert(pile1.MaterialDependentPile.getBaseNormalStiffness(), 1.7)
    assert(pile1.MaterialDependentPile.getBaseForceResistance(), 1.8)


def test2():
    pile2.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_MATERIAL_DEPENDENT)
    pile2.MaterialDependentPile.setInterfaceCoefficient(1.1)  
    pile2.MaterialDependentPile.setUseStiffnessMaterialDependent(False)
    pile2.MaterialDependentPile.setShearStiffness(1.3)
    pile2.MaterialDependentPile.setNormalStiffness(1.4)
    pile2.MaterialDependentPile.setUseShearResistanceCutoff(False)
    pile2.MaterialDependentPile.setPerimeter(1.6)
    pile2.MaterialDependentPile.setUseBaseResistance(False)

    assert(pile2.MaterialDependentPile.getInterfaceCoefficient(), 1.1)
    assert(pile2.MaterialDependentPile.getUseStiffnessMaterialDependent(), False)
    assert(pile2.MaterialDependentPile.getShearStiffness(), 1.3)
    assert(pile2.MaterialDependentPile.getNormalStiffness(), 1.4)
    assert(pile2.MaterialDependentPile.getUseShearResistanceCutoff(), False)
    assert(pile2.MaterialDependentPile.getPerimeter(), 1.6)
    assert(pile2.MaterialDependentPile.getUseBaseResistance(), False)

def test3():
    pile3.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_MATERIAL_DEPENDENT)
    pile3.MaterialDependentPile.setInterfaceCoefficient(1.1)
    pile3.MaterialDependentPile.setUseStiffnessMaterialDependent(True)
    pile3.MaterialDependentPile.setStiffnessCoefficient(1.2)
    pile3.MaterialDependentPile.setUseShearResistanceCutoff(False)
    pile3.MaterialDependentPile.setPerimeter(1.6)
    pile3.MaterialDependentPile.setUseBaseResistance(False)

    assert(pile3.MaterialDependentPile.getInterfaceCoefficient(), 1.1)
    assert(pile3.MaterialDependentPile.getUseStiffnessMaterialDependent(), True)
    assert(pile3.MaterialDependentPile.getStiffnessCoefficient(), 1.2)
    assert(pile3.MaterialDependentPile.getUseShearResistanceCutoff(), False)
    assert(pile3.MaterialDependentPile.getPerimeter(), 1.6)
    assert(pile3.MaterialDependentPile.getUseBaseResistance(), False)

def test4():
    pile4.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_MATERIAL_DEPENDENT)
    pile4.MaterialDependentPile.setInterfaceCoefficient(1.1)
    pile4.MaterialDependentPile.setUseStiffnessMaterialDependent(False)
    pile4.MaterialDependentPile.setShearStiffness(1.3)
    pile4.MaterialDependentPile.setNormalStiffness(1.4)
    pile4.MaterialDependentPile.setUseShearResistanceCutoff(True)
    pile4.MaterialDependentPile.setShearResistanceCutoff(1.5)
    pile4.MaterialDependentPile.setPerimeter(1.6)
    pile4.MaterialDependentPile.setUseBaseResistance(False)
    
    assert(pile4.MaterialDependentPile.getInterfaceCoefficient(), 1.1)
    assert(pile4.MaterialDependentPile.getUseStiffnessMaterialDependent(), False)
    assert(pile4.MaterialDependentPile.getShearStiffness(), 1.3)
    assert(pile4.MaterialDependentPile.getNormalStiffness(), 1.4)
    assert(pile4.MaterialDependentPile.getUseShearResistanceCutoff(), True)
    assert(pile4.MaterialDependentPile.getShearResistanceCutoff(), 1.5)
    assert(pile4.MaterialDependentPile.getPerimeter(), 1.6)
    assert(pile4.MaterialDependentPile.getUseBaseResistance(), False)

def test5():
    pile5.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_MATERIAL_DEPENDENT)
    pile5.MaterialDependentPile.setInterfaceCoefficient(1.1)
    pile5.MaterialDependentPile.setUseStiffnessMaterialDependent(False) 
    pile5.MaterialDependentPile.setShearStiffness(1.3)
    pile5.MaterialDependentPile.setNormalStiffness(1.4)
    pile5.MaterialDependentPile.setUseShearResistanceCutoff(False)
    pile5.MaterialDependentPile.setPerimeter(1.6)
    pile5.MaterialDependentPile.setUseBaseResistance(True)
    pile5.MaterialDependentPile.setBaseNormalStiffness(1.7)
    pile5.MaterialDependentPile.setBaseForceResistance(1.8)
    
    assert(pile5.MaterialDependentPile.getInterfaceCoefficient(), 1.1)
    assert(pile5.MaterialDependentPile.getUseStiffnessMaterialDependent(), False)
    assert(pile5.MaterialDependentPile.getShearStiffness(), 1.3)
    assert(pile5.MaterialDependentPile.getNormalStiffness(), 1.4)
    assert(pile5.MaterialDependentPile.getUseShearResistanceCutoff(), False)
    assert(pile5.MaterialDependentPile.getPerimeter(), 1.6)
    assert(pile5.MaterialDependentPile.getUseBaseResistance(), True)
    assert(pile5.MaterialDependentPile.getBaseNormalStiffness(), 1.7)
    assert(pile5.MaterialDependentPile.getBaseForceResistance(), 1.8)

def test6():
    pile6.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_MATERIAL_DEPENDENT)
    pile6.MaterialDependentPile.setInterfaceCoefficient(1.1)
    pile6.MaterialDependentPile.setUseStiffnessMaterialDependent(True)
    pile6.MaterialDependentPile.setStiffnessCoefficient(1.2)
    pile6.MaterialDependentPile.setUseShearResistanceCutoff(True)
    pile6.MaterialDependentPile.setShearResistanceCutoff(1.5)
    pile6.MaterialDependentPile.setPerimeter(1.6)
    pile6.MaterialDependentPile.setUseBaseResistance(False)

    assert(pile6.MaterialDependentPile.getInterfaceCoefficient(), 1.1)
    assert(pile6.MaterialDependentPile.getUseStiffnessMaterialDependent(), True)
    assert(pile6.MaterialDependentPile.getStiffnessCoefficient(), 1.2)
    assert(pile6.MaterialDependentPile.getUseShearResistanceCutoff(), True)
    assert(pile6.MaterialDependentPile.getShearResistanceCutoff(), 1.5)
    assert(pile6.MaterialDependentPile.getPerimeter(), 1.6)
    assert(pile6.MaterialDependentPile.getUseBaseResistance(), False)

def test7():
    pile7.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_MATERIAL_DEPENDENT)
    pile7.MaterialDependentPile.setInterfaceCoefficient(1.1)
    pile7.MaterialDependentPile.setUseStiffnessMaterialDependent(True)
    pile7.MaterialDependentPile.setStiffnessCoefficient(1.2)
    pile7.MaterialDependentPile.setUseShearResistanceCutoff(False)
    pile7.MaterialDependentPile.setPerimeter(1.6)
    pile7.MaterialDependentPile.setUseBaseResistance(True)
    pile7.MaterialDependentPile.setBaseNormalStiffness(1.7)
    pile7.MaterialDependentPile.setBaseForceResistance(1.8)

    assert(pile7.MaterialDependentPile.getInterfaceCoefficient(), 1.1)
    assert(pile7.MaterialDependentPile.getUseStiffnessMaterialDependent(), True)
    assert(pile7.MaterialDependentPile.getStiffnessCoefficient(), 1.2)
    assert(pile7.MaterialDependentPile.getUseShearResistanceCutoff(), False) 
    assert(pile7.MaterialDependentPile.getPerimeter(), 1.6)
    assert(pile7.MaterialDependentPile.getUseBaseResistance(), True)
    assert(pile7.MaterialDependentPile.getBaseNormalStiffness(), 1.7)
    assert(pile7.MaterialDependentPile.getBaseForceResistance(), 1.8)

def test8():
    pile8.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_MATERIAL_DEPENDENT)
    pile8.MaterialDependentPile.setInterfaceCoefficient(1.1)
    pile8.MaterialDependentPile.setUseStiffnessMaterialDependent(False)
    pile8.MaterialDependentPile.setShearStiffness(1.3)
    pile8.MaterialDependentPile.setNormalStiffness(1.4)
    pile8.MaterialDependentPile.setUseShearResistanceCutoff(True)
    pile8.MaterialDependentPile.setShearResistanceCutoff(1.5)
    pile8.MaterialDependentPile.setPerimeter(1.6)
    pile8.MaterialDependentPile.setUseBaseResistance(True)
    pile8.MaterialDependentPile.setBaseNormalStiffness(1.7)
    pile8.MaterialDependentPile.setBaseForceResistance(1.8)

    assert(pile8.MaterialDependentPile.getInterfaceCoefficient(), 1.1)
    assert(pile8.MaterialDependentPile.getUseStiffnessMaterialDependent(), False)
    assert(pile8.MaterialDependentPile.getShearStiffness(), 1.3)
    assert(pile8.MaterialDependentPile.getNormalStiffness(), 1.4)
    assert(pile8.MaterialDependentPile.getUseShearResistanceCutoff(), True)
    assert(pile8.MaterialDependentPile.getShearResistanceCutoff(), 1.5)
    assert(pile8.MaterialDependentPile.getPerimeter(), 1.6)
    assert(pile8.MaterialDependentPile.getUseBaseResistance(), True)
    assert(pile8.MaterialDependentPile.getBaseNormalStiffness(), 1.7)
    assert(pile8.MaterialDependentPile.getBaseForceResistance(), 1.8)

test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()

model.saveAs(final_python_model)

pass