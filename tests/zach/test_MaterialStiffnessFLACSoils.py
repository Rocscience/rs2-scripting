from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_Stiffness.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\stiffnessFLACSoils_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\stiffnessFLACSoils_python.fez'

modeler = RS2Modeler()

model = modeler.openFile(base_model)

model.saveAs(final_python_model)

matList = model.getAllMaterialProperties()
mat1 = matList[0]
mat2 = matList[1]
mat3 = matList[2]

def test1():
    mat = mat1

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.CHSOIL)

    mat.Stiffness.ChSoil.setGRef(1.1)
    mat.Stiffness.ChSoil.setNG(1.2)
    mat.Stiffness.ChSoil.setKRef(1.3)
    mat.Stiffness.ChSoil.setMK(1.4)
    mat.Stiffness.ChSoil.setReferencePressure(1.5)

    assert(mat.Stiffness.ChSoil.getGRef(), 1.1)
    assert(mat.Stiffness.ChSoil.getNG(), 1.2)
    assert(mat.Stiffness.ChSoil.getKRef(), 1.3)
    assert(mat.Stiffness.ChSoil.getMK(), 1.4)
    assert(mat.Stiffness.ChSoil.getReferencePressure(), 1.5)

def test2():
    mat = mat2

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.CYSOIL)

    mat.Stiffness.CySoil.setKRefiso(1.1)
    mat.Stiffness.CySoil.setMK(1.2)
    mat.Stiffness.CySoil.setRK(1.3)
    mat.Stiffness.CySoil.setReferencePressure(1.4)
    mat.Stiffness.CySoil.setPoissonsRatio(0.05)

    assert(mat.Stiffness.CySoil.getKRefiso(), 1.1)
    assert(mat.Stiffness.CySoil.getMK(), 1.2)
    assert(mat.Stiffness.CySoil.getRK(), 1.3)
    assert(mat.Stiffness.CySoil.getReferencePressure(), 1.4)
    assert(mat.Stiffness.CySoil.getPoissonsRatio(), 0.05)

def test3():
    mat = mat3

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.DOUBLE_YIELD)

    mat.Stiffness.DoubleYield.setKRefiso(1.1)
    mat.Stiffness.DoubleYield.setMK(1.2)
    mat.Stiffness.DoubleYield.setRK(1.3)
    mat.Stiffness.DoubleYield.setReferencePressure(1.4)
    mat.Stiffness.DoubleYield.setPoissonsRatio(0.05)

    assert(mat.Stiffness.DoubleYield.getKRefiso(), 1.1)
    assert(mat.Stiffness.DoubleYield.getMK(), 1.2)
    assert(mat.Stiffness.DoubleYield.getRK(), 1.3)
    assert(mat.Stiffness.DoubleYield.getReferencePressure(), 1.4)
    assert(mat.Stiffness.DoubleYield.getPoissonsRatio(), 0.05)

test1()
test2()
test3()


model.save()

pass