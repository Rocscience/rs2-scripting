from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class EndAnchored(PropertyProxy):
	def getBoltDiameter(self) -> float:
		return self._getDoubleProperty("BP_BOLT_DIAMETER")
	def setBoltDiameter(self, value: float):
		return self._setDoubleProperty("BP_BOLT_DIAMETER", value)
	def getBoltModulusE(self) -> float:
		return self._getDoubleProperty("BP_BOLT_MODULUS")
	def setBoltModulusE(self, value: float):
		return self._setDoubleProperty("BP_BOLT_MODULUS", value)
	def getTensileCapacity(self) -> float:
		return self._getDoubleProperty("BP_TENSILE_END")
	def setTensileCapacity(self, value: float):
		return self._setDoubleProperty("BP_TENSILE_END", value)
	def getResidualTensileCapacity(self) -> float:
		return self._getDoubleProperty("BP_RES_TENSILE_END")
	def setResidualTensileCapacity(self, value: float):
		return self._setDoubleProperty("BP_RES_TENSILE_END", value)
	def getOutofPlaneSpacing(self) -> float:
		return self._getDoubleProperty("BP_OUT_OF_PLANE_SPACING_BOLT")
	def setOutofPlaneSpacing(self, value: float):
		return self._setDoubleProperty("BP_OUT_OF_PLANE_SPACING_BOLT", value)
	def getPreTensioningForce(self) -> float:
		return self._getDoubleProperty("BP_PRETENSIONING")
	def setPreTensioningForce(self, value: float):
		return self._setDoubleProperty("BP_PRETENSIONING", value)
	def getConstantPretensioningForceInInstallStage(self) -> bool:
		return self._getBoolProperty("BP_USE_CONSTANT_FORCE")
	def setConstantPretensioningForceInInstallStage(self, value: bool):
		return self._setBoolProperty("BP_USE_CONSTANT_FORCE", value)
	def setProperties(self, BoltDiameter : float = None, BoltModulusE : float = None, TensileCapacity : float = None, ResidualTensileCapacity : float = None, OutofPlaneSpacing : float = None, PreTensioningForce : float = None, ConstantPretensioningForceInInstallStage : bool = None):
		if BoltDiameter is not None:
			self._setDoubleProperty("BP_BOLT_DIAMETER", BoltDiameter)
		if BoltModulusE is not None:
			self._setDoubleProperty("BP_BOLT_MODULUS", BoltModulusE)
		if TensileCapacity is not None:
			self._setDoubleProperty("BP_TENSILE_END", TensileCapacity)
		if ResidualTensileCapacity is not None:
			self._setDoubleProperty("BP_RES_TENSILE_END", ResidualTensileCapacity)
		if OutofPlaneSpacing is not None:
			self._setDoubleProperty("BP_OUT_OF_PLANE_SPACING_BOLT", OutofPlaneSpacing)
		if PreTensioningForce is not None:
			self._setDoubleProperty("BP_PRETENSIONING", PreTensioningForce)
		if ConstantPretensioningForceInInstallStage is not None:
			self._setBoolProperty("BP_USE_CONSTANT_FORCE", ConstantPretensioningForceInInstallStage)
	def getProperties(self):
		return {
		"BoltDiameter" : self.getBoltDiameter(), 
		"BoltModulusE" : self.getBoltModulusE(), 
		"TensileCapacity" : self.getTensileCapacity(), 
		"ResidualTensileCapacity" : self.getResidualTensileCapacity(), 
		"OutofPlaneSpacing" : self.getOutofPlaneSpacing(), 
		"PreTensioningForce" : self.getPreTensioningForce(), 
		"ConstantPretensioningForceInInstallStage" : self.getConstantPretensioningForceInInstallStage(), 
		}
