from xml.etree.ElementTree import TreeBuilder
from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.modeler.properties.PropertyEnums import *

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel.fez'
# modified by user via ui
final_ui_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\thermalExpansion_ui.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Material\thermalExpansion_python.fez'

modeler = RS2Modeler()

model = modeler.openFile(base_model)

model.saveAs(final_python_model)

matList = model.getAllMaterialProperties()
mat1 = matList[0]
mat2 = matList[1]

def test1():
    mat1.Thermal.setThermalExpansion(True)
    mat1.Thermal.setExpansionCoefficient(1.1)

    assert(mat1.Thermal.getThermalExpansion(), True)
    assert(mat1.Thermal.getExpansionCoefficient(), 1.1)

def test2():
    mat2.Thermal.setThermalExpansion(False)

    assert(mat2.Thermal.getThermalExpansion(), False)

test1()
test2()

model.save()

pass