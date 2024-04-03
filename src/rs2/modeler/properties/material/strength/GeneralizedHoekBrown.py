from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
class GeneralizedHoekBrownStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getAParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_A_PARAMETER", self.propertyID], proxyArgumentIndices=[1])
	def getResidualAParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_A_PARAMETER_RES", self.propertyID], proxyArgumentIndices=[1])
	def getCompressiveStrengthFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_COMPRESSIVE_STRENGTH", self.propertyID], proxyArgumentIndices=[1])
	def getDilationParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_DILATION_PARAMETER", self.propertyID], proxyArgumentIndices=[1])
	def getMbParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_MB_PARAMETER", self.propertyID], proxyArgumentIndices=[1])
	def getResidualMbParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_MB_PARAMETER_RES", self.propertyID], proxyArgumentIndices=[1])
	def getHoekMartinMiFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_MI_TENSION_CUTOFF", self.propertyID], proxyArgumentIndices=[1])
	def getSParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_S_PARAMETER", self.propertyID], proxyArgumentIndices=[1])
	def getResidualSParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_S_PARAMETER_RES", self.propertyID], proxyArgumentIndices=[1])
	def getTensileCutoffFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_UD_TENSION_CUTOFF", self.propertyID], proxyArgumentIndices=[1])
class GeneralizedHoekBrownDefinedStageFactor(GeneralizedHoekBrownStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setAParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_A_PARAMETER", value, self.propertyID], proxyArgumentIndices=[2])
	def setResidualAParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_A_PARAMETER_RES", value, self.propertyID], proxyArgumentIndices=[2])
	def setCompressiveStrengthFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_COMPRESSIVE_STRENGTH", value, self.propertyID], proxyArgumentIndices=[2])
	def setDilationParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_DILATION_PARAMETER", value, self.propertyID], proxyArgumentIndices=[2])
	def setMbParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_MB_PARAMETER", value, self.propertyID], proxyArgumentIndices=[2])
	def setResidualMbParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_MB_PARAMETER_RES", value, self.propertyID], proxyArgumentIndices=[2])
	def setHoekMartinMiFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_MI_TENSION_CUTOFF", value, self.propertyID], proxyArgumentIndices=[2])
	def setSParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_S_PARAMETER", value, self.propertyID], proxyArgumentIndices=[2])
	def setResidualSParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_S_PARAMETER_RES", value, self.propertyID], proxyArgumentIndices=[2])
	def setTensileCutoffFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_UD_TENSION_CUTOFF", value, self.propertyID], proxyArgumentIndices=[2])
class GeneralizedHoekBrown(PropertyProxy):
	"""
	Examples:
		:ref:`Material Property Strength Example`
	
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[GeneralizedHoekBrownDefinedStageFactor, GeneralizedHoekBrownStageFactor]) : Reference object for modifying strength generalized hoek brown stage factor properties.
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[GeneralizedHoekBrownDefinedStageFactor, GeneralizedHoekBrownStageFactor](self._client, stageFactorInterfaceID, ID, GeneralizedHoekBrownDefinedStageFactor, GeneralizedHoekBrownStageFactor)
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
	def getAParameter(self) -> float:
		return self._getDoubleProperty("MP_A_PARAMETER")
	def setAParameter(self, value: float):
		return self._setDoubleProperty("MP_A_PARAMETER", value)
	def getGSIParameter(self) -> float:
		return self._getDoubleProperty("MP_GSI_PARAMETER")
	def setGSIParameter(self, value: float):
		return self._setDoubleProperty("MP_GSI_PARAMETER", value)
	def getMiParameter(self) -> float:
		return self._getDoubleProperty("MP_MI_PARAMETER")
	def setMiParameter(self, value: float):
		return self._setDoubleProperty("MP_MI_PARAMETER", value)
	def getDParameter(self) -> float:
		return self._getDoubleProperty("MP_D_PARAMETER")
	def setDParameter(self, value: float):
		return self._setDoubleProperty("MP_D_PARAMETER", value)
	def getResidualMbParameter(self) -> float:
		return self._getDoubleProperty("MP_MB_PARAMETER_RES")
	def setResidualMbParameter(self, value: float):
		return self._setDoubleProperty("MP_MB_PARAMETER_RES", value)
	def getResidualSParameter(self) -> float:
		return self._getDoubleProperty("MP_S_PARAMETER_RES")
	def setResidualSParameter(self, value: float):
		return self._setDoubleProperty("MP_S_PARAMETER_RES", value)
	def getResidualAParameter(self) -> float:
		return self._getDoubleProperty("MP_A_PARAMETER_RES")
	def setResidualAParameter(self, value: float):
		return self._setDoubleProperty("MP_A_PARAMETER_RES", value)
	def getResidualGSIParameter(self) -> float:
		return self._getDoubleProperty("MP_GSI_PARAMETER_RES")
	def setResidualGSIParameter(self, value: float):
		return self._setDoubleProperty("MP_GSI_PARAMETER_RES", value)
	def getResidualMiParameter(self) -> float:
		return self._getDoubleProperty("MP_MI_PARAMETER_RES")
	def setResidualMiParameter(self, value: float):
		return self._setDoubleProperty("MP_MI_PARAMETER_RES", value)
	def getResidualDParameter(self) -> float:
		return self._getDoubleProperty("MP_D_PARAMETER_RES")
	def setResidualDParameter(self, value: float):
		return self._setDoubleProperty("MP_D_PARAMETER_RES", value)
	def getDilationParameter(self) -> float:
		return self._getDoubleProperty("MP_DILATION_PARAMETER")
	def setDilationParameter(self, value: float):
		return self._setDoubleProperty("MP_DILATION_PARAMETER", value)
	def getApplySSRShearStrengthReduction(self) -> bool:
		return self._getBoolProperty("MP_APPLY_SSR")
	def setApplySSRShearStrengthReduction(self, value: bool):
		return self._setBoolProperty("MP_APPLY_SSR", value)
	def getTensileCutoffType(self) -> TensileCutoffOptions:
		return TensileCutoffOptions(self._getEnumETensileCutoffOptionsProperty("MP_TENSION_CUTOFF_OPTIONS"))
	def setTensileCutoffType(self, value: TensileCutoffOptions):
		return self._setEnumETensileCutoffOptionsProperty("MP_TENSION_CUTOFF_OPTIONS", value)
	def getTensileCutoff(self) -> float:
		return self._getDoubleProperty("MP_UD_TENSION_CUTOFF")
	def setTensileCutoff(self, value: float):
		return self._setDoubleProperty("MP_UD_TENSION_CUTOFF", value)
	def getHoekMartinMi(self) -> float:
		return self._getDoubleProperty("MP_MI_TENSION_CUTOFF")
	def setHoekMartinMi(self, value: float):
		return self._setDoubleProperty("MP_MI_TENSION_CUTOFF", value)
	def setProperties(self, MaterialType : MaterialType = None, CompressiveStrength : float = None, MbParameter : float = None, SParameter : float = None, AParameter : float = None, GSIParameter : float = None, MiParameter : float = None, DParameter : float = None, ResidualMbParameter : float = None, ResidualSParameter : float = None, ResidualAParameter : float = None, ResidualGSIParameter : float = None, ResidualMiParameter : float = None, ResidualDParameter : float = None, DilationParameter : float = None, ApplySSRShearStrengthReduction : bool = None, TensileCutoffType : TensileCutoffOptions = None, TensileCutoff : float = None, HoekMartinMi : float = None):
		if MaterialType is not None:
			self._setEnumEMaterialAnalysisTypesProperty("MP_MATERIAL_TYPE", MaterialType)
		if CompressiveStrength is not None:
			self._setDoubleProperty("MP_COMPRESSIVE_STRENGTH", CompressiveStrength)
		if MbParameter is not None:
			self._setDoubleProperty("MP_MB_PARAMETER", MbParameter)
		if SParameter is not None:
			self._setDoubleProperty("MP_S_PARAMETER", SParameter)
		if AParameter is not None:
			self._setDoubleProperty("MP_A_PARAMETER", AParameter)
		if GSIParameter is not None:
			self._setDoubleProperty("MP_GSI_PARAMETER", GSIParameter)
		if MiParameter is not None:
			self._setDoubleProperty("MP_MI_PARAMETER", MiParameter)
		if DParameter is not None:
			self._setDoubleProperty("MP_D_PARAMETER", DParameter)
		if ResidualMbParameter is not None:
			self._setDoubleProperty("MP_MB_PARAMETER_RES", ResidualMbParameter)
		if ResidualSParameter is not None:
			self._setDoubleProperty("MP_S_PARAMETER_RES", ResidualSParameter)
		if ResidualAParameter is not None:
			self._setDoubleProperty("MP_A_PARAMETER_RES", ResidualAParameter)
		if ResidualGSIParameter is not None:
			self._setDoubleProperty("MP_GSI_PARAMETER_RES", ResidualGSIParameter)
		if ResidualMiParameter is not None:
			self._setDoubleProperty("MP_MI_PARAMETER_RES", ResidualMiParameter)
		if ResidualDParameter is not None:
			self._setDoubleProperty("MP_D_PARAMETER_RES", ResidualDParameter)
		if DilationParameter is not None:
			self._setDoubleProperty("MP_DILATION_PARAMETER", DilationParameter)
		if ApplySSRShearStrengthReduction is not None:
			self._setBoolProperty("MP_APPLY_SSR", ApplySSRShearStrengthReduction)
		if TensileCutoffType is not None:
			self._setEnumETensileCutoffOptionsProperty("MP_TENSION_CUTOFF_OPTIONS", TensileCutoffType)
		if TensileCutoff is not None:
			self._setDoubleProperty("MP_UD_TENSION_CUTOFF", TensileCutoff)
		if HoekMartinMi is not None:
			self._setDoubleProperty("MP_MI_TENSION_CUTOFF", HoekMartinMi)
	def getProperties(self):
		return {
		"MaterialType" : self.getMaterialType(), 
		"CompressiveStrength" : self.getCompressiveStrength(), 
		"MbParameter" : self.getMbParameter(), 
		"SParameter" : self.getSParameter(), 
		"AParameter" : self.getAParameter(), 
		"GSIParameter" : self.getGSIParameter(), 
		"MiParameter" : self.getMiParameter(), 
		"DParameter" : self.getDParameter(), 
		"ResidualMbParameter" : self.getResidualMbParameter(), 
		"ResidualSParameter" : self.getResidualSParameter(), 
		"ResidualAParameter" : self.getResidualAParameter(), 
		"ResidualGSIParameter" : self.getResidualGSIParameter(), 
		"ResidualMiParameter" : self.getResidualMiParameter(), 
		"ResidualDParameter" : self.getResidualDParameter(), 
		"DilationParameter" : self.getDilationParameter(), 
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		"TensileCutoffType" : self.getTensileCutoffType(), 
		"TensileCutoff" : self.getTensileCutoff(), 
		"HoekMartinMi" : self.getHoekMartinMi(), 
		}
