from rs2.ProxyObject import ProxyObject
from typing import Generic
from typing import TypeVar
from rs2.PropertyEnums import *

DefinedStageFactor = TypeVar('DefinedStageFactor', bound=ProxyObject)
StageFactor = TypeVar('StageFactor', bound=ProxyObject)

class RelativeStageFactorInterface(ProxyObject, Generic[DefinedStageFactor, StageFactor]):
	def getDefinedStageFactors(self) -> dict[int, DefinedStageFactor]:
		"""
		Returns a map of stage factors. The key is the absolute or relative stage at which the stage factor is applied. The value is the stage factor object
		"""
		stageFactorReferenceIds = self._callFunction('getDefinedStageFactors', [], keepReturnValueReference=True)
		stageFactors = {}
		for stageKey in stageFactorReferenceIds :
			stageFactors[stageKey] = DefinedStageFactor(self._client, stageFactorReferenceIds[stageKey], self)
		return stageFactors
	def getStageFactor(self, stage: int) -> StageFactor:
		"""
		Returns the stage factor for the given stage.
		"""
		factorReferenceID = self._callFunction('getStageFactor', [stage], keepReturnValueReference=True)
		return StageFactor(self._client, factorReferenceID, self)
	def createStageFactor(self, stage: int) -> DefinedStageFactor:
		"""
		Creates a stage factor for the given stage.

		NOTE: Invalidates any existing stage factor proxies. Get them again using getDefinedStageFactors or getStageFactor.
		"""
		factorReferenceID = self._callFunction('createStageFactor', [stage], keepReturnValueReference=True)
		return DefinedStageFactor(self._client, factorReferenceID, self)
	def setDefinedStageFactors(self, method: StageFactorDefinitionMethod, stageFactors: dict[int, StageFactor]):
		"""
		Sets the defined stage factors to those given. The method indicates if the stages in the keys of the map are absolute or relative.

		NOTE: Invalidates any existing stage factor proxies. Get them again using getDefinedStageFactors or getStageFactor.
		"""
		stageFactorIdMap = {}
		for stage in stageFactors :
			stageFactorIdMap[stage] = stageFactors[stage]._ID
		return self._callFunction("setDefinedStageFactors", [method.value, stageFactorIdMap], proxyArgumentIndices = [1])
	def getStageFactorMethod(self) -> StageFactorDefinitionMethod:
		return StageFactorDefinitionMethod(self._callFunction("areRelativeStageFactorsSelected"))