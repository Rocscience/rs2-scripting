from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_BoltAndPile.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Bolt\endAnchored_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Bolt\endAnchored_python.fez'

model = modeler.openFile(base_model)

boltList = model.getAllBoltProperties()
bolt1 = boltList[0]
bolt2 = boltList[1]

def test1():
    bolt1.setBoltType(BoltTypes.END_ANCHORED)
    bolt1.EndAnchored.setBoltDiameter(1.1)
    bolt1.EndAnchored.setBoltModulusE(1.2)
    bolt1.EndAnchored.setTensileCapacity(1.43)
    bolt1.EndAnchored.setResidualTensileCapacity(1.4)
    bolt1.EndAnchored.setOutofPlaneSpacing(1.5) 
    bolt1.EndAnchored.setPreTensioningForce(1.6)
    bolt1.EndAnchored.setConstantPretensioningForceInInstallStage(True)

    assert(bolt1.EndAnchored.getBoltDiameter(), 1.1)
    assert(bolt1.EndAnchored.getBoltModulusE(), 1.2) 
    assert(bolt1.EndAnchored.getTensileCapacity(), 1.43)
    assert(bolt1.EndAnchored.getResidualTensileCapacity(), 1.4)
    assert(bolt1.EndAnchored.getOutofPlaneSpacing(), 1.5)
    assert(bolt1.EndAnchored.getPreTensioningForce(), 1.6)
    assert(bolt1.EndAnchored.getConstantPretensioningForceInInstallStage(), True)


def test2():
    bolt2.setBoltType(BoltTypes.END_ANCHORED)
    bolt2.EndAnchored.setBoltDiameter(1.1)
    bolt2.EndAnchored.setBoltModulusE(1.2)
    bolt2.EndAnchored.setTensileCapacity(1.43)
    bolt2.EndAnchored.setResidualTensileCapacity(1.4)
    bolt2.EndAnchored.setOutofPlaneSpacing(1.5) 
    bolt2.EndAnchored.setPreTensioningForce(1.6)
    bolt2.EndAnchored.setConstantPretensioningForceInInstallStage(False)

    assert(bolt2.EndAnchored.getBoltDiameter(), 1.1)
    assert(bolt2.EndAnchored.getBoltModulusE(), 1.2) 
    assert(bolt2.EndAnchored.getTensileCapacity(), 1.43)
    assert(bolt2.EndAnchored.getResidualTensileCapacity(), 1.4)
    assert(bolt2.EndAnchored.getOutofPlaneSpacing(), 1.5)
    assert(bolt2.EndAnchored.getPreTensioningForce(), 1.6)
    assert(bolt2.EndAnchored.getConstantPretensioningForceInInstallStage(), False)


model.saveAs(final_python_model)

pass