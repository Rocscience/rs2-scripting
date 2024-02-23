from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\Pile\applyForce_final.fez")

pileList = model.getAllPileProperties()
pile1 = pileList[0]
pile2 = pileList[1]

def test1():
    pile1.ForceDisplacement.setApply(PileEndCondition.FP_FORCE)
    pile1.ForceDisplacement.setApplyOn(PileForceApplicationPoint.FP_TOP)
    pile1.ForceDisplacement.setX(1.1)
    pile1.ForceDisplacement.setY(1.2)

    
    assert(pile1.ForceDisplacement.getApply(), PileEndCondition.FP_FORCE)
    assert(pile1.ForceDisplacement.getApplyOn(), PileForceApplicationPoint.FP_TOP)  
    assert(pile1.ForceDisplacement.getX(), 1.1)
    assert(pile1.ForceDisplacement.getY(), 1.2)

def test2():
    pile2.ForceDisplacement.setApply(PileEndCondition.FP_FORCE)
    pile2.ForceDisplacement.setApplyOn(PileForceApplicationPoint.FP_BOTTOM)
    pile2.ForceDisplacement.setX(1.1)
    pile2.ForceDisplacement.setY(1.2)

    assert(pile2.ForceDisplacement.getApply(), PileEndCondition.FP_FORCE)
    assert(pile2.ForceDisplacement.getApplyOn(), PileForceApplicationPoint.FP_BOTTOM)  
    assert(pile2.ForceDisplacement.getX(), 1.1)
    assert(pile2.ForceDisplacement.getY(), 1.2)
    

test1()
test2()

model.save()

pass