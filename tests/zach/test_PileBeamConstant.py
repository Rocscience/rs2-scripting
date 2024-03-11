from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_BoltAndPile.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Pile\beamConstant_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Pile\beamConstant_python.fez'

model = modeler.openFile(base_model)

pileList = model.getAllPileProperties()
pile1 = pileList[0]

def test1():
    pile1.Beam.setApplication(PileApplicationType.APPLICATION_CONSTANT)
    pile1.Beam.setLinerProperty(linerName='Liner 2')

    assert(pile1.Beam.getApplication(),PileApplicationType.APPLICATION_CONSTANT)
    assert(pile1.Beam.getLinerProperty(), 'Liner 2')

test1()

model.saveAs(final_python_model)

pass