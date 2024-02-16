from rs2.interpreter.UtilityResult import *

class JointElementResult:
    def __init__(self, start_x, start_y, end_x, end_y, distance, normal_stress, shear_stress,confining_stress, normal_displacement, shear_displacement, yielded):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.distance = distance
        self.normal_stress = normal_stress
        self.shear_stress = shear_stress
        self.confining_stress = confining_stress
        self.normal_displacement = normal_displacement
        self.shear_displacement = shear_displacement
        self.yielded = bool(yielded)
        ResetInvalid.validate(self)

class JointResult:
    def __init__(self, entity_id, joint_element_results):
        self.entity_id = entity_id
        self.joint_element_results = joint_element_results




