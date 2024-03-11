from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.modeler.properties.PropertyEnums import *
from rs2.interpreter.InterpreterEnums import *
from rs2.interpreter.MeshResults import MeshResults
from rs2.interpreter.HistoryQueryResults import *
from rs2.interpreter.TimeQueryResults import *
from rs2.interpreter.InterpreterGraphEnums import *
from rs2.interpreter.JointResult import *
from rs2.interpreter.LinerResult import *
from rs2.interpreter.BoltResult import*
from rs2.interpreter.CompositeResult import*
from rs2.interpreter.MaterialQueryResults import *
import csv

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_InterpretStructuralInterfaceAxisymmetric.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Interpret\interpretStructuralInterfaceAxisymmetric_python.fez'
# CSV to write data
csvFile = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Interpret\interpretStructuralInterfaceAxisymmetric.csv'

modeler = RS2Modeler()
interpreter = RS2Interpreter()

model = modeler.openFile(base_model)

model.saveAs(final_python_model)

def extractLinerElementResults(linerElements: list[LinerElementResult]):
    # Extracts individual values (stress, displacement, etc.) from a list of linerElementResults
    # Returns a list of lists, where each internal list contains all extracted values for a particular liner element
    allElementResults = []
    for x in range(len(linerElements)):
        element = linerElements[x]
        elementResults = []
        elementResults.append(element.node_start)
        elementResults.append(element.node_end)
        elementResults.append(element.start_x)
        elementResults.append(element.start_y)
        elementResults.append(element.end_x)
        elementResults.append(element.end_y)
        elementResults.append(element.distance)
        elementResults.append(element.axial_force)
        elementResults.append(element.moment1)
        elementResults.append(element.moment_mid)
        elementResults.append(element.moment2)
        elementResults.append(element.shear_force)
        elementResults.append(element.displacement_total)
        elementResults.append(element.displacement_x)
        elementResults.append(element.displacement_y)
        elementResults.append(element.axi_sym_force)
        elementResults.append(element.axi_sym_moment)
        elementResults.append(element.beam_yield)
        elementResults.append(element.temperature)

        allElementResults.append(elementResults)
    return allElementResults


def extractJointElementResults(jointElements: list[JointElementResult]):
    # Extracts individual values (stress, displacement, etc.) from a list of jointElementResults
    # Returns a list of lists, where each internal list contains all extracted values for a particular joint element
    allElementResults = []
    for x in range(len(jointElements)):
        element = jointElements[x]
        elementResults = []
        elementResults.append(element.start_x)
        elementResults.append(element.start_y)
        elementResults.append(element.end_x)
        elementResults.append(element.end_y)
        elementResults.append(element.distance)
        elementResults.append(element.normal_stress)
        elementResults.append(element.shear_stress)
        elementResults.append(element.confining_stress)
        elementResults.append(element.normal_displacement)
        elementResults.append(element.shear_displacement)
        elementResults.append(element.yielded)

        allElementResults.append(elementResults)
    return allElementResults


def test1():

    model.compute()
    model.save()

    interpretModel = interpreter.openFile(final_python_model)

    allStructResults = interpretModel.GetStructuralResults([1,2,3,4])
    extractedStructResults = []
    for stage in range (1,5):
        structResultList = allStructResults[stage]

        for i in range(len(structResultList)):
            struct = structResultList[i]

            structLinerResult = struct.liner_result
            structLinerElementResult = structLinerResult.liner_element_results
            structJointResult = struct.joint_result
            structJointElementResult = structJointResult.joint_element_results
            extractedStructResults.append(extractLinerElementResults(structLinerElementResult))
            extractedStructResults.append(extractJointElementResults(structJointElementResult))

    print(extractedStructResults)

    struct1LinerStage2 = allStructResults[2][0].liner_result
    struct1JointStage2 = allStructResults[2][0].joint_result
    struct2LinerStage2 = allStructResults[2][1].liner_result
    struct2JointStage2 = allStructResults[2][1].joint_result
    struct1LinerStage3 = allStructResults[3][0].liner_result
    struct1JointStage3 = allStructResults[3][0].joint_result
    struct2LinerStage3 = allStructResults[3][1].liner_result
    struct2JointStage3 = allStructResults[3][1].joint_result

    assert(len(allStructResults[1]) == 0) # Assert structural interfaces do not exist at stage 1 (Not installed yet)

    assert(extractLinerElementResults(struct1LinerStage2.liner_element_results)[0][7] != extractLinerElementResults(struct1LinerStage3.liner_element_results)[0][7]) # Assert liner axial force change Struct 1
    assert(extractLinerElementResults(struct2LinerStage2.liner_element_results)[0][7] != extractLinerElementResults(struct2LinerStage3.liner_element_results)[0][7]) # Assert liner axial force change Struct 2

    assert(extractLinerElementResults(struct1LinerStage2.liner_element_results)[0][18] != extractLinerElementResults(struct1LinerStage3.liner_element_results)[0][18]) # Assert liner temperature change Struct 1
    assert(extractLinerElementResults(struct2LinerStage2.liner_element_results)[0][18] != extractLinerElementResults(struct2LinerStage3.liner_element_results)[0][18]) # Assert liner temperature change Struct 2

    assert(extractJointElementResults(struct1JointStage2.joint_element_results)[0][6] != extractJointElementResults(struct1JointStage3.joint_element_results)[0][6]) # Assert joint 1 shear stress change Struct 1
    assert(extractJointElementResults(struct1JointStage2.joint_element_results)[1][6] != extractJointElementResults(struct1JointStage3.joint_element_results)[1][6]) # Assert joint 2 shear stress change Struct 1
    assert(extractJointElementResults(struct2JointStage2.joint_element_results)[0][6] != extractJointElementResults(struct2JointStage3.joint_element_results)[0][6]) # Assert joint 1 shear stress change Struct 2
    assert(extractJointElementResults(struct2JointStage2.joint_element_results)[1][6] != extractJointElementResults(struct2JointStage3.joint_element_results)[1][6]) # Assert joint 2 shear stress change Struct 2

    assert(len(allStructResults[4]) != 0) # Assert that structural interfaces exist at stage 4 (Structural Interfaces cannot be removed)

    # Write results to CSV
    with open(csvFile, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(extractedStructResults)


test1()

model.save()

pass