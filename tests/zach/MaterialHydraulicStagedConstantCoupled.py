from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_HydraulicStaged.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\hydraulicStagedConstantCoupled_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\hydraulicStagedConstantCoupled_python.fez'

modeler = RS2Modeler()

model = modeler.openFile(base_model)

model.saveAs(final_python_model)

matList = model.getAllMaterialProperties()
mat1 = matList[0]
mat2 = matList[1]

def test1():
    mat = mat1

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_CONSTANT)
    mat.Hydraulic.FEAGroundwater.Constant.setUseCV(False)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_CONSTANT)
    assert(mat.Hydraulic.FEAGroundwater.Constant.getUseCV(), False)


def test2():
    mat = mat2

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_CONSTANT)
    mat.Hydraulic.FEAGroundwater.Constant.setUseCV(True)
    mat.Hydraulic.FEAGroundwater.Constant.setCV(1.1)
    mat.Hydraulic.FEAGroundwater.Constant.setInitialK(1.2)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_CONSTANT)
    assert(mat.Hydraulic.FEAGroundwater.Constant.getUseCV(), True)
    assert(mat.Hydraulic.FEAGroundwater.Constant.getCV(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.Constant.getInitialK(), 1.2)

test1()
test2()

model.save()

pass