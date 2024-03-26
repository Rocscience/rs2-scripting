from rs2.interpreter.InterpreterEnums import *
from rs2.interpreter.InterpreterGraphEnums import *
from rs2.modeler.properties import *

from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.supportResults.BoltResult import*

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

composite_results = interpreter_model.GetCompositeResults( stages)
print_dict_elements(composite_results)

structural_results = interpreter_model2.GetStructuralResults( stages)
print_dict_elements(structural_results)

liner_results = interpreter_model.GetLinerResults(stages)
print_dict_elements(liner_results)

joint_results = interpreter_model.GetJointResults(stages)
print_dict_elements(joint_results)

bolt_results = interpreter_model.GetBoltResults( stages)
print_dict_elements(bolt_results)

pass