from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.joint.MohrCoulombMaterial import MohrCoulombMaterial
from rs2.modeler.properties.joint.BartonBandisMaterial import BartonBandisMaterial
from rs2.modeler.properties.joint.GeosyntheticHyperbolicMaterial import GeosyntheticHyperbolicMaterial
class MaterialJoint(PropertyProxy):
	"""
	Attributes:
		MohrCoulombMaterial (MohrCoulombMaterial): Reference object for modifying property.
		BartonBandisMaterial (BartonBandisMaterial): Reference object for modifying property.
		GeosyntheticHyperbolicMaterial (GeosyntheticHyperbolicMaterial): Reference object for modifying property.

	Examples:
		:ref:`Material Joint Example`
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		self.MohrCoulombMaterial = MohrCoulombMaterial(client, ID, documentProxyID)
		self.BartonBandisMaterial = BartonBandisMaterial(client, ID, documentProxyID)
		self.GeosyntheticHyperbolicMaterial = GeosyntheticHyperbolicMaterial(client, ID, documentProxyID)
		super().__init__(client, ID, documentProxyID)
	def getSlipCriterion(self) -> JointTypes:
		return JointTypes(self._getEnumEJointTypesProperty("JP_SLIP_CRITIRION"))
	def setSlipCriterion(self, value: JointTypes):
		return self._setEnumEJointTypesProperty("JP_SLIP_CRITIRION", value)
	def SetApplySSR(self, applySSR: bool):
		return self._callFunction("SetApplySSR", [applySSR])
	def GetApplySSR(self) -> bool:
		return self._callFunction("GetApplySSR", [])
