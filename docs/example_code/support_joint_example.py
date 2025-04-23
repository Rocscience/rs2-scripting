from rs2.interpreter.RS2Interpreter import RS2Interpreter
import os, inspect

RS2Interpreter.startApplication(port=60087)
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
interpreter = RS2Interpreter(port=60087)
model = interpreter.openFile(rf"{current_dir}\example_models\SupportResults.fez")

stages = [1, 2]

results = model.GetJointResults(stages)

for stageNum, allJointResults in results.items():
    print(f"Stage {stageNum} Joint Results\n")
    for singleJointResult in allJointResults:
        jointID = singleJointResult.entity_id
        print(f"\tJoint Unique ID = {jointID}")
        joint_element_results = singleJointResult.joint_element_results
        print("\tJoint Element Results:\n")
        for jointResult in joint_element_results:
            start_x = jointResult.start_x
            start_y = jointResult.start_y
            end_x = jointResult.end_x
            end_y = jointResult.end_y
            distance = jointResult.distance
            normal_stress = jointResult.normal_stress
            shear_stress = jointResult.shear_stress
            confining_stress = jointResult.confining_stress
            normal_displacement = jointResult.normal_displacement
            shear_displacement = jointResult.shear_displacement
            yieldedStatus = jointResult.yielded
            print(f"\tStart X-Coord = {start_x}, Start Y-Coord = {start_y}, End X-Coord = {end_x}, End Y-Coord = {end_y}")
            print(f"\tDistance = {distance}, Normal Stress = {normal_stress}, Shear Stress = {shear_stress}, Confining Stress = {confining_stress}")
            print(f"\tNormal Displacement = {normal_displacement}, Shear Displacement = {shear_displacement}, Yielded = {yieldedStatus}\n")

model.close()

interpreter.closeProgram()