from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
class DruckerPragerStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getDilationParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_DP_DILATION_PARAMETER", self.propertyID], proxyArgumentIndices=[1])
	def getPeakKParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_K_PARAMETER", self.propertyID], proxyArgumentIndices=[1])
	def getResidualKParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_K_PARAMETER_RES", self.propertyID], proxyArgumentIndices=[1])
	def getPeakTensileStrengthFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_PEAK_TENSILE_STRENGTH", self.propertyID], proxyArgumentIndices=[1])
	def getPeakQParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_Q_PARAMETER", self.propertyID], proxyArgumentIndices=[1])
	def getResidualQParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_Q_PARAMETER_RES", self.propertyID], proxyArgumentIndices=[1])
	def getResidualTensileStrengthFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_TENSILE_STRENGTH_RES", self.propertyID], proxyArgumentIndices=[1])
class DruckerPragerDefinedStageFactor(DruckerPragerStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setDilationParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_DP_DILATION_PARAMETER", value, self.propertyID], proxyArgumentIndices=[2])
	def setPeakKParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_K_PARAMETER", value, self.propertyID], proxyArgumentIndices=[2])
	def setResidualKParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_K_PARAMETER_RES", value, self.propertyID], proxyArgumentIndices=[2])
	def setPeakTensileStrengthFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_PEAK_TENSILE_STRENGTH", value, self.propertyID], proxyArgumentIndices=[2])
	def setPeakQParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_Q_PARAMETER", value, self.propertyID], proxyArgumentIndices=[2])
	def setResidualQParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_Q_PARAMETER_RES", value, self.propertyID], proxyArgumentIndices=[2])
	def setResidualTensileStrengthFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_TENSILE_STRENGTH_RES", value, self.propertyID], proxyArgumentIndices=[2])
class DruckerPrager(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[DruckerPragerDefinedStageFactor, DruckerPragerStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Material Property Strength Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[DruckerPragerDefinedStageFactor, DruckerPragerStageFactor](self._client, stageFactorInterfaceID, ID, DruckerPragerDefinedStageFactor, DruckerPragerStageFactor)
	def getMaterialType(self) -> MaterialType:
		return MaterialType(self._getEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE"))
	def setMaterialType(self, value: MaterialType):
		return self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", value)
	def getPeakQParameter(self) -> float:
		return self._getDoubleProperty("MP_Q_PARAMETER")
	def setPeakQParameter(self, value: float):
		return self._setDoubleProperty("MP_Q_PARAMETER", value)
	def getPeakKParameter(self) -> float:
		return self._getDoubleProperty("MP_K_PARAMETER")
	def setPeakKParameter(self, value: float):
		return self._setDoubleProperty("MP_K_PARAMETER", value)
	def getPeakTensileStrength(self) -> float:
		return self._getDoubleProperty("MP_PEAK_TENSILE_STRENGTH")
	def setPeakTensileStrength(self, value: float):
		return self._setDoubleProperty("MP_PEAK_TENSILE_STRENGTH", value)
	def getResidualQParameter(self) -> float:
		return self._getDoubleProperty("MP_Q_PARAMETER_RES")
	def setResidualQParameter(self, value: float):
		return self._setDoubleProperty("MP_Q_PARAMETER_RES", value)
	def getResidualKParameter(self) -> float:
		return self._getDoubleProperty("MP_K_PARAMETER_RES")
	def setResidualKParameter(self, value: float):
		return self._setDoubleProperty("MP_K_PARAMETER_RES", value)
	def getResidualTensileStrength(self) -> float:
		return self._getDoubleProperty("MP_TENSILE_STRENGTH_RES")
	def setResidualTensileStrength(self, value: float):
		return self._setDoubleProperty("MP_TENSILE_STRENGTH_RES", value)
	def getDilationParameter(self) -> float:
		return self._getDoubleProperty("MP_DP_DILATION_PARAMETER")
	def setDilationParameter(self, value: float):
		return self._setDoubleProperty("MP_DP_DILATION_PARAMETER", value)
	def getApplySSRShearStrengthReduction(self) -> bool:
		return self._getBoolProperty("MP_APPLY_SSR")
	def setApplySSRShearStrengthReduction(self, value: bool):
		return self._setBoolProperty("MP_APPLY_SSR", value)
	def setProperties(self, MaterialType : MaterialType = None, PeakQParameter : float = None, PeakKParameter : float = None, PeakTensileStrength : float = None, ResidualQParameter : float = None, ResidualKParameter : float = None, ResidualTensileStrength : float = None, DilationParameter : float = None, ApplySSRShearStrengthReduction : bool = None):
		if MaterialType is not None:
			self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", MaterialType)
		if PeakQParameter is not None:
			self._setDoubleProperty("MP_Q_PARAMETER", PeakQParameter)
		if PeakKParameter is not None:
			self._setDoubleProperty("MP_K_PARAMETER", PeakKParameter)
		if PeakTensileStrength is not None:
			self._setDoubleProperty("MP_PEAK_TENSILE_STRENGTH", PeakTensileStrength)
		if ResidualQParameter is not None:
			self._setDoubleProperty("MP_Q_PARAMETER_RES", ResidualQParameter)
		if ResidualKParameter is not None:
			self._setDoubleProperty("MP_K_PARAMETER_RES", ResidualKParameter)
		if ResidualTensileStrength is not None:
			self._setDoubleProperty("MP_TENSILE_STRENGTH_RES", ResidualTensileStrength)
		if DilationParameter is not None:
			self._setDoubleProperty("MP_DP_DILATION_PARAMETER", DilationParameter)
		if ApplySSRShearStrengthReduction is not None:
			self._setBoolProperty("MP_APPLY_SSR", ApplySSRShearStrengthReduction)
	def getProperties(self):
		return {
		"MaterialType" : self.getMaterialType(), 
		"PeakQParameter" : self.getPeakQParameter(), 
		"PeakKParameter" : self.getPeakKParameter(), 
		"PeakTensileStrength" : self.getPeakTensileStrength(), 
		"ResidualQParameter" : self.getResidualQParameter(), 
		"ResidualKParameter" : self.getResidualKParameter(), 
		"ResidualTensileStrength" : self.getResidualTensileStrength(), 
		"DilationParameter" : self.getDilationParameter(), 
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		}
