from rs2.interpreter.RS2Interpreter import RS2Interpreter
import os, inspect

RS2Interpreter.startApplication(port=60088)
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(lambda: None))) 
interpreter = RS2Interpreter(port=60088)
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
            axial_force1 = linerResult.axial_force1
            axial_force_mid = linerResult.axial_force_mid
            axial_force2 = linerResult.axial_force2
            moment1 = linerResult.moment1
            moment_mid = linerResult.moment_mid
            moment2 = linerResult.moment2
            shear_force1 = linerResult.shear_force1
            shear_force_mid = linerResult.shear_force_mid
            shear_force2 = linerResult.shear_force2
            displacement_total1 = linerResult.displacement_total1
            displacement_total_mid = linerResult.displacement_total_mid
            displacement_total2 = linerResult.displacement_total2
            displacement_x1 = linerResult.displacement_x1
            displacement_x_mid = linerResult.displacement_x_mid
            displacement_x2 = linerResult.displacement_x2
            displacement_y1 = linerResult.displacement_y1
            displacement_y_mid = linerResult.displacement_y_mid
            displacement_y2 = linerResult.displacement_y2
            axi_sym_force1 = linerResult.axi_sym_force1
            axi_sym_force_mid = linerResult.axi_sym_force_mid
            axi_sym_force2 = linerResult.axi_sym_force2
            axi_sym_moment1 = linerResult.axi_sym_moment1
            axi_sym_moment_mid = linerResult.axi_sym_moment_mid
            axi_sym_moment2 = linerResult.axi_sym_moment2
            beam_yield = linerResult.beam_yield
            temperature1 = linerResult.temperature1
            temperature_mid = linerResult.temperature_mid
            temperature2 = linerResult.temperature2
            print(f"\tComposite Layer = {composite_layer}, Node Start = {node_start}, Node End = {node_end}")
            print(f"\tStart X-Coord = {start_x}, Start Y-Coord = {start_y}, End X-Coord = {end_x}, End Y-Coord = {end_y}")
            print(f"\tDistance = {distance}, Axial Force 1 = {axial_force1}, Axial Force-Mid = {axial_force_mid}")
            print(f"\tAxial Force 2 = {axial_force2}, Moment 1 = {moment1}, Moment-Mid = {moment_mid}")
            print(f"\tMoment 2 = {moment2}, Shear Force = {shear_force1}, Shear Force-Mid = {shear_force_mid}")
            print(f"\tShear Force 2 = {shear_force2}, Displacement Total 1 = {displacement_total1}, Displacement Total - Mid = {displacement_total_mid}")
            print(f"\tDisplacement Total 2 = {displacement_total2}, Displacement X 1 = {displacement_x1}, Displacement X-Mid = {displacement_x_mid}")
            print(f"\tDisplacement X2 = {displacement_x2}, Displacement Y1 = {displacement_y1}, Displacement Y-Mid = {displacement_y_mid}")
            print(f"\tDisplacement Y2 = {displacement_y2}, Axial Symmetry Force 1 = {axi_sym_force1}, Axial Symmetry Force-Mid = {axi_sym_force_mid}")
            print(f"\tAxial Symmetry Force2 = {axi_sym_force2}, Axial Symmetry Moment 1 = {axi_sym_moment1}, Axial Symmetry Moment-Mid = {axi_sym_moment_mid}")
            print(f"\tAxial Symmetry Moment2 = {axi_sym_moment2}, Beam Yield = {beam_yield}, Temperature 1 = {temperature1}")
            print(f"\tTemperature-Mid = {temperature_mid}, Temperature 2 = {temperature2}\n")

model.close()

interpreter.closeProgram()