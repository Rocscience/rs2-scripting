from operator import truediv
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.bolt import PlainStrandCable

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_BoltAndPile.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Bolt\plainStrand_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Bolt\plainStrand_python.fez'

model = modeler.openFile(base_model)

boltList = model.getAllBoltProperties()
bolt1 = boltList[0]
bolt2 = boltList[1]
bolt3 = boltList[2]
bolt4 = boltList[3]
bolt5 = boltList[4]
bolt6 = boltList[5]
bolt7 = boltList[6]
bolt8 = boltList[7]
bolt9 = boltList[8]
bolt10 = boltList[9]
bolt11 = boltList[10]
bolt12 = boltList[11]
bolt13 = boltList[12]

def test1():
    bolt1.setBoltType(BoltTypes.QUEENS_CABLE)
    bolt1.PlainStrandCable.setBoreholeDiameter(19.1)
    bolt1.PlainStrandCable.setCableDiameter(1.2)
    bolt1.PlainStrandCable.setCableModulusE(1.3)
    bolt1.PlainStrandCable.setCablePeak(1.4)
    bolt1.PlainStrandCable.setOutofPlaneSpacing(1.5)
    bolt1.PlainStrandCable.setWaterCementRatio(0.6)
    bolt1.PlainStrandCable.setJointShear(True)
    bolt1.PlainStrandCable.setFacePlates(True)
    bolt1.PlainStrandCable.setAddPullOutForce(True)
    bolt1.PlainStrandCable.setPullOutForce(1.7)
    bolt1.PlainStrandCable.setConstantShearStiffness(True)
    bolt1.PlainStrandCable.setStiffness(1.8)
    bolt1.PlainStrandCable.setAddBulges(True)
    bolt1.PlainStrandCable.setBulgeType(BulgeTypes.PHASE2_BULGE_GARFORD_25)
    bolt1.PlainStrandCable.setBulgeLocations([1,2])

    assert(bolt1.PlainStrandCable.getBoreholeDiameter(), 19.1)
    assert(bolt1.PlainStrandCable.getCableDiameter(), 1.2)
    assert(bolt1.PlainStrandCable.getCableModulusE(), 1.3)
    assert(bolt1.PlainStrandCable.getCablePeak(), 1.4)
    assert(bolt1.PlainStrandCable.getOutofPlaneSpacing(), 1.5)
    assert(bolt1.PlainStrandCable.getWaterCementRatio(), 0.6)
    assert(bolt1.PlainStrandCable.getJointShear(), True)
    assert(bolt1.PlainStrandCable.getFacePlates(), True)
    assert(bolt1.PlainStrandCable.getAddPullOutForce(), True)
    assert(bolt1.PlainStrandCable.getPullOutForce(), 1.7)
    assert(bolt1.PlainStrandCable.getConstantShearStiffness(), True)
    assert(bolt1.PlainStrandCable.getStiffness(), 1.8)
    assert(bolt1.PlainStrandCable.getAddBulges(), True)
    assert(bolt1.PlainStrandCable.getBulgeType(), BulgeTypes.PHASE2_BULGE_GARFORD_25)
    assert(bolt1.PlainStrandCable.getBulgeLocations(), [1,2])

def test2():
    bolt2.setBoltType(BoltTypes.QUEENS_CABLE)
    bolt2.PlainStrandCable.setBoreholeDiameter(19.1)
    bolt2.PlainStrandCable.setCableDiameter(1.2)
    bolt2.PlainStrandCable.setCableModulusE(1.3)
    bolt2.PlainStrandCable.setCablePeak(1.4)
    bolt2.PlainStrandCable.setOutofPlaneSpacing(1.5)
    bolt2.PlainStrandCable.setWaterCementRatio(0.6)
    bolt2.PlainStrandCable.setJointShear(False)
    bolt2.PlainStrandCable.setFacePlates(False)
    bolt2.PlainStrandCable.setAddPullOutForce(False)
    bolt2.PlainStrandCable.setConstantShearStiffness(False)
    bolt2.PlainStrandCable.setAddBulges(False)
    
    assert(bolt2.PlainStrandCable.getBoreholeDiameter(), 19.1)  
    assert(bolt2.PlainStrandCable.getCableDiameter(), 1.2)
    assert(bolt2.PlainStrandCable.getCableModulusE(), 1.3)
    assert(bolt2.PlainStrandCable.getCablePeak(), 1.4)
    assert(bolt2.PlainStrandCable.getOutofPlaneSpacing(), 1.5)
    assert(bolt2.PlainStrandCable.getWaterCementRatio(), 0.6)
    assert(bolt2.PlainStrandCable.getJointShear(), False)
    assert(bolt2.PlainStrandCable.getFacePlates(), False)
    assert(bolt2.PlainStrandCable.getAddPullOutForce(), False)
    assert(bolt2.PlainStrandCable.getConstantShearStiffness(), False)
    assert(bolt2.PlainStrandCable.getAddBulges(), False)

def test3():
    bolt3.setBoltType(BoltTypes.QUEENS_CABLE)
    bolt3.PlainStrandCable.setBoreholeDiameter(19.1)
    bolt3.PlainStrandCable.setCableDiameter(1.2)
    bolt3.PlainStrandCable.setCableModulusE(1.3)
    bolt3.PlainStrandCable.setCablePeak(1.4)
    bolt3.PlainStrandCable.setOutofPlaneSpacing(1.5)
    bolt3.PlainStrandCable.setWaterCementRatio(0.6)
    bolt3.PlainStrandCable.setJointShear(True)
    bolt3.PlainStrandCable.setFacePlates(False)
    bolt3.PlainStrandCable.setAddPullOutForce(False)
    bolt3.PlainStrandCable.setConstantShearStiffness(False)
    bolt3.PlainStrandCable.setAddBulges(False)
    
    assert(bolt3.PlainStrandCable.getBoreholeDiameter(), 19.1)  
    assert(bolt3.PlainStrandCable.getCableDiameter(), 1.2)
    assert(bolt3.PlainStrandCable.getCableModulusE(), 1.3)
    assert(bolt3.PlainStrandCable.getCablePeak(), 1.4)
    assert(bolt3.PlainStrandCable.getOutofPlaneSpacing(), 1.5)
    assert(bolt3.PlainStrandCable.getWaterCementRatio(), 0.6)
    assert(bolt3.PlainStrandCable.getJointShear(), True)
    assert(bolt3.PlainStrandCable.getFacePlates(), False)
    assert(bolt3.PlainStrandCable.getAddPullOutForce(), False)
    assert(bolt3.PlainStrandCable.getConstantShearStiffness(), False)
    assert(bolt3.PlainStrandCable.getAddBulges(), False)

def test4():
    bolt4.setBoltType(BoltTypes.QUEENS_CABLE)
    bolt4.PlainStrandCable.setBoreholeDiameter(19.1)
    bolt4.PlainStrandCable.setCableDiameter(1.2)
    bolt4.PlainStrandCable.setCableModulusE(1.3)
    bolt4.PlainStrandCable.setCablePeak(1.4)
    bolt4.PlainStrandCable.setOutofPlaneSpacing(1.5)
    bolt4.PlainStrandCable.setWaterCementRatio(0.6)
    bolt4.PlainStrandCable.setJointShear(False)
    bolt4.PlainStrandCable.setFacePlates(True)
    bolt4.PlainStrandCable.setAddPullOutForce(False)
    bolt4.PlainStrandCable.setConstantShearStiffness(False)
    bolt4.PlainStrandCable.setAddBulges(False)
    
    assert(bolt4.PlainStrandCable.getBoreholeDiameter(), 19.1)  
    assert(bolt4.PlainStrandCable.getCableDiameter(), 1.2)
    assert(bolt4.PlainStrandCable.getCableModulusE(), 1.3)
    assert(bolt4.PlainStrandCable.getCablePeak(), 1.4)
    assert(bolt4.PlainStrandCable.getOutofPlaneSpacing(), 1.5)
    assert(bolt4.PlainStrandCable.getWaterCementRatio(), 0.6)
    assert(bolt4.PlainStrandCable.getJointShear(), False)
    assert(bolt4.PlainStrandCable.getFacePlates(), True)
    assert(bolt4.PlainStrandCable.getAddPullOutForce(), False)
    assert(bolt4.PlainStrandCable.getConstantShearStiffness(), False)
    assert(bolt4.PlainStrandCable.getAddBulges(), False)

def test5():
    bolt5.setBoltType(BoltTypes.QUEENS_CABLE)
    bolt5.PlainStrandCable.setBoreholeDiameter(19.1)
    bolt5.PlainStrandCable.setCableDiameter(1.2)
    bolt5.PlainStrandCable.setCableModulusE(1.3)
    bolt5.PlainStrandCable.setCablePeak(1.4)
    bolt5.PlainStrandCable.setOutofPlaneSpacing(1.5)
    bolt5.PlainStrandCable.setWaterCementRatio(0.6)
    bolt5.PlainStrandCable.setJointShear(False)
    bolt5.PlainStrandCable.setFacePlates(False)
    bolt5.PlainStrandCable.setAddPullOutForce(True)
    bolt5.PlainStrandCable.setPullOutForce(1.7)
    bolt5.PlainStrandCable.setConstantShearStiffness(False)
    bolt5.PlainStrandCable.setAddBulges(False)
    
    assert(bolt5.PlainStrandCable.getBoreholeDiameter(), 19.1)  
    assert(bolt5.PlainStrandCable.getCableDiameter(), 1.2)
    assert(bolt5.PlainStrandCable.getCableModulusE(), 1.3)
    assert(bolt5.PlainStrandCable.getCablePeak(), 1.4)
    assert(bolt5.PlainStrandCable.getOutofPlaneSpacing(), 1.5)
    assert(bolt5.PlainStrandCable.getWaterCementRatio(), 0.6)
    assert(bolt5.PlainStrandCable.getJointShear(), False)
    assert(bolt5.PlainStrandCable.getFacePlates(), False)
    assert(bolt5.PlainStrandCable.getAddPullOutForce(), True)
    assert(bolt5.PlainStrandCable.getPullOutForce(), 1.7)
    assert(bolt5.PlainStrandCable.getConstantShearStiffness(), False)
    assert(bolt5.PlainStrandCable.getAddBulges(), False)

def test6():
    bolt6.setBoltType(BoltTypes.QUEENS_CABLE)
    bolt6.PlainStrandCable.setBoreholeDiameter(19.1)
    bolt6.PlainStrandCable.setCableDiameter(1.2)
    bolt6.PlainStrandCable.setCableModulusE(1.3)
    bolt6.PlainStrandCable.setCablePeak(1.4)
    bolt6.PlainStrandCable.setOutofPlaneSpacing(1.5)
    bolt6.PlainStrandCable.setWaterCementRatio(0.6)
    bolt6.PlainStrandCable.setJointShear(False)
    bolt6.PlainStrandCable.setFacePlates(False)
    bolt6.PlainStrandCable.setAddPullOutForce(False)
    bolt6.PlainStrandCable.setConstantShearStiffness(True)
    bolt6.PlainStrandCable.setStiffness(1.8)
    bolt6.PlainStrandCable.setAddBulges(False)
    
    assert(bolt6.PlainStrandCable.getBoreholeDiameter(), 19.1)  
    assert(bolt6.PlainStrandCable.getCableDiameter(), 1.2)
    assert(bolt6.PlainStrandCable.getCableModulusE(), 1.3)
    assert(bolt6.PlainStrandCable.getCablePeak(), 1.4)
    assert(bolt6.PlainStrandCable.getOutofPlaneSpacing(), 1.5)
    assert(bolt6.PlainStrandCable.getWaterCementRatio(), 0.6)
    assert(bolt6.PlainStrandCable.getJointShear(), False)
    assert(bolt6.PlainStrandCable.getFacePlates(), False)
    assert(bolt6.PlainStrandCable.getAddPullOutForce(), False)
    assert(bolt6.PlainStrandCable.getConstantShearStiffness(), True)
    assert(bolt6.PlainStrandCable.getStiffness,1.8)
    assert(bolt6.PlainStrandCable.getAddBulges(), False)

def test7():
    bolt7.setBoltType(BoltTypes.QUEENS_CABLE)
    bolt7.PlainStrandCable.setBoreholeDiameter(19.1)
    bolt7.PlainStrandCable.setCableDiameter(1.2)
    bolt7.PlainStrandCable.setCableModulusE(1.3)
    bolt7.PlainStrandCable.setCablePeak(1.4)
    bolt7.PlainStrandCable.setOutofPlaneSpacing(1.5)
    bolt7.PlainStrandCable.setWaterCementRatio(0.6)
    bolt7.PlainStrandCable.setJointShear(False)
    bolt7.PlainStrandCable.setFacePlates(False)
    bolt7.PlainStrandCable.setAddPullOutForce(False)
    bolt7.PlainStrandCable.setConstantShearStiffness(False)
    bolt7.PlainStrandCable.setAddBulges(True)
    bolt7.PlainStrandCable.setBulgeType(BulgeTypes.PHASE2_BULGE_GARFORD_25)
    bolt7.PlainStrandCable.setBulgeLocations([1,2])
    
    assert(bolt7.PlainStrandCable.getBoreholeDiameter(), 19.1)  
    assert(bolt7.PlainStrandCable.getCableDiameter(), 1.2)
    assert(bolt7.PlainStrandCable.getCableModulusE(), 1.3)
    assert(bolt7.PlainStrandCable.getCablePeak(), 1.4)
    assert(bolt7.PlainStrandCable.getOutofPlaneSpacing(), 1.5)
    assert(bolt7.PlainStrandCable.getWaterCementRatio(), 0.6)
    assert(bolt7.PlainStrandCable.getJointShear(), False)
    assert(bolt7.PlainStrandCable.getFacePlates(), False)
    assert(bolt7.PlainStrandCable.getAddPullOutForce(), False)
    assert(bolt7.PlainStrandCable.getConstantShearStiffness(), False)
    assert(bolt7.PlainStrandCable.getAddBulges(), True)
    assert(bolt7.PlainStrandCable.getBulgeType(), BulgeTypes.PHASE2_BULGE_GARFORD_25)
    assert(bolt7.PlainStrandCable.getBulgeLocations(), [1,2])

def test8():
    bolt8.setBoltType(BoltTypes.QUEENS_CABLE)
    bolt8.PlainStrandCable.setBoreholeDiameter(19.1)
    bolt8.PlainStrandCable.setCableDiameter(1.2)
    bolt8.PlainStrandCable.setCableModulusE(1.3)
    bolt8.PlainStrandCable.setCablePeak(1.4)
    bolt8.PlainStrandCable.setOutofPlaneSpacing(1.5)
    bolt8.PlainStrandCable.setWaterCementRatio(0.6)
    bolt8.PlainStrandCable.setJointShear(False)
    bolt8.PlainStrandCable.setFacePlates(False)
    bolt8.PlainStrandCable.setAddPullOutForce(False)
    bolt8.PlainStrandCable.setConstantShearStiffness(False)
    bolt8.PlainStrandCable.setAddBulges(True)
    bolt8.PlainStrandCable.setBulgeType(BulgeTypes.PHASE2_BULGE_NUTCASE_21)
    bolt8.PlainStrandCable.setBulgeLocations([1,2])
    
    assert(bolt8.PlainStrandCable.getBoreholeDiameter(), 19.1)  
    assert(bolt8.PlainStrandCable.getCableDiameter(), 1.2)
    assert(bolt8.PlainStrandCable.getCableModulusE(), 1.3)
    assert(bolt8.PlainStrandCable.getCablePeak(), 1.4)
    assert(bolt8.PlainStrandCable.getOutofPlaneSpacing(), 1.5)
    assert(bolt8.PlainStrandCable.getWaterCementRatio(), 0.6)
    assert(bolt8.PlainStrandCable.getJointShear(), False)
    assert(bolt8.PlainStrandCable.getFacePlates(), False)
    assert(bolt8.PlainStrandCable.getAddPullOutForce(), False)
    assert(bolt8.PlainStrandCable.getConstantShearStiffness(), False)
    assert(bolt8.PlainStrandCable.getAddBulges(), True)
    assert(bolt8.PlainStrandCable.getBulgeType(), BulgeTypes.PHASE2_BULGE_NUTCASE_21)
    assert(bolt8.PlainStrandCable.getBulgeLocations(), [1,2])

def test9():
    bolt9.setBoltType(BoltTypes.QUEENS_CABLE)
    bolt9.PlainStrandCable.setBoreholeDiameter(19.1)
    bolt9.PlainStrandCable.setCableDiameter(1.2)
    bolt9.PlainStrandCable.setCableModulusE(1.3)
    bolt9.PlainStrandCable.setCablePeak(1.4)
    bolt9.PlainStrandCable.setOutofPlaneSpacing(1.5)
    bolt9.PlainStrandCable.setWaterCementRatio(0.6)
    bolt9.PlainStrandCable.setJointShear(True)
    bolt9.PlainStrandCable.setFacePlates(False)
    bolt9.PlainStrandCable.setAddPullOutForce(True)
    bolt9.PlainStrandCable.setPullOutForce(1.7)
    bolt9.PlainStrandCable.setConstantShearStiffness(False)
    bolt9.PlainStrandCable.setAddBulges(True)
    bolt9.PlainStrandCable.setBulgeType(BulgeTypes.PHASE2_BULGE_GARFORD_25)
    bolt9.PlainStrandCable.setBulgeLocations([1,2])
    
    assert(bolt9.PlainStrandCable.getBoreholeDiameter(), 19.1)  
    assert(bolt9.PlainStrandCable.getCableDiameter(), 1.2)
    assert(bolt9.PlainStrandCable.getCableModulusE(), 1.3)
    assert(bolt9.PlainStrandCable.getCablePeak(), 1.4)
    assert(bolt9.PlainStrandCable.getOutofPlaneSpacing(), 1.5)
    assert(bolt9.PlainStrandCable.getWaterCementRatio(), 0.6)
    assert(bolt9.PlainStrandCable.getJointShear(), True)
    assert(bolt9.PlainStrandCable.getFacePlates(), False)
    assert(bolt9.PlainStrandCable.getAddPullOutForce(), True)
    assert(bolt5.PlainStrandCable.getPullOutForce(), 1.7)
    assert(bolt9.PlainStrandCable.getConstantShearStiffness(), False)
    assert(bolt9.PlainStrandCable.getAddBulges(), True)
    assert(bolt9.PlainStrandCable.getBulgeType(), BulgeTypes.PHASE2_BULGE_GARFORD_25)
    assert(bolt9.PlainStrandCable.getBulgeLocations(), [1,2])

def test10():
    bolt10.setBoltType(BoltTypes.QUEENS_CABLE)
    bolt10.PlainStrandCable.setBoreholeDiameter(19.1)
    bolt10.PlainStrandCable.setCableDiameter(1.2)
    bolt10.PlainStrandCable.setCableModulusE(1.3)
    bolt10.PlainStrandCable.setCablePeak(1.4)
    bolt10.PlainStrandCable.setOutofPlaneSpacing(1.5)
    bolt10.PlainStrandCable.setWaterCementRatio(0.6)
    bolt10.PlainStrandCable.setJointShear(False)
    bolt10.PlainStrandCable.setFacePlates(True)
    bolt10.PlainStrandCable.setAddPullOutForce(False)
    bolt10.PlainStrandCable.setConstantShearStiffness(True)
    bolt10.PlainStrandCable.setStiffness(1.8)
    bolt10.PlainStrandCable.setAddBulges(False)
    
    assert(bolt10.PlainStrandCable.getBoreholeDiameter(), 19.1)  
    assert(bolt10.PlainStrandCable.getCableDiameter(), 1.2)
    assert(bolt10.PlainStrandCable.getCableModulusE(), 1.3)
    assert(bolt10.PlainStrandCable.getCablePeak(), 1.4)
    assert(bolt10.PlainStrandCable.getOutofPlaneSpacing(), 1.5)
    assert(bolt10.PlainStrandCable.getWaterCementRatio(), 0.6)
    assert(bolt10.PlainStrandCable.getJointShear(), False)
    assert(bolt10.PlainStrandCable.getFacePlates(), True)
    assert(bolt10.PlainStrandCable.getAddPullOutForce(), False)
    assert(bolt10.PlainStrandCable.getConstantShearStiffness(), True)
    assert(bolt10.PlainStrandCable.getStiffness,1.8)
    assert(bolt10.PlainStrandCable.getAddBulges(), False)

def test11():
    bolt11.setBoltType(BoltTypes.QUEENS_CABLE)
    bolt11.PlainStrandCable.setBoreholeDiameter(19.1)
    bolt11.PlainStrandCable.setCableDiameter(1.2)
    bolt11.PlainStrandCable.setCableModulusE(1.3)
    bolt11.PlainStrandCable.setCablePeak(1.4)
    bolt11.PlainStrandCable.setOutofPlaneSpacing(1.5)
    bolt11.PlainStrandCable.setWaterCementRatio(0.6)
    bolt11.PlainStrandCable.setJointShear(True)
    bolt11.PlainStrandCable.setFacePlates(True)
    bolt11.PlainStrandCable.setAddPullOutForce(True)
    bolt11.PlainStrandCable.setPullOutForce(1.7)
    bolt11.PlainStrandCable.setConstantShearStiffness(False)
    bolt11.PlainStrandCable.setAddBulges(False)
    
    assert(bolt11.PlainStrandCable.getBoreholeDiameter(), 19.1)  
    assert(bolt11.PlainStrandCable.getCableDiameter(), 1.2)
    assert(bolt11.PlainStrandCable.getCableModulusE(), 1.3)
    assert(bolt11.PlainStrandCable.getCablePeak(), 1.4)
    assert(bolt11.PlainStrandCable.getOutofPlaneSpacing(), 1.5)
    assert(bolt11.PlainStrandCable.getWaterCementRatio(), 0.6)
    assert(bolt11.PlainStrandCable.getJointShear(), True)
    assert(bolt11.PlainStrandCable.getFacePlates(), True)
    assert(bolt11.PlainStrandCable.getAddPullOutForce(), True)
    assert(bolt11.PlainStrandCable.getPullOutForce(), 1.7)
    assert(bolt11.PlainStrandCable.getConstantShearStiffness(), False)
    assert(bolt11.PlainStrandCable.getAddBulges(), False)

def test12():
    bolt12.setBoltType(BoltTypes.QUEENS_CABLE)
    bolt12.PlainStrandCable.setBoreholeDiameter(19.1)
    bolt12.PlainStrandCable.setCableDiameter(1.2)
    bolt12.PlainStrandCable.setCableModulusE(1.3)
    bolt12.PlainStrandCable.setCablePeak(1.4)
    bolt12.PlainStrandCable.setOutofPlaneSpacing(1.5)
    bolt12.PlainStrandCable.setWaterCementRatio(0.6)
    bolt12.PlainStrandCable.setJointShear(False)
    bolt12.PlainStrandCable.setFacePlates(False)
    bolt12.PlainStrandCable.setAddPullOutForce(False)
    bolt12.PlainStrandCable.setConstantShearStiffness(True)
    bolt12.PlainStrandCable.setStiffness(1.8)
    bolt12.PlainStrandCable.setAddBulges(True)
    bolt12.PlainStrandCable.setBulgeType(BulgeTypes.PHASE2_BULGE_GARFORD_25)
    bolt12.PlainStrandCable.setBulgeLocations([1,2])
    
    assert(bolt12.PlainStrandCable.getBoreholeDiameter(), 19.1)  
    assert(bolt12.PlainStrandCable.getCableDiameter(), 1.2)
    assert(bolt12.PlainStrandCable.getCableModulusE(), 1.3)
    assert(bolt12.PlainStrandCable.getCablePeak(), 1.4)
    assert(bolt12.PlainStrandCable.getOutofPlaneSpacing(), 1.5)
    assert(bolt12.PlainStrandCable.getWaterCementRatio(), 0.6)
    assert(bolt12.PlainStrandCable.getJointShear(), False)
    assert(bolt12.PlainStrandCable.getFacePlates(), False)
    assert(bolt12.PlainStrandCable.getAddPullOutForce(), False)
    assert(bolt12.PlainStrandCable.getConstantShearStiffness(), True)
    assert(bolt12.PlainStrandCable.getStiffness,1.8)
    assert(bolt12.PlainStrandCable.getAddBulges(), True)
    assert(bolt12.PlainStrandCable.getBulgeType(), BulgeTypes.PHASE2_BULGE_GARFORD_25)
    assert(bolt12.PlainStrandCable.getBulgeLocations(), [1,2])

def test13():
    bolt13.setBoltType(BoltTypes.QUEENS_CABLE)
    bolt13.PlainStrandCable.setBoreholeDiameter(19.1)
    bolt13.PlainStrandCable.setCableDiameter(1.2)
    bolt13.PlainStrandCable.setCableModulusE(1.3)
    bolt13.PlainStrandCable.setCablePeak(1.4)
    bolt13.PlainStrandCable.setOutofPlaneSpacing(1.5)
    bolt13.PlainStrandCable.setWaterCementRatio(0.6)
    bolt13.PlainStrandCable.setJointShear(True)
    bolt13.PlainStrandCable.setFacePlates(True)
    bolt13.PlainStrandCable.setAddPullOutForce(False)
    bolt13.PlainStrandCable.setConstantShearStiffness(False)
    bolt13.PlainStrandCable.setAddBulges(True)
    bolt13.PlainStrandCable.setBulgeType(BulgeTypes.PHASE2_BULGE_GARFORD_25)
    bolt13.PlainStrandCable.setBulgeLocations([1,2])
    
    assert(bolt13.PlainStrandCable.getBoreholeDiameter(), 19.1)  
    assert(bolt13.PlainStrandCable.getCableDiameter(), 1.2)
    assert(bolt13.PlainStrandCable.getCableModulusE(), 1.3)
    assert(bolt13.PlainStrandCable.getCablePeak(), 1.4)
    assert(bolt13.PlainStrandCable.getOutofPlaneSpacing(), 1.5)
    assert(bolt13.PlainStrandCable.getWaterCementRatio(), 0.6)
    assert(bolt13.PlainStrandCable.getJointShear(), True)
    assert(bolt13.PlainStrandCable.getFacePlates(), True)
    assert(bolt13.PlainStrandCable.getAddPullOutForce(), False)
    assert(bolt13.PlainStrandCable.getConstantShearStiffness(), False)
    assert(bolt13.PlainStrandCable.getAddBulges(), True)
    assert(bolt13.PlainStrandCable.getBulgeType(), BulgeTypes.PHASE2_BULGE_GARFORD_25)
    assert(bolt13.PlainStrandCable.getBulgeLocations(), [1,2])

test1()
test2() 
test3()
test4()
test5()
test6()
test7() 
test8()
test9()
test10()
test11()
test12()
test13()

model.saveAs(final_python_model)

pass