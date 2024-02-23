from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\Pile\beamByLength_final.fez")

pileList = model.getAllPileProperties()
pile1 = pileList[0]

def test1():
    pile1.Beam.setApplication(PileApplicationType.APPLICATION_BY_LENGTH)
    pile1.Beam.defineBeamSegment([1.1,1.2],['Liner 2', 'Liner 3'])

    assert(pile1.Beam.getApplication(),PileApplicationType.APPLICATION_BY_LENGTH)
    assert(pile1.Beam.getBeamSegment(), ([1.1,1.2],['Liner 2', 'Liner 3']))

test1()

model.save()

pass