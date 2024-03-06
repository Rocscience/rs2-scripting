from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_Stiffness.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\stiffnessSofteningHardeningSoils_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\stiffnessSofteningHardeningSoils_python.fez'

modeler = RS2Modeler()

model = modeler.openFile(base_model)

model.saveAs(final_python_model)

matList = model.getAllMaterialProperties()
mat1 = matList[0]
mat2 = matList[1]
mat3 = matList[2]


def test1():
    mat = mat1

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.BARCELONA_BASIC)
    mat.Strength.BarcelonaBasic.setElasticParameters(ElasticParameters.CONSTANT_SHEAR_MODULUS)

    mat.Stiffness.Isotropic.setShearModulus(1.1)

    assert(mat.Stiffness.Isotropic.getShearModulus(), 1,1)

def test2():
    mat = mat2

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.BARCELONA_BASIC)
    mat.Strength.BarcelonaBasic.setElasticParameters(ElasticParameters.CONSTANT_POISSON_RATIO)

    mat.Stiffness.Isotropic.setPoissonsRatio(0.1)

    assert(mat.Stiffness.Isotropic.getPoissonsRatio(), 0,1)

def test3():
    mat = mat3

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.NORSAND)

    mat.Stiffness.Norsand.setShearModulusAtReferencePressure(1.1)
    mat.Stiffness.Norsand.setReferencePressureForShearModulus(1.2)
    mat.Stiffness.Norsand.setModulusExponent(0.3)
    mat.Stiffness.Norsand.setPoissonsRatio(0.4)
    mat.Stiffness.Norsand.setMinimumShearModulus(1.5)

    assert(mat.Stiffness.Norsand.getShearModulusAtReferencePressure(), 1.1)
    assert(mat.Stiffness.Norsand.getReferencePressureForShearModulus(), 1.2)
    assert(mat.Stiffness.Norsand.getModulusExponent(), 0.3)
    assert(mat.Stiffness.Norsand.getPoissonsRatio(), 0.4)
    assert(mat.Stiffness.Norsand.getMinimumShearModulus(), 1.5)

test1()
test2()
test3()

model.save()

pass