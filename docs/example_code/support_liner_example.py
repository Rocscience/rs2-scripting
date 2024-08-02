from rs2.interpreter.RS2Interpreter import RS2Interpreter
import os, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
interpreter = RS2Interpreter()
model = interpreter.openFile(rf"{current_dir}\example_models\SupportResults.fez")

stages = [1, 2]

results = model.GetLinerResults(stages)

for stageNum, allLinerResults in results.items():
    print(f"Stage {stageNum} Liner Results\n")
    for singleLinerResult in allLinerResults:
        linerID = singleLinerResult.entity_id
        print(f"\tLiner Unique ID = {linerID}")
        liner_element_results = singleLinerResult.liner_element_results
        print("\tLiner Element Results:\n")
        for linerResult in liner_element_results:
            composite_layer = linerResult.composite_layer
            node_start = linerResult.node_start
            node_end = linerResult.node_end
            start_x = linerResult.start_x
            start_y = linerResult.start_y
            end_x = linerResult.end_x
            end_y = linerResult.end_y
            distance = linerResult.distance
            axial_force = linerResult.axial_force1
            moment1 = linerResult.moment1
            moment_mid = linerResult.moment_mid
            moment2 = linerResult.moment2
            shear_force = linerResult.shear_force1
            displacement_total = linerResult.displacement_total1
            displacemet_x = linerResult.displacement_x1
            displacement_y = linerResult.displacement_y1
            axi_sym_force = linerResult.axi_sym_force1
            axi_sym_moment = linerResult.axi_sym_moment1
            beam_yield = linerResult.beam_yield
            temperature = linerResult.temperature1
            print(f"\tComposite Layer = {composite_layer}, Node Start = {node_start}, Node End = {node_end}")
            print(f"\tStart X-Coord = {start_x}, Start Y-Coord = {start_y}, End X-Coord = {end_x}, End Y-Coord = {end_y}")
            print(f"\tDistance = {distance}, Axial Force = {axial_force}, Moment 1 = {moment1}")
            print(f"\tMoment-Mid = {moment_mid}, Moment 2 = {moment2}, Shear Force = {shear_force}")
            print(f"\tDisplacement Total = {displacement_total}, Displacement X = {displacemet_x}, Displacement Y = {displacement_y}")
            print(f"\tAxial Symmetry Force = {axi_sym_force}, Axial Symmetry Moment = {axi_sym_moment}")
            print(f"\tBeam Yield = {beam_yield}, Temperature = {temperature}\n")

model.close()