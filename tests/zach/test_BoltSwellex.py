from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_BoltAndPile.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Bolt\swellex_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Bolt\swellex_python.fez'

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
bolt14 = boltList[13]
bolt15 = boltList[14]
bolt16 = boltList[15]
bolt17 = boltList[16]
bolt18 = boltList[17]
bolt19 = boltList[18]
bolt20 = boltList[19]
bolt21 = boltList[20]
bolt22 = boltList[21]
bolt23 = boltList[22]

def test1():
    bolt1.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt1.Swellex.setTensileCapacity(1.21)
    bolt1.Swellex.setResidualTensileCapacity(1.2)
    bolt1.Swellex.setTributaryArea(1.3)
    bolt1.Swellex.setBoltModulusE(1.4)
    bolt1.Swellex.setOutofPlaneSpacing(1.5)
    bolt1.Swellex.setMaterialDependent(True)
    bolt1.Swellex.setBondStrengthCoefficient(1.6)
    bolt1.Swellex.setBondShearStiffnessCoefficient(1.7)
    bolt1.Swellex.setBoltModel(BoltModels.P2_BOLT_PLASTIC)
    bolt1.Swellex.setJointShear(True)
    bolt1.Swellex.setPreTensioningForce(1.9)
    bolt1.Swellex.setConstantPretensioningForceInInstallStage(True)
    bolt1.Swellex.setFacePlates(True)
    bolt1.Swellex.setAddPullOutForce(True)
    bolt1.Swellex.setPullOutForce(1.11)

    assert(bolt1.Swellex.getTensileCapacity(), 1.21)
    assert(bolt1.Swellex.getResidualTensileCapacity(), 1.2)
    assert(bolt1.Swellex.getTributaryArea(), 1.3)
    assert(bolt1.Swellex.getBoltModulusE(), 1.4)
    assert(bolt1.Swellex.getOutofPlaneSpacing(), 1.5)
    assert(bolt1.Swellex.getMaterialDependent(), True)
    assert(bolt1.Swellex.getBondStrengthCoefficient(), 1.6)
    assert(bolt1.Swellex.getBondShearStiffnessCoefficient(), 1.7)
    assert(bolt1.Swellex.getBoltModel(), BoltModels.P2_BOLT_PLASTIC)
    assert(bolt1.Swellex.getJointShear(), True)
    assert(bolt1.Swellex.getPreTensioningForce(), 1.9)
    assert(bolt1.Swellex.getConstantPretensioningForceInInstallStage(), True)
    assert(bolt1.Swellex.getFacePlates(), True)
    assert(bolt1.Swellex.getAddPullOutForce(), True) 
    assert(bolt1.Swellex.getPullOutForce(), 1.11)

def test2():
    bolt2.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt2.Swellex.setTensileCapacity(1.21)
    bolt2.Swellex.setResidualTensileCapacity(1.2)
    bolt2.Swellex.setTributaryArea(1.3)
    bolt2.Swellex.setBoltModulusE(1.4)
    bolt2.Swellex.setOutofPlaneSpacing(1.5)
    bolt2.Swellex.setMaterialDependent(False)
    bolt2.Swellex.setBondShearStiffness(1.6)
    bolt2.Swellex.setBondStrength(1.7)
    bolt2.Swellex.setResidualBondStrength(0.8)
    bolt2.Swellex.setBoltModel(BoltModels.P2_BOLT_PLASTIC)
    bolt2.Swellex.setJointShear(False)
    bolt2.Swellex.setPreTensioningForce(1.9)
    bolt2.Swellex.setConstantPretensioningForceInInstallStage(False)
    bolt2.Swellex.setFacePlates(False)
    bolt2.Swellex.setAddPullOutForce(False)

    assert(bolt2.Swellex.getTensileCapacity(), 1.21)
    assert(bolt2.Swellex.getResidualTensileCapacity(), 1.2)
    assert(bolt2.Swellex.getTributaryArea(), 1.3)
    assert(bolt2.Swellex.getBoltModulusE(), 1.4)
    assert(bolt2.Swellex.getOutofPlaneSpacing(), 1.5)
    assert(bolt2.Swellex.getMaterialDependent(), False)
    assert(bolt2.Swellex.getBondShearStiffness(), 1.6)
    assert(bolt2.Swellex.getBondStrength(), 1.7)
    assert(bolt2.Swellex.getResidualBondStrength(), 0.8)
    assert(bolt2.Swellex.getBoltModel(), BoltModels.P2_BOLT_PLASTIC)
    assert(bolt2.Swellex.getJointShear(), False)
    assert(bolt2.Swellex.getPreTensioningForce(), 1.9)
    assert(bolt2.Swellex.getConstantPretensioningForceInInstallStage(), False)
    assert(bolt2.Swellex.getFacePlates(), False)
    assert(bolt2.Swellex.getAddPullOutForce(), False)

def test3():
    bolt3.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt3.Swellex.setTensileCapacity(1.21)
    bolt3.Swellex.setResidualTensileCapacity(1.2)
    bolt3.Swellex.setTributaryArea(1.3)
    bolt3.Swellex.setBoltModulusE(1.4)
    bolt3.Swellex.setOutofPlaneSpacing(1.5)
    bolt1.Swellex.setMaterialDependent(True)
    bolt1.Swellex.setBondStrengthCoefficient(1.6)
    bolt1.Swellex.setBondShearStiffnessCoefficient(1.7)
    bolt3.Swellex.setBoltModel(BoltModels.P2_BOLT_PLASTIC)
    bolt3.Swellex.setJointShear(False)
    bolt3.Swellex.setPreTensioningForce(1.9)
    bolt3.Swellex.setConstantPretensioningForceInInstallStage(False)
    bolt3.Swellex.setFacePlates(False)
    bolt3.Swellex.setAddPullOutForce(False)

    assert(bolt3.Swellex.getTensileCapacity(), 1.21)
    assert(bolt3.Swellex.getResidualTensileCapacity(), 1.2)
    assert(bolt3.Swellex.getTributaryArea(), 1.3)
    assert(bolt3.Swellex.getBoltModulusE(), 1.4)
    assert(bolt3.Swellex.getOutofPlaneSpacing(), 1.5)
    assert(bolt1.Swellex.getMaterialDependent(), True)
    assert(bolt1.Swellex.getBondStrengthCoefficient(), 1.6)
    assert(bolt1.Swellex.getBondShearStiffnessCoefficient(), 1.7)
    assert(bolt3.Swellex.getBoltModel(), BoltModels.P2_BOLT_PLASTIC)
    assert(bolt3.Swellex.getJointShear(), False)
    assert(bolt3.Swellex.getPreTensioningForce(), 1.9)
    assert(bolt3.Swellex.getConstantPretensioningForceInInstallStage(), False)
    assert(bolt3.Swellex.getFacePlates(), False)
    assert(bolt3.Swellex.getAddPullOutForce(), False)

def test4():
    bolt4.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt4.Swellex.setTensileCapacity(1.21)
    bolt4.Swellex.setResidualTensileCapacity(1.2)
    bolt4.Swellex.setTributaryArea(1.3)
    bolt4.Swellex.setBoltModulusE(1.4)
    bolt4.Swellex.setOutofPlaneSpacing(1.5)
    bolt4.Swellex.setMaterialDependent(False)
    bolt4.Swellex.setBondShearStiffness(1.6)
    bolt4.Swellex.setBondStrength(1.7)
    bolt4.Swellex.setResidualBondStrength(0.8)
    bolt4.Swellex.setBoltModel(BoltModels.P2_BOLT_PLASTIC)
    bolt4.Swellex.setJointShear(True)
    bolt4.Swellex.setPreTensioningForce(1.9)
    bolt4.Swellex.setConstantPretensioningForceInInstallStage(False)
    bolt4.Swellex.setFacePlates(False)
    bolt4.Swellex.setAddPullOutForce(False)

    assert(bolt4.Swellex.getTensileCapacity(), 1.21)
    assert(bolt4.Swellex.getResidualTensileCapacity(), 1.2)
    assert(bolt4.Swellex.getTributaryArea(), 1.3)
    assert(bolt4.Swellex.getBoltModulusE(), 1.4)
    assert(bolt4.Swellex.getOutofPlaneSpacing(), 1.5)
    assert(bolt4.Swellex.getMaterialDependent(), False)
    assert(bolt4.Swellex.getBondShearStiffness(), 1.6)
    assert(bolt4.Swellex.getBondStrength(), 1.7)
    assert(bolt4.Swellex.getResidualBondStrength(), 0.8)
    assert(bolt4.Swellex.getBoltModel(), BoltModels.P2_BOLT_PLASTIC)
    assert(bolt4.Swellex.getJointShear(), True)
    assert(bolt4.Swellex.getPreTensioningForce(), 1.9)
    assert(bolt4.Swellex.getConstantPretensioningForceInInstallStage(), False)
    assert(bolt4.Swellex.getFacePlates(), False)
    assert(bolt4.Swellex.getAddPullOutForce(), False)

def test5():
    bolt5.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt5.Swellex.setTensileCapacity(1.21)
    bolt5.Swellex.setResidualTensileCapacity(1.2)
    bolt5.Swellex.setTributaryArea(1.3)
    bolt5.Swellex.setBoltModulusE(1.4)
    bolt5.Swellex.setOutofPlaneSpacing(1.5)
    bolt5.Swellex.setMaterialDependent(False)
    bolt5.Swellex.setBondShearStiffness(1.6)
    bolt5.Swellex.setBondStrength(1.7)
    bolt5.Swellex.setResidualBondStrength(0.8)
    bolt5.Swellex.setBoltModel(BoltModels.P2_BOLT_PLASTIC)
    bolt5.Swellex.setJointShear(False)
    bolt5.Swellex.setPreTensioningForce(1.9)
    bolt5.Swellex.setConstantPretensioningForceInInstallStage(True)
    bolt5.Swellex.setFacePlates(False)
    bolt5.Swellex.setAddPullOutForce(False)

    assert(bolt5.Swellex.getTensileCapacity(), 1.21)
    assert(bolt5.Swellex.getResidualTensileCapacity(), 1.2)
    assert(bolt5.Swellex.getTributaryArea(), 1.3)
    assert(bolt5.Swellex.getBoltModulusE(), 1.4)
    assert(bolt5.Swellex.getOutofPlaneSpacing(), 1.5)
    assert(bolt5.Swellex.getMaterialDependent(), False)
    assert(bolt5.Swellex.getBondShearStiffness(), 1.6)
    assert(bolt5.Swellex.getBondStrength(), 1.7)
    assert(bolt5.Swellex.getResidualBondStrength(), 0.8)
    assert(bolt5.Swellex.getBoltModel(), BoltModels.P2_BOLT_PLASTIC)
    assert(bolt5.Swellex.getJointShear(), False)
    assert(bolt5.Swellex.getPreTensioningForce(), 1.9)
    assert(bolt5.Swellex.getConstantPretensioningForceInInstallStage(), True)
    assert(bolt5.Swellex.getFacePlates(), False)
    assert(bolt5.Swellex.getAddPullOutForce(), False)

def test6():
    bolt6.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt6.Swellex.setTensileCapacity(1.21)
    bolt6.Swellex.setResidualTensileCapacity(1.2)
    bolt6.Swellex.setTributaryArea(1.3)
    bolt6.Swellex.setBoltModulusE(1.4)
    bolt6.Swellex.setOutofPlaneSpacing(1.5)
    bolt6.Swellex.setMaterialDependent(False)
    bolt6.Swellex.setBondShearStiffness(1.6)
    bolt6.Swellex.setBondStrength(1.7)
    bolt6.Swellex.setResidualBondStrength(0.8)
    bolt6.Swellex.setBoltModel(BoltModels.P2_BOLT_PLASTIC)
    bolt6.Swellex.setJointShear(False)
    bolt6.Swellex.setPreTensioningForce(1.9)
    bolt6.Swellex.setConstantPretensioningForceInInstallStage(False)
    bolt6.Swellex.setFacePlates(True)
    bolt6.Swellex.setAddPullOutForce(False)

    assert(bolt6.Swellex.getTensileCapacity(), 1.21)
    assert(bolt6.Swellex.getResidualTensileCapacity(), 1.2)
    assert(bolt6.Swellex.getTributaryArea(), 1.3)
    assert(bolt6.Swellex.getBoltModulusE(), 1.4)
    assert(bolt6.Swellex.getOutofPlaneSpacing(), 1.5)
    assert(bolt6.Swellex.getMaterialDependent(), False)
    assert(bolt6.Swellex.getBondShearStiffness(), 1.6)
    assert(bolt6.Swellex.getBondStrength(), 1.7)
    assert(bolt6.Swellex.getResidualBondStrength(), 0.8)
    assert(bolt6.Swellex.getBoltModel(), BoltModels.P2_BOLT_PLASTIC)
    assert(bolt6.Swellex.getJointShear(), False)
    assert(bolt6.Swellex.getPreTensioningForce(), 1.9)
    assert(bolt6.Swellex.getConstantPretensioningForceInInstallStage(), False)
    assert(bolt6.Swellex.getFacePlates(), True)
    assert(bolt6.Swellex.getAddPullOutForce(), False)

def test7():
    bolt7.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt7.Swellex.setTensileCapacity(1.21)
    bolt7.Swellex.setResidualTensileCapacity(1.2)
    bolt7.Swellex.setTributaryArea(1.3)
    bolt7.Swellex.setBoltModulusE(1.4)
    bolt7.Swellex.setOutofPlaneSpacing(1.5)
    bolt7.Swellex.setMaterialDependent(False)
    bolt7.Swellex.setBondShearStiffness(1.6)
    bolt7.Swellex.setBondStrength(1.7)
    bolt7.Swellex.setResidualBondStrength(0.8)
    bolt7.Swellex.setBoltModel(BoltModels.P2_BOLT_PLASTIC)
    bolt7.Swellex.setJointShear(False)
    bolt7.Swellex.setPreTensioningForce(1.9)
    bolt7.Swellex.setConstantPretensioningForceInInstallStage(False)
    bolt7.Swellex.setFacePlates(False)
    bolt7.Swellex.setAddPullOutForce(True)
    bolt7.Swellex.setPullOutForce(1.11)

    assert(bolt7.Swellex.getTensileCapacity(), 1.21)
    assert(bolt7.Swellex.getResidualTensileCapacity(), 1.2)
    assert(bolt7.Swellex.getTributaryArea(), 1.3)
    assert(bolt7.Swellex.getBoltModulusE(), 1.4)
    assert(bolt7.Swellex.getOutofPlaneSpacing(), 1.5)
    assert(bolt7.Swellex.getMaterialDependent(), False)
    assert(bolt7.Swellex.getBondShearStiffness(), 1.6)
    assert(bolt7.Swellex.getBondStrength(), 1.7)
    assert(bolt7.Swellex.getResidualBondStrength(), 0.8)
    assert(bolt7.Swellex.getBoltModel(), BoltModels.P2_BOLT_PLASTIC)
    assert(bolt7.Swellex.getJointShear(), False)
    assert(bolt7.Swellex.getPreTensioningForce(), 1.9)
    assert(bolt7.Swellex.getConstantPretensioningForceInInstallStage(), False)
    assert(bolt7.Swellex.getFacePlates(), False)
    assert(bolt7.Swellex.getAddPullOutForce(), True)
    assert(bolt7.Swellex.getPullOutForce(), 1.11)

def test8():
    bolt8.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt8.Swellex.setTensileCapacity(1.21)
    bolt8.Swellex.setResidualTensileCapacity(1.2)
    bolt8.Swellex.setTributaryArea(1.3)
    bolt8.Swellex.setBoltModulusE(1.4)
    bolt8.Swellex.setOutofPlaneSpacing(1.5)
    bolt8.Swellex.setMaterialDependent(True)
    bolt8.Swellex.setBondStrengthCoefficient(1.6)
    bolt8.Swellex.setBondShearStiffnessCoefficient(1.7)
    bolt8.Swellex.setBoltModel(BoltModels.P2_BOLT_PLASTIC)
    bolt8.Swellex.setJointShear(False)
    bolt8.Swellex.setPreTensioningForce(1.9)
    bolt8.Swellex.setConstantPretensioningForceInInstallStage(True)
    bolt8.Swellex.setFacePlates(False)
    bolt8.Swellex.setAddPullOutForce(True)
    bolt8.Swellex.setPullOutForce(1.11)

    assert(bolt8.Swellex.getTensileCapacity(), 1.21)
    assert(bolt8.Swellex.getResidualTensileCapacity(), 1.2)
    assert(bolt8.Swellex.getTributaryArea(), 1.3)
    assert(bolt8.Swellex.getBoltModulusE(), 1.4)
    assert(bolt8.Swellex.getOutofPlaneSpacing(), 1.5)
    assert(bolt8.Swellex.getMaterialDependent(), True)
    assert(bolt8.Swellex.getBondStrengthCoefficient(), 1.6)
    assert(bolt8.Swellex.getBondShearStiffnessCoefficient(), 1.7)
    assert(bolt8.Swellex.getBoltModel(), BoltModels.P2_BOLT_PLASTIC)
    assert(bolt8.Swellex.getJointShear(), False)
    assert(bolt8.Swellex.getPreTensioningForce(), 1.9)
    assert(bolt8.Swellex.getConstantPretensioningForceInInstallStage(), True)
    assert(bolt8.Swellex.getFacePlates(), False)
    assert(bolt8.Swellex.getAddPullOutForce(), True)
    assert(bolt8.Swellex.getPullOutForce(), 1.11)

def test9():
    bolt9.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt9.Swellex.setTensileCapacity(1.21)
    bolt9.Swellex.setResidualTensileCapacity(1.2)
    bolt9.Swellex.setTributaryArea(1.3)
    bolt9.Swellex.setBoltModulusE(1.4)
    bolt9.Swellex.setOutofPlaneSpacing(1.5)
    bolt9.Swellex.setMaterialDependent(False)
    bolt9.Swellex.setBondShearStiffness(1.6)
    bolt9.Swellex.setBondStrength(1.7)
    bolt9.Swellex.setResidualBondStrength(0.8)
    bolt9.Swellex.setBoltModel(BoltModels.P2_BOLT_PLASTIC)
    bolt9.Swellex.setJointShear(True)
    bolt9.Swellex.setPreTensioningForce(1.9)
    bolt9.Swellex.setConstantPretensioningForceInInstallStage(False)
    bolt9.Swellex.setFacePlates(True)
    bolt9.Swellex.setAddPullOutForce(False)

    assert(bolt9.Swellex.getTensileCapacity(), 1.21)
    assert(bolt9.Swellex.getResidualTensileCapacity(), 1.2)
    assert(bolt9.Swellex.getTributaryArea(), 1.3)
    assert(bolt9.Swellex.getBoltModulusE(), 1.4)
    assert(bolt9.Swellex.getOutofPlaneSpacing(), 1.5)
    assert(bolt9.Swellex.getMaterialDependent(), False)
    assert(bolt9.Swellex.getBondShearStiffness(), 1.6)
    assert(bolt9.Swellex.getBondStrength(), 1.7)
    assert(bolt9.Swellex.getResidualBondStrength(), 0.8)
    assert(bolt9.Swellex.getBoltModel(), BoltModels.P2_BOLT_PLASTIC)
    assert(bolt9.Swellex.getJointShear(), True)
    assert(bolt9.Swellex.getPreTensioningForce(), 1.9)
    assert(bolt9.Swellex.getConstantPretensioningForceInInstallStage(), False)
    assert(bolt9.Swellex.getFacePlates(), True)
    assert(bolt9.Swellex.getAddPullOutForce(), False)

def test10():
    bolt10.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt10.Swellex.setTensileCapacity(1.21)
    bolt10.Swellex.setResidualTensileCapacity(1.2)
    bolt10.Swellex.setTributaryArea(1.3)
    bolt10.Swellex.setBoltModulusE(1.4)
    bolt10.Swellex.setOutofPlaneSpacing(1.5)
    bolt10.Swellex.setMaterialDependent(True)
    bolt10.Swellex.setBondStrengthCoefficient(1.6)
    bolt10.Swellex.setBondShearStiffnessCoefficient(1.7)
    bolt10.Swellex.setBoltModel(BoltModels.P2_BOLT_PLASTIC)
    bolt10.Swellex.setJointShear(True)
    bolt10.Swellex.setPreTensioningForce(1.9)
    bolt10.Swellex.setConstantPretensioningForceInInstallStage(True)
    bolt10.Swellex.setFacePlates(False)
    bolt10.Swellex.setAddPullOutForce(False)

    assert(bolt10.Swellex.getTensileCapacity(), 1.21)
    assert(bolt10.Swellex.getResidualTensileCapacity(), 1.2)
    assert(bolt10.Swellex.getTributaryArea(), 1.3)
    assert(bolt10.Swellex.getBoltModulusE(), 1.4)
    assert(bolt10.Swellex.getOutofPlaneSpacing(), 1.5)
    assert(bolt10.Swellex.getMaterialDependent(), True)
    assert(bolt10.Swellex.getBondStrengthCoefficient(), 1.6)
    assert(bolt10.Swellex.getBondShearStiffnessCoefficient(), 1.7)
    assert(bolt10.Swellex.getBoltModel(), BoltModels.P2_BOLT_PLASTIC)
    assert(bolt10.Swellex.getJointShear(), True)
    assert(bolt10.Swellex.getPreTensioningForce(), 1.9)
    assert(bolt10.Swellex.getConstantPretensioningForceInInstallStage(), True)
    assert(bolt10.Swellex.getFacePlates(), False)
    assert(bolt10.Swellex.getAddPullOutForce(), False)

def test11():
    bolt11.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt11.Swellex.setTensileCapacity(1.21)
    bolt11.Swellex.setResidualTensileCapacity(1.2)
    bolt11.Swellex.setTributaryArea(1.3)
    bolt11.Swellex.setBoltModulusE(1.4)
    bolt11.Swellex.setOutofPlaneSpacing(1.5)
    bolt11.Swellex.setMaterialDependent(False)
    bolt11.Swellex.setBondShearStiffness(1.6)
    bolt11.Swellex.setBondStrength(1.7)
    bolt11.Swellex.setResidualBondStrength(0.8)
    bolt11.Swellex.setBoltModel(BoltModels.P2_BOLT_PLASTIC)
    bolt11.Swellex.setJointShear(False)
    bolt11.Swellex.setPreTensioningForce(1.9)
    bolt11.Swellex.setConstantPretensioningForceInInstallStage(False)
    bolt11.Swellex.setFacePlates(True)
    bolt11.Swellex.setAddPullOutForce(True)
    bolt11.Swellex.setPullOutForce(1.11)

    assert(bolt11.Swellex.getTensileCapacity(), 1.21)
    assert(bolt11.Swellex.getResidualTensileCapacity(), 1.2)
    assert(bolt11.Swellex.getTributaryArea(), 1.3)
    assert(bolt11.Swellex.getBoltModulusE(), 1.4)
    assert(bolt11.Swellex.getOutofPlaneSpacing(), 1.5)
    assert(bolt11.Swellex.getMaterialDependent(), False)
    assert(bolt11.Swellex.getBondShearStiffness(), 1.6)
    assert(bolt11.Swellex.getBondStrength(), 1.7)
    assert(bolt11.Swellex.getResidualBondStrength(), 0.8)
    assert(bolt11.Swellex.getBoltModel(), BoltModels.P2_BOLT_PLASTIC)
    assert(bolt11.Swellex.getJointShear(), False)
    assert(bolt11.Swellex.getPreTensioningForce(), 1.9)
    assert(bolt11.Swellex.getConstantPretensioningForceInInstallStage(), False)
    assert(bolt11.Swellex.getFacePlates(), True)
    assert(bolt11.Swellex.getAddPullOutForce(), True)
    assert(bolt11.Swellex.getPullOutForce(), 1.11)

def test12():
    bolt12.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt12.Swellex.setTensileCapacity(1.21)
    bolt12.Swellex.setResidualTensileCapacity(1.2)
    bolt12.Swellex.setTributaryArea(1.3)
    bolt12.Swellex.setBoltModulusE(1.4)
    bolt12.Swellex.setOutofPlaneSpacing(1.5)
    bolt12.Swellex.setMaterialDependent(True)
    bolt12.Swellex.setBondStrengthCoefficient(1.6)
    bolt12.Swellex.setBondShearStiffnessCoefficient(1.7)
    bolt12.Swellex.setBoltModel(BoltModels.P2_BOLT_PLASTIC)
    bolt12.Swellex.setJointShear(True)
    bolt12.Swellex.setPreTensioningForce(1.9)
    bolt12.Swellex.setConstantPretensioningForceInInstallStage(False)
    bolt12.Swellex.setFacePlates(False)
    bolt12.Swellex.setAddPullOutForce(True)
    bolt12.Swellex.setPullOutForce(1.11)

    assert(bolt12.Swellex.getTensileCapacity(), 1.21)
    assert(bolt12.Swellex.getResidualTensileCapacity(), 1.2)
    assert(bolt12.Swellex.getTributaryArea(), 1.3)
    assert(bolt12.Swellex.getBoltModulusE(), 1.4)
    assert(bolt12.Swellex.getOutofPlaneSpacing(), 1.5)
    assert(bolt12.Swellex.getMaterialDependent(), True)
    assert(bolt12.Swellex.getBondStrengthCoefficient(), 1.6)
    assert(bolt12.Swellex.getBondShearStiffnessCoefficient(), 1.7)
    assert(bolt12.Swellex.getBoltModel(), BoltModels.P2_BOLT_PLASTIC)
    assert(bolt12.Swellex.getJointShear(), True)
    assert(bolt12.Swellex.getPreTensioningForce(), 1.9)
    assert(bolt12.Swellex.getConstantPretensioningForceInInstallStage(), False)
    assert(bolt12.Swellex.getFacePlates(), False)
    assert(bolt12.Swellex.getAddPullOutForce(), True)
    assert(bolt12.Swellex.getPullOutForce(), 1.11)

def test13():
    bolt13.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt13.Swellex.setTributaryArea(1.1)
    bolt13.Swellex.setBoltModulusE(1.2)
    bolt13.Swellex.setOutofPlaneSpacing(1.3)
    bolt13.Swellex.setBondShearStiffness(1.4)
    bolt13.Swellex.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
    bolt13.Swellex.setJointShear(True)
    bolt13.Swellex.setPreTensioningForce(1.5)
    bolt13.Swellex.setConstantPretensioningForceInInstallStage(True)
    bolt13.Swellex.setFacePlates(True)
    bolt13.Swellex.setAddPullOutForce(True)
    bolt13.Swellex.setPullOutForce(1.6)

    assert(bolt13.Swellex.getTributaryArea(), 1.1)
    assert(bolt13.Swellex.getBoltModulusE(), 1.2)
    assert(bolt13.Swellex.getOutofPlaneSpacing(), 1.3)  
    assert(bolt13.Swellex.getBondShearStiffness(), 1.4)
    assert(bolt13.Swellex.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
    assert(bolt13.Swellex.getJointShear(), True)
    assert(bolt13.Swellex.getPreTensioningForce(), 1.5)
    assert(bolt13.Swellex.getConstantPretensioningForceInInstallStage(), True)
    assert(bolt13.Swellex.getFacePlates(), True)
    assert(bolt13.Swellex.getAddPullOutForce(), True)
    assert(bolt13.Swellex.getPullOutForce(), 1.6)

def test14():
    bolt14.setBoltType(BoltTypes.SHEAR_BOLT)    
    bolt14.Swellex.setTributaryArea(1.1)
    bolt14.Swellex.setBoltModulusE(1.2)
    bolt14.Swellex.setOutofPlaneSpacing(1.3)
    bolt14.Swellex.setBondShearStiffness(1.4)
    bolt14.Swellex.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
    bolt14.Swellex.setJointShear(False)
    bolt14.Swellex.setPreTensioningForce(1.5)
    bolt14.Swellex.setConstantPretensioningForceInInstallStage(False)
    bolt14.Swellex.setFacePlates(False)
    bolt14.Swellex.setAddPullOutForce(False)

    assert(bolt14.Swellex.getTributaryArea(), 1.1)
    assert(bolt14.Swellex.getBoltModulusE(), 1.2)
    assert(bolt14.Swellex.getOutofPlaneSpacing(), 1.3)  
    assert(bolt14.Swellex.getBondShearStiffness(), 1.4)
    assert(bolt14.Swellex.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
    assert(bolt14.Swellex.getJointShear(), False)
    assert(bolt14.Swellex.getPreTensioningForce(), 1.5)
    assert(bolt14.Swellex.getConstantPretensioningForceInInstallStage(), False)
    assert(bolt14.Swellex.getFacePlates(), False)
    assert(bolt14.Swellex.getAddPullOutForce(), False)

def test15():
    bolt15.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt15.Swellex.setTributaryArea(1.1)
    bolt15.Swellex.setBoltModulusE(1.2)
    bolt15.Swellex.setOutofPlaneSpacing(1.3)
    bolt15.Swellex.setBondShearStiffness(1.4)
    bolt15.Swellex.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
    bolt15.Swellex.setJointShear(True)
    bolt15.Swellex.setPreTensioningForce(1.5)
    bolt15.Swellex.setConstantPretensioningForceInInstallStage(False)
    bolt15.Swellex.setFacePlates(False)
    bolt15.Swellex.setAddPullOutForce(False)

    assert(bolt15.Swellex.getTributaryArea(), 1.1)
    assert(bolt15.Swellex.getBoltModulusE(), 1.2)
    assert(bolt15.Swellex.getOutofPlaneSpacing(), 1.3)  
    assert(bolt15.Swellex.getBondShearStiffness(), 1.4)
    assert(bolt15.Swellex.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
    assert(bolt15.Swellex.getJointShear(), True)
    assert(bolt15.Swellex.getPreTensioningForce(), 1.5)
    assert(bolt15.Swellex.getConstantPretensioningForceInInstallStage(), False)
    assert(bolt15.Swellex.getFacePlates(), False)
    assert(bolt15.Swellex.getAddPullOutForce(), False)

def test16():
    bolt16.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt16.Swellex.setTributaryArea(1.1)
    bolt16.Swellex.setBoltModulusE(1.2)
    bolt16.Swellex.setOutofPlaneSpacing(1.3)
    bolt16.Swellex.setBondShearStiffness(1.4)
    bolt16.Swellex.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
    bolt16.Swellex.setJointShear(False)
    bolt16.Swellex.setPreTensioningForce(1.5)
    bolt16.Swellex.setConstantPretensioningForceInInstallStage(True)
    bolt16.Swellex.setFacePlates(False)
    bolt16.Swellex.setAddPullOutForce(False)

    assert(bolt16.Swellex.getTributaryArea(), 1.1)
    assert(bolt16.Swellex.getBoltModulusE(), 1.2)
    assert(bolt16.Swellex.getOutofPlaneSpacing(), 1.3)  
    assert(bolt16.Swellex.getBondShearStiffness(), 1.4)
    assert(bolt16.Swellex.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
    assert(bolt16.Swellex.getJointShear(), False)
    assert(bolt16.Swellex.getPreTensioningForce(), 1.5)
    assert(bolt16.Swellex.getConstantPretensioningForceInInstallStage(), True)
    assert(bolt16.Swellex.getFacePlates(), False)
    assert(bolt16.Swellex.getAddPullOutForce(), False)

def test17():
    bolt17.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt17.Swellex.setTributaryArea(1.1)
    bolt17.Swellex.setBoltModulusE(1.2)
    bolt17.Swellex.setOutofPlaneSpacing(1.3)
    bolt17.Swellex.setBondShearStiffness(1.4)
    bolt17.Swellex.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
    bolt17.Swellex.setJointShear(False)
    bolt17.Swellex.setPreTensioningForce(1.5)
    bolt17.Swellex.setConstantPretensioningForceInInstallStage(False)
    bolt17.Swellex.setFacePlates(True)
    bolt17.Swellex.setAddPullOutForce(False)

    assert(bolt17.Swellex.getTributaryArea(), 1.1)
    assert(bolt17.Swellex.getBoltModulusE(), 1.2)
    assert(bolt17.Swellex.getOutofPlaneSpacing(), 1.3)  
    assert(bolt17.Swellex.getBondShearStiffness(), 1.4)
    assert(bolt17.Swellex.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
    assert(bolt17.Swellex.getJointShear(), False)
    assert(bolt17.Swellex.getPreTensioningForce(), 1.5)
    assert(bolt17.Swellex.getConstantPretensioningForceInInstallStage(), False)
    assert(bolt17.Swellex.getFacePlates(), True)
    assert(bolt17.Swellex.getAddPullOutForce(), False)

def test18():
    bolt18.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt18.Swellex.setTributaryArea(1.1)
    bolt18.Swellex.setBoltModulusE(1.2)
    bolt18.Swellex.setOutofPlaneSpacing(1.3)
    bolt18.Swellex.setBondShearStiffness(1.4)
    bolt18.Swellex.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
    bolt18.Swellex.setJointShear(False)
    bolt18.Swellex.setPreTensioningForce(1.5)
    bolt18.Swellex.setConstantPretensioningForceInInstallStage(False)
    bolt18.Swellex.setFacePlates(False)
    bolt18.Swellex.setAddPullOutForce(True)
    bolt18.Swellex.setPullOutForce(1.6)


    assert(bolt18.Swellex.getTributaryArea(), 1.1)
    assert(bolt18.Swellex.getBoltModulusE(), 1.2)
    assert(bolt18.Swellex.getOutofPlaneSpacing(), 1.3)  
    assert(bolt18.Swellex.getBondShearStiffness(), 1.4)
    assert(bolt18.Swellex.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
    assert(bolt18.Swellex.getJointShear(), False)
    assert(bolt18.Swellex.getPreTensioningForce(), 1.5)
    assert(bolt18.Swellex.getConstantPretensioningForceInInstallStage(), False)
    assert(bolt18.Swellex.getFacePlates(), False)
    assert(bolt18.Swellex.getAddPullOutForce(), True)
    assert(bolt18.Swellex.getPullOutForce(), 1.6)

def test19():
    bolt19.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt19.Swellex.setTributaryArea(1.1)
    bolt19.Swellex.setBoltModulusE(1.2)
    bolt19.Swellex.setOutofPlaneSpacing(1.3)
    bolt19.Swellex.setBondShearStiffness(1.4)
    bolt19.Swellex.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
    bolt19.Swellex.setJointShear(True)
    bolt19.Swellex.setPreTensioningForce(1.5)
    bolt19.Swellex.setConstantPretensioningForceInInstallStage(False)
    bolt19.Swellex.setFacePlates(True)
    bolt19.Swellex.setAddPullOutForce(False)

    assert(bolt19.Swellex.getTributaryArea(), 1.1)
    assert(bolt19.Swellex.getBoltModulusE(), 1.2)
    assert(bolt19.Swellex.getOutofPlaneSpacing(), 1.3)  
    assert(bolt19.Swellex.getBondShearStiffness(), 1.4)
    assert(bolt19.Swellex.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
    assert(bolt19.Swellex.getJointShear(), True)
    assert(bolt19.Swellex.getPreTensioningForce(), 1.5)
    assert(bolt19.Swellex.getConstantPretensioningForceInInstallStage(), False)
    assert(bolt19.Swellex.getFacePlates(), True)
    assert(bolt19.Swellex.getAddPullOutForce(), False)

def test20():
    bolt20.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt20.Swellex.setTributaryArea(1.1)
    bolt20.Swellex.setBoltModulusE(1.2)
    bolt20.Swellex.setOutofPlaneSpacing(1.3)
    bolt20.Swellex.setBondShearStiffness(1.4)
    bolt20.Swellex.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
    bolt20.Swellex.setJointShear(False)
    bolt20.Swellex.setPreTensioningForce(1.5)
    bolt20.Swellex.setConstantPretensioningForceInInstallStage(True)
    bolt20.Swellex.setFacePlates(False)
    bolt20.Swellex.setAddPullOutForce(True)
    bolt20.Swellex.setPullOutForce(1.6)


    assert(bolt20.Swellex.getTributaryArea(), 1.1)
    assert(bolt20.Swellex.getBoltModulusE(), 1.2)
    assert(bolt20.Swellex.getOutofPlaneSpacing(), 1.3)  
    assert(bolt20.Swellex.getBondShearStiffness(), 1.4)
    assert(bolt20.Swellex.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
    assert(bolt20.Swellex.getJointShear(), False)
    assert(bolt20.Swellex.getPreTensioningForce(), 1.5)
    assert(bolt20.Swellex.getConstantPretensioningForceInInstallStage(), True)
    assert(bolt20.Swellex.getFacePlates(), False)
    assert(bolt20.Swellex.getAddPullOutForce(), True)
    assert(bolt20.Swellex.getPullOutForce(), 1.6)

def test21():
    bolt21.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt21.Swellex.setTributaryArea(1.1)
    bolt21.Swellex.setBoltModulusE(1.2)
    bolt21.Swellex.setOutofPlaneSpacing(1.3)
    bolt21.Swellex.setBondShearStiffness(1.4)
    bolt21.Swellex.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
    bolt21.Swellex.setJointShear(True)
    bolt21.Swellex.setPreTensioningForce(1.5)
    bolt21.Swellex.setConstantPretensioningForceInInstallStage(True)
    bolt21.Swellex.setFacePlates(False)
    bolt21.Swellex.setAddPullOutForce(False)

    assert(bolt21.Swellex.getTributaryArea(), 1.1)
    assert(bolt21.Swellex.getBoltModulusE(), 1.2)
    assert(bolt21.Swellex.getOutofPlaneSpacing(), 1.3)  
    assert(bolt21.Swellex.getBondShearStiffness(), 1.4)
    assert(bolt21.Swellex.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
    assert(bolt21.Swellex.getJointShear(), True)
    assert(bolt21.Swellex.getPreTensioningForce(), 1.5)
    assert(bolt21.Swellex.getConstantPretensioningForceInInstallStage(), True)
    assert(bolt21.Swellex.getFacePlates(), False)
    assert(bolt21.Swellex.getAddPullOutForce(), False)

def test22():
    bolt22.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt22.Swellex.setTributaryArea(1.1)
    bolt22.Swellex.setBoltModulusE(1.2)
    bolt22.Swellex.setOutofPlaneSpacing(1.3)
    bolt22.Swellex.setBondShearStiffness(1.4)
    bolt22.Swellex.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
    bolt22.Swellex.setJointShear(False)
    bolt22.Swellex.setPreTensioningForce(1.5)
    bolt22.Swellex.setConstantPretensioningForceInInstallStage(False)
    bolt22.Swellex.setFacePlates(True)
    bolt22.Swellex.setAddPullOutForce(True)
    bolt22.Swellex.setPullOutForce(1.6)


    assert(bolt22.Swellex.getTributaryArea(), 1.1)
    assert(bolt22.Swellex.getBoltModulusE(), 1.2)
    assert(bolt22.Swellex.getOutofPlaneSpacing(), 1.3)  
    assert(bolt22.Swellex.getBondShearStiffness(), 1.4)
    assert(bolt22.Swellex.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
    assert(bolt22.Swellex.getJointShear(), False)
    assert(bolt22.Swellex.getPreTensioningForce(), 1.5)
    assert(bolt22.Swellex.getConstantPretensioningForceInInstallStage(), False)
    assert(bolt22.Swellex.getFacePlates(), True)
    assert(bolt22.Swellex.getAddPullOutForce(), True)
    assert(bolt22.Swellex.getPullOutForce(), 1.6)

def test23():
    bolt23.setBoltType(BoltTypes.SHEAR_BOLT)
    bolt23.Swellex.setTributaryArea(1.1)
    bolt23.Swellex.setBoltModulusE(1.2)
    bolt23.Swellex.setOutofPlaneSpacing(1.3)
    bolt23.Swellex.setBondShearStiffness(1.4)
    bolt23.Swellex.setBoltModel(BoltModels.P2_BOLT_ELASTIC)
    bolt23.Swellex.setJointShear(True)
    bolt23.Swellex.setPreTensioningForce(1.5)
    bolt23.Swellex.setConstantPretensioningForceInInstallStage(False)
    bolt23.Swellex.setFacePlates(True)
    bolt23.Swellex.setAddPullOutForce(True)
    bolt23.Swellex.setPullOutForce(1.6)


    assert(bolt23.Swellex.getTributaryArea(), 1.1)
    assert(bolt23.Swellex.getBoltModulusE(), 1.2)
    assert(bolt23.Swellex.getOutofPlaneSpacing(), 1.3)  
    assert(bolt23.Swellex.getBondShearStiffness(), 1.4)
    assert(bolt23.Swellex.getBoltModel(), BoltModels.P2_BOLT_ELASTIC)
    assert(bolt23.Swellex.getJointShear(), True)
    assert(bolt23.Swellex.getPreTensioningForce(), 1.5)
    assert(bolt23.Swellex.getConstantPretensioningForceInInstallStage(), False)
    assert(bolt23.Swellex.getFacePlates(), True)
    assert(bolt23.Swellex.getAddPullOutForce(), True)
    assert(bolt23.Swellex.getPullOutForce(), 1.6)

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
test14()
test15()
test16()
test17()
test18()
test19()
test20()
test21()
test22()
test23()

model.saveAs(final_python_model)

pass