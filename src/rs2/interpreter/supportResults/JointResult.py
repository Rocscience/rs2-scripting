from rs2.interpreter._UtilityResult import *

class JointElementResult:
    """
    Attributes:
        start_x (double): Start X-Coordinate for support joint.
        start_y (double): Start Y-Coordinate for support joint.
        end_x (double): End X-Coordinate for support joint.
        end_y (double): End Y-Coordinate for support joint.
        distance (double): Distance of support joint.
        normal_stress (double): Normal Stress for support joint.
        shear_stress (double): Shear Stress for support joint.
        confining_stress (double): Confining Stress for support joint.
        normal_displacement (double): Normal Displacement for support joint.
        shear_displacement (double): Shear Displacement for support joint.
        yielded (bool): Boolean representing yielded status for support joint.
    
    Examples:
        :ref:`Support Joint Results Example`
	"""
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
    """
    Attributes:
        entity_id (str): Unique Identifier for support joint.
        joint_element_results (list[JointElementResult]): List of all joint element result for support joint.
    
	
    Examples:
        :ref:`Support Joint Results Example`	
    """
    def __init__(self, entity_id, joint_element_results: list[JointElementResult]):
        self.entity_id = entity_id
        self.joint_element_results: list[JointElementResult] = joint_element_results




