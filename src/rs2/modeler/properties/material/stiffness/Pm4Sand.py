from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class Pm4Sand(PropertyProxy):
	def getG0Parameter(self) -> float:
		return self._getDoubleProperty("MP_MD_G0")
	def setG0Parameter(self, value: float):
		return self._setDoubleProperty("MP_MD_G0", value)
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
	def getAutoCalculatePSedParameter(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_P_SED")
	def setAutoCalculatePSedParameter(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_P_SED", value)
	def getPSedParameter(self) -> float:
		return self._getDoubleProperty("MP_PM4_SAND_P_SED")
	def setPSedParameter(self, value: float):
		return self._setDoubleProperty("MP_PM4_SAND_P_SED", value)
	def getPostShake(self) -> bool:
		return self._getBoolProperty("MP_PM4_POST_SHAKE")
	def setPostShake(self, value: bool):
		return self._setBoolProperty("MP_PM4_POST_SHAKE", value)
	def getAutoCalculateFSedMin(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_F_SED_MIN")
	def setAutoCalculateFSedMin(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_F_SED_MIN", value)
	def getFSedMin(self) -> float:
		return self._getDoubleProperty("MP_PM4_SAND_F_SED_MIN")
	def setFSedMin(self, value: float):
		return self._setDoubleProperty("MP_PM4_SAND_F_SED_MIN", value)
	def setProperties(self, G0Parameter : float = None, VParameter : float = None, PatmParameter : float = None, AutoCalculateCGDParameter : bool = None, CGDParameter : float = None, AutoCalculatePSedParameter : bool = None, PSedParameter : float = None, PostShake : bool = None, AutoCalculateFSedMin : bool = None, FSedMin : float = None):
		if G0Parameter is not None:
			self._setDoubleProperty("MP_MD_G0", G0Parameter)
		if VParameter is not None:
			self._setDoubleProperty("MP_MD_V", VParameter)
		if PatmParameter is not None:
			self._setDoubleProperty("MP_MD_PATM", PatmParameter)
		if AutoCalculateCGDParameter is not None:
			self._setBoolProperty("MP_USE_AUTO_C_GD", AutoCalculateCGDParameter)
		if CGDParameter is not None:
			self._setDoubleProperty("MP_PM4_C_GD", CGDParameter)
		if AutoCalculatePSedParameter is not None:
			self._setBoolProperty("MP_USE_AUTO_P_SED", AutoCalculatePSedParameter)
		if PSedParameter is not None:
			self._setDoubleProperty("MP_PM4_SAND_P_SED", PSedParameter)
		if PostShake is not None:
			self._setBoolProperty("MP_PM4_POST_SHAKE", PostShake)
		if AutoCalculateFSedMin is not None:
			self._setBoolProperty("MP_USE_AUTO_F_SED_MIN", AutoCalculateFSedMin)
		if FSedMin is not None:
			self._setDoubleProperty("MP_PM4_SAND_F_SED_MIN", FSedMin)
	def getProperties(self):
		return {
		"G0Parameter" : self.getG0Parameter(), 
		"VParameter" : self.getVParameter(), 
		"PatmParameter" : self.getPatmParameter(), 
		"AutoCalculateCGDParameter" : self.getAutoCalculateCGDParameter(), 
		"CGDParameter" : self.getCGDParameter(), 
		"AutoCalculatePSedParameter" : self.getAutoCalculatePSedParameter(), 
		"PSedParameter" : self.getPSedParameter(), 
		"PostShake" : self.getPostShake(), 
		"AutoCalculateFSedMin" : self.getAutoCalculateFSedMin(), 
		"FSedMin" : self.getFSedMin(), 
		}
