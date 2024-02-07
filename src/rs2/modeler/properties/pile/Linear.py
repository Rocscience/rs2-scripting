from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class Linear(PropertyProxy):
	def getShearStiffness(self) -> float:
		return self._getDoubleProperty("PFP_SHEAR_STIFFNESS")
	def setShearStiffness(self, value: float):
		return self._setDoubleProperty("PFP_SHEAR_STIFFNESS", value)
	def getNormalStiffness(self) -> float:
		return self._getDoubleProperty("PFP_NORMAL_STIFFNESS")
	def setNormalStiffness(self, value: float):
		return self._setDoubleProperty("PFP_NORMAL_STIFFNESS", value)
	def getMaxTractionAtTheTop(self) -> float:
		return self._getDoubleProperty("PFP_MAX_TRACTION_TOP")
	def setMaxTractionAtTheTop(self, value: float):
		return self._setDoubleProperty("PFP_MAX_TRACTION_TOP", value)
	def getMaxTractionAtTheBottom(self) -> float:
		return self._getDoubleProperty("PFP_MAT_TRACTION_BOTTOM")
	def setMaxTractionAtTheBottom(self, value: float):
		return self._setDoubleProperty("PFP_MAT_TRACTION_BOTTOM", value)
	def getUseBaseResistance(self) -> bool:
		return self._getBoolProperty("PFP_USE_BASE_RESISTANCE")
	def setUseBaseResistance(self, value: bool):
		return self._setBoolProperty("PFP_USE_BASE_RESISTANCE", value)
	def getBaseNormalStiffness(self) -> float:
		return self._getDoubleProperty("PFP_BASE_NORMAL_STIFFNESS")
	def setBaseNormalStiffness(self, value: float):
		return self._setDoubleProperty("PFP_BASE_NORMAL_STIFFNESS", value)
	def getBaseForceResistance(self) -> float:
		return self._getDoubleProperty("PFP_BASE_FORCE_RESISTANCE")
	def setBaseForceResistance(self, value: float):
		return self._setDoubleProperty("PFP_BASE_FORCE_RESISTANCE", value)
	def setProperties(self, ShearStiffness : float = None, NormalStiffness : float = None, MaxTractionAtTheTop : float = None, MaxTractionAtTheBottom : float = None, UseBaseResistance : bool = None, BaseNormalStiffness : float = None, BaseForceResistance : float = None):
		if ShearStiffness is not None:
			self._setDoubleProperty("PFP_SHEAR_STIFFNESS", ShearStiffness)
		if NormalStiffness is not None:
			self._setDoubleProperty("PFP_NORMAL_STIFFNESS", NormalStiffness)
		if MaxTractionAtTheTop is not None:
			self._setDoubleProperty("PFP_MAX_TRACTION_TOP", MaxTractionAtTheTop)
		if MaxTractionAtTheBottom is not None:
			self._setDoubleProperty("PFP_MAT_TRACTION_BOTTOM", MaxTractionAtTheBottom)
		if UseBaseResistance is not None:
			self._setBoolProperty("PFP_USE_BASE_RESISTANCE", UseBaseResistance)
		if BaseNormalStiffness is not None:
			self._setDoubleProperty("PFP_BASE_NORMAL_STIFFNESS", BaseNormalStiffness)
		if BaseForceResistance is not None:
			self._setDoubleProperty("PFP_BASE_FORCE_RESISTANCE", BaseForceResistance)
	def getProperties(self):
		return {
		"ShearStiffness" : self.getShearStiffness(), 
		"NormalStiffness" : self.getNormalStiffness(), 
		"MaxTractionAtTheTop" : self.getMaxTractionAtTheTop(), 
		"MaxTractionAtTheBottom" : self.getMaxTractionAtTheBottom(), 
		"UseBaseResistance" : self.getUseBaseResistance(), 
		"BaseNormalStiffness" : self.getBaseNormalStiffness(), 
		"BaseForceResistance" : self.getBaseForceResistance(), 
		}
