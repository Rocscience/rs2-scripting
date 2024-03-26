from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.modeler.properties.PropertyEnums import *
from rs2.interpreter.InterpreterEnums import *
from rs2.interpreter.queryResults.MeshResults import MeshResults
from rs2.interpreter.queryResults.HistoryQueryResults import *
from rs2.interpreter.queryResults.TimeQueryResults import *
from rs2.interpreter.InterpreterGraphEnums import *
from rs2.interpreter.supportResults.JointResult import *
from rs2.interpreter.supportResults.LinerResult import *
from rs2.interpreter.supportResults.BoltResult import*
from rs2.interpreter.supportResults.CompositeResult import*
from rs2.interpreter.queryResults.MaterialQueryResults import *
import csv

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_InterpretCompositeNoJoint.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Interpret\interpretCompositeNoJoint_python.fez'
# CSV to write data
csvFile = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Interpret\interpretCompositeNoJoint.csv'

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

    allCompositeResults = interpretModel.GetCompositeResults([1,2,3,4])
    extractedCompositeResults = []
    for stage in range (1,5):
        compositeResultList = allCompositeResults[stage]

        for i in range(len(compositeResultList)):
            composite = compositeResultList[i]

            compositeLinerResult = composite.liner_result
            compositeLinerElementResult = compositeLinerResult.liner_element_results
            compositeJointResult = composite.joint_result
            compositeJointElementResult = compositeJointResult.joint_element_results
            extractedCompositeResults.append(extractLinerElementResults(compositeLinerElementResult))
            extractedCompositeResults.append(extractJointElementResults(compositeJointElementResult))

    print(extractedCompositeResults)

    compLinerStage2 = allCompositeResults[2][0].liner_result
    compJointStage2 = allCompositeResults[2][0].joint_result
    compLinerStage3 = allCompositeResults[3][0].liner_result
    compJointStage3 = allCompositeResults[3][0].joint_result

    assert(len(allCompositeResults[1]) == 0) # Assert composite does not exist in stage 1 (Not installed yet)

    assert(extractLinerElementResults(compLinerStage2.liner_element_results)[0][7] != extractLinerElementResults(compLinerStage3.liner_element_results)[0][7]) # Assert axial force change in the first element of each liner layer
    assert(extractLinerElementResults(compLinerStage2.liner_element_results)[2][7] != extractLinerElementResults(compLinerStage3.liner_element_results)[2][7])
    assert(extractLinerElementResults(compLinerStage2.liner_element_results)[4][7] != extractLinerElementResults(compLinerStage3.liner_element_results)[4][7])

    assert(extractLinerElementResults(compLinerStage2.liner_element_results)[0][7] == extractLinerElementResults(compLinerStage2.liner_element_results)[2][7]) # Assert that liner layers in the same stage are the same
    assert(extractLinerElementResults(compLinerStage2.liner_element_results)[2][7] == extractLinerElementResults(compLinerStage2.liner_element_results)[4][7])
    assert(extractLinerElementResults(compLinerStage3.liner_element_results)[0][7] == extractLinerElementResults(compLinerStage3.liner_element_results)[2][7])
    assert(extractLinerElementResults(compLinerStage3.liner_element_results)[2][7] == extractLinerElementResults(compLinerStage3.liner_element_results)[4][7])

    assert(len(allCompositeResults[4]) == 0) # Assert composite does not exist in stage 4 (Liner removed)


    # Write results to CSV
    with open(csvFile, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(extractedCompositeResults)


test1()

model.save()

pass