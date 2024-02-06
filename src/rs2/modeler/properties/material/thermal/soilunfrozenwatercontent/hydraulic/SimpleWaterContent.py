from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class SimpleWaterContent(PropertyProxy):
	def getSoilType(self) -> EnhancedSimpleSoilTypes:
		return EnhancedSimpleSoilTypes(self._getEnumEEnhancedSimpleSoilTypesProperty("MP_SOIL_TYPE_THERMAL"))
	def setSoilType(self, value: EnhancedSimpleSoilTypes):
		return self._setEnumEEnhancedSimpleSoilTypesProperty("MP_SOIL_TYPE_THERMAL", value)
	def setProperties(self, SoilType : EnhancedSimpleSoilTypes = None):
		if SoilType is not None:
			self._setEnumEEnhancedSimpleSoilTypesProperty("MP_SOIL_TYPE_THERMAL", SoilType)
	def getProperties(self):
		return {
		"SoilType" : self.getSoilType(), 
		}
