from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class Norsand(PropertyProxy):
	def getShearModulusAtReferencePressure(self) -> float:
		return self._getDoubleProperty("MP_NS_SHEAR_MODULUS")
	def setShearModulusAtReferencePressure(self, value: float):
		return self._setDoubleProperty("MP_NS_SHEAR_MODULUS", value)
	def getReferencePressureForShearModulus(self) -> float:
		return self._getDoubleProperty("MP_NS_REF_PRESSURE")
	def setReferencePressureForShearModulus(self, value: float):
		return self._setDoubleProperty("MP_NS_REF_PRESSURE", value)
	def getModulusExponent(self) -> float:
		return self._getDoubleProperty("MP_NS_MODULUS_EXP")
	def setModulusExponent(self, value: float):
		return self._setDoubleProperty("MP_NS_MODULUS_EXP", value)
	def getPoissonsRatio(self) -> float:
		return self._getDoubleProperty("MP_NS_POISSONS")
	def setPoissonsRatio(self, value: float):
		return self._setDoubleProperty("MP_NS_POISSONS", value)
	def getMinimumShearModulus(self) -> float:
		return self._getDoubleProperty("MP_NS_MIN_SHEAR_MODULUS")
	def setMinimumShearModulus(self, value: float):
		return self._setDoubleProperty("MP_NS_MIN_SHEAR_MODULUS", value)
	def setProperties(self, ShearModulusAtReferencePressure : float = None, ReferencePressureForShearModulus : float = None, ModulusExponent : float = None, PoissonsRatio : float = None, MinimumShearModulus : float = None):
		if ShearModulusAtReferencePressure is not None:
			self._setDoubleProperty("MP_NS_SHEAR_MODULUS", ShearModulusAtReferencePressure)
		if ReferencePressureForShearModulus is not None:
			self._setDoubleProperty("MP_NS_REF_PRESSURE", ReferencePressureForShearModulus)
		if ModulusExponent is not None:
			self._setDoubleProperty("MP_NS_MODULUS_EXP", ModulusExponent)
		if PoissonsRatio is not None:
			self._setDoubleProperty("MP_NS_POISSONS", PoissonsRatio)
		if MinimumShearModulus is not None:
			self._setDoubleProperty("MP_NS_MIN_SHEAR_MODULUS", MinimumShearModulus)
	def getProperties(self):
		return {
		"ShearModulusAtReferencePressure" : self.getShearModulusAtReferencePressure(), 
		"ReferencePressureForShearModulus" : self.getReferencePressureForShearModulus(), 
		"ModulusExponent" : self.getModulusExponent(), 
		"PoissonsRatio" : self.getPoissonsRatio(), 
		"MinimumShearModulus" : self.getMinimumShearModulus(), 
		}
