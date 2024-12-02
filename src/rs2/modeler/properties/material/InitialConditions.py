from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
class InitialConditionsStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getUnitWeightFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_UNIT_WEIGHT", self.propertyID], proxyArgumentIndices=[1])
	def getPorosityValueFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_POROSITY_VALUE", self.propertyID], proxyArgumentIndices=[1])
class InitialConditionsDefinedStageFactor(InitialConditionsStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setUnitWeightFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_UNIT_WEIGHT", value, self.propertyID], proxyArgumentIndices=[2])
	def setPorosityValueFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_POROSITY_VALUE", value, self.propertyID], proxyArgumentIndices=[2])
class InitialConditions(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[InitialConditionsDefinedStageFactor, InitialConditionsStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Initial Condition Stage Factor Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[InitialConditionsDefinedStageFactor, InitialConditionsStageFactor](self._client, stageFactorInterfaceID, ID, InitialConditionsDefinedStageFactor, InitialConditionsStageFactor)
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
		return StaticWaterModes(self._getEnumEStaticWaterModesProperty("MP_INITIAL_WATER_CONDITIONS"))
	def setInitialWaterCondition(self, value: StaticWaterModes):
		return self._setEnumEStaticWaterModesProperty("MP_INITIAL_WATER_CONDITIONS", value)
	def getInitialPoreWaterPressure(self) -> float:
		return self._getDoubleProperty("MP_INITIAL_PWP")
	def setInitialPoreWaterPressure(self, value: float):
		return self._setDoubleProperty("MP_INITIAL_PWP", value)
	def getInitialRu(self) -> float:
		return self._getDoubleProperty("MP_INITIAL_RU")
	def setInitialRu(self, value: float):
		return self._setDoubleProperty("MP_INITIAL_RU", value)
	def getInitialHuType(self) -> HuTypes:
		return HuTypes(self._getEnumEHuTypesProperty("MP_INITIAL_HU_TYPE"))
	def setInitialHuType(self, value: HuTypes):
		return self._setEnumEHuTypesProperty("MP_INITIAL_HU_TYPE", value)
	def getInitialHu(self) -> float:
		return self._getDoubleProperty("MP_INITIAL_HU")
	def setInitialHu(self, value: float):
		return self._setDoubleProperty("MP_INITIAL_HU", value)
	def getInitialTemperatureCondition(self) -> StaticWaterModes:
		return StaticWaterModes(self._getEnumEStaticWaterModesProperty("MP_INITIAL_TEMPERATURE_METHOD"))
	def setInitialTemperatureCondition(self, value: StaticWaterModes):
		return self._setEnumEStaticWaterModesProperty("MP_INITIAL_TEMPERATURE_METHOD", value)
	def getInitialTemperature(self) -> float:
		return self._getDoubleProperty("MP_INITIAL_TEMPERATURE_CONST")
	def setInitialTemperature(self, value: float):
		return self._setDoubleProperty("MP_INITIAL_TEMPERATURE_CONST", value)
	def setInitialPiezoByName(self, piezoName: str):
		"""
		piezoName is the id of the piezo line to be used or "None".
		"""
		return self._callFunction("setInitialPiezoByName", [piezoName])
	def getInitialPiezoName(self) -> str:
		"""
		Returns the id of the selected initial piezoLine or "None".
		"""
		return self._callFunction("getInitialPiezoName", [])
	def setInitialGridByName(self, gridName: str):
		"""
		gridName is the name of the grid to be used. "None" and "Default Grid" are available by default.
		"""
		return self._callFunction("setInitialGridByName", [gridName])
	def getInitialGridName(self) -> str:
		return self._callFunction("getInitialGridName", [])
	def setInitialTemperatureGridByName(self, gridName: str):
		"""
		gridName is the name of the grid to be used. "None" and "Default Grid" are available by default.
		"""
		return self._callFunction("setInitialTemperatureGridByName", [gridName])
	def getInitialTemperatureGridName(self) -> str:
		return self._callFunction("getInitialTemperatureGridName", [])
	def setProperties(self, InitialElementLoading : InitialElementLoadingType = None, AccountForMoistureContentInUnitWeight : bool = None, DryUnitWeight : float = None, MoistUnitWeight : float = None, SaturatedUnitWeight : float = None, UnitWeight : float = None, PorosityValue : float = None, InitialWaterCondition : StaticWaterModes = None, InitialPoreWaterPressure : float = None, InitialRu : float = None, InitialHuType : HuTypes = None, InitialHu : float = None, InitialTemperatureCondition : StaticWaterModes = None, InitialTemperature : float = None):
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
			self._setEnumEStaticWaterModesProperty("MP_INITIAL_WATER_CONDITIONS", InitialWaterCondition)
		if InitialPoreWaterPressure is not None:
			self._setDoubleProperty("MP_INITIAL_PWP", InitialPoreWaterPressure)
		if InitialRu is not None:
			self._setDoubleProperty("MP_INITIAL_RU", InitialRu)
		if InitialHuType is not None:
			self._setEnumEHuTypesProperty("MP_INITIAL_HU_TYPE", InitialHuType)
		if InitialHu is not None:
			self._setDoubleProperty("MP_INITIAL_HU", InitialHu)
		if InitialTemperatureCondition is not None:
			self._setEnumEStaticWaterModesProperty("MP_INITIAL_TEMPERATURE_METHOD", InitialTemperatureCondition)
		if InitialTemperature is not None:
			self._setDoubleProperty("MP_INITIAL_TEMPERATURE_CONST", InitialTemperature)
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
		"InitialHuType" : self.getInitialHuType(), 
		"InitialHu" : self.getInitialHu(), 
		"InitialTemperatureCondition" : self.getInitialTemperatureCondition(), 
		"InitialTemperature" : self.getInitialTemperature(), 
		}
