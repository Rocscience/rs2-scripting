from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2.modeler.properties.PropertyEnums import *

from rs2.modeler.properties.material.datum.PeakResidualDatum import PeakResidualDatum
from rs2.modeler.properties.material.datum.SimpleDatum import SimpleDatum

class Datum(PropertyProxy):
	"""
	:ref:`Material Property Datum Example`
	"""
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