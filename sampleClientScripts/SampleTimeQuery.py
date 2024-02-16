from rs2.modeler.RS2Modeler import RS2Modeler
from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.InterpreterGraphEnums import *

# Replace with a model with your desired model path
modelPath = r"C:\scriptingModels\Profiles_and_Boreholes_2.fez"
modeler = RS2Modeler()

model = modeler.openFile(modelPath)
points1 = [[6, -4], [6, 0]]
points2 = [[-4, 2], [10, 2]]
points_on_line = 10
guid1 = model.AddTimeQueryLine(points1, points_on_line)
guid2 = model.AddTimeQueryLine(points2, points_on_line)
print("Unique Identifer for Time Query Line = ", guid1)
model.RemoveTimeQueryLine([guid1])

id = model.AddTimeQueryPoint(5.5, 2.7)
id2 = model.AddTimeQueryPoint(10, -2)
print("ID of first point added = ", id)
model.RemoveTimeQueryPoint([id])

# Make sure to save and compute model before opening interpreter model and getting results
model.save()
model.compute()

# Get Time Query Point Results
interpreter = RS2Interpreter()
interpreter_model = interpreter.openFile(modelPath)
result = interpreter_model.GetAllTimeQueryPointResults(
    stages=[1, 2, 3, 4], 
    vertical_axis=TimeQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_XY)

for stageNumber, stageData in result.items():
    print(f"\nStage {stageNumber} Time Query Points Data")
    for time_query_point_data in stageData:
        uniqueIdentifier = time_query_point_data.GetUniqueIdentifier()
        all_node_values = time_query_point_data.GetAllValues()
        for node_val in all_node_values:
            x_coord = node_val.GetXCoordinate()
            y_coord = node_val.GetYCoordinate()
            stage_time = node_val.GetStageTime()
            value = node_val.GetValue()
            print(f"UniqueID = {uniqueIdentifier}, X-Coord = {x_coord}, Y-Coord = {y_coord}, Dynamic Stage Time = {stage_time}, Value = {value}\n")
        print("-----------------------")
    print(f"\nEnd of Stage {stageNumber} Data\n")

print("\n Time Query Line Results")
      
line_results = interpreter_model.GetAllTimeQueryLinesResults(
    stages=[1, 2, 3, 4], 
    vertical_axis=TimeQueryGraphEnums.VerticalAxisTypes.EFFECTIVE_STRESS_XY,
    apply_post_process_scaling=True
)

for stageNumber, stageData in line_results.items():
    print(f"\nStage {stageNumber} Time Query Line Data\n")
    for time_query_line_data in stageData:
        uniqueIdentifier = time_query_line_data.GetUniqueIdentifier()
        print(f"Unique Identifier for Line Query = {uniqueIdentifier} with data as follows:\n")
        all_node_obj = time_query_line_data.GetAllNodeObjects()
        for node_obj in all_node_obj:
            all_node_values = node_obj.GetNodeValues()
            for node_val in all_node_values:
                x_coord = node_val.GetXCoordinate()
                y_coord = node_val.GetYCoordinate()
                stage_time = node_val.GetStageTime()
                value = node_val.GetValue()
                print(f"X-Coord = {x_coord}, Y-Coord = {y_coord}, Dynamic Stage Time = {stage_time}, Value = {value}")
            print()
        print("\nEnd of Line Data\n")
    print("-----------------------")
    print(f"\nEnd of Stage {stageNumber} Data\n")