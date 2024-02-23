from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

model = modeler.openFile(r"C:\scriptingModels\Pile\pileConnectionType_final.fez")

pileList = model.getAllPileProperties()
pile1 = pileList[0]
pile2 = pileList[1]
pile3 = pileList[2]
pile4 = pileList[3]

def test1():
    pile1.setConnectionType(PileConnectionType.CONNECT_FREE)
    pile1.setLength(1.1)
    pile1.setOutOfPlaneSpacing(1.2)

    assert(pile1.getConnectionType(), PileConnectionType.CONNECT_FREE)
    assert(pile1.getLength(), 1.1)
    assert(pile1.getOutOfPlaneSpacing(), 1.2)


def test2():
    pile2.setConnectionType(PileConnectionType.CONNECT_HINGED)
    pile2.setLength(1.1)
    pile2.setOutOfPlaneSpacing(1.2)

    assert(pile2.getConnectionType(), PileConnectionType.CONNECT_HINGED) 
    assert(pile2.getLength(), 1.1)
    assert(pile2.getOutOfPlaneSpacing(), 1.2)

def test3():
    pile3.setConnectionType(PileConnectionType.CONNECT_RIGID)
    pile3.setLength(1.1)
    pile3.setOutOfPlaneSpacing(1.2)

    assert(pile3.getConnectionType(), PileConnectionType.CONNECT_RIGID)
    assert(pile3.getLength(), 1.1)  
    assert(pile3.getOutOfPlaneSpacing(), 1.2)

def test4():
    pile4.setConnectionType(PileConnectionType.CONNECT_SEMIRIGID)
    pile4.setLength(1.1)
    pile4.setOutOfPlaneSpacing(1.2)
    pile4.setMMax(1.3)

    assert(pile4.getConnectionType(), PileConnectionType.CONNECT_SEMIRIGID)
    assert(pile4.getLength(), 1.1)
    assert(pile4.getOutOfPlaneSpacing(), 1.2) 
    assert(pile4.getMMax(), 1.3)

test1()
test2()
test3()
test4()

model.save()

pass