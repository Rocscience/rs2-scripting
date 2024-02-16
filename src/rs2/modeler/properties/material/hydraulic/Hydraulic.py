from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.material.hydraulic.FEAGroundwater.FEAGroundwater import FEAGroundwater
from rs2.modeler.properties.material.hydraulic.StaticGroundwater import StaticGroundwater
class Hydraulic(PropertyProxy):
	"""
	:ref:`Hydraulic Property Stiffness Example`
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		self.StaticGroundwater = StaticGroundwater(client, ID, documentProxyID)
		self.FEAGroundwater = FEAGroundwater(client, ID, documentProxyID, stageFactorInterfaceID)
		super().__init__(client, ID, documentProxyID)
	def getMaterialBehaviour(self) -> MaterialBehaviours:
		return MaterialBehaviours(self._getEnumEMaterialBehavioursProperty("MP_MATERIAL_BEHAVIOUR"))
	def setMaterialBehaviour(self, value: MaterialBehaviours):
		return self._setEnumEMaterialBehavioursProperty("MP_MATERIAL_BEHAVIOUR", value)
	def getFluidBulkModulus(self) -> float:
		return self._getDoubleProperty("MP_FLUID_BULK_MODULUS")
	def setFluidBulkModulus(self, value: float):
		return self._setDoubleProperty("MP_FLUID_BULK_MODULUS", value)
