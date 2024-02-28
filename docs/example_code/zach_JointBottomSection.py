from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_Joint.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Joint\bottomSection_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Joint\bottomSection_python.fez'

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
    # Set slip criterion to MohrCoulomb so that Apply SSR is available. slip criteria are fully iterated in zach_JointSlipCriterion
    joint1.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint1.setInitialDeformation(True)
    joint1.SetPermeable(True)
    joint1.SetApplySSR(True)
    joint1.SetMeshConforming(True)

    assert(joint1.getInitialDeformation(), True)
    assert(joint1.GetPermeable(), True)
    assert(joint1.GetApplySSR(), True)
    assert(joint1.GetMeshConforming(), True)

def test2():
    joint2.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint2.setInitialDeformation(False)
    joint2.SetPermeable(False)
    joint2.SetApplySSR(False)
    joint2.SetMeshConforming(False)

    assert(joint2.getInitialDeformation(), False)
    assert(joint2.GetPermeable(), False)
    assert(joint2.GetApplySSR(), False)
    assert(joint2.GetMeshConforming(), False)

def test3():
    joint3.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint3.setInitialDeformation(True)
    joint3.SetPermeable(False)
    joint3.SetApplySSR(False)
    joint3.SetMeshConforming(False)

    assert(joint3.getInitialDeformation(), True)
    assert(joint3.GetPermeable(), False)
    assert(joint3.GetApplySSR(), False)
    assert(joint3.GetMeshConforming(), False)

def test4():
    joint4.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)  
    joint4.setInitialDeformation(False)
    joint4.SetPermeable(True)
    joint4.SetApplySSR(False)
    joint4.SetMeshConforming(False)

    assert(joint4.getInitialDeformation(), False)
    assert(joint4.GetPermeable(), True)
    assert(joint4.GetApplySSR(), False)
    assert(joint4.GetMeshConforming(), False)

def test5():
    joint5.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint5.setInitialDeformation(False)
    joint5.SetPermeable(False)
    joint5.SetApplySSR(True)
    joint5.SetMeshConforming(False)

    assert(joint5.getInitialDeformation(), False)
    assert(joint5.GetPermeable(), False)
    assert(joint5.GetApplySSR(), True)
    assert(joint5.GetMeshConforming(), False)

def test6():
    joint6.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint6.setInitialDeformation(False)
    joint6.SetPermeable(False)
    joint6.SetApplySSR(False)
    joint6.SetMeshConforming(True)

    assert(joint6.getInitialDeformation(), False)
    assert(joint6.GetPermeable(), False)
    assert(joint6.GetApplySSR(), False)
    assert(joint6.GetMeshConforming(), True)

def test7():
    joint7.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint7.setInitialDeformation(True)
    joint7.SetPermeable(False)
    joint7.SetApplySSR(False)
    joint7.SetMeshConforming(True)

    assert(joint7.getInitialDeformation(), True)
    assert(joint7.GetPermeable(), False)
    assert(joint7.GetApplySSR(), False)
    assert(joint7.GetMeshConforming(), True)

def test8():
    joint8.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint8.setInitialDeformation(False)
    joint8.SetPermeable(True)
    joint8.SetApplySSR(True)
    joint8.SetMeshConforming(False)

    assert(joint8.getInitialDeformation(), False)
    assert(joint8.GetPermeable(), True)
    assert(joint8.GetApplySSR(), True)
    assert(joint8.GetMeshConforming(), False)

def test9():
    joint9.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)  
    joint9.setInitialDeformation(True)
    joint9.SetPermeable(True)
    joint9.SetApplySSR(False)
    joint9.SetMeshConforming(False)

    assert(joint9.getInitialDeformation(), True)
    assert(joint9.GetPermeable(), True)
    assert(joint9.GetApplySSR(), False)
    assert(joint9.GetMeshConforming(), False)

def test10():
    joint10.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint10.setInitialDeformation(False)
    joint10.SetPermeable(False)
    joint10.SetApplySSR(True)
    joint10.SetMeshConforming(True)

    assert(joint10.getInitialDeformation(), False)
    assert(joint10.GetPermeable(), False)
    assert(joint10.GetApplySSR(), True)
    assert(joint10.GetMeshConforming(), True)

def test11():
    joint11.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint11.setInitialDeformation(True)
    joint11.SetPermeable(False)
    joint11.SetApplySSR(True)
    joint11.SetMeshConforming(False)

    assert(joint11.getInitialDeformation(), True)
    assert(joint11.GetPermeable(), False)
    assert(joint11.GetApplySSR(), True)
    assert(joint11.GetMeshConforming(), False)

def test12():
    joint12.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint12.setInitialDeformation(False)
    joint12.SetPermeable(True)
    joint12.SetApplySSR(False)
    joint12.SetMeshConforming(True)

    assert(joint12.getInitialDeformation(), False)
    assert(joint12.GetPermeable(), True)
    assert(joint12.GetApplySSR(), False)
    assert(joint12.GetMeshConforming(), True)

def test13():
    joint13.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint13.setInitialDeformation(False)
    joint13.SetPermeable(True)
    joint13.SetApplySSR(True)
    joint13.SetMeshConforming(True)

    assert(joint13.getInitialDeformation(), False)
    assert(joint13.GetPermeable(), True)
    assert(joint13.GetApplySSR(), True)
    assert(joint13.GetMeshConforming(), True)

def test14():
    joint14.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint14.setInitialDeformation(True)
    joint14.SetPermeable(False)
    joint14.SetApplySSR(True)
    joint14.SetMeshConforming(True)

    assert(joint14.getInitialDeformation(), True)
    assert(joint14.GetPermeable(), False)
    assert(joint14.GetApplySSR(), True)
    assert(joint14.GetMeshConforming(), True)

def test15():
    joint15.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint15.setInitialDeformation(True)
    joint15.SetPermeable(True)
    joint15.SetApplySSR(False)
    joint15.SetMeshConforming(True)

    assert(joint1.getInitialDeformation(), True)
    assert(joint1.GetPermeable(), True)
    assert(joint1.GetApplySSR(), False)
    assert(joint1.GetMeshConforming(), True)

def test16():
    joint16.setSlipCriterion(JointTypes.JOINT_MOHR_COULOMB)
    joint16.setInitialDeformation(True)
    joint16.SetPermeable(True)
    joint16.SetApplySSR(True)
    joint16.SetMeshConforming(False)

    assert(joint16.getInitialDeformation(), True)
    assert(joint16.GetPermeable(), True)
    assert(joint16.GetApplySSR(), True)
    assert(joint16.GetMeshConforming(), False)

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