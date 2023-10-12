from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class InitialConditions(PropertyProxy):
	def getInitialElementLoading(self) -> InitialElementLoadingType:
		return InitialElementLoadingType(self._getEnumEInitialElementLoadingTypeProperty("MP_INITIAL_ELEMENT_LOADING"))
	def setInitialElementLoading(self, value: InitialElementLoadingType):
		return self._setEnumEInitialElementLoadingTypeProperty("MP_INITIAL_ELEMENT_LOADING", value)
	def getAccountForMoistureContentInUnitWeight(self) -> bool:
		return self._getBoolProperty("MP_ACCOUNT_MOISTURE_UNIT_WEIGHT")
	def setAccountForMoistureContentInUnitWeight(self, value: bool):
		return self._setBoolProperty("MP_ACCOUNT_MOISTURE_UNIT_WEIGHT", value)
	def getDryUnitWeight(self) -> float:
		return self._getDoubleProperty("MP_DRY_UNIT_WEIGHT")
	def setDryUnitWeight(self, value: float):
		return self._setDoubleProperty("MP_DRY_UNIT_WEIGHT", value)
	def getMoistUnitWeight(self) -> float:
		return self._getDoubleProperty("MP_MOIST_UNIT_WEIGHT")
	def setMoistUnitWeight(self, value: float):
		return self._setDoubleProperty("MP_MOIST_UNIT_WEIGHT", value)
	def getSaturatedUnitWeight(self) -> float:
		return self._getDoubleProperty("MP_SATURATED_UNIT_WEIGHT")
	def setSaturatedUnitWeight(self, value: float):
		return self._setDoubleProperty("MP_SATURATED_UNIT_WEIGHT", value)
	def getUnitWeight(self) -> float:
		return self._getDoubleProperty("MP_UNIT_WEIGHT")
	def setUnitWeight(self, value: float):
		return self._setDoubleProperty("MP_UNIT_WEIGHT", value)
	def getPorosityValue(self) -> float:
		return self._getDoubleProperty("MP_POROSITY_VALUE")
	def setPorosityValue(self, value: float):
		return self._setDoubleProperty("MP_POROSITY_VALUE", value)
	def getInitialWaterCondition(self) -> StaticWaterModes:
		return StaticWaterModes(self._getEnumEStaticWaterModesProperty(""))
	def setInitialWaterCondition(self, value: StaticWaterModes):
		return self._setEnumEStaticWaterModesProperty("", value)
	def getInitialPoreWaterPressure(self) -> float:
		return self._getDoubleProperty("")
	def setInitialPoreWaterPressure(self, value: float):
		return self._setDoubleProperty("", value)
	def getInitialRu(self) -> float:
		return self._getDoubleProperty("")
	def setInitialRu(self, value: float):
		return self._setDoubleProperty("", value)
	def getInitialPiezoToUse(self) -> int:
		return int(self._getIntProperty(""))
	def setInitialPiezoToUse(self, value: int):
		return self._setIntProperty("", value)
	def getInitialHuType(self) -> HuTypes:
		return HuTypes(self._getEnumEHuTypesProperty(""))
	def setInitialHuType(self, value: HuTypes):
		return self._setEnumEHuTypesProperty("", value)
	def getInitialHu(self) -> float:
		return self._getDoubleProperty("")
	def setInitialHu(self, value: float):
		return self._setDoubleProperty("", value)
	def getIntiialGridToUse(self) -> int:
		return int(self._getIntProperty(""))
	def setIntiialGridToUse(self, value: int):
		return self._setIntProperty("", value)
	def getInitialTemperatureCondition(self) -> StaticWaterModes:
		return StaticWaterModes(self._getEnumEStaticWaterModesProperty(""))
	def setInitialTemperatureCondition(self, value: StaticWaterModes):
		return self._setEnumEStaticWaterModesProperty("", value)
	def getInitialTemperature(self) -> float:
		return self._getDoubleProperty("")
	def setInitialTemperature(self, value: float):
		return self._setDoubleProperty("", value)
	def getInitialTemperatureGridToUse(self) -> int:
		return int(self._getIntProperty(""))
	def setInitialTemperatureGridToUse(self, value: int):
		return self._setIntProperty("", value)
	def setProperties(self, InitialElementLoading : InitialElementLoadingType = None, AccountForMoistureContentInUnitWeight : bool = None, DryUnitWeight : float = None, MoistUnitWeight : float = None, SaturatedUnitWeight : float = None, UnitWeight : float = None, PorosityValue : float = None, InitialWaterCondition : StaticWaterModes = None, InitialPoreWaterPressure : float = None, InitialRu : float = None, InitialPiezoToUse : int = None, InitialHuType : HuTypes = None, InitialHu : float = None, IntiialGridToUse : int = None, InitialTemperatureCondition : StaticWaterModes = None, InitialTemperature : float = None, InitialTemperatureGridToUse : int = None):
		if InitialElementLoading is not None:
			self._setEnumEInitialElementLoadingTypeProperty("MP_INITIAL_ELEMENT_LOADING", InitialElementLoading)
		if AccountForMoistureContentInUnitWeight is not None:
			self._setBoolProperty("MP_ACCOUNT_MOISTURE_UNIT_WEIGHT", AccountForMoistureContentInUnitWeight)
		if DryUnitWeight is not None:
			self._setDoubleProperty("MP_DRY_UNIT_WEIGHT", DryUnitWeight)
		if MoistUnitWeight is not None:
			self._setDoubleProperty("MP_MOIST_UNIT_WEIGHT", MoistUnitWeight)
		if SaturatedUnitWeight is not None:
			self._setDoubleProperty("MP_SATURATED_UNIT_WEIGHT", SaturatedUnitWeight)
		if UnitWeight is not None:
			self._setDoubleProperty("MP_UNIT_WEIGHT", UnitWeight)
		if PorosityValue is not None:
			self._setDoubleProperty("MP_POROSITY_VALUE", PorosityValue)
		if InitialWaterCondition is not None:
			self._setEnumEStaticWaterModesProperty("", InitialWaterCondition)
		if InitialPoreWaterPressure is not None:
			self._setDoubleProperty("", InitialPoreWaterPressure)
		if InitialRu is not None:
			self._setDoubleProperty("", InitialRu)
		if InitialPiezoToUse is not None:
			self._setIntProperty("", InitialPiezoToUse)
		if InitialHuType is not None:
			self._setEnumEHuTypesProperty("", InitialHuType)
		if InitialHu is not None:
			self._setDoubleProperty("", InitialHu)
		if IntiialGridToUse is not None:
			self._setIntProperty("", IntiialGridToUse)
		if InitialTemperatureCondition is not None:
			self._setEnumEStaticWaterModesProperty("", InitialTemperatureCondition)
		if InitialTemperature is not None:
			self._setDoubleProperty("", InitialTemperature)
		if InitialTemperatureGridToUse is not None:
			self._setIntProperty("", InitialTemperatureGridToUse)
	def getProperties(self):
		return {
		"InitialElementLoading" : self.getInitialElementLoading(), 
		"AccountForMoistureContentInUnitWeight" : self.getAccountForMoistureContentInUnitWeight(), 
		"DryUnitWeight" : self.getDryUnitWeight(), 
		"MoistUnitWeight" : self.getMoistUnitWeight(), 
		"SaturatedUnitWeight" : self.getSaturatedUnitWeight(), 
		"UnitWeight" : self.getUnitWeight(), 
		"PorosityValue" : self.getPorosityValue(), 
		"InitialWaterCondition" : self.getInitialWaterCondition(), 
		"InitialPoreWaterPressure" : self.getInitialPoreWaterPressure(), 
		"InitialRu" : self.getInitialRu(), 
		"InitialPiezoToUse" : self.getInitialPiezoToUse(), 
		"InitialHuType" : self.getInitialHuType(), 
		"InitialHu" : self.getInitialHu(), 
		"IntiialGridToUse" : self.getIntiialGridToUse(), 
		"InitialTemperatureCondition" : self.getInitialTemperatureCondition(), 
		"InitialTemperature" : self.getInitialTemperature(), 
		"InitialTemperatureGridToUse" : self.getInitialTemperatureGridToUse(), 
		}
