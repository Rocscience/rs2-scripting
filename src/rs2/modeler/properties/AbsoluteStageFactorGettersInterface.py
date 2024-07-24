from rs2._common.ProxyObject import ProxyObject
from typing import Generic
from typing import TypeVar
from rs2.modeler.properties.PropertyEnums import *

DefinedStageFactor = TypeVar('DefinedStageFactor', bound=ProxyObject)
StageFactor = TypeVar('StageFactor', bound=ProxyObject)

class AbsoluteStageFactorGettersInterface(ProxyObject, Generic[DefinedStageFactor, StageFactor]):
	"""
	Examples:
	
		:ref:`Stage Factors Example`
		
	"""
	def __init__(self, client, proxyId, propertyID, definedFactorClass, factorClass):
		super().__init__(client, proxyId)
		self._definedStageFactorType = definedFactorClass
		self._stageFactorType = factorClass
		self.propertyID = propertyID
		
	def getDefinedStageFactors(self) -> dict[int, DefinedStageFactor]:
		"""
		Returns a map of stage factors. The key is the stage at which the stage factor is applied. The value is the stage factor object
		"""
		stageFactorReferenceIds = self._callFunction('getDefinedStageFactors', [], keepReturnValueReference=True)
		stageFactors = {}
		for stageKey in stageFactorReferenceIds :
			stageFactors[stageKey] = self._definedStageFactorType(self._client, stageFactorReferenceIds[stageKey], self.propertyID)
		return stageFactors
	def getStageFactor(self, stage: int) -> StageFactor:
		"""
		Returns the stage factor for the given stage.
		"""
		factorReferenceID = self._callFunction('getStageFactor', [stage], keepReturnValueReference=True)
		return self._stageFactorType(self._client, factorReferenceID,  self.propertyID)