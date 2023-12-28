from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.PropertyEnums import *

from rs2.proxyObjects.MaterialSubproxyObjects.DatumSubProxyObjects.PeakResidualDatum import PeakResidualDatum
from rs2.proxyObjects.MaterialSubproxyObjects.DatumSubProxyObjects.SimpleDatum import SimpleDatum
#keepme
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
		
	def getDatumFriction(self) -> PeakResidualDatum:
		return PeakResidualDatum(self._client, self._callFunction("getDatumFriction", [], keepReturnValueReference=True), self.documentProxyID)

	def getDatumSigmaCi(self) -> PeakResidualDatum:
		return PeakResidualDatum(self._client, self._callFunction("getDatumSigmaCi", [], keepReturnValueReference=True), self.documentProxyID)
		
	def getDatumGSI(self) -> PeakResidualDatum:
		return PeakResidualDatum(self._client, self._callFunction("getDatumGSI", [], keepReturnValueReference=True), self.documentProxyID)

	def getDatumD(self) -> PeakResidualDatum:
		return PeakResidualDatum(self._client, self._callFunction("getDatumD", [], keepReturnValueReference=True), self.documentProxyID)
		
	def getDatumMi(self) -> PeakResidualDatum:
		return PeakResidualDatum(self._client, self._callFunction("getDatumMi", [], keepReturnValueReference=True), self.documentProxyID)