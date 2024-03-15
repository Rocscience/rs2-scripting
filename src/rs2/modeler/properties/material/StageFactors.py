from rs2._common.ProxyObject import ProxyObject
from rs2._common.Client import Client
from rs2.modeler.properties.PropertyEnums import *

class StageFactors(ProxyObject):
	"""This interface is specifically for managing the table of stage factors (create, enable/disable, etc...)
	If you would like to modify specific stage factor values, you must get the stage factors through the stage factor interface present in the
	property's module.
	Ex:
	stageFactor = strength.HoekBrown.stageFactorInterface.getDefinedStageFactors()[1]
	stageFactor.setCompressiveStrengthFactor(2)
	"""
	ObjectReferenceId = int
	def __init__(self, client : Client, ID):
		super().__init__(client, ID)
	def setStageStrengthStiffnessStageFactors(self, value: bool):
		return self._callFunction("setApplyStrengthStiffnessStageFactors", [value])
	def getStageStrengthStiffnessStageFactors(self) -> bool:
		return self._callFunction("getApplyStrengthStiffnessStageFactors")
	def setStageThermalStageFactors(self, value: bool):
		return self._callFunction("setApplyThermalStageFactors", [value])
	def getStageThermalStageFactors(self) -> bool:
		return self._callFunction("getApplyThermalStageFactors")
	def setStageHydraulicStageFactor(self, value: bool):
		return self._callFunction("setApplyHydraulicStageFactor", [value])
	def getStageHydraulicStageFactor(self) -> bool:
		return self._callFunction("getApplyHydraulicStageFactor")
	def setStageDatumStageFactor(self, value: bool):
		return self._callFunction("setApplyDatumStageFactor", [value])
	def getStageDatumStageFactor(self) -> bool:
		return self._callFunction("getApplyDatumStageFactor")
	def setResetStress(self, value: bool):
		return self._callFunction("setResetStress", [value])
	def getResetStress(self) -> bool:
		return self._callFunction("getResetStress")
	def getDefinedStageFactors(self) -> dict[int, tuple[ObjectReferenceId, ObjectReferenceId, ObjectReferenceId]]:
		"""returns a dictionary of the defined stage factors. 
		The key is the stage number and the value is a tuple of stage factors defined for that stage (strengthStiffnessAndDatum, hydraulic, thermal)
		If a stage factor is not enabled, the values for that type will be None.
		Datum and Strength/Stiffness factors are combined and must be managed together.

		Returns:
			dict[int, (ObjectReferenceId, ObjectReferenceId, ObjectReferenceId): dictionary of defined stage factors (strengthStiffnessAndDatum, hydraulic, thermal)
		"""
		return self._callFunction("getDefinedStageFactors", keepReturnValueReference=True)
	
	def getStageFactor(self, stage: int) -> tuple[ObjectReferenceId, ObjectReferenceId, ObjectReferenceId]:
		"""returns the stage factors for the given stage. 
		If a stage factor is not enabled, the values for that type will be None.
		Datum and Strength/Stiffness factors are combined and must be managed together.

		Args:
			stage (int): stage number

		Returns:
			(ObjectReferenceId, ObjectReferenceId, ObjectReferenceId): tuple of stage factors (strengthStiffnessAndDatum, hydraulic, thermal)
		"""
		return self._callFunction("getStageFactor", [stage], keepReturnValueReference=True)

	def setDefinedStageFactors(self, stageFactors: dict[int, tuple[ObjectReferenceId, ObjectReferenceId, ObjectReferenceId]]):
		"""sets the stage factor table for the material. 
		The key is the stage number and the value is a tuple of stage factors defined for that stage (strengthStiffnessAndDatum, hydraulic, thermal)
		If a type of stage factor is not enabled, the values for that type should be None.
		If a tuple of stage factors is provided, a value for all enabled types must be provided.
		Datum and Strength/Stiffness factors are combined and must be managed together.

		Args:
			stageFactors (dict[int, (ObjectReferenceId, ObjectReferenceId, ObjectReferenceId)]): dictionary of defined stage factors (strengthStiffnessAndDatum, hydraulic, thermal)
		"""
		self._callFunction("setDefinedStageFactors", [stageFactors], proxyArgumentIndices=[0])
	
	def createStageFactor(self, stage: int):
		"""creates a stage factor for the material. A factor must be provided for all enabled types.
		"""
		return self._callFunction("createStageFactor", [stage], keepReturnValueReference=True)
					 