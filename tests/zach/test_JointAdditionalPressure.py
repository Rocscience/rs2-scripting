from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_Joint.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Joint\jointAdditionalPressure_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Joint\jointAdditionalPressure_python.fez'

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


def test1():
    joint1.MohrCoulomb.setApplyPorePressure(True)
    joint1.MohrCoulomb.setApplyAdditionalPressureInsideJoint(True)
    joint1.MohrCoulomb.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_VALUE)
    joint1.MohrCoulomb.setAdditionalPressureInsideJoint(1.1)
    joint1.MohrCoulomb.setApplyPressureToLinerSideOnly(True)

    assert(joint1.MohrCoulomb.getApplyPorePressure(), True)
    assert(joint1.MohrCoulomb.getApplyAdditionalPressureInsideJoint(), True)
    assert(joint1.MohrCoulomb.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_VALUE)
    assert(joint1.MohrCoulomb.getAdditionalPressureInsideJoint(), 1.1)  
    assert(joint1.MohrCoulomb.getApplyPressureToLinerSideOnly(), True)

def test2():
    joint2.MohrCoulomb.setApplyPorePressure(False)
    joint2.MohrCoulomb.setApplyAdditionalPressureInsideJoint(False)
    joint2.MohrCoulomb.setApplyPressureToLinerSideOnly(False)

    assert(joint2.MohrCoulomb.getApplyPorePressure(), False)
    assert(joint2.MohrCoulomb.getApplyAdditionalPressureInsideJoint(), False)
    assert(joint2.MohrCoulomb.getApplyPressureToLinerSideOnly(), False)

def test3():
    joint3.MohrCoulomb.setApplyPorePressure(True)
    joint3.MohrCoulomb.setApplyAdditionalPressureInsideJoint(False)
    joint3.MohrCoulomb.setApplyPressureToLinerSideOnly(False)

    assert(joint3.MohrCoulomb.getApplyPorePressure(), True)
    assert(joint3.MohrCoulomb.getApplyAdditionalPressureInsideJoint(), False)
    assert(joint3.MohrCoulomb.getApplyPressureToLinerSideOnly(), False)

def test4():
    joint4.MohrCoulomb.setApplyPorePressure(False)
    joint4.MohrCoulomb.setApplyAdditionalPressureInsideJoint(True)
    joint4.MohrCoulomb.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_VALUE)
    joint4.MohrCoulomb.setAdditionalPressureInsideJoint(1.1)
    joint4.MohrCoulomb.setApplyPressureToLinerSideOnly(False)

    assert(joint4.MohrCoulomb.getApplyPorePressure(), False)
    assert(joint4.MohrCoulomb.getApplyAdditionalPressureInsideJoint(), True)
    assert(joint4.MohrCoulomb.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_VALUE)
    assert(joint4.MohrCoulomb.getAdditionalPressureInsideJoint(), 1.1)
    assert(joint4.MohrCoulomb.getApplyPressureToLinerSideOnly(), False)

def test5():
    joint5.MohrCoulomb.setApplyPorePressure(False)
    joint5.MohrCoulomb.setApplyAdditionalPressureInsideJoint(True)
    joint5.MohrCoulomb.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
    joint5.MohrCoulomb.setPiezoID(0)
    joint5.MohrCoulomb.setApplyPressureToLinerSideOnly(False)

    assert(joint5.MohrCoulomb.getApplyPorePressure(), False)
    assert(joint5.MohrCoulomb.getApplyAdditionalPressureInsideJoint(), True)
    assert(joint5.MohrCoulomb.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
    assert(joint5.MohrCoulomb.getPiezoID(), 0)
    assert(joint5.MohrCoulomb.getApplyPressureToLinerSideOnly(), False)

def test6():
    joint6.MohrCoulomb.setApplyPorePressure(False)
    joint6.MohrCoulomb.setApplyAdditionalPressureInsideJoint(True)
    joint6.MohrCoulomb.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
    joint6.MohrCoulomb.setPiezoID(1)
    joint6.MohrCoulomb.setApplyPressureToLinerSideOnly(False)

    assert(joint6.MohrCoulomb.getApplyPorePressure(), False) 
    assert(joint6.MohrCoulomb.getApplyAdditionalPressureInsideJoint(), True)
    assert(joint6.MohrCoulomb.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
    assert(joint6.MohrCoulomb.getPiezoID(), 1)
    assert(joint6.MohrCoulomb.getApplyPressureToLinerSideOnly(), False)

def test7():
    joint7.MohrCoulomb.setApplyPorePressure(False)
    joint7.MohrCoulomb.setApplyAdditionalPressureInsideJoint(True)
    joint7.MohrCoulomb.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
    joint7.MohrCoulomb.setPiezoID(2)
    joint7.MohrCoulomb.setApplyPressureToLinerSideOnly(False)

    assert(joint7.MohrCoulomb.getApplyPorePressure(), False)
    assert(joint7.MohrCoulomb.getApplyAdditionalPressureInsideJoint(), True)
    assert(joint7.MohrCoulomb.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_PIEZO)
    assert(joint7.MohrCoulomb.getPiezoID(), 2)
    assert(joint7.MohrCoulomb.getApplyPressureToLinerSideOnly(), False)

def test8():
    joint8.MohrCoulomb.setApplyPorePressure(False)
    joint8.MohrCoulomb.setApplyAdditionalPressureInsideJoint(False)
    joint8.MohrCoulomb.setApplyPressureToLinerSideOnly(True)

    assert(joint8.MohrCoulomb.getApplyPorePressure(), False)
    assert(joint8.MohrCoulomb.getApplyAdditionalPressureInsideJoint(), False) 
    assert(joint8.MohrCoulomb.getApplyPressureToLinerSideOnly(), True)

def test9():
    joint9.MohrCoulomb.setApplyPorePressure(True)
    joint9.MohrCoulomb.setApplyAdditionalPressureInsideJoint(True)
    joint9.MohrCoulomb.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_VALUE)
    joint9.MohrCoulomb.setAdditionalPressureInsideJoint(1.1)
    joint9.MohrCoulomb.setApplyPressureToLinerSideOnly(False)

    assert(joint9.MohrCoulomb.getApplyPorePressure(), True)
    assert(joint9.MohrCoulomb.getApplyAdditionalPressureInsideJoint(), True)
    assert(joint9.MohrCoulomb.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_VALUE)
    assert(joint9.MohrCoulomb.getAdditionalPressureInsideJoint(), 1.1)
    assert(joint9.MohrCoulomb.getApplyPressureToLinerSideOnly(), False)

def test10():
    joint10.MohrCoulomb.setApplyPorePressure(True)
    joint10.MohrCoulomb.setApplyAdditionalPressureInsideJoint(False)
    joint10.MohrCoulomb.setApplyPressureToLinerSideOnly(True)

    assert(joint10.MohrCoulomb.getApplyPorePressure(), True)
    assert(joint10.MohrCoulomb.getApplyAdditionalPressureInsideJoint(), False) 
    assert(joint10.MohrCoulomb.getApplyPressureToLinerSideOnly(), True)

def test11():
    joint11.MohrCoulomb.setApplyPorePressure(False)
    joint11.MohrCoulomb.setApplyAdditionalPressureInsideJoint(True)
    joint11.MohrCoulomb.setAdditionalPressureType(AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_VALUE)
    joint11.MohrCoulomb.setAdditionalPressureInsideJoint(1.1)
    joint11.MohrCoulomb.setApplyPressureToLinerSideOnly(True)

    assert(joint11.MohrCoulomb.getApplyPorePressure(), False)
    assert(joint11.MohrCoulomb.getApplyAdditionalPressureInsideJoint(), True)
    assert(joint11.MohrCoulomb.getAdditionalPressureType(), AdditionalPressureType.JOINT_ADDITIONAL_PRESSURE_BY_VALUE)
    assert(joint11.MohrCoulomb.getAdditionalPressureInsideJoint(), 1.1)
    assert(joint11.MohrCoulomb.getApplyPressureToLinerSideOnly(), True)

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


model.save()
pass