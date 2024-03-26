from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class PM4SiltStrength(PropertyProxy):
	def getAutoCalculateSuParameter(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_SU")
	def setAutoCalculateSuParameter(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_SU", value)
	def getSuParameter(self) -> float:
		return self._getDoubleProperty("MP_PM4_SILT_SU")
	def setSuParameter(self, value: float):
		return self._setDoubleProperty("MP_PM4_SILT_SU", value)
	def getSuRatioParameter(self) -> float:
		return self._getDoubleProperty("MP_PM4_SILT_SU_RATIO")
	def setSuRatioParameter(self, value: float):
		return self._setDoubleProperty("MP_PM4_SILT_SU_RATIO", value)
	def getAutoCalculateEInitial(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_E_INITIAL")
	def setAutoCalculateEInitial(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_E_INITIAL", value)
	def getEInitial(self) -> float:
		return self._getDoubleProperty("MP_PM4_SILT_E_INITIAL")
	def setEInitial(self, value: float):
		return self._setDoubleProperty("MP_PM4_SILT_E_INITIAL", value)
	def getAutoCalculateLambda(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_LAMBDA")
	def setAutoCalculateLambda(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_LAMBDA", value)
	def getLambda(self) -> float:
		return self._getDoubleProperty("MP_PM4_SILT_LAMBDA")
	def setLambda(self, value: float):
		return self._setDoubleProperty("MP_PM4_SILT_LAMBDA", value)
	def getAutoCalculateFsu(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_FSU")
	def setAutoCalculateFsu(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_FSU", value)
	def getFsu(self) -> float:
		return self._getDoubleProperty("MP_PM4_SILT_FSU")
	def setFsu(self, value: float):
		return self._setDoubleProperty("MP_PM4_SILT_FSU", value)
	def getAutoCalculatePhiCv(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_PHI_CV")
	def setAutoCalculatePhiCv(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_PHI_CV", value)
	def getPhiCv(self) -> float:
		return self._getDoubleProperty("MP_PM4_PHI_CV")
	def setPhiCv(self, value: float):
		return self._setDoubleProperty("MP_PM4_PHI_CV", value)
	def getAutoCalculateNbWet(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_N_B_WET")
	def setAutoCalculateNbWet(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_N_B_WET", value)
	def getNbWet(self) -> float:
		return self._getDoubleProperty("MP_PM4_SILT_N_B_WET")
	def setNbWet(self, value: float):
		return self._setDoubleProperty("MP_PM4_SILT_N_B_WET", value)
	def getAutoCalculateNbDry(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_N_B_DRY")
	def setAutoCalculateNbDry(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_N_B_DRY", value)
	def getNbDry(self) -> float:
		return self._getDoubleProperty("MP_PM4_SILT_N_B_DRY")
	def setNbDry(self, value: float):
		return self._setDoubleProperty("MP_PM4_SILT_N_B_DRY", value)
	def getAutoCalculateNdParameter(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_ND")
	def setAutoCalculateNdParameter(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_ND", value)
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
	def getAutoCalculateRuMax(self) -> bool:
		return self._getBoolProperty("MP_USE_AUTO_RU_MAX")
	def setAutoCalculateRuMax(self, value: bool):
		return self._setBoolProperty("MP_USE_AUTO_RU_MAX", value)
	def getRuMax(self) -> float:
		return self._getDoubleProperty("MP_PM4_SILT_RU_MAX")
	def setRuMax(self, value: float):
		return self._setDoubleProperty("MP_PM4_SILT_RU_MAX", value)
	def getHp0Parameter(self) -> float:
		return self._getDoubleProperty("MP_PM4_HP0")
	def setHp0Parameter(self, value: float):
		return self._setDoubleProperty("MP_PM4_HP0", value)
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
	def setProperties(self, AutoCalculateSuParameter : bool = None, SuParameter : float = None, SuRatioParameter : float = None, AutoCalculateEInitial : bool = None, EInitial : float = None, AutoCalculateLambda : bool = None, Lambda : float = None, AutoCalculateFsu : bool = None, Fsu : float = None, AutoCalculatePhiCv : bool = None, PhiCv : float = None, AutoCalculateNbWet : bool = None, NbWet : float = None, AutoCalculateNbDry : bool = None, NbDry : float = None, AutoCalculateNdParameter : bool = None, NdParameter : float = None, AutoCalculateADoParameter : bool = None, ADoParameter : float = None, AutoCalculateRuMax : bool = None, RuMax : float = None, Hp0Parameter : float = None, AutoCalculateCEpsParameter : bool = None, CEpsParameter : float = None, YieldSurfaceM : float = None, AutoCalculateH0Parameter : bool = None, H0Parameter : float = None, AutoCalculateCKafParameter : bool = None, CKafParameter : float = None, AutoCalculateZmax : bool = None, Zmax : float = None, AutoCalculateCzParameter : bool = None, CzParameter : float = None):
		if AutoCalculateSuParameter is not None:
			self._setBoolProperty("MP_USE_AUTO_SU", AutoCalculateSuParameter)
		if SuParameter is not None:
			self._setDoubleProperty("MP_PM4_SILT_SU", SuParameter)
		if SuRatioParameter is not None:
			self._setDoubleProperty("MP_PM4_SILT_SU_RATIO", SuRatioParameter)
		if AutoCalculateEInitial is not None:
			self._setBoolProperty("MP_USE_AUTO_E_INITIAL", AutoCalculateEInitial)
		if EInitial is not None:
			self._setDoubleProperty("MP_PM4_SILT_E_INITIAL", EInitial)
		if AutoCalculateLambda is not None:
			self._setBoolProperty("MP_USE_AUTO_LAMBDA", AutoCalculateLambda)
		if Lambda is not None:
			self._setDoubleProperty("MP_PM4_SILT_LAMBDA", Lambda)
		if AutoCalculateFsu is not None:
			self._setBoolProperty("MP_USE_AUTO_FSU", AutoCalculateFsu)
		if Fsu is not None:
			self._setDoubleProperty("MP_PM4_SILT_FSU", Fsu)
		if AutoCalculatePhiCv is not None:
			self._setBoolProperty("MP_USE_AUTO_PHI_CV", AutoCalculatePhiCv)
		if PhiCv is not None:
			self._setDoubleProperty("MP_PM4_PHI_CV", PhiCv)
		if AutoCalculateNbWet is not None:
			self._setBoolProperty("MP_USE_AUTO_N_B_WET", AutoCalculateNbWet)
		if NbWet is not None:
			self._setDoubleProperty("MP_PM4_SILT_N_B_WET", NbWet)
		if AutoCalculateNbDry is not None:
			self._setBoolProperty("MP_USE_AUTO_N_B_DRY", AutoCalculateNbDry)
		if NbDry is not None:
			self._setDoubleProperty("MP_PM4_SILT_N_B_DRY", NbDry)
		if AutoCalculateNdParameter is not None:
			self._setBoolProperty("MP_USE_AUTO_ND", AutoCalculateNdParameter)
		if NdParameter is not None:
			self._setDoubleProperty("MP_DILATANCY_ND", NdParameter)
		if AutoCalculateADoParameter is not None:
			self._setBoolProperty("MP_USE_AUTO_A_DO", AutoCalculateADoParameter)
		if ADoParameter is not None:
			self._setDoubleProperty("MP_PM4_A_DO", ADoParameter)
		if AutoCalculateRuMax is not None:
			self._setBoolProperty("MP_USE_AUTO_RU_MAX", AutoCalculateRuMax)
		if RuMax is not None:
			self._setDoubleProperty("MP_PM4_SILT_RU_MAX", RuMax)
		if Hp0Parameter is not None:
			self._setDoubleProperty("MP_PM4_HP0", Hp0Parameter)
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
		"AutoCalculateSuParameter" : self.getAutoCalculateSuParameter(), 
		"SuParameter" : self.getSuParameter(), 
		"SuRatioParameter" : self.getSuRatioParameter(), 
		"AutoCalculateEInitial" : self.getAutoCalculateEInitial(), 
		"EInitial" : self.getEInitial(), 
		"AutoCalculateLambda" : self.getAutoCalculateLambda(), 
		"Lambda" : self.getLambda(), 
		"AutoCalculateFsu" : self.getAutoCalculateFsu(), 
		"Fsu" : self.getFsu(), 
		"AutoCalculatePhiCv" : self.getAutoCalculatePhiCv(), 
		"PhiCv" : self.getPhiCv(), 
		"AutoCalculateNbWet" : self.getAutoCalculateNbWet(), 
		"NbWet" : self.getNbWet(), 
		"AutoCalculateNbDry" : self.getAutoCalculateNbDry(), 
		"NbDry" : self.getNbDry(), 
		"AutoCalculateNdParameter" : self.getAutoCalculateNdParameter(), 
		"NdParameter" : self.getNdParameter(), 
		"AutoCalculateADoParameter" : self.getAutoCalculateADoParameter(), 
		"ADoParameter" : self.getADoParameter(), 
		"AutoCalculateRuMax" : self.getAutoCalculateRuMax(), 
		"RuMax" : self.getRuMax(), 
		"Hp0Parameter" : self.getHp0Parameter(), 
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
