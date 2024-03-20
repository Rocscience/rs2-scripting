from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_BoltAndPile.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Pile\applyDisp_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Pile\applyDisp_python.fez'

model = modeler.openFile(base_model)

pileList = model.getAllPileProperties()
pile1 = pileList[0]
pile2 = pileList[1]

def test1():
    pile1.ForceDisplacement.setApply(PileEndCondition.FP_DISPLACEMENT)
    pile1.ForceDisplacement.setApplyOn(PileForceApplicationPoint.FP_TOP)
    pile1.ForceDisplacement.setX(1.1)
    pile1.ForceDisplacement.setY(1.2)

    
    assert(pile1.ForceDisplacement.getApply(), PileEndCondition.FP_DISPLACEMENT)
    assert(pile1.ForceDisplacement.getApplyOn(), PileForceApplicationPoint.FP_TOP)  
    assert(pile1.ForceDisplacement.getX(), 1.1)
    assert(pile1.ForceDisplacement.getY(), 1.2)

def test2():
    pile2.ForceDisplacement.setApply(PileEndCondition.FP_DISPLACEMENT)
    pile2.ForceDisplacement.setApplyOn(PileForceApplicationPoint.FP_BOTTOM)
    pile2.ForceDisplacement.setX(1.1)
    pile2.ForceDisplacement.setY(1.2)

    assert(pile2.ForceDisplacement.getApply(), PileEndCondition.FP_DISPLACEMENT)
    assert(pile2.ForceDisplacement.getApplyOn(), PileForceApplicationPoint.FP_BOTTOM)  
    assert(pile2.ForceDisplacement.getX(), 1.1)
    assert(pile2.ForceDisplacement.getY(), 1.2)
    

test1()
test2()

model.saveAs(final_python_model)

pass