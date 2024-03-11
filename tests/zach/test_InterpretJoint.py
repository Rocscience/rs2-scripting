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
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_InterpretJoint.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Interpret\interpretJoint_python.fez'
# CSV to write data
csvFile = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Interpret\interpretJoint.csv'

modeler = RS2Modeler()
interpreter = RS2Interpreter()

model = modeler.openFile(base_model)

model.saveAs(final_python_model)

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

    allJointResults = interpretModel.GetJointResults([1,2,3,4])
    extractedJointResults = []
    for stage in range (1,5):
        jointResultList = allJointResults[stage]

        for i in range(len(jointResultList)):
            joint = jointResultList[i]

            jointElementResult = joint.joint_element_results
            extractedJointResults.append(extractJointElementResults(jointElementResult))

    print(extractedJointResults)

    joint1Stage1 = allJointResults[1][0]
    joint2Stage1 = allJointResults[1][1]
    joint1Stage2 = allJointResults[2][0]
    joint2Stage2 = allJointResults[2][1]
    joint1Stage3 = allJointResults[3][0]
    joint2Stage3 = allJointResults[3][1]
    joint1Stage4 = allJointResults[4][0]
    joint2Stage4 = allJointResults[4][1]


    assert(extractJointElementResults(joint1Stage1.joint_element_results)[0][6] == None) # Assert joint 1 shear stress is none at stage 1 (Joint not installed yet)
    assert(extractJointElementResults(joint2Stage1.joint_element_results)[0][6] == None) # Assert joint 2 shear stress is none at stage 1 (Joint not installed yet)

    assert(extractJointElementResults(joint1Stage2.joint_element_results)[0][6] != extractJointElementResults(joint1Stage3.joint_element_results)[0][6]) # Assert Joint 1 shear stress change
    assert(extractJointElementResults(joint2Stage2.joint_element_results)[0][6] != extractJointElementResults(joint2Stage3.joint_element_results)[0][6]) # Assert Joint 2 shear stress change

    assert(extractJointElementResults(joint1Stage4.joint_element_results)[0][6] != None) # Assert joint 1 shear stress exists (Joints cannot be removed)
    assert(extractJointElementResults(joint2Stage4.joint_element_results)[0][6] != None) # Assert joint 2 shear stress exists (Joints cannot be removed)

    # Write results to CSV
    with open(csvFile, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(extractedJointResults)


test1()

model.save()

pass