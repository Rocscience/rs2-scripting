from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class TransverselyIsotropic(PropertyProxy):
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
	def getYoungsModulusE1AndEz(self) -> float:
		return self._getDoubleProperty("MP_YOUNGS_MODULUS_E1_AND_EZ")
	def setYoungsModulusE1AndEz(self, value: float):
		return self._setDoubleProperty("MP_YOUNGS_MODULUS_E1_AND_EZ", value)
	def getYoungsModulusE2(self) -> float:
		return self._getDoubleProperty("MP_YOUNGS_MODULUS_E2")
	def setYoungsModulusE2(self, value: float):
		return self._setDoubleProperty("MP_YOUNGS_MODULUS_E2", value)
	def getPoissonsRatioV12(self) -> float:
		return self._getDoubleProperty("MP_POISSONS_RATIO_V12")
	def setPoissonsRatioV12(self, value: float):
		return self._setDoubleProperty("MP_POISSONS_RATIO_V12", value)
	def getPoissonsRatioVAndV1z(self) -> float:
		return self._getDoubleProperty("MP_POISSONS_RATIO_V_AND_V1Z")
	def setPoissonsRatioVAndV1z(self, value: float):
		return self._setDoubleProperty("MP_POISSONS_RATIO_V_AND_V1Z", value)
	def getUnloadingShearModulus(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_SHEAR_MODULUS")
	def setUnloadingShearModulus(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_SHEAR_MODULUS", value)
	def getUnloadingAngleCounterclockwiseFromHorizontalToE1(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_ELASTIC_ANGLE")
	def setUnloadingAngleCounterclockwiseFromHorizontalToE1(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_ELASTIC_ANGLE", value)
	def getUnloadingYoungsModulusE1AndEz(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_E1_AND_EZ")
	def setUnloadingYoungsModulusE1AndEz(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_E1_AND_EZ", value)
	def getUnloadingYoungsModulusE2(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_E2")
	def setUnloadingYoungsModulusE2(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_E2", value)
	def getUnloadingPoissonsRatioV12(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_POISSONS_RATIO_V12")
	def setUnloadingPoissonsRatioV12(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_POISSONS_RATIO_V12", value)
	def getUnloadingPoissonsRatioVAndV1z(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_POISSONS_RATIO_V_AND_V1Z")
	def setUnloadingPoissonsRatioVAndV1z(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_POISSONS_RATIO_V_AND_V1Z", value)
	def setProperties(self, UseUnloadingCondition : bool = None, UnloadingCondition : UnloadingConditions = None, ShearModulus : float = None, AngleCounterclockwiseFromHorizontalToE1 : float = None, YoungsModulusE1AndEz : float = None, YoungsModulusE2 : float = None, PoissonsRatioV12 : float = None, PoissonsRatioVAndV1z : float = None, UnloadingShearModulus : float = None, UnloadingAngleCounterclockwiseFromHorizontalToE1 : float = None, UnloadingYoungsModulusE1AndEz : float = None, UnloadingYoungsModulusE2 : float = None, UnloadingPoissonsRatioV12 : float = None, UnloadingPoissonsRatioVAndV1z : float = None):
		if UseUnloadingCondition is not None:
			self._setBoolProperty("MP_USE_UNLOADING_CONDITION", UseUnloadingCondition)
		if UnloadingCondition is not None:
			self._setEnumEUnloadingConditionsProperty("MP_UNLOADING_CONDITION", UnloadingCondition)
		if ShearModulus is not None:
			self._setDoubleProperty("MP_SHEAR_MODULUS", ShearModulus)
		if AngleCounterclockwiseFromHorizontalToE1 is not None:
			self._setDoubleProperty("MP_ELASTIC_ANGLE", AngleCounterclockwiseFromHorizontalToE1)
		if YoungsModulusE1AndEz is not None:
			self._setDoubleProperty("MP_YOUNGS_MODULUS_E1_AND_EZ", YoungsModulusE1AndEz)
		if YoungsModulusE2 is not None:
			self._setDoubleProperty("MP_YOUNGS_MODULUS_E2", YoungsModulusE2)
		if PoissonsRatioV12 is not None:
			self._setDoubleProperty("MP_POISSONS_RATIO_V12", PoissonsRatioV12)
		if PoissonsRatioVAndV1z is not None:
			self._setDoubleProperty("MP_POISSONS_RATIO_V_AND_V1Z", PoissonsRatioVAndV1z)
		if UnloadingShearModulus is not None:
			self._setDoubleProperty("MP_UNLOADING_SHEAR_MODULUS", UnloadingShearModulus)
		if UnloadingAngleCounterclockwiseFromHorizontalToE1 is not None:
			self._setDoubleProperty("MP_UNLOADING_ELASTIC_ANGLE", UnloadingAngleCounterclockwiseFromHorizontalToE1)
		if UnloadingYoungsModulusE1AndEz is not None:
			self._setDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_E1_AND_EZ", UnloadingYoungsModulusE1AndEz)
		if UnloadingYoungsModulusE2 is not None:
			self._setDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_E2", UnloadingYoungsModulusE2)
		if UnloadingPoissonsRatioV12 is not None:
			self._setDoubleProperty("MP_UNLOADING_POISSONS_RATIO_V12", UnloadingPoissonsRatioV12)
		if UnloadingPoissonsRatioVAndV1z is not None:
			self._setDoubleProperty("MP_UNLOADING_POISSONS_RATIO_V_AND_V1Z", UnloadingPoissonsRatioVAndV1z)
	def getProperties(self):
		return {
		"UseUnloadingCondition" : self.getUseUnloadingCondition(), 
		"UnloadingCondition" : self.getUnloadingCondition(), 
		"ShearModulus" : self.getShearModulus(), 
		"AngleCounterclockwiseFromHorizontalToE1" : self.getAngleCounterclockwiseFromHorizontalToE1(), 
		"YoungsModulusE1AndEz" : self.getYoungsModulusE1AndEz(), 
		"YoungsModulusE2" : self.getYoungsModulusE2(), 
		"PoissonsRatioV12" : self.getPoissonsRatioV12(), 
		"PoissonsRatioVAndV1z" : self.getPoissonsRatioVAndV1z(), 
		"UnloadingShearModulus" : self.getUnloadingShearModulus(), 
		"UnloadingAngleCounterclockwiseFromHorizontalToE1" : self.getUnloadingAngleCounterclockwiseFromHorizontalToE1(), 
		"UnloadingYoungsModulusE1AndEz" : self.getUnloadingYoungsModulusE1AndEz(), 
		"UnloadingYoungsModulusE2" : self.getUnloadingYoungsModulusE2(), 
		"UnloadingPoissonsRatioV12" : self.getUnloadingPoissonsRatioV12(), 
		"UnloadingPoissonsRatioVAndV1z" : self.getUnloadingPoissonsRatioVAndV1z(), 
		}