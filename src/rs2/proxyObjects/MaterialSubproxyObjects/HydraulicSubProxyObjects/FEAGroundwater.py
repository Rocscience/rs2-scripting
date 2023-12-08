from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.proxyObjects.MaterialSubproxyObjects.HydraulicSubProxyObjects.FEAGroundwaterProxies.Simple import Simple
from rs2.proxyObjects.MaterialSubproxyObjects.HydraulicSubProxyObjects.FEAGroundwaterProxies.Fredlund import Fredlund
from rs2.proxyObjects.MaterialSubproxyObjects.HydraulicSubProxyObjects.FEAGroundwaterProxies.Genuchten import Genuchten
from rs2.proxyObjects.MaterialSubproxyObjects.HydraulicSubProxyObjects.FEAGroundwaterProxies.Brooks import Brooks
from rs2.proxyObjects.MaterialSubproxyObjects.HydraulicSubProxyObjects.FEAGroundwaterProxies.Gardner import Gardner
from rs2.proxyObjects.MaterialSubproxyObjects.HydraulicSubProxyObjects.FEAGroundwaterProxies.Constant import Constant
from rs2.proxyObjects.MaterialSubproxyObjects.HydraulicSubProxyObjects.FEAGroundwaterProxies.UserDefined import UserDefined
class FEAGroundwater(PropertyProxy):
	"""
	:ref:`Hydraulic Property FEAGroundwater Example`
	"""
	def __init__(self, server : Client, ID, documentProxyID):
		self.Simple = Simple(server, ID, documentProxyID)
		self.Fredlund = Fredlund(server, ID, documentProxyID)
		self.Genuchten = Genuchten(server, ID, documentProxyID)
		self.Brooks = Brooks(server, ID, documentProxyID)
		self.Gardner = Gardner(server, ID, documentProxyID)
		self.Constant = Constant(server, ID, documentProxyID)
		self.UserDefined = UserDefined(server, ID, documentProxyID)
		super().__init__(server, ID, documentProxyID)
	def getModel(self) -> GroundWaterModes:
		return GroundWaterModes(self._getEnumEGroundWaterModesProperty("MP_HYDRAULIC_MODEL"))
	def setModel(self, value: GroundWaterModes):
		return self._setEnumEGroundWaterModesProperty("MP_HYDRAULIC_MODEL", value)
	def getK2K1(self) -> float:
		return self._getDoubleProperty("MP_K2_K1")
	def setK2K1(self, value: float):
		return self._setDoubleProperty("MP_K2_K1", value)
	def getK1Definition(self) -> AnisotropyDefinitions:
		return AnisotropyDefinitions(self._getEnumEAnisotropyDefinitionsProperty("MP_K1_DEFINITION"))
	def setK1Definition(self, value: AnisotropyDefinitions):
		return self._setEnumEAnisotropyDefinitionsProperty("MP_K1_DEFINITION", value)
	def getK1Angle(self) -> float:
		return self._getDoubleProperty("MP_K1_ANGLE")
	def setK1Angle(self, value: float):
		return self._setDoubleProperty("MP_K1_ANGLE", value)
	def getMvModel(self) -> MVModel:
		return MVModel(self._getEnumEMVModelProperty("MP_MV_MODEL"))
	def setMvModel(self, value: MVModel):
		return self._setEnumEMVModelProperty("MP_MV_MODEL", value)
	def getMv(self) -> float:
		return self._getDoubleProperty("MP_MV")
	def setMv(self, value: float):
		return self._setDoubleProperty("MP_MV", value)
