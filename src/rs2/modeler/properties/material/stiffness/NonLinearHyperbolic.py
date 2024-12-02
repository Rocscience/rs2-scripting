from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
class NonLinearHyperbolicStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getAtmosphericPressureFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_ATMOSPHERIC_PRESSURE", self.propertyID], proxyArgumentIndices=[1])
	def getBulkModulusExpMFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_BULK_MODULUS_EXP", self.propertyID], proxyArgumentIndices=[1])
	def getBulkModulusNumberFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_BULK_MODULUS_NUMBER", self.propertyID], proxyArgumentIndices=[1])
	def getFailureRatioRfFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_FAILURE_RATIO", self.propertyID], proxyArgumentIndices=[1])
	def getModulusExpNFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_MODULUS_EXP", self.propertyID], proxyArgumentIndices=[1])
	def getModulusNumberFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_MODULUS_NUMBER", self.propertyID], proxyArgumentIndices=[1])
	def getPoissonsRatioFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_NLH_POISSONS_RATIO", self.propertyID], proxyArgumentIndices=[1])
	def getUnloadingModulusNumberFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_UNLOADING_MODULUS_NUMBER", self.propertyID], proxyArgumentIndices=[1])
class NonLinearHyperbolicDefinedStageFactor(NonLinearHyperbolicStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setAtmosphericPressureFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_ATMOSPHERIC_PRESSURE", value, self.propertyID], proxyArgumentIndices=[2])
	def setBulkModulusExpMFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_BULK_MODULUS_EXP", value, self.propertyID], proxyArgumentIndices=[2])
	def setBulkModulusNumberFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_BULK_MODULUS_NUMBER", value, self.propertyID], proxyArgumentIndices=[2])
	def setFailureRatioRfFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_FAILURE_RATIO", value, self.propertyID], proxyArgumentIndices=[2])
	def setModulusExpNFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_MODULUS_EXP", value, self.propertyID], proxyArgumentIndices=[2])
	def setModulusNumberFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_MODULUS_NUMBER", value, self.propertyID], proxyArgumentIndices=[2])
	def setPoissonsRatioFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_NLH_POISSONS_RATIO", value, self.propertyID], proxyArgumentIndices=[2])
	def setUnloadingModulusNumberFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_UNLOADING_MODULUS_NUMBER", value, self.propertyID], proxyArgumentIndices=[2])
class NonLinearHyperbolic(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[NonLinearHyperbolicDefinedStageFactor, NonLinearHyperbolicStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Material Property Stiffness Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[NonLinearHyperbolicDefinedStageFactor, NonLinearHyperbolicStageFactor](self._client, stageFactorInterfaceID, ID, NonLinearHyperbolicDefinedStageFactor, NonLinearHyperbolicStageFactor)
	def getModulusNumber(self) -> float:
		return self._getDoubleProperty("MP_MODULUS_NUMBER")
	def setModulusNumber(self, value: float):
		return self._setDoubleProperty("MP_MODULUS_NUMBER", value)
	def getPoissonRatioType(self) -> PoissonRatioType:
		return PoissonRatioType(self._getEnumEPoissonRatioTypeProperty("MP_POISSON_RATIO_TYPE"))
	def setPoissonRatioType(self, value: PoissonRatioType):
		return self._setEnumEPoissonRatioTypeProperty("MP_POISSON_RATIO_TYPE", value)
	def getBulkModulusNumber(self) -> float:
		return self._getDoubleProperty("MP_BULK_MODULUS_NUMBER")
	def setBulkModulusNumber(self, value: float):
		return self._setDoubleProperty("MP_BULK_MODULUS_NUMBER", value)
	def getBulkModulusExpM(self) -> float:
		return self._getDoubleProperty("MP_BULK_MODULUS_EXP")
	def setBulkModulusExpM(self, value: float):
		return self._setDoubleProperty("MP_BULK_MODULUS_EXP", value)
	def getPoissonsRatio(self) -> float:
		return self._getDoubleProperty("MP_NLH_POISSONS_RATIO")
	def setPoissonsRatio(self, value: float):
		return self._setDoubleProperty("MP_NLH_POISSONS_RATIO", value)
	def getModulusExpN(self) -> float:
		return self._getDoubleProperty("MP_MODULUS_EXP")
	def setModulusExpN(self, value: float):
		return self._setDoubleProperty("MP_MODULUS_EXP", value)
	def getAtmosphericPressure(self) -> float:
		return self._getDoubleProperty("MP_ATMOSPHERIC_PRESSURE")
	def setAtmosphericPressure(self, value: float):
		return self._setDoubleProperty("MP_ATMOSPHERIC_PRESSURE", value)
	def getFailureRatioRf(self) -> float:
		return self._getDoubleProperty("MP_FAILURE_RATIO")
	def setFailureRatioRf(self, value: float):
		return self._setDoubleProperty("MP_FAILURE_RATIO", value)
	def getUnloadingModulusNumber(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_MODULUS_NUMBER")
	def setUnloadingModulusNumber(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_MODULUS_NUMBER", value)
	def setProperties(self, ModulusNumber : float = None, PoissonRatioType : PoissonRatioType = None, BulkModulusNumber : float = None, BulkModulusExpM : float = None, PoissonsRatio : float = None, ModulusExpN : float = None, AtmosphericPressure : float = None, FailureRatioRf : float = None, UnloadingModulusNumber : float = None):
		if ModulusNumber is not None:
			self._setDoubleProperty("MP_MODULUS_NUMBER", ModulusNumber)
		if PoissonRatioType is not None:
			self._setEnumEPoissonRatioTypeProperty("MP_POISSON_RATIO_TYPE", PoissonRatioType)
		if BulkModulusNumber is not None:
			self._setDoubleProperty("MP_BULK_MODULUS_NUMBER", BulkModulusNumber)
		if BulkModulusExpM is not None:
			self._setDoubleProperty("MP_BULK_MODULUS_EXP", BulkModulusExpM)
		if PoissonsRatio is not None:
			self._setDoubleProperty("MP_NLH_POISSONS_RATIO", PoissonsRatio)
		if ModulusExpN is not None:
			self._setDoubleProperty("MP_MODULUS_EXP", ModulusExpN)
		if AtmosphericPressure is not None:
			self._setDoubleProperty("MP_ATMOSPHERIC_PRESSURE", AtmosphericPressure)
		if FailureRatioRf is not None:
			self._setDoubleProperty("MP_FAILURE_RATIO", FailureRatioRf)
		if UnloadingModulusNumber is not None:
			self._setDoubleProperty("MP_UNLOADING_MODULUS_NUMBER", UnloadingModulusNumber)
	def getProperties(self):
		return {
		"ModulusNumber" : self.getModulusNumber(), 
		"PoissonRatioType" : self.getPoissonRatioType(), 
		"BulkModulusNumber" : self.getBulkModulusNumber(), 
		"BulkModulusExpM" : self.getBulkModulusExpM(), 
		"PoissonsRatio" : self.getPoissonsRatio(), 
		"ModulusExpN" : self.getModulusExpN(), 
		"AtmosphericPressure" : self.getAtmosphericPressure(), 
		"FailureRatioRf" : self.getFailureRatioRf(), 
		"UnloadingModulusNumber" : self.getUnloadingModulusNumber(), 
		}
