from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.proxyObjects.JointSubproxyObjects.MohrCoulomb import MohrCoulomb
from rs2.proxyObjects.JointSubproxyObjects.BartonBandis import BartonBandis
from rs2.proxyObjects.JointSubproxyObjects.GeosyntheticHyperbolic import GeosyntheticHyperbolic
from rs2.proxyObjects.JointSubproxyObjects.HyperbolicSoftening import HyperbolicSoftening
from rs2.proxyObjects.JointSubproxyObjects.MaterialDependent import MaterialDependent
from rs2.proxyObjects.JointSubproxyObjects.DisplacementDependent import DisplacementDependent
class JointProperty(PropertyProxy):
	"""
	:ref:`Joint Example`
	"""
	def __init__(self, server : Client, ID, documentProxyID):
		self.MohrCoulomb = MohrCoulomb(server, ID, documentProxyID)
		self.BartonBandis = BartonBandis(server, ID, documentProxyID)
		self.GeosyntheticHyperbolic = GeosyntheticHyperbolic(server, ID, documentProxyID)
		self.HyperbolicSoftening = HyperbolicSoftening(server, ID, documentProxyID)
		self.MaterialDependent = MaterialDependent(server, ID, documentProxyID)
		self.DisplacementDependent = DisplacementDependent(server, ID, documentProxyID)
		super().__init__(server, ID, documentProxyID)
	def getJointName(self) -> str:
		return self._getCStringProperty("JP_NAME")
	def setJointName(self, value: str):
		return self._setCStringProperty("JP_NAME", value)
	def getJointColor(self) -> int:
		return self._getUnsignedLongProperty("JP_COLOR")
	def setJointColor(self, value: int):
		return self._setUnsignedLongProperty("JP_COLOR", value)
	def getSlipCriterion(self) -> JointTypes:
		return JointTypes(self._getEnumEJointTypesProperty("JP_SLIP_CRITIRION"))
	def setSlipCriterion(self, value: JointTypes):
		return self._setEnumEJointTypesProperty("JP_SLIP_CRITIRION", value)
	def getInitialDeformation(self) -> bool:
		return self._getBoolProperty("JP_INITIAL_DEFORMATION")
	def setInitialDeformation(self, value: bool):
		return self._setBoolProperty("JP_INITIAL_DEFORMATION", value)
	def SetApplySSR(self, applySSR: bool):
		return self._callFunction("SetApplySSR", [applySSR])
	def GetApplySSR(self) -> bool:
		return self._callFunction("GetApplySSR", [])
	def SetPermeable(self, permeable: bool):
		return self._callFunction("SetPermeable", [permeable])
	def GetPermeable(self) -> bool:
		return self._callFunction("GetPermeable", [])
	def SetMeshConforming(self, meshConforming: bool):
		return self._callFunction("SetMeshConforming", [meshConforming])
	def GetMeshConforming(self) -> bool:
		return self._callFunction("GetMeshConforming", [])
