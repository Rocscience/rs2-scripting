from math import fabs
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_BoltAndPile.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Bolt\fullyBonded_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Bolt\fullyBonded_python.fez'

model = modeler.openFile(base_model)

boltList = model.getAllBoltProperties()
bolt1 = boltList[0]
bolt2 = boltList[1]
bolt3 = boltList[2]
bolt4 = boltList[3]
bolt5 = boltList[4]

def test1():
    bolt1.setBoltType(BoltTypes.FULLY_BONDED)
    bolt1.FullyBonded.setBoltDiameter(1.1)
    bolt1.FullyBonded.setBoltModulusE(1.2) 
    bolt1.FullyBonded.setTensileCapacity(1.43)
    bolt1.FullyBonded.setResidualTensileCapacity(1.4)
    bolt1.FullyBonded.setOutofPlaneSpacing(1.5)
    bolt1.FullyBonded.setPreTensioningForce(1.6)
    bolt1.FullyBonded.setConstantPretensioningForceInInstallStage(True)
    bolt1.FullyBonded.setJointShear(True)
    
    assert(bolt1.FullyBonded.getBoltDiameter(), 1.1)
    assert(bolt1.FullyBonded.getBoltModulusE(), 1.2)
    assert(bolt1.FullyBonded.getTensileCapacity(), 1.43)
    assert(bolt1.FullyBonded.getResidualTensileCapacity(), 1.4)
    assert(bolt1.FullyBonded.getOutofPlaneSpacing(), 1.5)  
    assert(bolt1.FullyBonded.getPreTensioningForce(), 1.6)
    assert(bolt1.FullyBonded.getConstantPretensioningForceInInstallStage(), True) 
    assert(bolt1.FullyBonded.getJointShear(), True)

def test2():
    bolt2.setBoltType(BoltTypes.FULLY_BONDED)
    bolt2.FullyBonded.setBoltDiameter(1.1)
    bolt2.FullyBonded.setBoltModulusE(1.2) 
    bolt2.FullyBonded.setTensileCapacity(1.43)
    bolt2.FullyBonded.setResidualTensileCapacity(1.4)
    bolt2.FullyBonded.setOutofPlaneSpacing(1.5)
    bolt2.FullyBonded.setPreTensioningForce(1.6)
    bolt2.FullyBonded.setConstantPretensioningForceInInstallStage(False)
    bolt2.FullyBonded.setJointShear(False)
    
    assert(bolt2.FullyBonded.getBoltDiameter(), 1.1)
    assert(bolt2.FullyBonded.getBoltModulusE(), 1.2)
    assert(bolt2.FullyBonded.getTensileCapacity(), 1.43)
    assert(bolt2.FullyBonded.getResidualTensileCapacity(), 1.4)
    assert(bolt2.FullyBonded.getOutofPlaneSpacing(), 1.5)  
    assert(bolt2.FullyBonded.getPreTensioningForce(), 1.6)
    assert(bolt2.FullyBonded.getConstantPretensioningForceInInstallStage(), False) 
    assert(bolt2.FullyBonded.getJointShear(), False)

def test3():
    bolt3.setBoltType(BoltTypes.FULLY_BONDED)
    bolt3.FullyBonded.setBoltDiameter(1.1)
    bolt3.FullyBonded.setBoltModulusE(1.2) 
    bolt3.FullyBonded.setTensileCapacity(1.43)
    bolt3.FullyBonded.setResidualTensileCapacity(1.4)
    bolt3.FullyBonded.setOutofPlaneSpacing(1.5)
    bolt3.FullyBonded.setPreTensioningForce(1.6)
    bolt3.FullyBonded.setConstantPretensioningForceInInstallStage(True)
    bolt3.FullyBonded.setJointShear(False)

    assert(bolt3.FullyBonded.getBoltDiameter(), 1.1)
    assert(bolt3.FullyBonded.getBoltModulusE(), 1.2)
    assert(bolt3.FullyBonded.getTensileCapacity(), 1.43)
    assert(bolt3.FullyBonded.getResidualTensileCapacity(), 1.4)
    assert(bolt3.FullyBonded.getOutofPlaneSpacing(), 1.5)  
    assert(bolt3.FullyBonded.getPreTensioningForce(), 1.6)
    assert(bolt3.FullyBonded.getConstantPretensioningForceInInstallStage(), True) 
    assert(bolt3.FullyBonded.getJointShear(), False)

def test4():
    bolt4.setBoltType(BoltTypes.FULLY_BONDED)
    bolt4.FullyBonded.setBoltDiameter(1.1)
    bolt4.FullyBonded.setBoltModulusE(1.2) 
    bolt4.FullyBonded.setTensileCapacity(1.43)
    bolt4.FullyBonded.setResidualTensileCapacity(1.4)
    bolt4.FullyBonded.setOutofPlaneSpacing(1.5)
    bolt4.FullyBonded.setPreTensioningForce(1.6)
    bolt4.FullyBonded.setConstantPretensioningForceInInstallStage(False)
    bolt4.FullyBonded.setJointShear(True)   

    assert(bolt4.FullyBonded.getBoltDiameter(), 1.1)
    assert(bolt4.FullyBonded.getBoltModulusE(), 1.2)
    assert(bolt4.FullyBonded.getTensileCapacity(), 1.43)
    assert(bolt4.FullyBonded.getResidualTensileCapacity(), 1.4)
    assert(bolt4.FullyBonded.getOutofPlaneSpacing(), 1.5)  
    assert(bolt4.FullyBonded.getPreTensioningForce(), 1.6)
    assert(bolt4.FullyBonded.getConstantPretensioningForceInInstallStage(), False) 
    assert(bolt4.FullyBonded.getJointShear(), True)

test1()
test2()
test3()
test4()

model.saveAs(final_python_model)

pass