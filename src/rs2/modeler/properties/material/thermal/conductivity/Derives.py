from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class Derives(PropertyProxy):
	def getParticleConductivity(self) -> float:
		return self._getDoubleProperty("MP_THERMAL_PARTICLE_CONDUCTIVITY")
	def setParticleConductivity(self, value: float):
		return self._setDoubleProperty("MP_THERMAL_PARTICLE_CONDUCTIVITY", value)
	def setProperties(self, ParticleConductivity : float = None):
		if ParticleConductivity is not None:
			self._setDoubleProperty("MP_THERMAL_PARTICLE_CONDUCTIVITY", ParticleConductivity)
	def getProperties(self):
		return {
		"ParticleConductivity" : self.getParticleConductivity(), 
		}
