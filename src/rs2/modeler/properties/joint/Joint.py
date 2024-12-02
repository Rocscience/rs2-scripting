from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.joint.NoneSlip import NoneSlip
from rs2.modeler.properties.joint.MohrCoulomb import MohrCoulomb
from rs2.modeler.properties.joint.BartonBandis import BartonBandis
from rs2.modeler.properties.joint.GeosyntheticHyperbolic import GeosyntheticHyperbolic
from rs2.modeler.properties.joint.HyperbolicSoftening import HyperbolicSoftening
from rs2.modeler.properties.joint.MaterialDependent import MaterialDependent
from rs2.modeler.properties.joint.DisplacementDependent import DisplacementDependent
class JointProperty(PropertyProxy):
	"""
	Attributes:
		NoneSlip (NoneSlip): Reference object for modifying property.
		MohrCoulomb (MohrCoulomb): Reference object for modifying property.
		BartonBandis (BartonBandis): Reference object for modifying property.
		GeosyntheticHyperbolic (GeosyntheticHyperbolic): Reference object for modifying property.
		HyperbolicSoftening (HyperbolicSoftening): Reference object for modifying property.
		MaterialDependent (MaterialDependent): Reference object for modifying property.
		DisplacementDependent (DisplacementDependent): Reference object for modifying property.

	Examples:
		:ref:`Joint Example`
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		self.NoneSlip = NoneSlip(client, ID, documentProxyID)
		self.MohrCoulomb = MohrCoulomb(client, ID, documentProxyID)
		self.BartonBandis = BartonBandis(client, ID, documentProxyID)
		self.GeosyntheticHyperbolic = GeosyntheticHyperbolic(client, ID, documentProxyID)
		self.HyperbolicSoftening = HyperbolicSoftening(client, ID, documentProxyID)
		self.MaterialDependent = MaterialDependent(client, ID, documentProxyID)
		self.DisplacementDependent = DisplacementDependent(client, ID, documentProxyID)
		super().__init__(client, ID, documentProxyID)
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
	def SetAllowSlipStartFromStage(self, stage: int):
		return self._callFunction("SetAllowSlipStartFromStage", [stage])
	def GetAllowSlipStartFromStage(self) -> int:
		return self._callFunction("GetAllowSlipStartFromStage", [])
