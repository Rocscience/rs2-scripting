from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2.modeler.properties.PropertyEnums import *

from rs2.modeler.properties.material.datum.PeakResidualDatum import PeakResidualDatum
from rs2.modeler.properties.material.datum.SimpleDatum import SimpleDatum

from rs2._common.Client import Client
from rs2.modeler.properties.AbsoluteStageFactorInterface import AbsoluteStageFactorInterface
from rs2._common.ProxyObject import ProxyObject

class DatumValueStageFactorGetters(ProxyObject):
	def getDatum(self) -> float:
		return self._callFunction("getDatum")
	def getChange(self) -> float:
		return self._callFunction("getChange1")
	def getResidualChange(self) -> float:
		return self._callFunction("getChange2")
	def getPeakCutoffValue(self) -> float:
		return self._callFunction("getCutoff1")
	def getResidualCutoffValue(self) -> float:
		return self._callFunction("getCutoff2")
class DatumValueStageFactor(DatumValueStageFactorGetters):
	def setDatum(self, depth : float):
		self._callFunction("setDatum", [depth])
	def setChange(self, change : float):
		self._callFunction("setChange1", [change])
	def setResidualChange(self, residualChange: float):
		self._callFunction("setChange2", [residualChange])
	def setPeakCutoffValue(self, peakCutoffValue: float):
		self._callFunction("setCutoff1", [peakCutoffValue])
	def setResidualCutoffValue(self, residualCutoffValue: float):
		self._callFunction("setCutoff2", [residualCutoffValue])

class DatumStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getDatumYoungsStageFactor(self) -> DatumValueStageFactorGetters:
		return DatumValueStageFactorGetters(self._client, self._callFunction("getDatumYoungsStageFactorViewModel", keepReturnValueReference=True))
	def getDatumCohesionStageFactor(self) -> DatumValueStageFactorGetters:
		return DatumValueStageFactorGetters(self._client, self._callFunction("getDatumCohesionStageFactorViewModel", keepReturnValueReference=True))
	def getDatumFrictionStageFactor(self) -> DatumValueStageFactorGetters:
		return DatumValueStageFactorGetters(self._client, self._callFunction("getDatumFrictionStageFactorViewModel", keepReturnValueReference=True))
	
class DatumDefinedStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getDatumYoungsStageFactor(self) -> DatumValueStageFactor:
		return DatumValueStageFactor(self._client, self._callFunction("getDatumYoungsStageFactorViewModel", keepReturnValueReference=True))
	def getDatumCohesionStageFactor(self) -> DatumValueStageFactor:
		return DatumValueStageFactor(self._client, self._callFunction("getDatumCohesionStageFactorViewModel", keepReturnValueReference=True))
	def getDatumFrictionStageFactor(self) -> DatumValueStageFactor:
		return DatumValueStageFactor(self._client, self._callFunction("getDatumFrictionStageFactorViewModel", keepReturnValueReference=True))
	
class Datum(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorInterface[DatumDefinedStageFactor, DatumStageFactor]): Reference object for modifying stage factor property.
	
	Examples:
		:ref:`Material Property Datum Example`
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorInterface[DatumDefinedStageFactor, DatumStageFactor](self._client, stageFactorInterfaceID, ID, DatumDefinedStageFactor, DatumStageFactor)

	def setUsingDatum(self, use : bool):
		self._callFunction("setUsingDatum", [use])
	def getUsingDatum(self) -> bool:
		return bool(self._callFunction("getUsingDatum"))
	
	def getDatumUnloadingYoungsModulus(self) -> SimpleDatum:
		return SimpleDatum(self._client, self._callFunction("getDatumUnloadingYoungsModulus", [], keepReturnValueReference=True), self.documentProxyID)
		
	def getDatumYoungsModulus(self) -> SimpleDatum:
		return SimpleDatum(self._client, self._callFunction("getDatumYoungsModulus", [], keepReturnValueReference=True), self.documentProxyID)
		
	def getDatumCohesion(self) -> PeakResidualDatum:
		return PeakResidualDatum(self._client, self._callFunction("getDatumCohesion", [], keepReturnValueReference=True), self.documentProxyID)
		
	def getDatumFrictionAngle(self) -> PeakResidualDatum:
		return PeakResidualDatum(self._client, self._callFunction("getDatumFriction", [], keepReturnValueReference=True), self.documentProxyID)