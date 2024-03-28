from rs2.interpreter.RS2Interpreter import RS2Interpreter
import os, inspect

def OutputJointResult(singleJointResult):
    jointID = singleJointResult.entity_id
    print(f"\t\tJoint Unique ID = {jointID}")
    joint_element_results = singleJointResult.joint_element_results
    print("\t\tJoint Element Results:\n")
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
        print(f"\t\tStart X-Coord = {start_x}, Start Y-Coord = {start_y}, End X-Coord = {end_x}, End Y-Coord = {end_y}")
        print(f"\t\tDistance = {distance}, Normal Stress = {normal_stress}, Shear Stress = {shear_stress}, Confining Stress = {confining_stress}")
        print(f"\t\tNormal Displacement = {normal_displacement}, Shear Displacement = {shear_displacement}, Yielded = {yieldedStatus}\n")

def OutputLinerResult(singleLinerResult):
    linerID = singleLinerResult.entity_id
    print(f"\t\tLiner Unique ID = {linerID}")
    liner_element_results = singleLinerResult.liner_element_results
    print("\t\tLiner Element Results:\n")
    for linerResult in liner_element_results:
        composite_layer = linerResult.composite_layer
        node_start = linerResult.node_start
        node_end = linerResult.node_end
        start_x = linerResult.start_x
        start_y = linerResult.start_y
        end_x = linerResult.end_x
        end_y = linerResult.end_y
        distance = linerResult.distance
        axial_force = linerResult.axial_force
        moment1 = linerResult.moment1
        moment_mid = linerResult.moment_mid
        moment2 = linerResult.moment2
        shear_force = linerResult.shear_force
        displacement_total = linerResult.displacement_total
        displacemet_x = linerResult.displacement_x
        displacement_y = linerResult.displacement_y
        axi_sym_force = linerResult.axi_sym_force
        axi_sym_moment = linerResult.axi_sym_moment
        beam_yield = linerResult.beam_yield
        temperature = linerResult.temperature
        print(f"\t\tComposite Layer = {composite_layer}, Node Start = {node_start}, Node End = {node_end}")
        print(f"\t\tStart X-Coord = {start_x}, Start Y-Coord = {start_y}, End X-Coord = {end_x}, End Y-Coord = {end_y}")
        print(f"\t\tDistance = {distance}, Axial Force = {axial_force}, Moment 1 = {moment1}")
        print(f"\t\tMoment-Mid = {moment_mid}, Moment 2 = {moment2}, Shear Force = {shear_force}")
        print(f"\t\tDisplacement Total = {displacement_total}, Displacement X = {displacemet_x}, Displacement Y = {displacement_y}")
        print(f"\t\tAxial Symmetry Force = {axi_sym_force}, Axial Symmetry Moment = {axi_sym_moment}")
        print(f"\t\tBeam Yield = {beam_yield}, Temperature = {temperature}\n")

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
interpreter = RS2Interpreter()
model = interpreter.openFile(rf"{current_dir}\example_models\SupportResults.fez")

stages = [1, 2]

results = model.GetCompositeResults(stages)

for stageNum, allCompositeResults in results.items():
    print(f"Stage {stageNum} Composite Results\n")
    for singleCompositeResult in allCompositeResults:
        compositeID = singleCompositeResult.entity_id
        print(f"\Composite Unique ID = {compositeID}")

        joint_result = singleCompositeResult.joint_result
        print(f"\tJoint Result for Composite with ID {compositeID}:\n")
        OutputJointResult(joint_result)

        liner_result = singleCompositeResult.liner_result
        print(f"\tLiner Result for Composite with ID {compositeID}:\n")
        OutputLinerResult(liner_result)
        
model.close()