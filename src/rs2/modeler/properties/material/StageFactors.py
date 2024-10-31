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
	def setStageHydroDistributionStageFactor(self, value: bool):
		return self._callFunction("setApplyHydroDistributionStageFactor", [value])
	def getStageHydroDistributionStageFactor(self) -> bool:
		return self._callFunction("getApplyHydroDistributionStageFactor")
	def setStageDatumStageFactor(self, value: bool):
		return self._callFunction("setApplyDatumStageFactor", [value])
	def getStageDatumStageFactor(self) -> bool:
		return self._callFunction("getApplyDatumStageFactor")
	def setResetStress(self, value: bool):
		return self._callFunction("setResetStress", [value])
	def getResetStress(self) -> bool:
		return self._callFunction("getResetStress")
	def getDefinedStageFactors(self) -> dict[int, tuple[ProxyObject, ProxyObject, ProxyObject]]:
		"""returns a dictionary of the defined stage factors. 
		The key is the stage number and the value is a tuple of stage factors defined for that stage (strengthStiffnessAndDatum, hydraulic, thermal)
		If a stage factor is not enabled, the values for that type will be None.
		Datum and Strength/Stiffness factors are combined and must be managed together.

		Returns:
			dict[int, (ObjectReferenceId, ObjectReferenceId, ObjectReferenceId): dictionary of defined stage factors (strengthStiffnessAndDatum, hydraulic, thermal)
		"""
		definedFactorIds = self._callFunction("getDefinedStageFactors", keepReturnValueReference=True)
		return self._getObjectDictionaryFromReferenceDictionary(definedFactorIds)
	
	def getStageFactor(self, stage: int) -> tuple[ProxyObject, ProxyObject, ProxyObject]:
		"""returns the stage factors for the given stage. 
		If a stage factor is not enabled, the values for that type will be None.
		Datum and Strength/Stiffness factors are combined and must be managed together.

		Args:
			stage (int): stage number

		Returns:
			(ObjectReferenceId, ObjectReferenceId, ObjectReferenceId): tuple of stage factors (strengthStiffnessAndDatum, hydraulic, thermal)
		"""
		stageFactorIds = self._callFunction("getStageFactor", [stage], keepReturnValueReference=True)
		return self._getObjectTupleFromReferenceTuple(stageFactorIds)

	def setDefinedStageFactors(self, stageFactors: dict[int, tuple[ProxyObject, ProxyObject, ProxyObject]]):
		"""sets the stage factor table for the material. 
		The key is the stage number and the value is a tuple of stage factors defined for that stage (strengthStiffnessAndDatum, hydraulic, thermal)
		If a type of stage factor is not enabled, the values for that type should be None.
		If a tuple of stage factors is provided, a value for all enabled types must be provided.
		Datum and Strength/Stiffness factors are combined and must be managed together.

		Args:
			stageFactors (dict[int, (ObjectReferenceId, ObjectReferenceId, ObjectReferenceId)]): dictionary of defined stage factors (strengthStiffnessAndDatum, hydraulic, thermal)
		"""
		stageFactorReferences = self._getReferenceDictionaryFromObjectDictionary(stageFactors)
		self._callFunction("setDefinedStageFactors", [stageFactorReferences], proxyArgumentIndices=[0])
	
	def createStageFactor(self, stage: int):
		"""creates a stage factor for the material. A factor must be provided for all enabled types.
		"""
		stageFactorReferences = self._callFunction("createStageFactor", [stage], keepReturnValueReference=True)
		return self._getObjectTupleFromReferenceTuple(stageFactorReferences)
	
	def _getProxyFromReferenceOrNone(self, ID : int) -> ProxyObject:
		return ProxyObject(self._client, ID) if ID is not None else None
	def _getReferenceFromProxyOrNone(self, proxy : ProxyObject) -> int:
		return proxy._ID if proxy is not None else None
	
	def _getObjectTupleFromReferenceTuple(self, stageFactors : tuple[int, int, int]) -> tuple[ProxyObject, ProxyObject, ProxyObject]:
		matFactorProxy = self._getProxyFromReferenceOrNone(stageFactors[0])
		hydroFactorProxy = self._getProxyFromReferenceOrNone(stageFactors[1])
		thermalFactorProxy = self._getProxyFromReferenceOrNone(stageFactors[2])
		return (matFactorProxy, hydroFactorProxy, thermalFactorProxy)
	
	def _getReferenceTupleFromObjectTuple(self, stageFactors : tuple[ProxyObject, ProxyObject, ProxyObject]) -> tuple[int, int, int]:
		matFactorId = self._getReferenceFromProxyOrNone(stageFactors[0])
		hydroFactorId = self._getReferenceFromProxyOrNone(stageFactors[1])
		thermalFactorId = self._getReferenceFromProxyOrNone(stageFactors[2])
		return (matFactorId, hydroFactorId, thermalFactorId)
	
	def _getObjectDictionaryFromReferenceDictionary(self, stageFactors : dict[int, tuple[int, int, int]]) -> dict[int, tuple[ProxyObject, ProxyObject, ProxyObject]]:
		return {key : self._getObjectTupleFromReferenceTuple(value) for key, value in stageFactors.items()}
	
	def _getReferenceDictionaryFromObjectDictionary(self, stageFactors : dict[int, tuple[ProxyObject, ProxyObject, ProxyObject]]) -> dict[int, tuple[int, int, int]]:
		return {key : self._getReferenceTupleFromObjectTuple(value) for key, value in stageFactors.items()}