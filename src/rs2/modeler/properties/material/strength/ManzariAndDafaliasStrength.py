from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class ManzariAndDafaliasStrength(PropertyProxy):
	def getCriticalStateM(self) -> float:
		return self._getDoubleProperty("MP_CRITICAL_STATE_M")
	def setCriticalStateM(self, value: float):
		return self._setDoubleProperty("MP_CRITICAL_STATE_M", value)
	def getCParameter(self) -> float:
		return self._getDoubleProperty("MP_CRITICAL_STATE_C")
	def setCParameter(self, value: float):
		return self._setDoubleProperty("MP_CRITICAL_STATE_C", value)
	def getLambdaC(self) -> float:
		return self._getDoubleProperty("MP_CRITICAL_STATE_LAMBDA_C")
	def setLambdaC(self, value: float):
		return self._setDoubleProperty("MP_CRITICAL_STATE_LAMBDA_C", value)
	def getE0Parameter(self) -> float:
		return self._getDoubleProperty("MP_CRITICAL_STATE_E0")
	def setE0Parameter(self, value: float):
		return self._setDoubleProperty("MP_CRITICAL_STATE_E0", value)
	def getXiParameter(self) -> float:
		return self._getDoubleProperty("MP_CRITICAL_STATE_XI")
	def setXiParameter(self, value: float):
		return self._setDoubleProperty("MP_CRITICAL_STATE_XI", value)
	def getYieldSurfaceM(self) -> float:
		return self._getDoubleProperty("MP_YIELD_SURFACE_M")
	def setYieldSurfaceM(self, value: float):
		return self._setDoubleProperty("MP_YIELD_SURFACE_M", value)
	def getH0Parameter(self) -> float:
		return self._getDoubleProperty("MP_PLASTIC_MODULUS_H0")
	def setH0Parameter(self, value: float):
		return self._setDoubleProperty("MP_PLASTIC_MODULUS_H0", value)
	def getChParameter(self) -> float:
		return self._getDoubleProperty("MP_PLASTIC_MODULUS_CH")
	def setChParameter(self, value: float):
		return self._setDoubleProperty("MP_PLASTIC_MODULUS_CH", value)
	def getNbParameter(self) -> float:
		return self._getDoubleProperty("MP_PLASTIC_MODULUS_NB")
	def setNbParameter(self, value: float):
		return self._setDoubleProperty("MP_PLASTIC_MODULUS_NB", value)
	def getA0Parameter(self) -> float:
		return self._getDoubleProperty("MP_DILATANCY_A0")
	def setA0Parameter(self, value: float):
		return self._setDoubleProperty("MP_DILATANCY_A0", value)
	def getNdParameter(self) -> float:
		return self._getDoubleProperty("MP_DILATANCY_ND")
	def setNdParameter(self, value: float):
		return self._setDoubleProperty("MP_DILATANCY_ND", value)
	def getZmax(self) -> float:
		return self._getDoubleProperty("MP_FABRIC_DILATANCY_TENSOR_ZMAX")
	def setZmax(self, value: float):
		return self._setDoubleProperty("MP_FABRIC_DILATANCY_TENSOR_ZMAX", value)
	def getCzParameter(self) -> float:
		return self._getDoubleProperty("MP_FABRIC_DILATANCY_TENSOR_CZ")
	def setCzParameter(self, value: float):
		return self._setDoubleProperty("MP_FABRIC_DILATANCY_TENSOR_CZ", value)
	def getApplySSRShearStrengthReduction(self) -> bool:
		return self._getBoolProperty("MP_APPLY_SSR")
	def setApplySSRShearStrengthReduction(self, value: bool):
		return self._setBoolProperty("MP_APPLY_SSR", value)
	def setProperties(self, CriticalStateM : float = None, CParameter : float = None, LambdaC : float = None, E0Parameter : float = None, XiParameter : float = None, YieldSurfaceM : float = None, H0Parameter : float = None, ChParameter : float = None, NbParameter : float = None, A0Parameter : float = None, NdParameter : float = None, Zmax : float = None, CzParameter : float = None, ApplySSRShearStrengthReduction : bool = None):
		if CriticalStateM is not None:
			self._setDoubleProperty("MP_CRITICAL_STATE_M", CriticalStateM)
		if CParameter is not None:
			self._setDoubleProperty("MP_CRITICAL_STATE_C", CParameter)
		if LambdaC is not None:
			self._setDoubleProperty("MP_CRITICAL_STATE_LAMBDA_C", LambdaC)
		if E0Parameter is not None:
			self._setDoubleProperty("MP_CRITICAL_STATE_E0", E0Parameter)
		if XiParameter is not None:
			self._setDoubleProperty("MP_CRITICAL_STATE_XI", XiParameter)
		if YieldSurfaceM is not None:
			self._setDoubleProperty("MP_YIELD_SURFACE_M", YieldSurfaceM)
		if H0Parameter is not None:
			self._setDoubleProperty("MP_PLASTIC_MODULUS_H0", H0Parameter)
		if ChParameter is not None:
			self._setDoubleProperty("MP_PLASTIC_MODULUS_CH", ChParameter)
		if NbParameter is not None:
			self._setDoubleProperty("MP_PLASTIC_MODULUS_NB", NbParameter)
		if A0Parameter is not None:
			self._setDoubleProperty("MP_DILATANCY_A0", A0Parameter)
		if NdParameter is not None:
			self._setDoubleProperty("MP_DILATANCY_ND", NdParameter)
		if Zmax is not None:
			self._setDoubleProperty("MP_FABRIC_DILATANCY_TENSOR_ZMAX", Zmax)
		if CzParameter is not None:
			self._setDoubleProperty("MP_FABRIC_DILATANCY_TENSOR_CZ", CzParameter)
		if ApplySSRShearStrengthReduction is not None:
			self._setBoolProperty("MP_APPLY_SSR", ApplySSRShearStrengthReduction)
	def getProperties(self):
		return {
		"CriticalStateM" : self.getCriticalStateM(), 
		"CParameter" : self.getCParameter(), 
		"LambdaC" : self.getLambdaC(), 
		"E0Parameter" : self.getE0Parameter(), 
		"XiParameter" : self.getXiParameter(), 
		"YieldSurfaceM" : self.getYieldSurfaceM(), 
		"H0Parameter" : self.getH0Parameter(), 
		"ChParameter" : self.getChParameter(), 
		"NbParameter" : self.getNbParameter(), 
		"A0Parameter" : self.getA0Parameter(), 
		"NdParameter" : self.getNdParameter(), 
		"Zmax" : self.getZmax(), 
		"CzParameter" : self.getCzParameter(), 
		"ApplySSRShearStrengthReduction" : self.getApplySSRShearStrengthReduction(), 
		}
