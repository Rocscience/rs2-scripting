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

def test1():
    count = 0
    placementTypeList = [CompositeJointPlacementTypes.BETWEEN_SOIL_ROCK_AND_FIRST_LINER, CompositeJointPlacementTypes.BETWEEN_FIRST_AND_SECOND_LINER, CompositeJointPlacementTypes.BETWEEN_SECOND_AND_THIRD_LINER, CompositeJointPlacementTypes.BETWEEN_THIRD_AND_FOURTH_LINER]
    layerList = [1,2,3,4]
    for x in range(4):
        placementType = placementTypeList[x]

        for y in layerList:
            comp = compList[count]

            comp.setNumberOfLayers(y)
            comp.setJointApplied(True)
            comp.setJointPlacement(placementType)

            assert(comp.getNumberOfLayers(),y)
            assert(comp.getJointApplied(),True)
            assert(comp.getJointPlacement(),placementType)
            count+=1

        layerList.pop(0)
      
test1()

model.save()
pass