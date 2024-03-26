from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.modeler.properties.PropertyEnums import *
from rs2.interpreter.InterpreterEnums import *
from rs2.interpreter.QueryResults.MeshResults import MeshResults
from rs2.interpreter.QueryResults.HistoryQueryResults import *
from rs2.interpreter.QueryResults.TimeQueryResults import *
from rs2.interpreter.InterpreterGraphEnums import *
from rs2.interpreter.SupportResults.JointResult import *
from rs2.interpreter.SupportResults.LinerResult import *
from rs2.interpreter.SupportResults.BoltResult import*
from rs2.interpreter.SupportResults.CompositeResult import*
from rs2.interpreter.QueryResults.MaterialQueryResults import *
import csv

# vanila untouched
base_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\BaseModel_InterpretLiner6Noded.fez'
#unit test result
final_python_model = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Interpret\interpretLiner6Noded_python.fez'
# CSV to write data
csvFile = r'S:\Students\2024-1 Jan-Apr\Zachary\scriptingModels\Interpret\interpretLiner6Noded.csv'

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



def test1():

    model.compute()
    model.save()

    interpretModel = interpreter.openFile(final_python_model)

    linerResultsList = interpretModel.GetLinerResults([1,2,3,4])
    extractedLinerResults = []

    for stage in range (1,5):
        linerResult = linerResultsList[stage]

        if len(linerResult) != 0: # Screen to make sure liner exists at given stage
            linerElementResults = linerResult[0].liner_element_results
            extractedLinerResults.append(extractLinerElementResults(linerElementResults))
        else:
            extractedLinerResults.append([[0]*18]*3)

    assert(len(linerResultsList[1]) == 0)
    linerStage2 = linerResultsList[2]
    linerStage3 = linerResultsList[3]
    assert(extractLinerElementResults(linerStage2[0].liner_element_results)[0][7] != extractLinerElementResults(linerStage3[0].liner_element_results)[0][7]) # Assert axial force change
    assert(extractLinerElementResults(linerStage2[0].liner_element_results)[0][18] != extractLinerElementResults(linerStage3[0].liner_element_results)[0][18]) # Assert temperature change
    assert(len(linerResultsList[4]) == 0)

    # Write results to CSV
    with open(csvFile, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(extractedLinerResults)


test1()

model.save()

pass