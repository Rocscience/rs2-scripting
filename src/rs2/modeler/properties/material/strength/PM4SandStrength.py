from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class PM4SandStrength(PropertyProxy):
	def getDr(self) -> float:
		return self._getDoubleProperty("MP_PM4_SAND_DR")
	def setDr(self, value: float):
		return self._setDoubleProperty("MP_PM4_SAND_DR", value)
	def getQParameter(self) -> float:
		return self._getDoubleProperty("MP_PM4_SAND_Q")
	def setQParameter(self, value: float):
		return self._setDoubleProperty("MP_PM4_SAND_Q", value)
	def getRParameter(self) -> float:
		return self._getDoubleProperty("MP_PM4_SAND_R")
	def setRParameter(self, value: float):
		return self._setDoubleProperty("MP_PM4_SAND_R", value)
	def getEMax(self) -> float:
		return self._getDoubleProperty("MP_PM4_SAND_E_MAX")
	def setEMax(self, value: float):
		return self._setDoubleProperty("MP_PM4_SAND_E_MAX", value)
	def getEMin(self) -> float:
		return self._getDoubleProperty("MP_PM4_SAND_E_MIN")
	def setEMin(self, value: float):
		return self._setDoubleProperty("MP_PM4_SAND_E_MIN", value)
	def getPhiCv(self) -> float:
		return self._getDoubleProperty("MP_PM4_PHI_CV")
	def setPhiCv(self, value: float):
		return self._setDoubleProperty("MP_PM4_PHI_CV", value)
	def getNbParameter(self) -> float:
		return self._getDoubleProperty("MP_PLASTIC_MODULUS_NB")
	def setNbParameter(self, value: float):
		return self._setDoubleProperty("MP_PLASTIC_MODULUS_NB", value)
	def getNdParameter(self) -> float:
		return self._getDoubleProperty("MP_DILATANCY_ND")
	def setNdParameter(self, value: float):
		return self._setDoubleProperty("MP_DILATANCY_ND", value)
	def getAutoCalculateADoParameter(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_A_DO")
	def setAutoCalculateADoParameter(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_A_DO", value)
	def getADoParameter(self) -> float:
		return self._getDoubleProperty("MP_PM4_A_DO")
	def setADoParameter(self, value: float):
		return self._setDoubleProperty("MP_PM4_A_DO", value)
	def getHp0Parameter(self) -> float:
		return self._getDoubleProperty("MP_PM4_HP0")
	def setHp0Parameter(self, value: float):
		return self._setDoubleProperty("MP_PM4_HP0", value)
	def getAutoCalculateCDRParameter(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_C_DR")
	def setAutoCalculateCDRParameter(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_C_DR", value)
	def getCDRParameter(self) -> float:
		return self._getDoubleProperty("MP_PM4_SAND_C_DR")
	def setCDRParameter(self, value: float):
		return self._setDoubleProperty("MP_PM4_SAND_C_DR", value)
	def getAutoCalculateCEpsParameter(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_C_EPS")
	def setAutoCalculateCEpsParameter(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_C_EPS", value)
	def getCEpsParameter(self) -> float:
		return self._getDoubleProperty("MP_PM4_C_EPS")
	def setCEpsParameter(self, value: float):
		return self._setDoubleProperty("MP_PM4_C_EPS", value)
	def getYieldSurfaceM(self) -> float:
		return self._getDoubleProperty("MP_YIELD_SURFACE_M")
	def setYieldSurfaceM(self, value: float):
		return self._setDoubleProperty("MP_YIELD_SURFACE_M", value)
	def getAutoCalculateH0Parameter(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_H0")
	def setAutoCalculateH0Parameter(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_H0", value)
	def getH0Parameter(self) -> float:
		return self._getDoubleProperty("MP_PLASTIC_MODULUS_H0")
	def setH0Parameter(self, value: float):
		return self._setDoubleProperty("MP_PLASTIC_MODULUS_H0", value)
	def getAutoCalculateCKafParameter(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_C_KAF")
	def setAutoCalculateCKafParameter(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_C_KAF", value)
	def getCKafParameter(self) -> float:
		return self._getDoubleProperty("MP_PM4_C_KAF")
	def setCKafParameter(self, value: float):
		return self._setDoubleProperty("MP_PM4_C_KAF", value)
	def getAutoCalculateZmax(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_Z_MAX")
	def setAutoCalculateZmax(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_Z_MAX", value)
	def getZmax(self) -> float:
		return self._getDoubleProperty("MP_FABRIC_DILATANCY_TENSOR_ZMAX")
	def setZmax(self, value: float):
		return self._setDoubleProperty("MP_FABRIC_DILATANCY_TENSOR_ZMAX", value)
	def getAutoCalculateCzParameter(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_C_Z")
	def setAutoCalculateCzParameter(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_C_Z", value)
	def getCzParameter(self) -> float:
		return self._getDoubleProperty("MP_FABRIC_DILATANCY_TENSOR_CZ")
	def setCzParameter(self, value: float):
		return self._setDoubleProperty("MP_FABRIC_DILATANCY_TENSOR_CZ", value)
	def setProperties(self, Dr : float = None, QParameter : float = None, RParameter : float = None, EMax : float = None, EMin : float = None, PhiCv : float = None, NbParameter : float = None, NdParameter : float = None, AutoCalculateADoParameter : bool = None, ADoParameter : float = None, Hp0Parameter : float = None, AutoCalculateCDRParameter : bool = None, CDRParameter : float = None, AutoCalculateCEpsParameter : bool = None, CEpsParameter : float = None, YieldSurfaceM : float = None, AutoCalculateH0Parameter : bool = None, H0Parameter : float = None, AutoCalculateCKafParameter : bool = None, CKafParameter : float = None, AutoCalculateZmax : bool = None, Zmax : float = None, AutoCalculateCzParameter : bool = None, CzParameter : float = None):
		if Dr is not None:
			self._setDoubleProperty("MP_PM4_SAND_DR", Dr)
		if QParameter is not None:
			self._setDoubleProperty("MP_PM4_SAND_Q", QParameter)
		if RParameter is not None:
			self._setDoubleProperty("MP_PM4_SAND_R", RParameter)
		if EMax is not None:
			self._setDoubleProperty("MP_PM4_SAND_E_MAX", EMax)
		if EMin is not None:
			self._setDoubleProperty("MP_PM4_SAND_E_MIN", EMin)
		if PhiCv is not None:
			self._setDoubleProperty("MP_PM4_PHI_CV", PhiCv)
		if NbParameter is not None:
			self._setDoubleProperty("MP_PLASTIC_MODULUS_NB", NbParameter)
		if NdParameter is not None:
			self._setDoubleProperty("MP_DILATANCY_ND", NdParameter)
		if AutoCalculateADoParameter is not None:
			self._setBoolProperty("MP_USE_AUTO_A_DO", AutoCalculateADoParameter)
		if ADoParameter is not None:
			self._setDoubleProperty("MP_PM4_A_DO", ADoParameter)
		if Hp0Parameter is not None:
			self._setDoubleProperty("MP_PM4_HP0", Hp0Parameter)
		if AutoCalculateCDRParameter is not None:
			self._setBoolProperty("MP_USE_AUTO_C_DR", AutoCalculateCDRParameter)
		if CDRParameter is not None:
			self._setDoubleProperty("MP_PM4_SAND_C_DR", CDRParameter)
		if AutoCalculateCEpsParameter is not None:
			self._setBoolProperty("MP_USE_AUTO_C_EPS", AutoCalculateCEpsParameter)
		if CEpsParameter is not None:
			self._setDoubleProperty("MP_PM4_C_EPS", CEpsParameter)
		if YieldSurfaceM is not None:
			self._setDoubleProperty("MP_YIELD_SURFACE_M", YieldSurfaceM)
		if AutoCalculateH0Parameter is not None:
			self._setBoolProperty("MP_USE_AUTO_H0", AutoCalculateH0Parameter)
		if H0Parameter is not None:
			self._setDoubleProperty("MP_PLASTIC_MODULUS_H0", H0Parameter)
		if AutoCalculateCKafParameter is not None:
			self._setBoolProperty("MP_USE_AUTO_C_KAF", AutoCalculateCKafParameter)
		if CKafParameter is not None:
			self._setDoubleProperty("MP_PM4_C_KAF", CKafParameter)
		if AutoCalculateZmax is not None:
			self._setBoolProperty("MP_USE_AUTO_Z_MAX", AutoCalculateZmax)
		if Zmax is not None:
			self._setDoubleProperty("MP_FABRIC_DILATANCY_TENSOR_ZMAX", Zmax)
		if AutoCalculateCzParameter is not None:
			self._setBoolProperty("MP_USE_AUTO_C_Z", AutoCalculateCzParameter)
		if CzParameter is not None:
			self._setDoubleProperty("MP_FABRIC_DILATANCY_TENSOR_CZ", CzParameter)
	def getProperties(self):
		return {
		"Dr" : self.getDr(), 
		"QParameter" : self.getQParameter(), 
		"RParameter" : self.getRParameter(), 
		"EMax" : self.getEMax(), 
		"EMin" : self.getEMin(), 
		"PhiCv" : self.getPhiCv(), 
		"NbParameter" : self.getNbParameter(), 
		"NdParameter" : self.getNdParameter(), 
		"AutoCalculateADoParameter" : self.getAutoCalculateADoParameter(), 
		"ADoParameter" : self.getADoParameter(), 
		"Hp0Parameter" : self.getHp0Parameter(), 
		"AutoCalculateCDRParameter" : self.getAutoCalculateCDRParameter(), 
		"CDRParameter" : self.getCDRParameter(), 
		"AutoCalculateCEpsParameter" : self.getAutoCalculateCEpsParameter(), 
		"CEpsParameter" : self.getCEpsParameter(), 
		"YieldSurfaceM" : self.getYieldSurfaceM(), 
		"AutoCalculateH0Parameter" : self.getAutoCalculateH0Parameter(), 
		"H0Parameter" : self.getH0Parameter(), 
		"AutoCalculateCKafParameter" : self.getAutoCalculateCKafParameter(), 
		"CKafParameter" : self.getCKafParameter(), 
		"AutoCalculateZmax" : self.getAutoCalculateZmax(), 
		"Zmax" : self.getZmax(), 
		"AutoCalculateCzParameter" : self.getAutoCalculateCzParameter(), 
		"CzParameter" : self.getCzParameter(), 
		}
