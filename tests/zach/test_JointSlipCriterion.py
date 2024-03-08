from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_Joint.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Joint\slipCriterion_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Joint\slipCriterion_python.fez'

model = modeler.openFile(base_model)

model.saveAs(final_python_model)

jointList = model.getAllJointProperties()

joint1 = jointList[0]
joint2 = jointList[1]
joint3 = jointList[2]
joint4 = jointList[3]
joint5 = jointList[4]
joint6 = jointList[5]
joint7 = jointList[6] 
joint8 = jointList[7]
joint9 = jointList[8]
joint10 = jointList[9]
joint11 = jointList[10]
joint12 = jointList[11]
joint13 = jointList[12]
joint14 = jointList[13] 
joint15 = jointList[14]
joint16 = jointList[15]

def test1():
    joint1.setSlipCriterion(JointTypes.JOINT_NONE)

    assert(joint1.getSlipCriterion(),JointTypes.JOINT_NONE)

def test2():
    joint2.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint2.MohrCoulomb.setTensileStrength(1.1)
    joint2.MohrCoulomb.setPeakCohesion(1.2)
    joint2.MohrCoulomb.setPeakFrictionAngle(1.3)
    #joint2.MohrCoulomb.setIncludeDilation(True) *This method does not currently exist
    joint2.MohrCoulomb.setDilationAngle(1.4)
    joint2.MohrCoulomb.setDMin(1.5)
    joint2.MohrCoulomb.setDMax(1.6)
    joint2.MohrCoulomb.setDirectional(True)
    joint2.MohrCoulomb.setResidualStrength(True)
    joint2.MohrCoulomb.setResTensileStrength(1.7)
    joint2.MohrCoulomb.setResCohesion(1.8)
    joint2.MohrCoulomb.setResFrictionAngle(1.9)

    assert(joint2.getSlipCriterion(), JointTypes.JOINT_MOHR_COULOMB)
    assert(joint2.MohrCoulomb.getTensileStrength(), 1.1)
    assert(joint2.MohrCoulomb.getPeakCohesion(), 1.2)
    assert(joint2.MohrCoulomb.getPeakFrictionAngle(), 1.3)
    #assert(joint2.MohrCoulomb.getIncludeDilation(), True)
    assert(joint2.MohrCoulomb.getDilationAngle(), 1.4)
    assert(joint2.MohrCoulomb.getDMin(), 1.5)
    assert(joint2.MohrCoulomb.getDMax(), 1.6)
    assert(joint2.MohrCoulomb.getDirectional(), True) 
    assert(joint2.MohrCoulomb.getResidualStrength(), True)
    assert(joint2.MohrCoulomb.getResTensileStrength(), 1.7)
    assert(joint2.MohrCoulomb.getResCohesion(), 1.8)
    assert(joint2.MohrCoulomb.getResFrictionAngle(), 1.9)

def test3():
    joint3.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint3.MohrCoulomb.setTensileStrength(1.1)
    joint3.MohrCoulomb.setPeakCohesion(1.2)
    joint3.MohrCoulomb.setPeakFrictionAngle(1.3)
    #joint3.MohrCoulomb.setIncludeDilation(False) *This method does not currently exist
    joint3.MohrCoulomb.setDMin(1.5)
    joint3.MohrCoulomb.setDMax(1.6)
    joint3.MohrCoulomb.setDirectional(False)
    joint3.MohrCoulomb.setResidualStrength(False)

    assert(joint3.getSlipCriterion(), JointTypes.JOINT_MOHR_COULOMB)
    assert(joint3.MohrCoulomb.getTensileStrength(), 1.1)
    assert(joint3.MohrCoulomb.getPeakCohesion(), 1.2)
    assert(joint3.MohrCoulomb.getPeakFrictionAngle(), 1.3)
    #assert(joint3.MohrCoulomb.getIncludeDilation(), False)    
    assert(joint3.MohrCoulomb.getDMin(), 1.5)
    assert(joint3.MohrCoulomb.getDMax(), 1.6)
    assert(joint3.MohrCoulomb.getDirectional(), False)
    assert(joint3.MohrCoulomb.getResidualStrength(), False)

def test4():
    joint4.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint4.MohrCoulomb.setTensileStrength(1.1)
    joint4.MohrCoulomb.setPeakCohesion(1.2)
    joint4.MohrCoulomb.setPeakFrictionAngle(1.3)
    #joint4.MohrCoulomb.setIncludeDilation(True) *This method does not currently exist
    joint4.MohrCoulomb.setDilationAngle(1.4)
    joint4.MohrCoulomb.setDMin(1.5)
    joint4.MohrCoulomb.setDMax(1.6)
    joint4.MohrCoulomb.setDirectional(False)
    joint4.MohrCoulomb.setResidualStrength(False)

    assert(joint4.getSlipCriterion(), JointTypes.JOINT_MOHR_COULOMB)
    assert(joint4.MohrCoulomb.getTensileStrength(), 1.1)
    assert(joint4.MohrCoulomb.getPeakCohesion(), 1.2)
    assert(joint4.MohrCoulomb.getPeakFrictionAngle(), 1.3)
    #assert(joint4.MohrCoulomb.getIncludeDilation(), True)
    assert(joint4.MohrCoulomb.getDilationAngle(), 1.4)
    assert(joint4.MohrCoulomb.getDMin(), 1.5)
    assert(joint4.MohrCoulomb.getDMax(), 1.6)
    assert(joint4.MohrCoulomb.getDirectional(), False)
    assert(joint4.MohrCoulomb.getResidualStrength(), False)

def test5():
    joint5.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint5.MohrCoulomb.setTensileStrength(1.1)
    joint5.MohrCoulomb.setPeakCohesion(1.2)
    joint5.MohrCoulomb.setPeakFrictionAngle(1.3)
    #joint5.MohrCoulomb.setIncludeDilation(False) *This method does not currently exist
    joint5.MohrCoulomb.setDMin(1.5)
    joint5.MohrCoulomb.setDMax(1.6)
    joint5.MohrCoulomb.setDirectional(True)
    joint5.MohrCoulomb.setResidualStrength(False)

    assert(joint5.getSlipCriterion(), JointTypes.JOINT_MOHR_COULOMB)
    assert(joint5.MohrCoulomb.getTensileStrength(), 1.1)
    assert(joint5.MohrCoulomb.getPeakCohesion(), 1.2)
    assert(joint5.MohrCoulomb.getPeakFrictionAngle(), 1.3)
    #assert(joint5.MohrCoulomb.getIncludeDilation(), False)
    assert(joint5.MohrCoulomb.getDMin(), 1.5)
    assert(joint5.MohrCoulomb.getDMax(), 1.6)
    assert(joint5.MohrCoulomb.getDirectional(), True)
    assert(joint5.MohrCoulomb.getResidualStrength(), False)

def test6():
    joint6.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint6.MohrCoulomb.setTensileStrength(1.1)
    joint6.MohrCoulomb.setPeakCohesion(1.2)
    joint6.MohrCoulomb.setPeakFrictionAngle(1.3)
    #joint6.MohrCoulomb.setIncludeDilation(False) *This method does not currently exist
    joint6.MohrCoulomb.setDMin(1.5)
    joint6.MohrCoulomb.setDMax(1.6)
    joint6.MohrCoulomb.setDirectional(False)
    joint6.MohrCoulomb.setResidualStrength(True)
    joint6.MohrCoulomb.setResTensileStrength(1.7)
    joint6.MohrCoulomb.setResCohesion(1.8)
    joint6.MohrCoulomb.setResFrictionAngle(1.9)

    assert(joint6.getSlipCriterion(), JointTypes.JOINT_MOHR_COULOMB)
    assert(joint6.MohrCoulomb.getTensileStrength(), 1.1)
    assert(joint6.MohrCoulomb.getPeakCohesion(), 1.2)
    assert(joint6.MohrCoulomb.getPeakFrictionAngle(), 1.3)
    #assert(joint6.MohrCoulomb.getIncludeDilation(), False)
    assert(joint6.MohrCoulomb.getDMin(), 1.5)
    assert(joint6.MohrCoulomb.getDMax(), 1.6)
    assert(joint6.MohrCoulomb.getDirectional(), False)
    assert(joint6.MohrCoulomb.getResidualStrength(), True)
    assert(joint6.MohrCoulomb.getResTensileStrength(), 1.7)
    assert(joint6.MohrCoulomb.getResCohesion(), 1.8)
    assert(joint6.MohrCoulomb.getResFrictionAngle(), 1.9)

def test7():
    joint7.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint7.MohrCoulomb.setTensileStrength(1.1)
    joint7.MohrCoulomb.setPeakCohesion(1.2)
    joint7.MohrCoulomb.setPeakFrictionAngle(1.3)
    #joint7.MohrCoulomb.setIncludeDilation(True) *This method does not currently exist
    joint7.MohrCoulomb.setDilationAngle(1.4)
    joint7.MohrCoulomb.setDMin(1.5)
    joint7.MohrCoulomb.setDMax(1.6)
    joint7.MohrCoulomb.setDirectional(True)
    joint7.MohrCoulomb.setResidualStrength(False)

    assert(joint7.getSlipCriterion(), JointTypes.JOINT_MOHR_COULOMB)
    assert(joint7.MohrCoulomb.getTensileStrength(), 1.1)
    assert(joint7.MohrCoulomb.getPeakCohesion(), 1.2)
    assert(joint7.MohrCoulomb.getPeakFrictionAngle(), 1.3)
    #assert(joint7.MohrCoulomb.getIncludeDilation(), True)
    assert(joint7.MohrCoulomb.getDilationAngle(), 1.4)
    assert(joint7.MohrCoulomb.getDMin(), 1.5)
    assert(joint7.MohrCoulomb.getDMax(), 1.6)
    assert(joint7.MohrCoulomb.getDirectional(), True)
    assert(joint7.MohrCoulomb.getResidualStrength(), False)


def test8():
    joint8.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint8.MohrCoulomb.setTensileStrength(1.1)
    joint8.MohrCoulomb.setPeakCohesion(1.2)
    joint8.MohrCoulomb.setPeakFrictionAngle(1.3)
    #joint8.MohrCoulomb.setIncludeDilation(True) *This method does not currently exist
    joint8.MohrCoulomb.setDilationAngle(1.4)
    joint8.MohrCoulomb.setDMin(1.5)
    joint8.MohrCoulomb.setDMax(1.6)
    joint8.MohrCoulomb.setDirectional(False)
    joint8.MohrCoulomb.setResidualStrength(True)
    joint8.MohrCoulomb.setResTensileStrength(1.7)
    joint8.MohrCoulomb.setResCohesion(1.8)
    joint8.MohrCoulomb.setResFrictionAngle(1.9)

    assert(joint8.getSlipCriterion(), JointTypes.JOINT_MOHR_COULOMB)
    assert(joint8.MohrCoulomb.getTensileStrength(), 1.1)
    assert(joint8.MohrCoulomb.getPeakCohesion(), 1.2)
    assert(joint8.MohrCoulomb.getPeakFrictionAngle(), 1.3)
    #assert(joint8.MohrCoulomb.getIncludeDilation(), True)
    assert(joint8.MohrCoulomb.getDilationAngle(), 1.4)
    assert(joint8.MohrCoulomb.getDMin(), 1.5)
    assert(joint8.MohrCoulomb.getDMax(), 1.6)
    assert(joint8.MohrCoulomb.getDirectional(), False)
    assert(joint8.MohrCoulomb.getResidualStrength(), True)
    assert(joint8.MohrCoulomb.getResTensileStrength(), 1.7)
    assert(joint8.MohrCoulomb.getResCohesion(), 1.8)
    assert(joint8.MohrCoulomb.getResFrictionAngle(), 1.9)

def test9():
    joint9.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint9.MohrCoulomb.setTensileStrength(1.1)
    joint9.MohrCoulomb.setPeakCohesion(1.2)
    joint9.MohrCoulomb.setPeakFrictionAngle(1.3)
    #joint9.MohrCoulomb.setIncludeDilation(False) *This method does not currently exist
    joint9.MohrCoulomb.setDMin(1.5)
    joint9.MohrCoulomb.setDMax(1.6)
    joint9.MohrCoulomb.setDirectional(True)
    joint9.MohrCoulomb.setResidualStrength(True)
    joint9.MohrCoulomb.setResTensileStrength(1.7)
    joint9.MohrCoulomb.setResCohesion(1.8)
    joint9.MohrCoulomb.setResFrictionAngle(1.9)

    assert(joint9.getSlipCriterion(), JointTypes.JOINT_MOHR_COULOMB)
    assert(joint9.MohrCoulomb.getTensileStrength(), 1.1)
    assert(joint9.MohrCoulomb.getPeakCohesion(), 1.2)
    assert(joint9.MohrCoulomb.getPeakFrictionAngle(), 1.3)
    #assert(joint9.MohrCoulomb.getIncludeDilation(), False)
    assert(joint9.MohrCoulomb.getDMin(), 1.5)
    assert(joint9.MohrCoulomb.getDMax(), 1.6)
    assert(joint9.MohrCoulomb.getDirectional(), True)
    assert(joint9.MohrCoulomb.getResidualStrength(), True)
    assert(joint9.MohrCoulomb.getResTensileStrength(), 1.7)
    assert(joint9.MohrCoulomb.getResCohesion(), 1.8)
    assert(joint9.MohrCoulomb.getResFrictionAngle(), 1.9)    

def test10():
    joint10.setSlipCriterion(JointTypes.JOINT_BARTON_BANDIS)
    joint10.BartonBandis.setJCS(1.11)
    joint10.BartonBandis.setJRC(1.12)
    joint10.BartonBandis.setResidualFrictionAngle(1.13)
    joint10.BartonBandis.setResidualStrength(True)

    assert(joint10.getSlipCriterion(), JointTypes.JOINT_BARTON_BANDIS)
    assert(joint10.BartonBandis.getJCS(), 1.11)
    assert(joint10.BartonBandis.getJRC(), 1.12) 
    assert(joint10.BartonBandis.getResidualFrictionAngle(), 1.13)
    assert(joint10.BartonBandis.getResidualStrength(), True)

def test11():
    joint11.setSlipCriterion(JointTypes.JOINT_BARTON_BANDIS)
    joint11.BartonBandis.setJCS(1.11)
    joint11.BartonBandis.setJRC(1.12)
    joint11.BartonBandis.setResidualFrictionAngle(1.13)
    joint11.BartonBandis.setResidualStrength(False)

    assert(joint11.getSlipCriterion(), JointTypes.JOINT_BARTON_BANDIS)
    assert(joint11.BartonBandis.getJCS(), 1.11)
    assert(joint11.BartonBandis.getJRC(), 1.12)
    assert(joint11.BartonBandis.getResidualFrictionAngle(), 1.13)
    assert(joint11.BartonBandis.getResidualStrength(), False)

def test12():
    joint12.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SIMPLE)
    joint12.GeosyntheticHyperbolic.setPeakAdhesionAtSigninf(1.14)
    joint12.GeosyntheticHyperbolic.setPeakFrictionAngleAtSign0(1.15)
    joint12.GeosyntheticHyperbolic.setResAdhesionAtSigninf(1.16)
    joint12.GeosyntheticHyperbolic.setResFrictionAngleAtSign0(1.17)

    assert(joint12.getSlipCriterion(), JointTypes.JOINT_HYPERBOLIC_SIMPLE)
    assert(joint12.GeosyntheticHyperbolic.getPeakAdhesionAtSigninf(), 1.14)
    assert(joint12.GeosyntheticHyperbolic.getPeakFrictionAngleAtSign0(), 1.15)
    assert(joint12.GeosyntheticHyperbolic.getResAdhesionAtSigninf(), 1.16)
    assert(joint12.GeosyntheticHyperbolic.getResFrictionAngleAtSign0(), 1.17)

def test13():
    joint13.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SOFTENING)
    joint13.HyperbolicSoftening.setPeakCohesion(1.18)
    joint13.HyperbolicSoftening.setPeakFriction(1.19)
    joint13.HyperbolicSoftening.setResCohesion(1.21)
    joint13.HyperbolicSoftening.setResFriction(1.22)
    joint13.HyperbolicSoftening.setTensileStrength(1.23)
    joint13.HyperbolicSoftening.setResTensileStrength(1.24)
    joint13.HyperbolicSoftening.setDeltaR(1.25)
    joint13.HyperbolicSoftening.setInitialSlope(1.26)
    joint13.HyperbolicSoftening.setWorkSoftening(True)

    assert(joint13.getSlipCriterion(), JointTypes.JOINT_HYPERBOLIC_SOFTENING)
    assert(joint13.HyperbolicSoftening.getPeakCohesion(), 1.18)
    assert(joint13.HyperbolicSoftening.getPeakFriction(), 1.19)
    assert(joint13.HyperbolicSoftening.getResCohesion(), 1.21)
    assert(joint13.HyperbolicSoftening.getResFriction(), 1.22)
    assert(joint13.HyperbolicSoftening.getTensileStrength(), 1.23)
    assert(joint13.HyperbolicSoftening.getResTensileStrength(), 1.24)
    assert(joint13.HyperbolicSoftening.getDeltaR(), 1.25)
    assert(joint13.HyperbolicSoftening.getInitialSlope(), 1.26)
    assert(joint13.HyperbolicSoftening.getWorkSoftening(), True)

def test14():
    joint14.setSlipCriterion(JointTypes.JOINT_HYPERBOLIC_SOFTENING)
    joint14.HyperbolicSoftening.setPeakCohesion(1.18)
    joint14.HyperbolicSoftening.setPeakFriction(1.19)
    joint14.HyperbolicSoftening.setResCohesion(1.21)
    joint14.HyperbolicSoftening.setResFriction(1.22)
    joint14.HyperbolicSoftening.setTensileStrength(1.23)
    joint14.HyperbolicSoftening.setResTensileStrength(1.24)
    joint14.HyperbolicSoftening.setDeltaR(1.25)
    joint14.HyperbolicSoftening.setInitialSlope(1.26)
    joint14.HyperbolicSoftening.setWorkSoftening(False)

    assert(joint14.getSlipCriterion(), JointTypes.JOINT_HYPERBOLIC_SOFTENING)
    assert(joint14.HyperbolicSoftening.getPeakCohesion(), 1.18)
    assert(joint14.HyperbolicSoftening.getPeakFriction(), 1.19)
    assert(joint14.HyperbolicSoftening.getResCohesion(), 1.21)
    assert(joint14.HyperbolicSoftening.getResFriction(), 1.22)
    assert(joint14.HyperbolicSoftening.getTensileStrength(), 1.23)
    assert(joint14.HyperbolicSoftening.getResTensileStrength(), 1.24)
    assert(joint14.HyperbolicSoftening.getDeltaR(), 1.25)
    assert(joint14.HyperbolicSoftening.getInitialSlope(), 1.26)
    assert(joint14.HyperbolicSoftening.getWorkSoftening(), False)

def test15():
    joint15.setSlipCriterion(JointTypes.JOINT_MATERIAL_DEPENDENT)
    joint15.MaterialDependent.setInterfaceCoefficient(1.27)

    assert(joint15.MaterialDependent.getInterfaceCoefficient(), 1.27)
    assert(joint15.getSlipCriterion(), JointTypes.JOINT_MATERIAL_DEPENDENT)


def test16():
    joint16.setSlipCriterion(JointTypes.JOINT_DISPLACEMENT_DEPENDENT)
    joint16.DisplacementDependent.setDisplacementDependentTable([[1.1,1.2,1.3,1.4],[1.5,1.6,1.7,1.8]])

    assert(joint16.getSlipCriterion(), JointTypes.JOINT_DISPLACEMENT_DEPENDENT)
    assert(joint16.DisplacementDependent.getDisplacementDependentTable(), [[1.1,1.2,1.3,1.4],[1.5,1.6,1.7,1.8]])

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

model.save()
pass