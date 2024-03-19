from rs2.interpreter.InterpreterEnums import *
from rs2.interpreter.InterpreterGraphEnums import *
from rs2.modeler.properties import *

from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.BoltResult import*

def print_object_attributes(obj, indent=0):
    # Get the dictionary of attributes for the object
    attributes = vars(obj)
    
    # Iterate over each attribute
    for attr_name, attr_value in attributes.items():
        if attr_value is None: #Don't print
            continue
        # Print the attribute name and its value
        if isinstance(attr_value, (int, float, str, Enum)):
            print(f"{' ' * indent}{attr_name}: {attr_value}")
        else:
            print(f"{' ' * indent}{attr_name}")

        # If the attribute is an instance of a class, recursively print its attributes
        if isinstance(attr_value, (list, tuple)):
            for item in attr_value:
                if isinstance(item, (int, float, str, Enum)):
                    print(f"{' ' * (indent + 2)}{item}")
                else:
                    print_object_attributes(item, indent + 2)
                print()
                print()

        elif isinstance(attr_value, (int, float, str, Enum)):
            continue
        else:
            print_object_attributes(attr_value, indent + 2)

def print_dict_elements(data_dict):
    for key, pile_results in data_dict.items():
        print(f"Key: {key}")
        for pile_result in pile_results:
            print_object_attributes(pile_result)


interpreter = RS2Interpreter()

interpreter_model = interpreter.openFile(r"C:\scriptingModels\joint.fez")
interpreter_model2 = interpreter.openFile(r"C:\scriptingModels\supportStructuralResults.fez")

stages = [1]


pile_results = interpreter_model.GetPileResults( stages)
print_dict_elements(pile_results)

# composite_results = interpreter_model.GetCompositeResults( stages)
# print_dict_elements(composite_results)

# structural_results = interpreter_model2.GetStructuralResults( stages)
# print_dict_elements(structural_results)

# liner_results = interpreter_model.GetLinerResults(stages)
# print_dict_elements(liner_results)

# joint_results = interpreter_model.GetJointResults(stages)
# print_dict_elements(joint_results)

# results = interpreter_model.GetBoltResults( stages)
# #print_dict_elements(bolt_results)
# for stageNum, allBoltResults in results.items():
    # print(f"Stage {stageNum} Bolt Results")
    # for singleBoltResult in allBoltResults:
    #     boltID = singleBoltResult.entity_id
    #     start_x = singleBoltResult.start_x
    #     start_y = singleBoltResult.start_y
    #     end_x = singleBoltResult.end_x
    #     end_y = singleBoltResult.end_y
    #     print(f"\tBolt Unique ID = {boltID}, \n\tStart X-Coord = {start_x}, \n\tStart Y-Coord = {start_y}, End X-Coord = {end_x}, End Y-Coord = {end_y}")
    #     yieldingResults = singleBoltResult.yielding_results
    #     print("\tBolt Yielding Results:")
    #     for boltYieldData in yieldingResults:
    #         start_x = boltYieldData.start_x
    #         start_y = boltYieldData.start_y
    #         end_x = boltYieldData.end_x
    #         end_y = boltYieldData.end_y
    #         yieldingStatus = boltYieldData.yielding_flag
    #         print(f"\t\tYielded Start X-Coord = {start_x}, Yielded Start Y-Coord = {start_y}, Yielded End X-Coord = {end_x}, Yielded End Y-Coord = {end_y}")
    #         print(f"\t\tYielded Status = {yieldingStatus}")
    #     print("\tForce Displacement Results:")
    #     forceDisplacementResults = singleBoltResult.force_displacement_results
    #     for dispResult in forceDisplacementResults:
    #         loc_x = dispResult.location_x
    #         loc_y = dispResult.location_y
    #         dist = dispResult.distance
    #         axial_force = dispResult.axial_force
    #         axial_stress = dispResult.axial_stress
    #         shear_force = dispResult.shear_force
    #         rock_disp = dispResult.rock_displacement
    #         bolt_disp = dispResult.bolt_displacement
    #         print(f"\t\tLocation X = {loc_x}, Location Y = {loc_y}, Distance = {dist}, Axial Force = {axial_force}, Axial Stress = {axial_stress}")
    #         print(f"\t\tShear Force = {shear_force}, Rock Displacement = {rock_disp}, Bolt Displacement = {bolt_disp}\n")