from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class EndAnchored(PropertyProxy):
	def getOutofPlaneSpacing(self) -> float:
		return self._getDoubleProperty("BP_OUT_OF_PLANE_SPACING_BOLT")
	def setOutofPlaneSpacing(self, value: float):
		return self._validateAndSetDoubleProperty("BP_OUT_OF_PLANE_SPACING_BOLT", value)
	def getBoltDiameter(self) -> float:
		return self._getDoubleProperty("BP_BOLT_DIAMETER")
	def setBoltDiameter(self, value: float):
		return self._validateAndSetDoubleProperty("BP_BOLT_DIAMETER", value)
	def getBoltModulusE(self) -> float:
		return self._getDoubleProperty("BP_BOLT_MODULUS")
	def setBoltModulusE(self, value: float):
		return self._validateAndSetDoubleProperty("BP_BOLT_MODULUS", value)
	def getPreTensioningForce(self) -> float:
		return self._getDoubleProperty("BP_PRETENSIONING")
	def setPreTensioningForce(self, value: float):
		return self._validateAndSetDoubleProperty("BP_PRETENSIONING", value)
	def getTensileCapacity(self) -> float:
		return self._getDoubleProperty("BP_TENSILE_END")
	def setTensileCapacity(self, value: float):
		return self._validateAndSetDoubleProperty("BP_TENSILE_END", value)
	def getConstantPretensioningForceInInstallStage(self) -> bool:
		return self._getBoolProperty("BP_USE_CONSTANT_FORCE")
	def setConstantPretensioningForceInInstallStage(self, value: bool):
		return self._validateAndSetBoolProperty("BP_USE_CONSTANT_FORCE", value)
	def getResidualTensileCapacity(self) -> float:
		return self._getDoubleProperty("BP_RES_TENSILE_END")
	def setResidualTensileCapacity(self, value: float):
		return self._validateAndSetDoubleProperty("BP_RES_TENSILE_END", value)
	def setProperties(self, BoltDiameter : float = None, OutofPlaneSpacing : float = None, BoltModulusE : float = None, TensileCapacity : float = None, PreTensioningForce : float = None, ResidualTensileCapacity : float = None, ConstantPretensioningForceInInstallStage : bool = None):
		if BoltDiameter is not None:
			self._validateAndSetDoubleProperty("BP_BOLT_DIAMETER", BoltDiameter)
		if OutofPlaneSpacing is not None:
			self._validateAndSetDoubleProperty("BP_OUT_OF_PLANE_SPACING_BOLT", OutofPlaneSpacing)
		if BoltModulusE is not None:
			self._validateAndSetDoubleProperty("BP_BOLT_MODULUS", BoltModulusE)
		if TensileCapacity is not None:
			self._validateAndSetDoubleProperty("BP_TENSILE_END", TensileCapacity)
		if PreTensioningForce is not None:
			self._validateAndSetDoubleProperty("BP_PRETENSIONING", PreTensioningForce)
		if ResidualTensileCapacity is not None:
			self._validateAndSetDoubleProperty("BP_RES_TENSILE_END", ResidualTensileCapacity)
		if ConstantPretensioningForceInInstallStage is not None:
			self._validateAndSetBoolProperty("BP_USE_CONSTANT_FORCE", ConstantPretensioningForceInInstallStage)