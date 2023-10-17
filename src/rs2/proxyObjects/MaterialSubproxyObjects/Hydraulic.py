from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.proxyObjects.MaterialSubproxyObjects.HydraulicSubProxyObjects.StaticGroundwater import StaticGroundwater
from rs2.proxyObjects.MaterialSubproxyObjects.HydraulicSubProxyObjects.FEAGroundwater import FEAGroundwater
class Hydraulic(PropertyProxy):
	"""
	:ref:`Hydraulic Property Stiffness Example`
	"""
	def __init__(self, server : Client, ID, documentProxyID):
		self.StaticGroundwater = StaticGroundwater(server, ID, documentProxyID)
		self.FEAGroundwater = FEAGroundwater(server, ID, documentProxyID)
		super().__init__(server, ID, documentProxyID)
	def getMaterialBehaviour(self) -> MaterialBehaviours:
		return MaterialBehaviours(self._getEnumEMaterialBehavioursProperty("MP_MATERIAL_BEHAVIOUR"))
	def setMaterialBehaviour(self, value: MaterialBehaviours):
		return self._setEnumEMaterialBehavioursProperty("MP_MATERIAL_BEHAVIOUR", value)
	def getFluidBulkModulus(self) -> float:
		return self._getDoubleProperty("MP_FLUID_BULK_MODULUS")
	def setFluidBulkModulus(self, value: float):
		return self._setDoubleProperty("MP_FLUID_BULK_MODULUS", value)
