from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_HydraulicTransient.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\hydraulicTransientSimple_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\hydraulicTransientSimple_python.fez'

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
mat12 = matList[11]
mat13 = matList[12]
mat14 = matList[13]
mat15 = matList[14]

def test1():
    mat = mat1

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat.Hydraulic.setMaterialBehaviour(MaterialBehaviours.DRAINED)
    mat.Hydraulic.setFluidBulkModulus(1.1)
    # Set Biot's Coefficient missing

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)
    assert(mat.Hydraulic.getMaterialBehaviour(), MaterialBehaviours.DRAINED) 
    assert(mat.Hydraulic.getFluidBulkModulus(), 1.1)
    # Get Biot's Coefficient missing

def test2():
    mat = mat2

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat.Hydraulic.setMaterialBehaviour(MaterialBehaviours.UNDRAINED)
    mat.Hydraulic.setFluidBulkModulus(1.1)
    # Set Biot's Coefficient missing

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)
    assert(mat.Hydraulic.getMaterialBehaviour(), MaterialBehaviours.UNDRAINED) 
    assert(mat.Hydraulic.getFluidBulkModulus(), 1.1)
    # Get Biot's Coefficient missing

def test3():
    mat = mat3

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat.Hydraulic.FEAGroundwater.Simple.setKs(1.1)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.2)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    mat.Hydraulic.FEAGroundwater.setK1Angle(1.3)
    mat.Hydraulic.FEAGroundwater.Simple.setWCInputType(WCInputType.WC_INPUT_WC)
    mat.Hydraulic.FEAGroundwater.Simple.setWCSat(0.4)
    mat.Hydraulic.FEAGroundwater.Simple.setWCRes(0.5)
    mat.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_CONSTANT)
    mat.Hydraulic.FEAGroundwater.setMv(1.6)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getKs(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.2)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    assert(mat.Hydraulic.FEAGroundwater.getK1Angle(), 1.3)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCInputType(), WCInputType.WC_INPUT_WC)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCSat(), 0.4)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCRes(), 0.5)
    assert(mat.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_CONSTANT)
    assert(mat.Hydraulic.FEAGroundwater.getMv(), 1.6)

def test4():
    mat = mat4

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat.Hydraulic.FEAGroundwater.Simple.setKs(1.1)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.2)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_SURFACE)
    mat.Hydraulic.FEAGroundwater.setK1SurfaceToUseByName('Anisotropic Surface 4')
    mat.Hydraulic.FEAGroundwater.Simple.setWCInputType(WCInputType.WC_INPUT_WC)
    mat.Hydraulic.FEAGroundwater.Simple.setWCSat(0.4)
    mat.Hydraulic.FEAGroundwater.Simple.setWCRes(0.5)
    mat.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_CONSTANT)
    mat.Hydraulic.FEAGroundwater.setMv(1.6)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getKs(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.2)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_SURFACE)
    assert(mat.Hydraulic.FEAGroundwater.getK1SurfaceToUse(), 'Anistropic Surface 4')
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCInputType(), WCInputType.WC_INPUT_WC)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCSat(), 0.4)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCRes(), 0.5)
    assert(mat.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_CONSTANT)
    assert(mat.Hydraulic.FEAGroundwater.getMv(), 1.6)

def test5():
    mat = mat5

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat.Hydraulic.FEAGroundwater.Simple.setKs(1.1)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.2)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_SURFACE)
    mat.Hydraulic.FEAGroundwater.setK1SurfaceToUseByName('Anisotropic Surface 7')
    mat.Hydraulic.FEAGroundwater.Simple.setWCInputType(WCInputType.WC_INPUT_WC)
    mat.Hydraulic.FEAGroundwater.Simple.setWCSat(0.4)
    mat.Hydraulic.FEAGroundwater.Simple.setWCRes(0.5)
    mat.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_CONSTANT)
    mat.Hydraulic.FEAGroundwater.setMv(1.6)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getKs(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.2)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_SURFACE)
    assert(mat.Hydraulic.FEAGroundwater.getK1SurfaceToUse(), 'Anistropic Surface 7')
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCInputType(), WCInputType.WC_INPUT_WC)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCSat(), 0.4)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCRes(), 0.5)
    assert(mat.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_CONSTANT)
    assert(mat.Hydraulic.FEAGroundwater.getMv(), 1.6)


def test6():
    mat = mat6

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat.Hydraulic.FEAGroundwater.Simple.setKs(1.1)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.2)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    mat.Hydraulic.FEAGroundwater.setK1Angle(1.3)
    mat.Hydraulic.FEAGroundwater.Simple.setWCInputType(WCInputType.WC_INPUT_DOS)
    mat.Hydraulic.FEAGroundwater.Simple.setDoSSat(0.4)
    mat.Hydraulic.FEAGroundwater.Simple.setDoSRes(0.5)
    mat.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_CONSTANT)
    mat.Hydraulic.FEAGroundwater.setMv(1.6)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getKs(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.2)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    assert(mat.Hydraulic.FEAGroundwater.getK1Angle(), 1.3)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCInputType(), WCInputType.WC_INPUT_DOS)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getDoSSat(), 0.4)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getDoSRes(), 0.5)
    assert(mat.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_CONSTANT)
    assert(mat.Hydraulic.FEAGroundwater.getMv(), 1.6)

def test7():
    mat = mat7

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat.Hydraulic.FEAGroundwater.Simple.setKs(1.1)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.2)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    mat.Hydraulic.FEAGroundwater.setK1Angle(1.3)
    mat.Hydraulic.FEAGroundwater.Simple.setWCInputType(WCInputType.WC_INPUT_WC)
    mat.Hydraulic.FEAGroundwater.Simple.setWCSat(0.4)
    mat.Hydraulic.FEAGroundwater.Simple.setWCRes(0.5)
    mat.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_NONE)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getKs(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.2)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    assert(mat.Hydraulic.FEAGroundwater.getK1Angle(), 1.3)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCInputType(), WCInputType.WC_INPUT_WC)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCSat(), 0.4)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCRes(), 0.5)
    assert(mat.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_NONE)

def test8():
    mat = mat8

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat.Hydraulic.FEAGroundwater.Simple.setKs(1.1)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.2)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    mat.Hydraulic.FEAGroundwater.setK1Angle(1.3)
    mat.Hydraulic.FEAGroundwater.Simple.setWCInputType(WCInputType.WC_INPUT_WC)
    mat.Hydraulic.FEAGroundwater.Simple.setWCSat(0.4)
    mat.Hydraulic.FEAGroundwater.Simple.setWCRes(0.5)
    mat.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_FLUID)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getKs(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.2)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    assert(mat.Hydraulic.FEAGroundwater.getK1Angle(), 1.3)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCInputType(), WCInputType.WC_INPUT_WC)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCSat(), 0.4)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCRes(), 0.5)
    assert(mat.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_FLUID)

def test9():
    mat = mat9

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat.Hydraulic.FEAGroundwater.Simple.setKs(1.1)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.2)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    mat.Hydraulic.FEAGroundwater.setK1Angle(1.3)
    mat.Hydraulic.FEAGroundwater.Simple.setWCInputType(WCInputType.WC_INPUT_WC)
    mat.Hydraulic.FEAGroundwater.Simple.setWCSat(0.4)
    mat.Hydraulic.FEAGroundwater.Simple.setWCRes(0.5)
    mat.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_1D_ELASTIC)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getKs(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.2)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    assert(mat.Hydraulic.FEAGroundwater.getK1Angle(), 1.3)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCInputType(), WCInputType.WC_INPUT_WC)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCSat(), 0.4)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCRes(), 0.5)
    assert(mat.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_1D_ELASTIC)

def test10():
    mat = mat10

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat.Hydraulic.FEAGroundwater.Simple.setKs(1.1)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.2)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    mat.Hydraulic.FEAGroundwater.setK1Angle(1.3)
    mat.Hydraulic.FEAGroundwater.Simple.setWCInputType(WCInputType.WC_INPUT_WC)
    mat.Hydraulic.FEAGroundwater.Simple.setWCSat(0.4)
    mat.Hydraulic.FEAGroundwater.Simple.setWCRes(0.5)
    mat.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_2D_ELASTIC)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getKs(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.2)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    assert(mat.Hydraulic.FEAGroundwater.getK1Angle(), 1.3)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCInputType(), WCInputType.WC_INPUT_WC)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCSat(), 0.4)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getWCRes(), 0.5)
    assert(mat.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_2D_ELASTIC)

def test11():
    mat = mat11

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat.Hydraulic.FEAGroundwater.Simple.setSoilType(EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_GENERAL)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getSoilType(), EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_GENERAL)

def test12():
    mat = mat12

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat.Hydraulic.FEAGroundwater.Simple.setSoilType(EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_SAND)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getSoilType(), EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_SAND)

def test13():
    mat = mat13

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat.Hydraulic.FEAGroundwater.Simple.setSoilType(EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_SILT)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getSoilType(), EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_SILT)

def test14():
    mat = mat14

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat.Hydraulic.FEAGroundwater.Simple.setSoilType(EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_CLAY)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getSoilType(), EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_CLAY)

def test15():
    mat = mat15

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_SIMPLE)
    mat.Hydraulic.FEAGroundwater.Simple.setSoilType(EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_LOAM)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_SIMPLE)
    assert(mat.Hydraulic.FEAGroundwater.Simple.getSoilType(), EnhancedSimpleSoilTypes.SL_ES_SOIL_TYPE_LOAM)

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

model.save()

pass