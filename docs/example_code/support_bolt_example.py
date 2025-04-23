from rs2.interpreter.RS2Interpreter import RS2Interpreter
import os, inspect

RS2Interpreter.startApplication(port=60085)
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
interpreter = RS2Interpreter(port=60085)
model = interpreter.openFile(rf"{current_dir}\example_models\SupportResults.fez")

stages = [1, 2]

results = model.GetBoltResults(stages)

for stageNum, allBoltResults in results.items():
    print(f"Stage {stageNum} Bolt Results")
    for singleBoltResult in allBoltResults:
        boltID = singleBoltResult.entity_id
        start_x = singleBoltResult.start_x
        start_y = singleBoltResult.start_y
        end_x = singleBoltResult.end_x
        end_y = singleBoltResult.end_y
        print(f"\tBolt Unique ID = {boltID}, \n\tStart X-Coord = {start_x}, \n\tStart Y-Coord = {start_y}, End X-Coord = {end_x}, End Y-Coord = {end_y}")
        yieldingResults = singleBoltResult.yielding_results
        print("\tBolt Yielding Results:")
        for boltYieldData in yieldingResults:
            start_x = boltYieldData.start_x
            start_y = boltYieldData.start_y
            end_x = boltYieldData.end_x
            end_y = boltYieldData.end_y
            yieldingStatus = boltYieldData.yielding_flag
            print(f"\t\tYielded Start X-Coord = {start_x}, Yielded Start Y-Coord = {start_y}, Yielded End X-Coord = {end_x}, Yielded End Y-Coord = {end_y}")
            print(f"\t\tYielded Status = {yieldingStatus}")
        print("\tForce Displacement Results:")
        forceDisplacementResults = singleBoltResult.force_displacement_results
        for dispResult in forceDisplacementResults:
            loc_x = dispResult.location_x
            loc_y = dispResult.location_y
            dist = dispResult.distance
            axial_force = dispResult.axial_force
            axial_stress = dispResult.axial_stress
            shear_force = dispResult.shear_force
            rock_disp = dispResult.rock_displacement
            bolt_disp = dispResult.bolt_displacement
            print(f"\t\tLocation X = {loc_x}, Location Y = {loc_y}, Distance = {dist}, Axial Force = {axial_force}, Axial Stress = {axial_stress}")
            print(f"\t\tShear Force = {shear_force}, Rock Displacement = {rock_disp}, Bolt Displacement = {bolt_disp}\n")

model.close()

interpreter.closeProgram()