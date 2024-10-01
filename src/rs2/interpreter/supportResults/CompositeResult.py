from rs2.interpreter.supportResults.LinerResult import LinerResult
from rs2.interpreter.supportResults.JointResult import JointResult

class PileResult:
    """
    Attributes:
        entity_id (str): Unique Identifier for support pile.
        joint_result (list[JointResult]): List of all joint results for support pile.
        liner_result (list[LinerResult]): List of all liner results for support pile.
        
    Examples:
    
		:ref:`Support Pile Results Example`
	"""
    def __init__(self, entity_id, joint_result: list[JointResult], liner_result: list[LinerResult]):
        self.entity_id = entity_id
        self.joint_result: list[JointResult] = joint_result
        self.liner_result: list[LinerResult] = liner_result

class CompositeResult:
    """
    Attributes:
        entity_id (str): Unique Identifier for support composite.
        joint_result (list[JointResult]): List of all joint results for support composite.
        liner_result (list[LinerResult]): List of all liner results for support composite.
	
    Examples:
    
		:ref:`Support Composite Results Example`
	"""
    def __init__(self, entity_id, joint_result: list[JointResult], liner_result: list[LinerResult]):
        self.entity_id = entity_id
        self.joint_result: list[JointResult] = joint_result
        self.liner_result: list[LinerResult] = liner_result

class StructuralResult:
    """
    Attributes:
        entity_id (str): Unique Identifier for support structural.
        joint_result (list[JointResult]): List of all joint results for support structural.
        liner_result (list[LinerResult]): List of all liner results for support structural.
    
    Examples:
    
		:ref:`Support Structural Results Example`
        
	"""
    def __init__(self, entity_id, joint_result: list[JointResult], liner_result: list[LinerResult]):
        self.entity_id = entity_id
        self.joint_result: list[JointResult] = joint_result
        self.liner_result: list[LinerResult] = liner_result




