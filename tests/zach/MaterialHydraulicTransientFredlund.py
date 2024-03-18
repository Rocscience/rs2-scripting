from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_HydraulicTransient.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\hydraulicTransientFredlundXing_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\hydraulicTransientFredlundXing_python.fez'

modeler = RS2Modeler()

model = modeler.openFile(base_model)

model.saveAs(final_python_model)

matList = model.getAllMaterialProperties()
mat1 = matList[0]
mat2 = matList[1]
mat3 = matList[2]
mat4 = matList[3]
mat5 = matList[4]
mat6 = matList[5]
mat7 = matList[6] 
mat8 = matList[7]
mat9 = matList[8]
mat10 = matList[9]
mat11 = matList[10]

def test1():
    mat = mat1

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_FREDLUND)
    mat.Hydraulic.setMaterialBehaviour(MaterialBehaviours.DRAINED)
    mat.Hydraulic.setFluidBulkModulus(1.1)
    # Set Biot's Coefficient missing

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_FREDLUND)
    assert(mat.Hydraulic.getMaterialBehaviour(), MaterialBehaviours.DRAINED) 
    assert(mat.Hydraulic.getFluidBulkModulus(), 1.1)
    # Get Biot's Coefficient missing

def test2():
    mat = mat2

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_FREDLUND)
    mat.Hydraulic.setMaterialBehaviour(MaterialBehaviours.UNDRAINED)
    mat.Hydraulic.setFluidBulkModulus(1.1)
    # Set Biot's Coefficient missing

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_FREDLUND)
    assert(mat.Hydraulic.getMaterialBehaviour(), MaterialBehaviours.UNDRAINED) 
    assert(mat.Hydraulic.getFluidBulkModulus(), 1.1)
    # Get Biot's Coefficient missing

def test3():
    mat = mat3

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_FREDLUND)
    mat.Hydraulic.FEAGroundwater.Fredlund.setKs(1.1)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.2)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    mat.Hydraulic.FEAGroundwater.setK1Angle(1.3)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCInputType(WCInputType.WC_INPUT_WC)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCSat(0.4)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCRes(0.5)
    mat.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_CONSTANT)
    mat.Hydraulic.FEAGroundwater.setMv(1.6)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_FREDLUND)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getKs(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.2)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    assert(mat.Hydraulic.FEAGroundwater.getK1Angle(), 1.3)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCInputType(), WCInputType.WC_INPUT_WC)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCSat(), 0.4)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCRes(), 0.5)
    assert(mat.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_CONSTANT)
    assert(mat.Hydraulic.FEAGroundwater.getMv(), 1.6)

def test4():
    mat = mat4

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_FREDLUND)
    mat.Hydraulic.FEAGroundwater.Fredlund.setKs(1.1)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.2)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_SURFACE)
    mat.Hydraulic.FEAGroundwater.setK1SurfaceToUseByName('Anisotropic Surface 4')
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCInputType(WCInputType.WC_INPUT_WC)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCSat(0.4)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCRes(0.5)
    mat.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_CONSTANT)
    mat.Hydraulic.FEAGroundwater.setMv(1.6)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_FREDLUND)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getKs(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.2)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_SURFACE)
    assert(mat.Hydraulic.FEAGroundwater.getK1SurfaceToUse(), 'Anistropic Surface 4')
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCInputType(), WCInputType.WC_INPUT_WC)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCSat(), 0.4)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCRes(), 0.5)
    assert(mat.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_CONSTANT)
    assert(mat.Hydraulic.FEAGroundwater.getMv(), 1.6)

def test5():
    mat = mat5

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_FREDLUND)
    mat.Hydraulic.FEAGroundwater.Fredlund.setKs(1.1)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.2)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_SURFACE)
    mat.Hydraulic.FEAGroundwater.setK1SurfaceToUseByName('Anisotropic Surface 7')
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCInputType(WCInputType.WC_INPUT_WC)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCSat(0.4)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCRes(0.5)
    mat.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_CONSTANT)
    mat.Hydraulic.FEAGroundwater.setMv(1.6)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_FREDLUND)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getKs(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.2)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_SURFACE)
    assert(mat.Hydraulic.FEAGroundwater.getK1SurfaceToUse(), 'Anistropic Surface 7')
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCInputType(), WCInputType.WC_INPUT_WC)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCSat(), 0.4)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCRes(), 0.5)
    assert(mat.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_CONSTANT)
    assert(mat.Hydraulic.FEAGroundwater.getMv(), 1.6)


def test6():
    mat = mat6

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_FREDLUND)
    mat.Hydraulic.FEAGroundwater.Fredlund.setKs(1.1)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.2)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    mat.Hydraulic.FEAGroundwater.setK1Angle(1.3)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCInputType(WCInputType.WC_INPUT_DOS)
    mat.Hydraulic.FEAGroundwater.Fredlund.setDoSSat(0.4)
    mat.Hydraulic.FEAGroundwater.Fredlund.setDoSRes(0.5)
    mat.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_CONSTANT)
    mat.Hydraulic.FEAGroundwater.setMv(1.6)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_FREDLUND)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getKs(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.2)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    assert(mat.Hydraulic.FEAGroundwater.getK1Angle(), 1.3)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCInputType(), WCInputType.WC_INPUT_DOS)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getDoSSat(), 0.4)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getDoSRes(), 0.5)
    assert(mat.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_CONSTANT)
    assert(mat.Hydraulic.FEAGroundwater.getMv(), 1.6)

def test7():
    mat = mat7

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_FREDLUND)
    mat.Hydraulic.FEAGroundwater.Fredlund.setKs(1.1)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.2)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    mat.Hydraulic.FEAGroundwater.setK1Angle(1.3)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCInputType(WCInputType.WC_INPUT_WC)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCSat(0.4)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCRes(0.5)
    mat.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_NONE)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_FREDLUND)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getKs(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.2)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    assert(mat.Hydraulic.FEAGroundwater.getK1Angle(), 1.3)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCInputType(), WCInputType.WC_INPUT_WC)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCSat(), 0.4)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCRes(), 0.5)
    assert(mat.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_NONE)

def test8():
    mat = mat8

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_FREDLUND)
    mat.Hydraulic.FEAGroundwater.Fredlund.setKs(1.1)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.2)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    mat.Hydraulic.FEAGroundwater.setK1Angle(1.3)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCInputType(WCInputType.WC_INPUT_WC)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCSat(0.4)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCRes(0.5)
    mat.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_FLUID)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_FREDLUND)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getKs(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.2)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    assert(mat.Hydraulic.FEAGroundwater.getK1Angle(), 1.3)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCInputType(), WCInputType.WC_INPUT_WC)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCSat(), 0.4)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCRes(), 0.5)
    assert(mat.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_FLUID)

def test9():
    mat = mat9

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_FREDLUND)
    mat.Hydraulic.FEAGroundwater.Fredlund.setKs(1.1)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.2)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    mat.Hydraulic.FEAGroundwater.setK1Angle(1.3)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCInputType(WCInputType.WC_INPUT_WC)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCSat(0.4)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCRes(0.5)
    mat.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_1D_ELASTIC)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_FREDLUND)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getKs(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.2)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    assert(mat.Hydraulic.FEAGroundwater.getK1Angle(), 1.3)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCInputType(), WCInputType.WC_INPUT_WC)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCSat(), 0.4)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCRes(), 0.5)
    assert(mat.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_1D_ELASTIC)

def test10():
    mat = mat10

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_FREDLUND)
    mat.Hydraulic.FEAGroundwater.Fredlund.setKs(1.1)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.2)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    mat.Hydraulic.FEAGroundwater.setK1Angle(1.3)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCInputType(WCInputType.WC_INPUT_WC)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCSat(0.4)
    mat.Hydraulic.FEAGroundwater.Fredlund.setWCRes(0.5)
    mat.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_2D_ELASTIC)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_FREDLUND)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getKs(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.2)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    assert(mat.Hydraulic.FEAGroundwater.getK1Angle(), 1.3)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCInputType(), WCInputType.WC_INPUT_WC)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCSat(), 0.4)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getWCRes(), 0.5)
    assert(mat.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_2D_ELASTIC)

def test11():
    mat = mat11

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_FREDLUND)
    mat.Hydraulic.FEAGroundwater.Fredlund.setA(1.1)
    mat.Hydraulic.FEAGroundwater.Fredlund.setB(1.2)
    mat.Hydraulic.FEAGroundwater.Fredlund.setC(1.3)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_FREDLUND)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getA(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getB(), 1.2)
    assert(mat.Hydraulic.FEAGroundwater.Fredlund.getC(), 1.3)


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