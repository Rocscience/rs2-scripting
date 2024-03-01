from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_Composite.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Composite\compositeJointPlacement_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Composite\compositeJointPlacement_python.fez'

model = modeler.openFile(base_model)

model.saveAs(final_python_model)

compList = model.getAllCompositeLinerProperties()

comp1 = compList[0]
comp2 = compList[1]
comp3 = compList[2]
comp4 = compList[3]
comp5 = compList[4]
comp6 = compList[5]
comp7 = compList[6]
comp8 = compList[7]
comp9 = compList[8]
comp10 = compList[9]


def test1():
    comp = comp1

    comp.setNumberOfLayers(1)
    comp.setJointApplied(True)
    comp.setJointPlacement(CompositeJointPlacementTypes.BETWEEN_SOIL_ROCK_AND_FIRST_LINER)

    assert(comp.getNumberOfLayers(),1)
    assert(comp.getJointApplied(), True)
    assert(comp.getJointPlacement(), CompositeJointPlacementTypes.BETWEEN_SOIL_ROCK_AND_FIRST_LINER)

def test2():
    comp = comp2

    comp.setNumberOfLayers(2)
    comp.setJointApplied(True)
    comp.setJointPlacement(CompositeJointPlacementTypes.BETWEEN_SOIL_ROCK_AND_FIRST_LINER)

    assert(comp.getNumberOfLayers(),2)
    assert(comp.getJointApplied(), True)
    assert(comp.getJointPlacement(), CompositeJointPlacementTypes.BETWEEN_SOIL_ROCK_AND_FIRST_LINER)

def test3():
    comp = comp3

    comp.setNumberOfLayers(3)
    comp.setJointApplied(True)
    comp.setJointPlacement(CompositeJointPlacementTypes.BETWEEN_SOIL_ROCK_AND_FIRST_LINER)

    assert(comp.getNumberOfLayers(),3)
    assert(comp.getJointApplied(), True)
    assert(comp.getJointPlacement(), CompositeJointPlacementTypes.BETWEEN_SOIL_ROCK_AND_FIRST_LINER)

def test4():
    comp = comp4

    comp.setNumberOfLayers(4)
    comp.setJointApplied(True)
    comp.setJointPlacement(CompositeJointPlacementTypes.BETWEEN_SOIL_ROCK_AND_FIRST_LINER)

    assert(comp.getNumberOfLayers(),4)
    assert(comp.getJointApplied(), True)
    assert(comp.getJointPlacement(), CompositeJointPlacementTypes.BETWEEN_SOIL_ROCK_AND_FIRST_LINER)

def test5():
    comp = comp5

    comp.setNumberOfLayers(2)
    comp.setJointApplied(True)
    comp.setJointPlacement(CompositeJointPlacementTypes.BETWEEN_FIRST_AND_SECOND_LINER)

    assert(comp.getNumberOfLayers(),2)
    assert(comp.getJointApplied(), True)
    assert(comp.getJointPlacement(), CompositeJointPlacementTypes.BETWEEN_FIRST_AND_SECOND_LINER)

def test6():
    comp = comp6

    comp.setNumberOfLayers(3)
    comp.setJointApplied(True)
    comp.setJointPlacement(CompositeJointPlacementTypes.BETWEEN_FIRST_AND_SECOND_LINER)

    assert(comp.getNumberOfLayers(),3)
    assert(comp.getJointApplied(), True)
    assert(comp.getJointPlacement(), CompositeJointPlacementTypes.BETWEEN_FIRST_AND_SECOND_LINER)

def test7():
    comp = comp7

    comp.setNumberOfLayers(4)
    comp.setJointApplied(True)
    comp.setJointPlacement(CompositeJointPlacementTypes.BETWEEN_FIRST_AND_SECOND_LINER)

    assert(comp.getNumberOfLayers(),4)
    assert(comp.getJointApplied(), True)
    assert(comp.getJointPlacement(), CompositeJointPlacementTypes.BETWEEN_FIRST_AND_SECOND_LINER)

def test8():
    comp = comp8

    comp.setNumberOfLayers(3)
    comp.setJointApplied(True)
    comp.setJointPlacement(CompositeJointPlacementTypes.BETWEEN_SECOND_AND_THIRD_LINER)

    assert(comp.getNumberOfLayers(),3)
    assert(comp.getJointApplied(), True)
    assert(comp.getJointPlacement(), CompositeJointPlacementTypes.BETWEEN_SECOND_AND_THIRD_LINER)

def test9():
    comp = comp9

    comp.setNumberOfLayers(4)
    comp.setJointApplied(True)
    comp.setJointPlacement(CompositeJointPlacementTypes.BETWEEN_SECOND_AND_THIRD_LINER)

    assert(comp.getNumberOfLayers(),4)
    assert(comp.getJointApplied(), True)
    assert(comp.getJointPlacement(), CompositeJointPlacementTypes.BETWEEN_SECOND_AND_THIRD_LINER)

def test10():
    comp = comp10

    comp.setNumberOfLayers(4)
    comp.setJointApplied(True)
    comp.setJointPlacement(CompositeJointPlacementTypes.BETWEEN_THIRD_AND_FOURTH_LINER)

    assert(comp.getNumberOfLayers(),4)
    assert(comp.getJointApplied(), True)
    assert(comp.getJointPlacement(), CompositeJointPlacementTypes.BETWEEN_THIRD_AND_FOURTH_LINER)


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


model.save()
pass