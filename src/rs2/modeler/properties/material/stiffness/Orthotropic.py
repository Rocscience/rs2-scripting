from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class Orthotropic(PropertyProxy):
	def getUseUnloadingCondition(self) -> bool:
		return self._getBoolProperty("MP_USE_UNLOADING_CONDITION")
	def setUseUnloadingCondition(self, value: bool):
		return self._setBoolProperty("MP_USE_UNLOADING_CONDITION", value)
	def getUnloadingCondition(self) -> UnloadingConditions:
		return UnloadingConditions(self._getEnumEUnloadingConditionsProperty("MP_UNLOADING_CONDITION"))
	def setUnloadingCondition(self, value: UnloadingConditions):
		return self._setEnumEUnloadingConditionsProperty("MP_UNLOADING_CONDITION", value)
	def getShearModulus(self) -> float:
		return self._getDoubleProperty("MP_SHEAR_MODULUS")
	def setShearModulus(self, value: float):
		return self._setDoubleProperty("MP_SHEAR_MODULUS", value)
	def getAngleCounterclockwiseFromHorizontalToE1(self) -> float:
		return self._getDoubleProperty("MP_ELASTIC_ANGLE")
	def setAngleCounterclockwiseFromHorizontalToE1(self, value: float):
		return self._setDoubleProperty("MP_ELASTIC_ANGLE", value)
	def getYoungsModulusE1(self) -> float:
		return self._getDoubleProperty("MP_YOUNGS_MODULUS_E1")
	def setYoungsModulusE1(self, value: float):
		return self._setDoubleProperty("MP_YOUNGS_MODULUS_E1", value)
	def getYoungsModulusE2(self) -> float:
		return self._getDoubleProperty("MP_YOUNGS_MODULUS_E2")
	def setYoungsModulusE2(self, value: float):
		return self._setDoubleProperty("MP_YOUNGS_MODULUS_E2", value)
	def getYoungsModulusEZ(self) -> float:
		return self._getDoubleProperty("MP_YOUNGS_MODULUS_EZ")
	def setYoungsModulusEZ(self, value: float):
		return self._setDoubleProperty("MP_YOUNGS_MODULUS_EZ", value)
	def getPoissonsRatioV12(self) -> float:
		return self._getDoubleProperty("MP_POISSONS_RATIO_V12")
	def setPoissonsRatioV12(self, value: float):
		return self._setDoubleProperty("MP_POISSONS_RATIO_V12", value)
	def getPoissonsRatioV2(self) -> float:
		return self._getDoubleProperty("MP_POISSONS_RATIO_V2")
	def setPoissonsRatioV2(self, value: float):
		return self._setDoubleProperty("MP_POISSONS_RATIO_V2", value)
	def getPoissonsRatioV2z(self) -> float:
		return self._getDoubleProperty("MP_POISSONS_RATIO_V2Z")
	def setPoissonsRatioV2z(self, value: float):
		return self._setDoubleProperty("MP_POISSONS_RATIO_V2Z", value)
	def getUnloadingShearModulus(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_SHEAR_MODULUS")
	def setUnloadingShearModulus(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_SHEAR_MODULUS", value)
	def getUnloadingAngleCounterclockwiseFromHorizontalToE1(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_ELASTIC_ANGLE")
	def setUnloadingAngleCounterclockwiseFromHorizontalToE1(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_ELASTIC_ANGLE", value)
	def getUnloadingYoungsModulusE1(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_E1")
	def setUnloadingYoungsModulusE1(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_E1", value)
	def getUnloadingYoungsModulusE2(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_E2")
	def setUnloadingYoungsModulusE2(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_E2", value)
	def getUnloadingYoungsModulusEZ(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_EZ")
	def setUnloadingYoungsModulusEZ(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_EZ", value)
	def getUnloadingPoissonsRatioV12(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_POISSONS_RATIO_V12")
	def setUnloadingPoissonsRatioV12(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_POISSONS_RATIO_V12", value)
	def getUnloadingPoissonsRatioV2(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_POISSONS_RATIO_V2")
	def setUnloadingPoissonsRatioV2(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_POISSONS_RATIO_V2", value)
	def getUnloadingPoissonsRatioV2z(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_POISSONS_RATIO_V2Z")
	def setUnloadingPoissonsRatioV2z(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_POISSONS_RATIO_V2Z", value)
	def setProperties(self, UseUnloadingCondition : bool = None, UnloadingCondition : UnloadingConditions = None, ShearModulus : float = None, AngleCounterclockwiseFromHorizontalToE1 : float = None, YoungsModulusE1 : float = None, YoungsModulusE2 : float = None, YoungsModulusEZ : float = None, PoissonsRatioV12 : float = None, PoissonsRatioV2 : float = None, PoissonsRatioV2z : float = None, UnloadingShearModulus : float = None, UnloadingAngleCounterclockwiseFromHorizontalToE1 : float = None, UnloadingYoungsModulusE1 : float = None, UnloadingYoungsModulusE2 : float = None, UnloadingYoungsModulusEZ : float = None, UnloadingPoissonsRatioV12 : float = None, UnloadingPoissonsRatioV2 : float = None, UnloadingPoissonsRatioV2z : float = None):
		if UseUnloadingCondition is not None:
			self._setBoolProperty("MP_USE_UNLOADING_CONDITION", UseUnloadingCondition)
		if UnloadingCondition is not None:
			self._setEnumEUnloadingConditionsProperty("MP_UNLOADING_CONDITION", UnloadingCondition)
		if ShearModulus is not None:
			self._setDoubleProperty("MP_SHEAR_MODULUS", ShearModulus)
		if AngleCounterclockwiseFromHorizontalToE1 is not None:
			self._setDoubleProperty("MP_ELASTIC_ANGLE", AngleCounterclockwiseFromHorizontalToE1)
		if YoungsModulusE1 is not None:
			self._setDoubleProperty("MP_YOUNGS_MODULUS_E1", YoungsModulusE1)
		if YoungsModulusE2 is not None:
			self._setDoubleProperty("MP_YOUNGS_MODULUS_E2", YoungsModulusE2)
		if YoungsModulusEZ is not None:
			self._setDoubleProperty("MP_YOUNGS_MODULUS_EZ", YoungsModulusEZ)
		if PoissonsRatioV12 is not None:
			self._setDoubleProperty("MP_POISSONS_RATIO_V12", PoissonsRatioV12)
		if PoissonsRatioV2 is not None:
			self._setDoubleProperty("MP_POISSONS_RATIO_V2", PoissonsRatioV2)
		if PoissonsRatioV2z is not None:
			self._setDoubleProperty("MP_POISSONS_RATIO_V2Z", PoissonsRatioV2z)
		if UnloadingShearModulus is not None:
			self._setDoubleProperty("MP_UNLOADING_SHEAR_MODULUS", UnloadingShearModulus)
		if UnloadingAngleCounterclockwiseFromHorizontalToE1 is not None:
			self._setDoubleProperty("MP_UNLOADING_ELASTIC_ANGLE", UnloadingAngleCounterclockwiseFromHorizontalToE1)
		if UnloadingYoungsModulusE1 is not None:
			self._setDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_E1", UnloadingYoungsModulusE1)
		if UnloadingYoungsModulusE2 is not None:
			self._setDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_E2", UnloadingYoungsModulusE2)
		if UnloadingYoungsModulusEZ is not None:
			self._setDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_EZ", UnloadingYoungsModulusEZ)
		if UnloadingPoissonsRatioV12 is not None:
			self._setDoubleProperty("MP_UNLOADING_POISSONS_RATIO_V12", UnloadingPoissonsRatioV12)
		if UnloadingPoissonsRatioV2 is not None:
			self._setDoubleProperty("MP_UNLOADING_POISSONS_RATIO_V2", UnloadingPoissonsRatioV2)
		if UnloadingPoissonsRatioV2z is not None:
			self._setDoubleProperty("MP_UNLOADING_POISSONS_RATIO_V2Z", UnloadingPoissonsRatioV2z)
	def getProperties(self):
		return {
		"UseUnloadingCondition" : self.getUseUnloadingCondition(), 
		"UnloadingCondition" : self.getUnloadingCondition(), 
		"ShearModulus" : self.getShearModulus(), 
		"AngleCounterclockwiseFromHorizontalToE1" : self.getAngleCounterclockwiseFromHorizontalToE1(), 
		"YoungsModulusE1" : self.getYoungsModulusE1(), 
		"YoungsModulusE2" : self.getYoungsModulusE2(), 
		"YoungsModulusEZ" : self.getYoungsModulusEZ(), 
		"PoissonsRatioV12" : self.getPoissonsRatioV12(), 
		"PoissonsRatioV2" : self.getPoissonsRatioV2(), 
		"PoissonsRatioV2z" : self.getPoissonsRatioV2z(), 
		"UnloadingShearModulus" : self.getUnloadingShearModulus(), 
		"UnloadingAngleCounterclockwiseFromHorizontalToE1" : self.getUnloadingAngleCounterclockwiseFromHorizontalToE1(), 
		"UnloadingYoungsModulusE1" : self.getUnloadingYoungsModulusE1(), 
		"UnloadingYoungsModulusE2" : self.getUnloadingYoungsModulusE2(), 
		"UnloadingYoungsModulusEZ" : self.getUnloadingYoungsModulusEZ(), 
		"UnloadingPoissonsRatioV12" : self.getUnloadingPoissonsRatioV12(), 
		"UnloadingPoissonsRatioV2" : self.getUnloadingPoissonsRatioV2(), 
		"UnloadingPoissonsRatioV2z" : self.getUnloadingPoissonsRatioV2z(), 
		}