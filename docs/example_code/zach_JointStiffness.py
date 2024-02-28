from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_Joint.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Joint\jointStiffness_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Joint\jointStiffness_python.fez'

model = modeler.openFile(base_model)

model.saveAs(final_python_model)

jointList = model.getAllJointProperties()

joint1 = jointList[0]
joint2 = jointList[1]
joint3 = jointList[2]


def test1():
    joint1.MohrCoulomb.setNormalStiffness(1.1)
    joint1.MohrCoulomb.setShearStiffness(1.2)

    assert(joint1.MohrCoulomb.getNormalStiffness(), 1.1)
    assert(joint1.MohrCoulomb.getShearStiffness(), 1.2)

def test2():
    joint2.setSlipCriterion(JointTypes.JOINT_MATERIAL_DEPENDENT)
    joint2.MaterialDependent.setDefineStiffness(DefineStiffness.DEFINE_PARAMETER)
    joint2.MaterialDependent.setNormalStiffness(1.1)
    joint2.MaterialDependent.setShearStiffness(1.2)

    assert(joint2.getSlipCriterion(), JointTypes.JOINT_MATERIAL_DEPENDENT)
    assert(joint2.MaterialDependent.getDefineStiffness(), DefineStiffness.DEFINE_PARAMETER)
    assert(joint2.MaterialDependent.getNormalStiffness(),1.1)
    assert(joint2.MaterialDependent.getShearStiffness(),1.2)
    

def test3():
    joint3.setSlipCriterion(JointTypes.JOINT_MATERIAL_DEPENDENT)
    joint3.MaterialDependent.setDefineStiffness(DefineStiffness.MATERIAL_DEPENDENT)
    joint3.MaterialDependent.setStiffnessCoefficient(1.3)

    assert(joint3.getSlipCriterion(), JointTypes.JOINT_MATERIAL_DEPENDENT)
    assert(joint3.MaterialDependent.getDefineStiffness(), DefineStiffness.MATERIAL_DEPENDENT)  
    assert(joint3.MaterialDependent.getStiffnessCoefficient(), 1.3)


test1()
test2()
test3()


model.save()
pass