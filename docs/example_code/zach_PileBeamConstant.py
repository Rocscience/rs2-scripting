from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\Pile\beamConstant_final.fez")

pileList = model.getAllPileProperties()
pile1 = pileList[0]

def test1():
    pile1.Beam.setApplication(PileApplicationType.APPLICATION_CONSTANT)
    pile1.Beam.setLinerProperty(linerName='Liner 2')

    assert(pile1.Beam.getApplication(),PileApplicationType.APPLICATION_CONSTANT)
    assert(pile1.Beam.getLinerProperty(), 'Liner 2')

test1()

model.save()

pass