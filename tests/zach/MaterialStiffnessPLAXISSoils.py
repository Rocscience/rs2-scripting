from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_Stiffness.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\stiffnessPLAXISSoils_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\stiffnessPLAXISSoils_python.fez'

modeler = RS2Modeler()

model = modeler.openFile(base_model)

model.saveAs(final_python_model)

matList = model.getAllMaterialProperties()
mat1 = matList[0]
mat2 = matList[1]
mat3 = matList[2]
mat4 = matList[3]
mat5 = matList[4]

def test1():
    mat = mat1

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.HARDENING_SOIL)

    #Eref values were chosen because they were the ones that were accepted by RS2
    mat.Stiffness.HardeningSoil.setERef50(4000.1)
    mat.Stiffness.HardeningSoil.setERefoed(4000.2)
    mat.Stiffness.HardeningSoil.setERefur(12000.3)
    mat.Stiffness.HardeningSoil.setM(1.4)
    mat.Stiffness.HardeningSoil.setReferencePressure(1.5)
    mat.Stiffness.HardeningSoil.setPoissonsRatio(0.06)
    mat.Stiffness.HardeningSoil.setPlimit(1.7)

    assert(mat.Stiffness.HardeningSoil.getERef50(), 4000.1)
    assert(mat.Stiffness.HardeningSoil.getERefoed(), 4000.2)
    assert(mat.Stiffness.HardeningSoil.getERefur(), 12000.3)
    assert(mat.Stiffness.HardeningSoil.getM(), 1.4)
    assert(mat.Stiffness.HardeningSoil.getReferencePressure(), 1.5)
    assert(mat.Stiffness.HardeningSoil.getPoissonsRatio(), 0.06)
    assert(mat.Stiffness.HardeningSoil.getPlimit(), 1.7)

def test2():
    mat = mat2

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.HARDENING_SOIL_SMALL_STRAIN_STIFFNESS)

    mat.Stiffness.HardeningSoilSmallStrainStiffness.setERef50(4000.1)
    mat.Stiffness.HardeningSoilSmallStrainStiffness.setERefoed(4000.2)
    mat.Stiffness.HardeningSoilSmallStrainStiffness.setERefur(12000.3)
    mat.Stiffness.HardeningSoilSmallStrainStiffness.setM(1.4)
    mat.Stiffness.HardeningSoilSmallStrainStiffness.setReferencePressure(1.5)
    mat.Stiffness.HardeningSoilSmallStrainStiffness.setPoissonsRatio(0.06)
    mat.Stiffness.HardeningSoilSmallStrainStiffness.setPlimit(1.7)
    mat.Stiffness.HardeningSoilSmallStrainStiffness.setG0ref(1.8)
    mat.Stiffness.HardeningSoilSmallStrainStiffness.setGama07(1.9)

    assert(mat.Stiffness.HardeningSoilSmallStrainStiffness.getERef50(), 4000.1)
    assert(mat.Stiffness.HardeningSoilSmallStrainStiffness.getERefoed(), 4000.2)
    assert(mat.Stiffness.HardeningSoilSmallStrainStiffness.getERefur(), 12000.3)
    assert(mat.Stiffness.HardeningSoilSmallStrainStiffness.getM(), 1.4)
    assert(mat.Stiffness.HardeningSoilSmallStrainStiffness.getReferencePressure(), 1.5)
    assert(mat.Stiffness.HardeningSoilSmallStrainStiffness.getPoissonsRatio(), 0.06)
    assert(mat.Stiffness.HardeningSoilSmallStrainStiffness.getPlimit(), 1.7)
    assert(mat.Stiffness.HardeningSoilSmallStrainStiffness.getG0ref(), 1.8)
    assert(mat.Stiffness.HardeningSoilSmallStrainStiffness.getGama07(), 1.9)

def test3():
    mat = mat3

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.SOFT_SOIL)

    mat.Stiffness.SoftSoil.setPoissonsRatio(0.06)
    mat.Stiffness.SoftSoil.setPlimit(1.7)

    assert(mat.Stiffness.SoftSoil.getPoissonsRatio(), 0.06)
    assert(mat.Stiffness.SoftSoil.getPlimit(), 1.7)

def test4():
    mat = mat4

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.SOFT_SOIL_CREEP)

    mat.Stiffness.SoftSoilCreep.setPoissonsRatio(0.06)
    mat.Stiffness.SoftSoilCreep.setPlimit(1.7)

    assert(mat.Stiffness.SoftSoilCreep.getPoissonsRatio(), 0.06)
    assert(mat.Stiffness.SoftSoilCreep.getPlimit(), 1.7)

def test5():
    mat = mat5

    mat.Strength.setFailureCriterion(StrengthCriteriaTypes.SWELLING_ROCK)

    mat.Stiffness.SwellingRock.setAngleToBeddingPlanes(1.1)
    mat.Stiffness.SwellingRock.setElasticModulusTangentialToBeddingPlane(1.2)
    mat.Stiffness.SwellingRock.setElasticModulusNormalToBeddingPlanes(1.3)
    mat.Stiffness.SwellingRock.setPoissonsRatioOutOfBeddingPlanes(0.4)
    mat.Stiffness.SwellingRock.setPoissonsRatioWithinBeddingPlanes(0.05)
    mat.Stiffness.SwellingRock.setShearModulus(1.6)

    assert(mat.Stiffness.SwellingRock.getAngleToBeddingPlanes(), 1.1)
    assert(mat.Stiffness.SwellingRock.getElasticModulusTangentialToBeddingPlane(), 1.2)
    assert(mat.Stiffness.SwellingRock.getElasticModulusNormalToBeddingPlanes(), 1.3)
    assert(mat.Stiffness.SwellingRock.getPoissonsRatioOutOfBeddingPlanes(), 0.4)
    assert(mat.Stiffness.SwellingRock.getPoissonsRatioWithinBeddingPlanes(), 0.05)
    assert(mat.Stiffness.SwellingRock.getShearModulus(), 1.6)


test1()
test2()
test3()
test4()
test5()

model.save()

pass