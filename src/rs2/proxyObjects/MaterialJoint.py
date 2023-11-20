from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.proxyObjects.JointSubproxyObjects.MohrCoulombMaterial import MohrCoulombMaterial
from rs2.proxyObjects.JointSubproxyObjects.BartonBandisMaterial import BartonBandisMaterial
from rs2.proxyObjects.JointSubproxyObjects.GeosyntheticHyperbolicMaterial import GeosyntheticHyperbolicMaterial
class MaterialJoint(PropertyProxy):
	"""
	:ref:`Material Joint Example`
	"""
	def __init__(self, server : Client, ID, documentProxyID):
		self.MohrCoulombMaterial = MohrCoulombMaterial(server, ID, documentProxyID)
		self.BartonBandisMaterial = BartonBandisMaterial(server, ID, documentProxyID)
		self.GeosyntheticHyperbolicMaterial = GeosyntheticHyperbolicMaterial(server, ID, documentProxyID)
		super().__init__(server, ID, documentProxyID)
	def getSlipCriterion(self) -> JointTypes:
		return JointTypes(self._getEnumEJointTypesProperty("JP_SLIP_CRITIRION"))
	def setSlipCriterion(self, value: JointTypes):
		return self._setEnumEJointTypesProperty("JP_SLIP_CRITIRION", value)
	def SetApplySSR(self, applySSR: bool):
		return self._callFunction("SetApplySSR", [applySSR])
	def GetApplySSR(self) -> bool:
		return self._callFunction("GetApplySSR", [])
