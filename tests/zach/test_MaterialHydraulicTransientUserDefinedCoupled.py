from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_HydraulicTransientCoupled.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\hydraulicTransientUserDefinedCoupled_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\hydraulicTransientUserDefinedCoupled_python.fez'

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

def test1():
    mat = mat1

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_USER_DEFINED)
    mat.Hydraulic.setMaterialBehaviour(MaterialBehaviours.DRAINED)
    mat.Hydraulic.setFluidBulkModulus(1.1)
    # Set Biot's Coefficient missing

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_USER_DEFINED)
    assert(mat.Hydraulic.getMaterialBehaviour(), MaterialBehaviours.DRAINED) 
    assert(mat.Hydraulic.getFluidBulkModulus(), 1.1)
    # Get Biot's Coefficient missing

def test2():
    mat = mat2

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_USER_DEFINED)
    mat.Hydraulic.setMaterialBehaviour(MaterialBehaviours.UNDRAINED)
    mat.Hydraulic.setFluidBulkModulus(1.1)
    # Set Biot's Coefficient missing

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_USER_DEFINED)
    assert(mat.Hydraulic.getMaterialBehaviour(), MaterialBehaviours.UNDRAINED) 
    assert(mat.Hydraulic.getFluidBulkModulus(), 1.1)
    # Get Biot's Coefficient missing

def test3():
    mat = mat3

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_USER_DEFINED)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.1)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    mat.Hydraulic.FEAGroundwater.setK1Angle(1.2)
    mat.Hydraulic.FEAGroundwater.UserDefined.setUserDefinedPermeabilityAndWaterContentFunction('User Defined 1')

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_USER_DEFINED)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)  
    assert(mat.Hydraulic.FEAGroundwater.getK1Angle(), 1.2)
    assert(mat.Hydraulic.FEAGroundwater.UserDefined.getUserDefinedPermeabilityAndWaterContentFunction(), 'User Defined 1')

def test4():
    mat = mat4

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_USER_DEFINED)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.1)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)
    mat.Hydraulic.FEAGroundwater.setK1Angle(1.2)
    mat.Hydraulic.FEAGroundwater.UserDefined.setUserDefinedPermeabilityAndWaterContentFunction('User Defined 3')

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_USER_DEFINED)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_ANGLE)  
    assert(mat.Hydraulic.FEAGroundwater.getK1Angle(), 1.2)
    assert(mat.Hydraulic.FEAGroundwater.UserDefined.getUserDefinedPermeabilityAndWaterContentFunction(), 'User Defined 3')

def test5():
    mat = mat9

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_USER_DEFINED)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.1)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_SURFACE)
    mat.Hydraulic.FEAGroundwater.setK1SurfaceToUseByName('Anisotropic Surface 4')
    mat.Hydraulic.FEAGroundwater.UserDefined.setUserDefinedPermeabilityAndWaterContentFunction('User Defined 1')
    mat.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_CONSTANT)
    mat.Hydraulic.FEAGroundwater.setMv(1.3)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_USER_DEFINED)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_SURFACE)  
    assert(mat.Hydraulic.FEAGroundwater.getK1SurfaceToUse(), 'Anistropic Surface 4')
    assert(mat.Hydraulic.FEAGroundwater.UserDefined.getUserDefinedPermeabilityAndWaterContentFunction(), 'User Defined 1')
    assert(mat.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_CONSTANT)
    assert(mat.Hydraulic.FEAGroundwater.getMv(), 1.3)

def test6():
    mat = mat10

    mat.Hydraulic.FEAGroundwater.setModel(GroundWaterModes.SL_WATER_MODE_USER_DEFINED)
    mat.Hydraulic.FEAGroundwater.setK2K1(1.1)
    mat.Hydraulic.FEAGroundwater.setK1Definition(AnisotropyDefinitions.ANISOTROPY_DEFINITION_SURFACE)
    mat.Hydraulic.FEAGroundwater.setK1SurfaceToUseByName('Anisotropic Surface 7')
    mat.Hydraulic.FEAGroundwater.UserDefined.setUserDefinedPermeabilityAndWaterContentFunction('User Defined 1')
    mat.Hydraulic.FEAGroundwater.setMvModel(MVModel.MV_CONSTANT)
    mat.Hydraulic.FEAGroundwater.setMv(1.3)

    assert(mat.Hydraulic.FEAGroundwater.getModel(), GroundWaterModes.SL_WATER_MODE_USER_DEFINED)
    assert(mat.Hydraulic.FEAGroundwater.getK2K1(), 1.1)
    assert(mat.Hydraulic.FEAGroundwater.getK1Definition(), AnisotropyDefinitions.ANISOTROPY_DEFINITION_SURFACE)  
    assert(mat.Hydraulic.FEAGroundwater.getK1SurfaceToUse(), 'Anistropic Surface 7')
    assert(mat.Hydraulic.FEAGroundwater.UserDefined.getUserDefinedPermeabilityAndWaterContentFunction(), 'User Defined 1')
    assert(mat.Hydraulic.FEAGroundwater.getMvModel(), MVModel.MV_CONSTANT)
    assert(mat.Hydraulic.FEAGroundwater.getMv(), 1.3)

test1()
test2()
test3()
test4()
test5()
test6()

model.save()

pass