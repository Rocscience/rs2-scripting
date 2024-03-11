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
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_InterpretPileExcavatedAutoRemoveOff.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Interpret\interpretPileExcavatedAutoRemoveOff_python.fez'
# CSV to write data
csvFile = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Interpret\interpretPileExcavatedAutoRemoveOff.csv'

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

    allPileResults = interpretModel.GetPileResults([1,2,3,4])
    extractedPileResults = []
    for stage in range (1,5):
        pileResultList = allPileResults[stage]

        for i in range(len(pileResultList)):
            pile = pileResultList[i]

            pileLinerResult = pile.liner_result
            pileLinerElementResult = pileLinerResult.liner_element_results
            pileJointResult = pile.joint_result
            pileJointElementResult = pileJointResult.joint_element_results
            extractedPileResults.append(extractLinerElementResults(pileLinerElementResult))
            extractedPileResults.append(extractJointElementResults(pileJointElementResult))

    print(extractedPileResults)

    pile1LinerStage1 = allPileResults[1][0].liner_result
    pile1JointStage1 = allPileResults[1][0].joint_result
    pile2LinerStage1 = allPileResults[1][1].liner_result
    pile2JointStage1 = allPileResults[1][1].joint_result
    pile1LinerStage2 = allPileResults[2][0].liner_result
    pile1JointStage2 = allPileResults[2][0].joint_result
    pile2LinerStage2 = allPileResults[2][1].liner_result
    pile2JointStage2 = allPileResults[2][1].joint_result
    pile1LinerStage3 = allPileResults[3][0].liner_result
    pile1JointStage3 = allPileResults[3][0].joint_result
    pile2LinerStage3 = allPileResults[3][1].liner_result
    pile2JointStage3 = allPileResults[3][1].joint_result
    pile1LinerStage4 = allPileResults[4][0].liner_result
    pile1JointStage4 = allPileResults[4][0].joint_result
    pile2LinerStage4 = allPileResults[4][1].liner_result
    pile2JointStage4 = allPileResults[4][1].joint_result

    assert(len(pile1LinerStage1.liner_element_results) == 0) # Assert pile 1 liner does not exist at stage 1
    assert(len(pile2LinerStage1.liner_element_results) == 0) # Assert pile 2 liner does not exist at stage 1

    assert(extractJointElementResults(pile1JointStage1.joint_element_results)[0][7] == None) # Assert pile 1 joint confining stress is none at stage 1 (joint does not exist)
    assert(extractJointElementResults(pile2JointStage1.joint_element_results)[0][7] == None) # Assert pile 2 joint confining stress is none at stage 1 (joint does not exist)

    assert(extractLinerElementResults(pile1LinerStage2.liner_element_results)[0][7] == 0) # Assert pile 1 liner axial force is 0 at stage 2 (liner exists but no forces act on it)
    assert(extractLinerElementResults(pile1LinerStage2.liner_element_results)[0][7] == 0) # Assert pile 2 liner axial force is 0 at stage 2 (liner exists but no forces act on it)

    assert(extractJointElementResults(pile1JointStage2.joint_element_results)[0][7] == None) # Assert pile 1 joint confining stress is none at stage 2 (joint removed when excavated)
    assert(extractJointElementResults(pile2JointStage2.joint_element_results)[0][7] == None) # Assert pile 2 joint confining stress is none at stage 2 (joint removed when excavated)
    
    assert(extractLinerElementResults(pile1LinerStage3.liner_element_results)[0][7] == 0) # Assert pile 1 liner axial force is 0 at stage 3 (liner exists but no forces act on it)
    assert(extractLinerElementResults(pile1LinerStage3.liner_element_results)[0][7] == 0) # Assert pile 2 liner axial force is 0 at stage 3 (liner exists but no forces act on it)

    assert(extractJointElementResults(pile1JointStage3.joint_element_results)[0][7] == None) # Assert pile 1 joint confining stress is none at stage 3 (joint removed when excavated)
    assert(extractJointElementResults(pile2JointStage3.joint_element_results)[0][7] == None) # Assert pile 2 joint confining stress is none at stage 3 (joint removed when excavated)

    assert(len(pile1LinerStage4.liner_element_results) == 0) # Assert pile 1 liner does not exist at stage 4
    assert(len(pile2LinerStage4.liner_element_results) == 0) # Assert pile 2 liner does not exist at stage 4

    assert(extractJointElementResults(pile1JointStage4.joint_element_results)[0][7] == None) # Assert pile 1 joint confining stress is none at stage 4 (joint does not exist)
    assert(extractJointElementResults(pile2JointStage4.joint_element_results)[0][7] == None) # Assert pile 2 joint confining stress is none at stage 4 (joint does not exist)


    # Write results to CSV
    with open(csvFile, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(extractedPileResults)


test1()

model.save()

pass