from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
class StaticGroundwaterStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getPiezoToUse(self) -> str:
		return self._callFunction("getPiezoToUse", [self.propertyID], proxyArgumentIndices=[0])
	def getGridToUse(self) -> str:
		return self._callFunction("getGridToUse", [self.propertyID], proxyArgumentIndices=[0])
class StaticGroundwaterDefinedStageFactor(StaticGroundwaterStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setPiezoToUse(self, piezoName: str):
		return self._callFunction("setPiezoToUse", [piezoName, self.propertyID], proxyArgumentIndices=[1])
	def setGridToUse(self, gridName: str):
		return self._callFunction("setGridToUse", [gridName, self.propertyID], proxyArgumentIndices=[1])
class StaticGroundwater(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[StaticGroundwaterDefinedStageFactor, StaticGroundwaterStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Hydraulic Property Static Groundwater Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[StaticGroundwaterDefinedStageFactor, StaticGroundwaterStageFactor](self._client, stageFactorInterfaceID, ID, StaticGroundwaterDefinedStageFactor, StaticGroundwaterStageFactor)
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
	def setPiezoToUse(self, piezoName: str):
		"""
		piezoName is the id of the piezo line to be used or "None".
		"""
		return self._callFunction("setPiezoToUse", [piezoName])
	def getPiezoToUse(self) -> str:
		"""
		Returns the id of the piezo line to be used or "None".
		"""
		return self._callFunction("getPiezoToUse", [])
	def setGridToUse(self, gridName: str):
		"""
		gridName is the name of the grid to be used. "None" and "Default Grid" are available by default.
		"""
		return self._callFunction("setGridToUse", [gridName])
	def getGridToUse(self) -> str:
		return self._callFunction("getGridToUse", [])
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
