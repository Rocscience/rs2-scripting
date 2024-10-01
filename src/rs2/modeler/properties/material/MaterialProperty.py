from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.material.InitialConditions import InitialConditions
from rs2.modeler.properties.material.stiffness.Stiffness import Stiffness
from rs2.modeler.properties.material.strength.Strength import Strength
from rs2.modeler.properties.material.hydraulic.Hydraulic import Hydraulic
from rs2.modeler.properties.material.thermal.Thermal import Thermal
from rs2.modeler.properties.material.datum.Datum import Datum
from rs2.modeler.properties.material.StageFactors import StageFactors
class MaterialProperty(PropertyProxy):
	"""
	Attributes:
		StageFactors (StageFactors): Reference object for modifying property.
		InitialConditions (InitialConditions): Reference object for modifying property.
		Stiffness (Stiffness): Reference object for modifying property.
		Strength (Strength): Reference object for modifying property.
		Hydraulic (Hydraulic): Reference object for modifying property.
		Thermal (Thermal): Reference object for modifying property.
		Datum (Datum): Reference object for modifying property.

	Examples:
		:ref:`Material Example`
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		super().__init__(client, ID, documentProxyID)
		strengthStiffnessStageFactorInterface = self._callFunction("getStrengthStiffnessStageFactorInterface", [], keepReturnValueReference=True)
		datumStageFactorInterface = self._callFunction("getDatumStageFactorInterface", [], keepReturnValueReference=True)
		hydroStageFactorInterface = self._callFunction("getHydroStageFactorInterface", [], keepReturnValueReference=True)
		thermalStageFactorInterface = self._callFunction("getThermalStageFactorInterface", [], keepReturnValueReference=True)
		self.StageFactors = StageFactors(client, self._callFunction("getStageFactorManager", [], keepReturnValueReference = True))
		self.InitialConditions = InitialConditions(client, ID, documentProxyID, strengthStiffnessStageFactorInterface)
		self.Stiffness = Stiffness(client, ID, documentProxyID, strengthStiffnessStageFactorInterface)
		self.Strength = Strength(client, ID, documentProxyID, strengthStiffnessStageFactorInterface)
		self.Hydraulic = Hydraulic(client, ID, documentProxyID, hydroStageFactorInterface)
		self.Thermal = Thermal(client, ID, documentProxyID, thermalStageFactorInterface)
		self.Datum = Datum(client, ID, documentProxyID, datumStageFactorInterface)
	def getMaterialName(self) -> str:
		return self._getCStringProperty("MP_NAME")
	def setMaterialName(self, value: str):
		return self._setCStringProperty("MP_NAME", value)
	def getMaterialColor(self) -> int:
		return self._getUnsignedLongProperty("MP_COLOUR")
	def setMaterialColor(self, value: int):
		return self._setUnsignedLongProperty("MP_COLOUR", value)
	def getHatch(self) -> bool:
		return self._getBoolProperty("MP_USE_HATCH")
	def setHatch(self, value: bool):
		return self._setBoolProperty("MP_USE_HATCH", value)
	def getHatchStyle(self) -> HatchStyle:
		return HatchStyle(self._getEnumGdiplusHatchStyleProperty("MP_HATCH_STYLE"))
	def setHatchStyle(self, value: HatchStyle):
		return self._setEnumGdiplusHatchStyleProperty("MP_HATCH_STYLE", value)
	def getHatchColour(self) -> int:
		return self._getUnsignedLongProperty("MP_HATCH_COLOR")
	def setHatchColour(self, value: int):
		return self._setUnsignedLongProperty("MP_HATCH_COLOR", value)
