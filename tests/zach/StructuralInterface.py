from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_StructuralInterface.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Composite\structuralInterface_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Composite\structuralInterface_python.fez'

model = modeler.openFile(base_model)

model.saveAs(final_python_model)

structList = model.getAllStructuralInterfaceProperties()

struct1 = structList[0]
struct2 = structList[1]
struct3 = structList[2]
struct4 = structList[3]
struct5 = structList[4]
struct6 = structList[5]

# Joint properties in base model: Joint 1, Joint 5, Joint 3
# Liner properties in base model: Liner 1, Liner 3, Liner 5, Liner 4, Liner 6

def test1():
    struct = struct1

    struct.setPositiveJointPropertyByName('Joint 1')
    struct.setLinerPropertyByName('Liner 1')
    struct.setNegativeJointPropertyByName('Joint 5')

    assert(struct.getPositiveJointPropertyName(), 'Joint 1')
    assert(struct.getLinerPropertyName(), 'Liner 1')
    assert(struct.getNegativeJointPropertyName(), 'Joint 5')

def test2():
    struct = struct2

    struct.setPositiveJointPropertyByName('Joint 1')
    struct.setLinerPropertyByName('Liner 3')
    struct.setNegativeJointPropertyByName('Joint 3')

    assert(struct.getPositiveJointPropertyName(), 'Joint 1')
    assert(struct.getLinerPropertyName(), 'Liner 3')
    assert(struct.getNegativeJointPropertyName(), 'Joint 3')

def test3():
    struct = struct3

    struct.setPositiveJointPropertyByName('Joint 5')
    struct.setLinerPropertyByName('Liner 5')
    struct.setNegativeJointPropertyByName('Joint 1')

    assert(struct.getPositiveJointPropertyName(), 'Joint 5')
    assert(struct.getLinerPropertyName(), 'Liner 5')
    assert(struct.getNegativeJointPropertyName(), 'Joint 1')

def test4():
    struct = struct4

    struct.setPositiveJointPropertyByName('Joint 5')
    struct.setLinerPropertyByName('Liner 4')
    struct.setNegativeJointPropertyByName('Joint 3')

    assert(struct.getPositiveJointPropertyName(), 'Joint 5')
    assert(struct.getLinerPropertyName(), 'Liner 4')
    assert(struct.getNegativeJointPropertyName(), 'Joint 3')

def test5():
    struct = struct5

    struct.setPositiveJointPropertyByName('Joint 3')
    struct.setLinerPropertyByName('Liner 6')
    struct.setNegativeJointPropertyByName('Joint 1')

    assert(struct.getPositiveJointPropertyName(), 'Joint 3')
    assert(struct.getLinerPropertyName(), 'Liner 6')
    assert(struct.getNegativeJointPropertyName(), 'Joint 1')

def test6():
    struct = struct6

    struct.setPositiveJointPropertyByName('Joint 3')
    struct.setLinerPropertyByName('Liner 1')
    struct.setNegativeJointPropertyByName('Joint 5')

    assert(struct.getPositiveJointPropertyName(), 'Joint 3')
    assert(struct.getLinerPropertyName(), 'Liner 1')
    assert(struct.getNegativeJointPropertyName(), 'Joint 5')

test1()
test2()
test3()
test4()
test5()
test6()

model.save()
pass