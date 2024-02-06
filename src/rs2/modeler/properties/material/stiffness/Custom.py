from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class Custom(PropertyProxy):
	def getUseUnloadingCondition(self) -> bool:
		return self._getBoolProperty("MP_USE_UNLOADING_CONDITION")
	def setUseUnloadingCondition(self, value: bool):
		return self._setBoolProperty("MP_USE_UNLOADING_CONDITION", value)
	def getUnloadingCondition(self) -> UnloadingConditions:
		return UnloadingConditions(self._getEnumEUnloadingConditionsProperty("MP_UNLOADING_CONDITION"))
	def setUnloadingCondition(self, value: UnloadingConditions):
		return self._setEnumEUnloadingConditionsProperty("MP_UNLOADING_CONDITION", value)
	def getCustomMode(self) -> CustomMode:
		return CustomMode(self._getEnumECustomModeProperty("MP_CUSTOM_MODE"))
	def setCustomMode(self, value: CustomMode):
		return self._setEnumECustomModeProperty("MP_CUSTOM_MODE", value)
	def getUseConstantPoissonsRatio(self) -> bool:
		return self._getBoolProperty("MP_USE_CONSTANT_POISSONS_RATIO")
	def setUseConstantPoissonsRatio(self, value: bool):
		return self._setBoolProperty("MP_USE_CONSTANT_POISSONS_RATIO", value)
	def getConstantPoissonsRatio(self) -> float:
		return self._getDoubleProperty("MP_CONSTANT_POISSONS_RATIO")
	def setConstantPoissonsRatio(self, value: float):
		return self._setDoubleProperty("MP_CONSTANT_POISSONS_RATIO", value)
	def getUnloadingUseConstantPoissonsRatio(self) -> bool:
		return self._getBoolProperty("MP_UNLOADING_USE_CONSTANT_POISSONS_RATIO")
	def setUnloadingUseConstantPoissonsRatio(self, value: bool):
		return self._setBoolProperty("MP_UNLOADING_USE_CONSTANT_POISSONS_RATIO", value)
	def getUnloadingConstantPoissonsRatio(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_CONSTANT_POISSONS_RATIO")
	def setUnloadingConstantPoissonsRatio(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_CONSTANT_POISSONS_RATIO", value)
	def setCustomStiffnessLoadingTable(self, mode: CustomMode, table: list[tuple[float,float,float]]):
		"""
		Tuple element order: (Custom Mode Parameter (p,q,S3...), Young's modulus, Poisson's Ratio).
		Poisson's ratio set to zero if useContantPoissonsRatio is set to True.
		"""
		return self._callFunction("setCustomStiffnessLoadingTable", [mode.value, table])
	def getCustomStiffnessLoadingTable(self) -> list[tuple[float,float,float]]:
		"""
		Tuple element order: (Custom Mode Parameter (p,q,S3...), Young's modulus, Poisson's Ratio).
		Poisson's ratio set to zero if useContantPoissonsRatio is set to True.
		"""
		return self._callFunction("getCustomStiffnessLoadingTable", [])
	def setCustomStiffnessUnloadingTable(self, mode: CustomMode, table: list[tuple[float,float,float]]):
		"""
		Tuple element order: (Custom Mode Parameter (p,q,S3...), Young's modulus, Poisson's Ratio).
		Poisson's ratio set to zero and ignored if useContantPoissonsRatio is set to True.
		"""
		return self._callFunction("setCustomStiffnessUnloadingTable", [mode.value, table])
	def getCustomStiffnessUnloadingTable(self) -> list[tuple[float,float,float]]:
		"""
		Tuple element order: (Custom Mode Parameter (p,q,S3...), Young's modulus, Poisson's Ratio).
		Poisson's ratio set to zero and ignored if useContantPoissonsRatio is set to True.
		"""
		return self._callFunction("getCustomStiffnessUnloadingTable", [])
	def setProperties(self, UseUnloadingCondition : bool = None, UnloadingCondition : UnloadingConditions = None, CustomMode : CustomMode = None, UseConstantPoissonsRatio : bool = None, ConstantPoissonsRatio : float = None, UnloadingUseConstantPoissonsRatio : bool = None, UnloadingConstantPoissonsRatio : float = None):
		if UseUnloadingCondition is not None:
			self._setBoolProperty("MP_USE_UNLOADING_CONDITION", UseUnloadingCondition)
		if UnloadingCondition is not None:
			self._setEnumEUnloadingConditionsProperty("MP_UNLOADING_CONDITION", UnloadingCondition)
		if CustomMode is not None:
			self._setEnumECustomModeProperty("MP_CUSTOM_MODE", CustomMode)
		if UseConstantPoissonsRatio is not None:
			self._setBoolProperty("MP_USE_CONSTANT_POISSONS_RATIO", UseConstantPoissonsRatio)
		if ConstantPoissonsRatio is not None:
			self._setDoubleProperty("MP_CONSTANT_POISSONS_RATIO", ConstantPoissonsRatio)
		if UnloadingUseConstantPoissonsRatio is not None:
			self._setBoolProperty("MP_UNLOADING_USE_CONSTANT_POISSONS_RATIO", UnloadingUseConstantPoissonsRatio)
		if UnloadingConstantPoissonsRatio is not None:
			self._setDoubleProperty("MP_UNLOADING_CONSTANT_POISSONS_RATIO", UnloadingConstantPoissonsRatio)
	def getProperties(self):
		return {
		"UseUnloadingCondition" : self.getUseUnloadingCondition(), 
		"UnloadingCondition" : self.getUnloadingCondition(), 
		"CustomMode" : self.getCustomMode(), 
		"UseConstantPoissonsRatio" : self.getUseConstantPoissonsRatio(), 
		"ConstantPoissonsRatio" : self.getConstantPoissonsRatio(), 
		"UnloadingUseConstantPoissonsRatio" : self.getUnloadingUseConstantPoissonsRatio(), 
		"UnloadingConstantPoissonsRatio" : self.getUnloadingConstantPoissonsRatio(), 
		}
