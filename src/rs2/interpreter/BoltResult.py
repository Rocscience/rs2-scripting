from enum import Enum

class BoltElementYieldStatus(Enum):
    BOLT_ELEMENT_NOT_YIELDED = 0
    BOLT_ELEMENT_TYPE_UNKNOWN_YIELDED  = 1
    BOLT_ELEMENT_TENSION_YIELDED = 2
    BOLT_ELEMENT_SHEAR_YIELDED  = 3
    BOLT_ELEMENT_TENSIONANDSHEAR_YIELDED = 4
    BOLT_ELEMENT_UNDEFINED_YIELDED = -1
  
class BoltYieldingResult:
    def __init__(self, start_x, start_y, end_x, end_y, yielding_flag):
        self.start_x = start_x #0
        self.start_y = start_y #1
        self.end_x = end_x #2
        self.end_y = end_y #3
        self.yielding_flag = yielding_flag #4

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
