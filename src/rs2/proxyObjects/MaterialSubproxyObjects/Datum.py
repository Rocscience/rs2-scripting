from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.PropertyEnums import *

from rs2.proxyObjects.MaterialSubproxyObjects.DatumSubProxyObjects.PeakResidualDatum import PeakResidualDatum
from rs2.proxyObjects.MaterialSubproxyObjects.DatumSubProxyObjects.SimpleDatum import SimpleDatum

class Datum(PropertyProxy):
	"""
	:ref:`Material Property Datum Example`
	"""
	def getDatumUnloadingYoungsModulus(self) -> SimpleDatum:
		return self._callFunction("getDatumUnloadingYoungsModulus", [], keepReturnValueReference=True)
		
	def getDatumYoungsModulus(self) -> SimpleDatum:
		return self._callFunction("getDatumYoungsModulus", [], keepReturnValueReference=True)
		
	def getDatumCohesion(self) -> PeakResidualDatum:
		return self._callFunction("getDatumCohesion", [], keepReturnValueReference=True)
		
	def getDatumFriction(self) -> PeakResidualDatum:
		return self._callFunction("getDatumFriction", [], keepReturnValueReference=True)

	def getDatumSigmaCi(self) -> PeakResidualDatum:
		return self._callFunction("getDatumSigmaCi", [], keepReturnValueReference=True)
		
	def getDatumGSI(self) -> PeakResidualDatum:
		return self._callFunction("getDatumGSI", [], keepReturnValueReference=True)

	def getDatumD(self) -> PeakResidualDatum:
		return self._callFunction("getDatumD", [], keepReturnValueReference=True)
		
	def getDatumMi(self) -> PeakResidualDatum:
		return self._callFunction("getDatumMi", [], keepReturnValueReference=True)