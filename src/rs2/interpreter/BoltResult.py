from enum import Enum
from rs2.interpreter.UtilityResult import *

class BoltElementYieldStatus(Enum):
    BOLT_ELEMENT_NOT_YIELDED = 0
    BOLT_ELEMENT_TYPE_UNKNOWN_YIELDED  = 1
    BOLT_ELEMENT_TENSION_YIELDED = 2
    BOLT_ELEMENT_SHEAR_YIELDED  = 4
    BOLT_ELEMENT_TENSIONANDSHEAR_YIELDED = BOLT_ELEMENT_TENSION_YIELDED + BOLT_ELEMENT_SHEAR_YIELDED
    BOLT_ELEMENT_UNDEFINED_YIELDED = -1
  
class BoltYieldingResult:
    def __init__(self, start_x, start_y, end_x, end_y, yielding_flag):
        self.start_x = start_x #0
        self.start_y = start_y #1
        self.end_x = end_x #2
        self.end_y = end_y #3
        self.yielding_flag = BoltElementYieldStatus(yielding_flag) #4
        ResetInvalid.validate(self)


class BoltForceDisplacementResult:
    def __init__(self, location_x, location_y, distance, axial_force, axial_stress, shear_force, rock_displacement, bolt_displacement):
        self.location_x = location_x #0
        self.location_y = location_y #1
        self.distance = distance #2
        self.axial_force = axial_force #3
        self.axial_stress = axial_stress #4
        self.shear_force = shear_force #5
        self.rock_displacement = rock_displacement #6
        self.bolt_displacement = bolt_displacement #7
        ResetInvalid.validate(self)

class BoltResult:
    def __init__(self, entity_id, entity_data, yielding_results: BoltYieldingResult, force_displacement_results: BoltForceDisplacementResult):
        if len(entity_data) == 0 or len(entity_data[0]) == 0:
            assert False, 'location not defined'
            return
        location_tensor = entity_data[0][0]
        start_x, start_y, end_x, end_y = location_tensor

        self.entity_id = entity_id
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.yielding_results: BoltYieldingResult = yielding_results
        self.force_displacement_results: BoltForceDisplacementResult = force_displacement_results

