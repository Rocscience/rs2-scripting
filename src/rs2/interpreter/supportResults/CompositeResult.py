from rs2.interpreter.supportResults.LinerResult import LinerResult
from rs2.interpreter.supportResults.JointResult import JointResult

class PileResult:
    def __init__(self, entity_id, joint_result: JointResult, liner_result: LinerResult):
        self.entity_id = entity_id
        self.joint_result: JointResult = joint_result
        self.liner_result: LinerResult = liner_result

class CompositeResult:
    def __init__(self, entity_id, joint_result: JointResult, liner_result: LinerResult):
        self.entity_id = entity_id
        self.joint_result: JointResult = joint_result
        self.liner_result: LinerResult = liner_result

class StructuralResult:
    def __init__(self, entity_id, joint_result: JointResult, liner_result: LinerResult):
        self.entity_id = entity_id
        self.joint_result: JointResult = joint_result
        self.liner_result: LinerResult = liner_result




