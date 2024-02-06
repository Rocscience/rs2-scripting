from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class Pm4Silt(PropertyProxy):
	def getG0Parameter(self) -> float:
		return self._getDoubleProperty("MP_MD_G0")
	def setG0Parameter(self, value: float):
		return self._setDoubleProperty("MP_MD_G0", value)
	def getAutoCalculateNGParameter(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_NG")
	def setAutoCalculateNGParameter(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_NG", value)
	def getNGParameter(self) -> float:
		return self._getDoubleProperty("MP_PM4_SILT_NG")
	def setNGParameter(self, value: float):
		return self._setDoubleProperty("MP_PM4_SILT_NG", value)
	def getAutoCalculateVParameter(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_V")
	def setAutoCalculateVParameter(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_V", value)
	def getVParameter(self) -> float:
		return self._getDoubleProperty("MP_MD_V")
	def setVParameter(self, value: float):
		return self._setDoubleProperty("MP_MD_V", value)
	def getPatmParameter(self) -> float:
		return self._getDoubleProperty("MP_MD_PATM")
	def setPatmParameter(self, value: float):
		return self._setDoubleProperty("MP_MD_PATM", value)
	def getAutoCalculateCGDParameter(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_C_GD")
	def setAutoCalculateCGDParameter(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_C_GD", value)
	def getCGDParameter(self) -> float:
		return self._getDoubleProperty("MP_PM4_C_GD")
	def setCGDParameter(self, value: float):
		return self._setDoubleProperty("MP_PM4_C_GD", value)
	def getAutoCalculateCGCParameter(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_C_GC")
	def setAutoCalculateCGCParameter(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_C_GC", value)
	def getCGCParameter(self) -> float:
		return self._getDoubleProperty("MP_PM4_SILT_C_GC")
	def setCGCParameter(self, value: float):
		return self._setDoubleProperty("MP_PM4_SILT_C_GC", value)
	def getPostShake(self) -> bool:
		return self._getBoolProperty("MP_PM4_POST_SHAKE")
	def setPostShake(self, value: bool):
		return self._setBoolProperty("MP_PM4_POST_SHAKE", value)
	def setProperties(self, G0Parameter : float = None, AutoCalculateNGParameter : bool = None, NGParameter : float = None, AutoCalculateVParameter : bool = None, VParameter : float = None, PatmParameter : float = None, AutoCalculateCGDParameter : bool = None, CGDParameter : float = None, AutoCalculateCGCParameter : bool = None, CGCParameter : float = None, PostShake : bool = None):
		if G0Parameter is not None:
			self._setDoubleProperty("MP_MD_G0", G0Parameter)
		if AutoCalculateNGParameter is not None:
			self._setBoolProperty("MP_USE_AUTO_NG", AutoCalculateNGParameter)
		if NGParameter is not None:
			self._setDoubleProperty("MP_PM4_SILT_NG", NGParameter)
		if AutoCalculateVParameter is not None:
			self._setBoolProperty("MP_USE_AUTO_V", AutoCalculateVParameter)
		if VParameter is not None:
			self._setDoubleProperty("MP_MD_V", VParameter)
		if PatmParameter is not None:
			self._setDoubleProperty("MP_MD_PATM", PatmParameter)
		if AutoCalculateCGDParameter is not None:
			self._setBoolProperty("MP_USE_AUTO_C_GD", AutoCalculateCGDParameter)
		if CGDParameter is not None:
			self._setDoubleProperty("MP_PM4_C_GD", CGDParameter)
		if AutoCalculateCGCParameter is not None:
			self._setBoolProperty("MP_USE_AUTO_C_GC", AutoCalculateCGCParameter)
		if CGCParameter is not None:
			self._setDoubleProperty("MP_PM4_SILT_C_GC", CGCParameter)
		if PostShake is not None:
			self._setBoolProperty("MP_PM4_POST_SHAKE", PostShake)
	def getProperties(self):
		return {
		"G0Parameter" : self.getG0Parameter(), 
		"AutoCalculateNGParameter" : self.getAutoCalculateNGParameter(), 
		"NGParameter" : self.getNGParameter(), 
		"AutoCalculateVParameter" : self.getAutoCalculateVParameter(), 
		"VParameter" : self.getVParameter(), 
		"PatmParameter" : self.getPatmParameter(), 
		"AutoCalculateCGDParameter" : self.getAutoCalculateCGDParameter(), 
		"CGDParameter" : self.getCGDParameter(), 
		"AutoCalculateCGCParameter" : self.getAutoCalculateCGCParameter(), 
		"CGCParameter" : self.getCGCParameter(), 
		"PostShake" : self.getPostShake(), 
		}
