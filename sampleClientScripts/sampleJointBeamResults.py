from rs2.interpreter.InterpreterEnums import *
from rs2.interpreter.InterpreterGraphEnums import *
from rs2.modeler.properties import *

from rs2.interpreter.RS2Interpreter import RS2Interpreter
from rs2.interpreter.BoltResult import*

interpreter = RS2Interpreter()

interpreter_model = interpreter.openFile("C:\scriptingModels\joint.fez")


def print_data_attributes(input_data):
    for data in input_data:
        print()
        for attr, value in vars(data).items():
            print(f"{attr}: {value}")

joint_results = interpreter_model.GetJointResults( stages=[1, 2,3])
beam_results = interpreter_model.GetBeamResults( stages=[1, 2])
bolt_yielding_results = interpreter_model.GetBoltYieldingResults( stages=[1, 2])
bolt_force_displacement_results = interpreter_model.GetBoltForceDisplacementResults( stages=[1, 2])




stage_number = 1

joint_results_stage_1 = joint_results[stage_number]
beam_results_stage_1 = beam_results[stage_number]
bolt_yielding_results_1 = bolt_yielding_results[stage_number]
bolt_force_displacement_results_1 = bolt_force_displacement_results[stage_number]

print_data_attributes(joint_results_stage_1)
print_data_attributes(beam_results_stage_1)
print_data_attributes(bolt_yielding_results_1)
print_data_attributes(bolt_force_displacement_results_1)

a = BoltElementYieldStatus.BOLT_ELEMENT_NOT_YIELDED
if (a == bolt_yielding_results_1[0].yielding_flag):
    print('same')
pass