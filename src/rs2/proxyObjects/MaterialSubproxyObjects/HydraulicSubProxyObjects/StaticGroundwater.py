from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class StaticGroundwater(PropertyProxy):
	def getStaticWaterMode(self) -> StaticWaterModes:
		return StaticWaterModes(self._getEnumEStaticWaterModesProperty("MP_STATIC_WATER_MODE"))
	def setStaticWaterMode(self, value: StaticWaterModes):
		return self._setEnumEStaticWaterModesProperty("MP_STATIC_WATER_MODE", value)
	def getStaticPoreWaterPressure(self) -> float:
		return self._getDoubleProperty("MP_CONSTANT_PWP")
	def setStaticPoreWaterPressure(self, value: float):
		return self._setDoubleProperty("MP_CONSTANT_PWP", value)
	def getRuValue(self) -> float:
		return self._getDoubleProperty("MP_RU_VALUE")
	def setRuValue(self, value: float):
		return self._setDoubleProperty("MP_RU_VALUE", value)
	def getHuType(self) -> HuTypes:
		return HuTypes(self._getEnumEHuTypesProperty("MP_HU_TYPE"))
	def setHuType(self, value: HuTypes):
		return self._setEnumEHuTypesProperty("MP_HU_TYPE", value)
	def getHuValue(self) -> float:
		return self._getDoubleProperty("MP_HU_VALUE")
	def setHuValue(self, value: float):
		return self._setDoubleProperty("MP_HU_VALUE", value)
	def setProperties(self, StaticWaterMode : StaticWaterModes = None, StaticPoreWaterPressure : float = None, RuValue : float = None, HuType : HuTypes = None, HuValue : float = None):
		if StaticWaterMode is not None:
			self._setEnumEStaticWaterModesProperty("MP_STATIC_WATER_MODE", StaticWaterMode)
		if StaticPoreWaterPressure is not None:
			self._setDoubleProperty("MP_CONSTANT_PWP", StaticPoreWaterPressure)
		if RuValue is not None:
			self._setDoubleProperty("MP_RU_VALUE", RuValue)
		if HuType is not None:
			self._setEnumEHuTypesProperty("MP_HU_TYPE", HuType)
		if HuValue is not None:
			self._setDoubleProperty("MP_HU_VALUE", HuValue)
	def getProperties(self):
		return {
		"StaticWaterMode" : self.getStaticWaterMode(), 
		"StaticPoreWaterPressure" : self.getStaticPoreWaterPressure(), 
		"RuValue" : self.getRuValue(), 
		"HuType" : self.getHuType(), 
		"HuValue" : self.getHuValue(), 
		}
