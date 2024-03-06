from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

modeler = RS2Modeler()

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_Composite.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Composite\compositeInstallRemove_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Composite\compositeInstallRemove_python.fez'

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

    comp.setInstallDelay(2,0)
    comp.setInstallDelay(3,1)
    comp.setInstallDelay(4,2)

    comp.setRemovedStage(1,-1)
    comp.setRemovedStage(2,1)
    comp.setRemovedStage(3,2)
    comp.setRemovedStage(4,3)

    assert(comp.getInstallDelay(2),0)
    assert(comp.getInstallDelay(3),1)
    assert(comp.getInstallDelay(4),2)

    assert(comp.getRemovedStage(1),-1)
    assert(comp.getRemovedStage(2),1)
    assert(comp.getRemovedStage(3),2)
    assert(comp.getRemovedStage(4),3)

def test2():
    comp = comp2

    comp.setNumberOfLayers(4)

    comp.setInstallDelay(2,1)
    comp.setInstallDelay(3,2)
    comp.setInstallDelay(4,3)

    comp.setRemovedStage(1,1)
    comp.setRemovedStage(2,2)
    comp.setRemovedStage(3,3)
    comp.setRemovedStage(4,4)

    assert(comp.getInstallDelay(2),1)
    assert(comp.getInstallDelay(3),2)
    assert(comp.getInstallDelay(4),3)

    assert(comp.getRemovedStage(1),1)
    assert(comp.getRemovedStage(2),2)
    assert(comp.getRemovedStage(3),3)
    assert(comp.getRemovedStage(4),4)

def test3(): 
    comp = comp3

    comp.setNumberOfLayers(4)

    comp.setInstallDelay(2,2) 
    comp.setInstallDelay(3,3)
    comp.setInstallDelay(4,4)

    comp.setRemovedStage(1,2)
    comp.setRemovedStage(2,3)
    comp.setRemovedStage(3,4)
    comp.setRemovedStage(4,5)

    assert(comp.getInstallDelay(2),2)
    assert(comp.getInstallDelay(3),3)
    assert(comp.getInstallDelay(4),4)

    assert(comp.getRemovedStage(1),2)
    assert(comp.getRemovedStage(2),3)
    assert(comp.getRemovedStage(3),4)
    assert(comp.getRemovedStage(4),5)



def test4(): 
    comp = comp4

    comp.setNumberOfLayers(4)

    comp.setInstallDelay(2,3)
    comp.setInstallDelay(3,4)
    comp.setInstallDelay(4,5)

    comp.setRemovedStage(1,3)
    comp.setRemovedStage(2,4)
    comp.setRemovedStage(3,5)
    comp.setRemovedStage(4,-1)

    assert(comp.getInstallDelay(2),3)
    assert(comp.getInstallDelay(3),4)
    assert(comp.getInstallDelay(4),5)

    assert(comp.getRemovedStage(1),3)
    assert(comp.getRemovedStage(2),4)
    assert(comp.getRemovedStage(3),5)
    assert(comp.getRemovedStage(4),-1)



def test5(): 
    comp = comp5

    comp.setNumberOfLayers(4)

    comp.setInstallDelay(2,4)
    comp.setInstallDelay(3,5)
    comp.setInstallDelay(4,0)

    comp.setRemovedStage(1,4)
    comp.setRemovedStage(2,5)
    comp.setRemovedStage(3,-1)
    comp.setRemovedStage(4,1)

    assert(comp.getInstallDelay(2),4)
    assert(comp.getInstallDelay(3),5)
    assert(comp.getInstallDelay(4),0)

    assert(comp.getRemovedStage(1),4)
    assert(comp.getRemovedStage(2),5)
    assert(comp.getRemovedStage(3),-1)
    assert(comp.getRemovedStage(4),1)



def test6(): 
    comp = comp6

    comp.setNumberOfLayers(4)

    comp.setInstallDelay(2,5)
    comp.setInstallDelay(3,0)
    comp.setInstallDelay(4,1)

    comp.setRemovedStage(1,5)
    comp.setRemovedStage(2,-1)
    comp.setRemovedStage(3,1)
    comp.setRemovedStage(4,2)

    assert(comp.getInstallDelay(2),5)
    assert(comp.getInstallDelay(3),0)
    assert(comp.getInstallDelay(4),1)

    assert(comp.getRemovedStage(1),5)
    assert(comp.getRemovedStage(2),-1)
    assert(comp.getRemovedStage(3),1)
    assert(comp.getRemovedStage(4),2)


test1()
test2()
test3()
test4()
test5()
test6()


model.save()
pass