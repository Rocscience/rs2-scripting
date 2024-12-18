from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_BoltAndPile.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Pile\elastic_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Pile\elastic_python.fez'

model = modeler.openFile(base_model)

pileList = model.getAllPileProperties()
pile1 = pileList[0]
pile2 = pileList[1]

def test1():
    pile1.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_ELASTIC)
    pile1.Elastic.setShearStiffness(1.1)
    pile1.Elastic.setNormalStiffness(1.2)
    pile1.Elastic.setUseBaseResistance(True)
    pile1.Elastic.setBaseNormalStiffness(1.3)
    pile1.Elastic.setBaseForceResistance(1.4)

    assert(pile1.Elastic.getShearStiffness(), 1.1)
    assert(pile1.Elastic.getNormalStiffness(), 1.2)
    assert(pile1.Elastic.getUseBaseResistance(), True)  
    assert(pile1.Elastic.getBaseNormalStiffness(), 1.3)
    assert(pile1.Elastic.getBaseForceResistance(), 1.4)

def test2():
    pile2.setSkinResistance(PileSkinResistanceType.SKIN_RESISTANCE_ELASTIC)
    pile2.Elastic.setShearStiffness(1.1)
    pile2.Elastic.setNormalStiffness(1.2)
    pile2.Elastic.setUseBaseResistance(False)

    assert(pile2.Elastic.getShearStiffness(), 1.1)
    assert(pile2.Elastic.getNormalStiffness(), 1.2)
    assert(pile2.Elastic.getUseBaseResistance(), False)
    

test1()
test2()

model.saveAs(final_python_model)

pass