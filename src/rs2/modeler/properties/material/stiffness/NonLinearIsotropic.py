from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
class NonLinearIsotropicStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getAParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_NLI_A", self.propertyID], proxyArgumentIndices=[1])
	def getAlphaFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_NLI_ALPHA", self.propertyID], proxyArgumentIndices=[1])
	def getBParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_NLI_B", self.propertyID], proxyArgumentIndices=[1])
	def getGMaxFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_NLI_G_MAX", self.propertyID], proxyArgumentIndices=[1])
	def getInitialEFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_NLI_INITIAL_E", self.propertyID], proxyArgumentIndices=[1])
	def getMParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_NLI_M", self.propertyID], proxyArgumentIndices=[1])
	def getPrefFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_NLI_PREF", self.propertyID], proxyArgumentIndices=[1])
	def getRParameterFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_NLI_R", self.propertyID], proxyArgumentIndices=[1])
	def getGammaYFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_NLI_TAU_Y", self.propertyID], proxyArgumentIndices=[1])
	def getPoissonsRatioFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_POISSONS_RATIO", self.propertyID], proxyArgumentIndices=[1])
	def getResidualYoungsModulusFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_YOUNGS_MODULUS_RES", self.propertyID], proxyArgumentIndices=[1])
class NonLinearIsotropicDefinedStageFactor(NonLinearIsotropicStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setAParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_NLI_A", value, self.propertyID], proxyArgumentIndices=[2])
	def setAlphaFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_NLI_ALPHA", value, self.propertyID], proxyArgumentIndices=[2])
	def setBParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_NLI_B", value, self.propertyID], proxyArgumentIndices=[2])
	def setGMaxFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_NLI_G_MAX", value, self.propertyID], proxyArgumentIndices=[2])
	def setInitialEFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_NLI_INITIAL_E", value, self.propertyID], proxyArgumentIndices=[2])
	def setMParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_NLI_M", value, self.propertyID], proxyArgumentIndices=[2])
	def setPrefFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_NLI_PREF", value, self.propertyID], proxyArgumentIndices=[2])
	def setRParameterFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_NLI_R", value, self.propertyID], proxyArgumentIndices=[2])
	def setGammaYFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_NLI_TAU_Y", value, self.propertyID], proxyArgumentIndices=[2])
	def setPoissonsRatioFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_POISSONS_RATIO", value, self.propertyID], proxyArgumentIndices=[2])
	def setResidualYoungsModulusFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_YOUNGS_MODULUS_RES", value, self.propertyID], proxyArgumentIndices=[2])
class NonLinearIsotropic(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[NonLinearIsotropicDefinedStageFactor, NonLinearIsotropicStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Material Property Stiffness Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[NonLinearIsotropicDefinedStageFactor, NonLinearIsotropicStageFactor](self._client, stageFactorInterfaceID, ID, NonLinearIsotropicDefinedStageFactor, NonLinearIsotropicStageFactor)
	def getUseUnloadingCondition(self) -> bool:
		return self._getBoolProperty("MP_USE_UNLOADING_CONDITION")
	def setUseUnloadingCondition(self, value: bool):
		return self._setBoolProperty("MP_USE_UNLOADING_CONDITION", value)
	def getUnloadingCondition(self) -> UnloadingConditions:
		return UnloadingConditions(self._getEnumEUnloadingConditionsProperty("MP_UNLOADING_CONDITION"))
	def setUnloadingCondition(self, value: UnloadingConditions):
		return self._setEnumEUnloadingConditionsProperty("MP_UNLOADING_CONDITION", value)
	def getNonLinearIsotropicFormula(self) -> NLIFormulaTypes:
		return NLIFormulaTypes(self._getEnumENLIFormulaTypesProperty("MP_NLI_TYPE"))
	def setNonLinearIsotropicFormula(self, value: NLIFormulaTypes):
		return self._setEnumENLIFormulaTypesProperty("MP_NLI_TYPE", value)
	def getPoissonsRatio(self) -> float:
		return self._getDoubleProperty("MP_POISSONS_RATIO")
	def setPoissonsRatio(self, value: float):
		return self._setDoubleProperty("MP_POISSONS_RATIO", value)
	def getUseResidualYoungsModulus(self) -> bool:
		return self._getBoolProperty("MP_USE_YOUNGS_MODULUS_RES")
	def setUseResidualYoungsModulus(self, value: bool):
		return self._setBoolProperty("MP_USE_YOUNGS_MODULUS_RES", value)
	def getResidualYoungsModulus(self) -> float:
		return self._getDoubleProperty("MP_YOUNGS_MODULUS_RES")
	def setResidualYoungsModulus(self, value: float):
		return self._setDoubleProperty("MP_YOUNGS_MODULUS_RES", value)
	def getInitialE(self) -> float:
		return self._getDoubleProperty("MP_NLI_INITIAL_E")
	def setInitialE(self, value: float):
		return self._setDoubleProperty("MP_NLI_INITIAL_E", value)
	def getAlpha(self) -> float:
		return self._getDoubleProperty("MP_NLI_ALPHA")
	def setAlpha(self, value: float):
		return self._setDoubleProperty("MP_NLI_ALPHA", value)
	def getPref(self) -> float:
		return self._getDoubleProperty("MP_NLI_PREF")
	def setPref(self, value: float):
		return self._setDoubleProperty("MP_NLI_PREF", value)
	def getAParameter(self) -> float:
		return self._getDoubleProperty("MP_NLI_A")
	def setAParameter(self, value: float):
		return self._setDoubleProperty("MP_NLI_A", value)
	def getBParameter(self) -> float:
		return self._getDoubleProperty("MP_NLI_B")
	def setBParameter(self, value: float):
		return self._setDoubleProperty("MP_NLI_B", value)
	def getMParameter(self) -> float:
		return self._getDoubleProperty("MP_NLI_M")
	def setMParameter(self, value: float):
		return self._setDoubleProperty("MP_NLI_M", value)
	def getGMax(self) -> float:
		return self._getDoubleProperty("MP_NLI_G_MAX")
	def setGMax(self, value: float):
		return self._setDoubleProperty("MP_NLI_G_MAX", value)
	def getGammaY(self) -> float:
		return self._getDoubleProperty("MP_NLI_TAU_Y")
	def setGammaY(self, value: float):
		return self._setDoubleProperty("MP_NLI_TAU_Y", value)
	def getRParameter(self) -> float:
		return self._getDoubleProperty("MP_NLI_R")
	def setRParameter(self, value: float):
		return self._setDoubleProperty("MP_NLI_R", value)
	def getUnloadingPoissonsRatio(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_POISSONS_RATIO")
	def setUnloadingPoissonsRatio(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_POISSONS_RATIO", value)
	def getUseUnloadingResidualYoungsModulus(self) -> bool:
		return self._getBoolProperty("MP_UNLOADING_USE_YOUNGS_MODULUS_RES")
	def setUseUnloadingResidualYoungsModulus(self, value: bool):
		return self._setBoolProperty("MP_UNLOADING_USE_YOUNGS_MODULUS_RES", value)
	def getUnloadingResidualYoungsModulus(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_RES")
	def setUnloadingResidualYoungsModulus(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_RES", value)
	def getUnloadingInitialE(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_NLI_INITIAL_E")
	def setUnloadingInitialE(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_NLI_INITIAL_E", value)
	def getUnloadingAlpha(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_NLI_ALPHA")
	def setUnloadingAlpha(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_NLI_ALPHA", value)
	def getUnloadingPref(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_NLI_PREF")
	def setUnloadingPref(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_NLI_PREF", value)
	def getUnloadingAParameter(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_NLI_A")
	def setUnloadingAParameter(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_NLI_A", value)
	def getUnloadingBParameter(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_NLI_B")
	def setUnloadingBParameter(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_NLI_B", value)
	def getUnloadingMParameter(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_NLI_M")
	def setUnloadingMParameter(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_NLI_M", value)
	def getUnloadingGMax(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_NLI_G_MAX")
	def setUnloadingGMax(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_NLI_G_MAX", value)
	def getUnloadingGammaY(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_NLI_TAU_Y")
	def setUnloadingGammaY(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_NLI_TAU_Y", value)
	def getUnloadingRParameter(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_NLI_R")
	def setUnloadingRParameter(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_NLI_R", value)
	def setProperties(self, UseUnloadingCondition : bool = None, UnloadingCondition : UnloadingConditions = None, NonLinearIsotropicFormula : NLIFormulaTypes = None, PoissonsRatio : float = None, UseResidualYoungsModulus : bool = None, ResidualYoungsModulus : float = None, InitialE : float = None, Alpha : float = None, Pref : float = None, AParameter : float = None, BParameter : float = None, MParameter : float = None, GMax : float = None, GammaY : float = None, RParameter : float = None, UnloadingPoissonsRatio : float = None, UseUnloadingResidualYoungsModulus : bool = None, UnloadingResidualYoungsModulus : float = None, UnloadingInitialE : float = None, UnloadingAlpha : float = None, UnloadingPref : float = None, UnloadingAParameter : float = None, UnloadingBParameter : float = None, UnloadingMParameter : float = None, UnloadingGMax : float = None, UnloadingGammaY : float = None, UnloadingRParameter : float = None):
		if UseUnloadingCondition is not None:
			self._setBoolProperty("MP_USE_UNLOADING_CONDITION", UseUnloadingCondition)
		if UnloadingCondition is not None:
			self._setEnumEUnloadingConditionsProperty("MP_UNLOADING_CONDITION", UnloadingCondition)
		if NonLinearIsotropicFormula is not None:
			self._setEnumENLIFormulaTypesProperty("MP_NLI_TYPE", NonLinearIsotropicFormula)
		if PoissonsRatio is not None:
			self._setDoubleProperty("MP_POISSONS_RATIO", PoissonsRatio)
		if UseResidualYoungsModulus is not None:
			self._setBoolProperty("MP_USE_YOUNGS_MODULUS_RES", UseResidualYoungsModulus)
		if ResidualYoungsModulus is not None:
			self._setDoubleProperty("MP_YOUNGS_MODULUS_RES", ResidualYoungsModulus)
		if InitialE is not None:
			self._setDoubleProperty("MP_NLI_INITIAL_E", InitialE)
		if Alpha is not None:
			self._setDoubleProperty("MP_NLI_ALPHA", Alpha)
		if Pref is not None:
			self._setDoubleProperty("MP_NLI_PREF", Pref)
		if AParameter is not None:
			self._setDoubleProperty("MP_NLI_A", AParameter)
		if BParameter is not None:
			self._setDoubleProperty("MP_NLI_B", BParameter)
		if MParameter is not None:
			self._setDoubleProperty("MP_NLI_M", MParameter)
		if GMax is not None:
			self._setDoubleProperty("MP_NLI_G_MAX", GMax)
		if GammaY is not None:
			self._setDoubleProperty("MP_NLI_TAU_Y", GammaY)
		if RParameter is not None:
			self._setDoubleProperty("MP_NLI_R", RParameter)
		if UnloadingPoissonsRatio is not None:
			self._setDoubleProperty("MP_UNLOADING_POISSONS_RATIO", UnloadingPoissonsRatio)
		if UseUnloadingResidualYoungsModulus is not None:
			self._setBoolProperty("MP_UNLOADING_USE_YOUNGS_MODULUS_RES", UseUnloadingResidualYoungsModulus)
		if UnloadingResidualYoungsModulus is not None:
			self._setDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_RES", UnloadingResidualYoungsModulus)
		if UnloadingInitialE is not None:
			self._setDoubleProperty("MP_UNLOADING_NLI_INITIAL_E", UnloadingInitialE)
		if UnloadingAlpha is not None:
			self._setDoubleProperty("MP_UNLOADING_NLI_ALPHA", UnloadingAlpha)
		if UnloadingPref is not None:
			self._setDoubleProperty("MP_UNLOADING_NLI_PREF", UnloadingPref)
		if UnloadingAParameter is not None:
			self._setDoubleProperty("MP_UNLOADING_NLI_A", UnloadingAParameter)
		if UnloadingBParameter is not None:
			self._setDoubleProperty("MP_UNLOADING_NLI_B", UnloadingBParameter)
		if UnloadingMParameter is not None:
			self._setDoubleProperty("MP_UNLOADING_NLI_M", UnloadingMParameter)
		if UnloadingGMax is not None:
			self._setDoubleProperty("MP_UNLOADING_NLI_G_MAX", UnloadingGMax)
		if UnloadingGammaY is not None:
			self._setDoubleProperty("MP_UNLOADING_NLI_TAU_Y", UnloadingGammaY)
		if UnloadingRParameter is not None:
			self._setDoubleProperty("MP_UNLOADING_NLI_R", UnloadingRParameter)
	def getProperties(self):
		return {
		"UseUnloadingCondition" : self.getUseUnloadingCondition(), 
		"UnloadingCondition" : self.getUnloadingCondition(), 
		"NonLinearIsotropicFormula" : self.getNonLinearIsotropicFormula(), 
		"PoissonsRatio" : self.getPoissonsRatio(), 
		"UseResidualYoungsModulus" : self.getUseResidualYoungsModulus(), 
		"ResidualYoungsModulus" : self.getResidualYoungsModulus(), 
		"InitialE" : self.getInitialE(), 
		"Alpha" : self.getAlpha(), 
		"Pref" : self.getPref(), 
		"AParameter" : self.getAParameter(), 
		"BParameter" : self.getBParameter(), 
		"MParameter" : self.getMParameter(), 
		"GMax" : self.getGMax(), 
		"GammaY" : self.getGammaY(), 
		"RParameter" : self.getRParameter(), 
		"UnloadingPoissonsRatio" : self.getUnloadingPoissonsRatio(), 
		"UseUnloadingResidualYoungsModulus" : self.getUseUnloadingResidualYoungsModulus(), 
		"UnloadingResidualYoungsModulus" : self.getUnloadingResidualYoungsModulus(), 
		"UnloadingInitialE" : self.getUnloadingInitialE(), 
		"UnloadingAlpha" : self.getUnloadingAlpha(), 
		"UnloadingPref" : self.getUnloadingPref(), 
		"UnloadingAParameter" : self.getUnloadingAParameter(), 
		"UnloadingBParameter" : self.getUnloadingBParameter(), 
		"UnloadingMParameter" : self.getUnloadingMParameter(), 
		"UnloadingGMax" : self.getUnloadingGMax(), 
		"UnloadingGammaY" : self.getUnloadingGammaY(), 
		"UnloadingRParameter" : self.getUnloadingRParameter(), 
		}
