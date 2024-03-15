from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_Composite.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Composite\compositeLinerType_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Composite\compositeLinerType_python.fez'

model = modeler.openFile(base_model)

model.saveAs(final_python_model)

compList = model.getAllCompositeLinerProperties()

comp1 = compList[0]
comp2 = compList[1]
comp3 = compList[2]
comp4 = compList[3]
comp5 = compList[4]
comp6 = compList[5]

def test1():
    comp = comp1

    comp.setNumberOfLayers(4)
    comp.setCompositeLinerPropertyByName(1, 'Liner 1')
    comp.setCompositeLinerPropertyByName(2, 'Liner 3')
    comp.setCompositeLinerPropertyByName(3, 'Liner 5')
    comp.setCompositeLinerPropertyByName(4, 'Liner 4')

    assert(comp.getCompositeLinerPropertyName(1), 'Liner 1')
    assert(comp.getCompositeLinerPropertyName(2), 'Liner 3')
    assert(comp.getCompositeLinerPropertyName(3), 'Liner 5')
    assert(comp.getCompositeLinerPropertyName(4), 'Liner 4')

def test2():
    comp = comp2

    comp.setNumberOfLayers(4)
    comp.setCompositeLinerPropertyByName(1, 'Liner 4')
    comp.setCompositeLinerPropertyByName(2, 'Liner 5')
    comp.setCompositeLinerPropertyByName(3, 'Liner 3')
    comp.setCompositeLinerPropertyByName(4, 'Liner 1')

    assert(comp.getCompositeLinerPropertyName(1), 'Liner 4')
    assert(comp.getCompositeLinerPropertyName(2), 'Liner 5')
    assert(comp.getCompositeLinerPropertyName(3), 'Liner 3')
    assert(comp.getCompositeLinerPropertyName(4), 'Liner 1')

def test3():
    comp = comp3

    comp.setNumberOfLayers(4)
    comp.setCompositeLinerPropertyByName(1, 'Liner 3')
    comp.setCompositeLinerPropertyByName(2, 'Liner 4')
    comp.setCompositeLinerPropertyByName(3, 'Liner 5')
    comp.setCompositeLinerPropertyByName(4, 'Liner 6')

    assert(comp.getCompositeLinerPropertyName(1), 'Liner 3')
    assert(comp.getCompositeLinerPropertyName(2), 'Liner 4')
    assert(comp.getCompositeLinerPropertyName(3), 'Liner 5')
    assert(comp.getCompositeLinerPropertyName(4), 'Liner 6')

def test4():
    comp = comp4

    comp.setNumberOfLayers(4)
    comp.setCompositeLinerPropertyByName(1, 'Liner 6')
    comp.setCompositeLinerPropertyByName(2, 'Liner 5')
    comp.setCompositeLinerPropertyByName(3, 'Liner 4')
    comp.setCompositeLinerPropertyByName(4, 'Liner 3')

    assert(comp.getCompositeLinerPropertyName(1), 'Liner 6')
    assert(comp.getCompositeLinerPropertyName(2), 'Liner 5')
    assert(comp.getCompositeLinerPropertyName(3), 'Liner 4')
    assert(comp.getCompositeLinerPropertyName(4), 'Liner 3')

def test5():
    comp = comp5

    comp.setNumberOfLayers(4)
    comp.setCompositeLinerPropertyByName(1, 'Liner 1')
    comp.setCompositeLinerPropertyByName(2, 'Liner 5')
    comp.setCompositeLinerPropertyByName(3, 'Liner 6')
    comp.setCompositeLinerPropertyByName(4, 'Liner 3')

    assert(comp.getCompositeLinerPropertyName(1), 'Liner 1')
    assert(comp.getCompositeLinerPropertyName(2), 'Liner 5')
    assert(comp.getCompositeLinerPropertyName(3), 'Liner 6')
    assert(comp.getCompositeLinerPropertyName(4), 'Liner 3')

def test6():
    comp = comp6

    comp.setNumberOfLayers(4)
    comp.setCompositeLinerPropertyByName(1, 'Liner 4')
    comp.setCompositeLinerPropertyByName(2, 'Liner 3')
    comp.setCompositeLinerPropertyByName(3, 'Liner 5')
    comp.setCompositeLinerPropertyByName(4, 'Liner 1')

    assert(comp.getCompositeLinerPropertyName(1), 'Liner 4')
    assert(comp.getCompositeLinerPropertyName(2), 'Liner 3')
    assert(comp.getCompositeLinerPropertyName(3), 'Liner 5')
    assert(comp.getCompositeLinerPropertyName(4), 'Liner 1')

test1()
test2()
test3()
test4()
test5()
test6()


model.save()
pass