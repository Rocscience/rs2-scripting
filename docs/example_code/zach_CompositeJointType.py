from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_Composite.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Composite\compositeJointType_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Composite\compositeJointType_python.fez'

model = modeler.openFile(base_model)

model.saveAs(final_python_model)

compList = model.getAllCompositeLinerProperties()

comp1 = compList[0]
comp2 = compList[1]
comp3 = compList[2]


def test1():
    comp = comp1

    comp.setJointApplied(True)
    comp.setCompositeJointPropertyByName('Joint 1')

    assert(comp.getJointApplied(), True)
    assert(comp.getCompositeJointPropertyName(), 'Joint 1')

def test2():
    comp = comp2

    comp.setJointApplied(True)
    comp.setCompositeJointPropertyByName('Joint 5')

    assert(comp.getJointApplied(), True)
    assert(comp.getCompositeJointPropertyName(), 'Joint 5')

def test3():
    comp = comp3

    comp.setJointApplied(True)
    comp.setCompositeJointPropertyByName('Joint 3')

    assert(comp.getJointApplied(), True)
    assert(comp.getCompositeJointPropertyName(), 'Joint 3')


test1()
test2()
test3()

model.save()
pass