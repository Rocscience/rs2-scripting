from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class CoteAndKonrad(PropertyProxy):
	def getParticleConductivity(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_PARTICLE_CONDUCTIVITY")
	def setParticleConductivity(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_PARTICLE_CONDUCTIVITY", value)
	def getUnfrozenKappa(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_UNFROZEN_KAPPA")
	def setUnfrozenKappa(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_UNFROZEN_KAPPA", value)
	def getFrozenKappa(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_FROZEN_KAPPA")
	def setFrozenKappa(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_FROZEN_KAPPA", value)
	def getChi(self) -> float:
		return self._getDoubleProperty("MP_CHI")
	def setChi(self, value: float):
		return self._setDoubleProperty("MP_CHI", value)
	def getEta(self) -> float:
		return self._getDoubleProperty("MP_ETA")
	def setEta(self, value: float):
		return self._setDoubleProperty("MP_ETA", value)
	def setProperties(self, ParticleConductivity : float = None, UnfrozenKappa : float = None, FrozenKappa : float = None, Chi : float = None, Eta : float = None):
		if ParticleConductivity is not None:
			self._setDoubleProperty("MP_THERMAL_PARTICLE_CONDUCTIVITY", ParticleConductivity)
		if UnfrozenKappa is not None:
			self._setDoubleProperty("MP_THERMAL_UNFROZEN_KAPPA", UnfrozenKappa)
		if FrozenKappa is not None:
			self._setDoubleProperty("MP_THERMAL_FROZEN_KAPPA", FrozenKappa)
		if Chi is not None:
			self._setDoubleProperty("MP_CHI", Chi)
		if Eta is not None:
			self._setDoubleProperty("MP_ETA", Eta)
	def getProperties(self):
		return {
		"ParticleConductivity" : self.getParticleConductivity(), 
		"UnfrozenKappa" : self.getUnfrozenKappa(), 
		"FrozenKappa" : self.getFrozenKappa(), 
		"Chi" : self.getChi(), 
		"Eta" : self.getEta(), 
		}
