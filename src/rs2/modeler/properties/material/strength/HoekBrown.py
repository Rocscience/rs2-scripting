from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
class HoekBrownStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getCompressiveStrengthFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_COMPRESSIVE_STRENGTH", self.propertyID], proxyArgumentIndices=[1])
	def getDilationParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_DILATION_PARAMETER", self.propertyID], proxyArgumentIndices=[1])
	def getMbParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_MB_PARAMETER", self.propertyID], proxyArgumentIndices=[1])
	def getResidualMbParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_MB_PARAMETER_RES", self.propertyID], proxyArgumentIndices=[1])
	def getSParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_S_PARAMETER", self.propertyID], proxyArgumentIndices=[1])
	def getResidualSParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_S_PARAMETER_RES", self.propertyID], proxyArgumentIndices=[1])
class HoekBrownDefinedStageFactor(HoekBrownStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setCompressiveStrengthFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_COMPRESSIVE_STRENGTH", value, self.propertyID], proxyArgumentIndices=[2])
	def setDilationParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_DILATION_PARAMETER", value, self.propertyID], proxyArgumentIndices=[2])
	def setMbParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_MB_PARAMETER", value, self.propertyID], proxyArgumentIndices=[2])
	def setResidualMbParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_MB_PARAMETER_RES", value, self.propertyID], proxyArgumentIndices=[2])
	def setSParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_S_PARAMETER", value, self.propertyID], proxyArgumentIndices=[2])
	def setResidualSParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_S_PARAMETER_RES", value, self.propertyID], proxyArgumentIndices=[2])
class HoekBrown(PropertyProxy):
	"""
	Examples:
		:ref:`Material Property Strength Example`
	
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[HoekBrownDefinedStageFactor, HoekBrownStageFactor]) : Reference object for modifying strength hoek brown stage factor properties.
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[HoekBrownDefinedStageFactor, HoekBrownStageFactor](self._client, stageFactorInterfaceID, ID, HoekBrownDefinedStageFactor, HoekBrownStageFactor)
	def getMaterialType(self) -> MaterialType:
		return MaterialType(self._getEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE"))
	def setMaterialType(self, value: MaterialType):
		return self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", value)
	def getCompressiveStrength(self) -> float:
		return self._getDoubleProperty("MP_COMPRESSIVE_STRENGTH")
	def setCompressiveStrength(self, value: float):
		return self._setDoubleProperty("MP_COMPRESSIVE_STRENGTH", value)
	def getMbParameter(self) -> float:
		return self._getDoubleProperty("MP_MB_PARAMETER")
	def setMbParameter(self, value: float):
		return self._setDoubleProperty("MP_MB_PARAMETER", value)
	def getSParameter(self) -> float:
		return self._getDoubleProperty("MP_S_PARAMETER")
	def setSParameter(self, value: float):
		return self._setDoubleProperty("MP_S_PARAMETER", value)
	def getResidualMbParameter(self) -> float:
		return self._getDoubleProperty("MP_MB_PARAMETER_RES")
	def setResidualMbParameter(self, value: float):
		return self._setDoubleProperty("MP_MB_PARAMETER_RES", value)
	def getResidualSParameter(self) -> float:
		return self._getDoubleProperty("MP_S_PARAMETER_RES")
	def setResidualSParameter(self, value: float):
		return self._setDoubleProperty("MP_S_PARAMETER_RES", value)
	def getDilationParameter(self) -> float:
		return self._getDoubleProperty("MP_DILATION_PARAMETER")
	def setDilationParameter(self, value: float):
		return self._setDoubleProperty("MP_DILATION_PARAMETER", value)
	def getApplySSRShearStrengthReduction(self) -> bool:
		return self._getBoolProperty("MP_APPLY_SSR")
	def setApplySSRShearStrengthReduction(self, value: bool):
		return self._setBoolProperty("MP_APPLY_SSR", value)
	def setProperties(self, MaterialType : MaterialType = None, CompressiveStrength : float = None, MbParameter : float = None, SParameter : float = None, ResidualMbParameter : float = None, ResidualSParameter : float = None, DilationParameter : float = None, ApplySSRShearStrengthReduction : bool = None):
		if MaterialType is not None:
			self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", MaterialType)
		if CompressiveStrength is not None:
			self._setDoubleProperty("MP_COMPRESSIVE_STRENGTH", CompressiveStrength)
		if MbParameter is not None:
			self._setDoubleProperty("MP_MB_PARAMETER", MbParameter)
		if SParameter is not None:
			self._setDoubleProperty("MP_S_PARAMETER", SParameter)
		if ResidualMbParameter is not None:
			self._setDoubleProperty("MP_MB_PARAMETER_RES", ResidualMbParameter)
		if ResidualSParameter is not None:
			self._setDoubleProperty("MP_S_PARAMETER_RES", ResidualSParameter)
		if DilationParameter is not None:
			self._setDoubleProperty("MP_DILATION_PARAMETER", DilationParameter)
		if ApplySSRShearStrengthReduction is not None:
			self._setBoolProperty("MP_APPLY_SSR", ApplySSRShearStrengthReduction)
	def getProperties(self):
		return {
		"MaterialType" : self.getMaterialType(), 
		"CompressiveStrength" : self.getCompressiveStrength(), 
		"MbParameter" : self.getMbParameter(), 
		"SParameter" : self.getSParameter(), 
		"ResidualMbParameter" : self.getResidualMbParameter(), 
		"ResidualSParameter" : self.getResidualSParameter(), 
		"DilationParameter" : self.getDilationParameter(), 
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		}
