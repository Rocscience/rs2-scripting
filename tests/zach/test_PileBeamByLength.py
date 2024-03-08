from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_BoltAndPile.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Pile\beamByLength_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Pile\beamByLength_python.fez'

model = modeler.openFile(base_model)

pileList = model.getAllPileProperties()
pile1 = pileList[0]

def test1():
    pile1.Beam.setApplication(PileApplicationType.APPLICATION_BY_LENGTH)
    pile1.Beam.defineBeamSegment([1.1,1.2],['Liner 2', 'Liner 3'])

    assert(pile1.Beam.getApplication(),PileApplicationType.APPLICATION_BY_LENGTH)
    assert(pile1.Beam.getBeamSegment(), ([1.1,1.2],['Liner 2', 'Liner 3']))

test1()

model.saveAs(final_python_model)

pass