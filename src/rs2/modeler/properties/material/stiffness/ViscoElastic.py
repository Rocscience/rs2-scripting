from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class ViscoElastic(PropertyProxy):
	def getViscoElasticType(self) -> ViscoElasticTypes:
		return ViscoElasticTypes(self._getEnumEViscoElasticTypesProperty("MP_VISCO_ELASTIC_TYPE"))
	def setViscoElasticType(self, value: ViscoElasticTypes):
		return self._setEnumEViscoElasticTypesProperty("MP_VISCO_ELASTIC_TYPE", value)
	def getBulkModulus(self) -> float:
		return self._getDoubleProperty("MP_BULK_MODULUS")
	def setBulkModulus(self, value: float):
		return self._setDoubleProperty("MP_BULK_MODULUS", value)
	def getMaxwellShearModulus(self) -> float:
		return self._getDoubleProperty("MP_MAXWELL_SHEAR_MODULUS")
	def setMaxwellShearModulus(self, value: float):
		return self._setDoubleProperty("MP_MAXWELL_SHEAR_MODULUS", value)
	def getMaxwellViscosity(self) -> float:
		return self._getDoubleProperty("MP_MAXWELL_VISCOSITY")
	def setMaxwellViscosity(self, value: float):
		return self._setDoubleProperty("MP_MAXWELL_VISCOSITY", value)
	def getKelvinShearModulus(self) -> float:
		return self._getDoubleProperty("MP_KELVIN_SHEAR_MODULUS")
	def setKelvinShearModulus(self, value: float):
		return self._setDoubleProperty("MP_KELVIN_SHEAR_MODULUS", value)
	def getKelvinViscosity(self) -> float:
		return self._getDoubleProperty("MP_KELVIN_VISCOSITY")
	def setKelvinViscosity(self, value: float):
		return self._setDoubleProperty("MP_KELVIN_VISCOSITY", value)
	def getShearModulus(self) -> float:
		return self._getDoubleProperty("MP_SHEAR_MODULUS")
	def setShearModulus(self, value: float):
		return self._setDoubleProperty("MP_SHEAR_MODULUS", value)
	def setProperties(self, ViscoElasticType : ViscoElasticTypes = None, BulkModulus : float = None, MaxwellShearModulus : float = None, MaxwellViscosity : float = None, KelvinShearModulus : float = None, KelvinViscosity : float = None, ShearModulus : float = None):
		if ViscoElasticType is not None:
			self._setEnumEViscoElasticTypesProperty("MP_VISCO_ELASTIC_TYPE", ViscoElasticType)
		if BulkModulus is not None:
			self._setDoubleProperty("MP_BULK_MODULUS", BulkModulus)
		if MaxwellShearModulus is not None:
			self._setDoubleProperty("MP_MAXWELL_SHEAR_MODULUS", MaxwellShearModulus)
		if MaxwellViscosity is not None:
			self._setDoubleProperty("MP_MAXWELL_VISCOSITY", MaxwellViscosity)
		if KelvinShearModulus is not None:
			self._setDoubleProperty("MP_KELVIN_SHEAR_MODULUS", KelvinShearModulus)
		if KelvinViscosity is not None:
			self._setDoubleProperty("MP_KELVIN_VISCOSITY", KelvinViscosity)
		if ShearModulus is not None:
			self._setDoubleProperty("MP_SHEAR_MODULUS", ShearModulus)
	def getProperties(self):
		return {
		"ViscoElasticType" : self.getViscoElasticType(), 
		"BulkModulus" : self.getBulkModulus(), 
		"MaxwellShearModulus" : self.getMaxwellShearModulus(), 
		"MaxwellViscosity" : self.getMaxwellViscosity(), 
		"KelvinShearModulus" : self.getKelvinShearModulus(), 
		"KelvinViscosity" : self.getKelvinViscosity(), 
		"ShearModulus" : self.getShearModulus(), 
		}
