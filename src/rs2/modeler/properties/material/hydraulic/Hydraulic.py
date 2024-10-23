from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.material.hydraulic.FEAGroundwater.FEAGroundwater import FEAGroundwater
from rs2.modeler.properties.material.hydraulic.StaticGroundwater import StaticGroundwater
from rs2.modeler.properties.material.hydraulic.HydroDistribution import HydroDistribution
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
class HydraulicStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getMaterialBehaviourFactor(self) -> str:
		return MaterialBehaviours(self._callFunction("getMaterialBehaviourFactor", []))
class HydraulicDefinedStageFactor(HydraulicStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setMaterialBehaviourFactor(self, materialBehavior: MaterialBehaviours):
		return self._callFunction("setMaterialBehaviourFactor", [materialBehavior.value])
class Hydraulic(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[HydraulicDefinedStageFactor, HydraulicStageFactor]): Reference object for modifying stage factor property.
		StaticGroundwater (StaticGroundwater): Reference object for modifying property.
		HydroDistribution (HydroDistribution): Reference object for modifying property.
		FEAGroundwater (FEAGroundwater): Reference object for modifying property.

	Examples:
		:ref:`Hydraulic Property Example`
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[HydraulicDefinedStageFactor, HydraulicStageFactor](self._client, stageFactorInterfaceID, ID, HydraulicDefinedStageFactor, HydraulicStageFactor)
		self.StaticGroundwater = StaticGroundwater(client, ID, documentProxyID, stageFactorInterfaceID)
		self.HydroDistribution = HydroDistribution(client, ID, documentProxyID, stageFactorInterfaceID)
		self.FEAGroundwater = FEAGroundwater(client, ID, documentProxyID, stageFactorInterfaceID)
	def getMaterialBehaviour(self) -> MaterialBehaviours:
		return MaterialBehaviours(self._getEnumEMaterialBehavioursProperty("MP_MATERIAL_BEHAVIOUR"))
	def setMaterialBehaviour(self, value: MaterialBehaviours):
		return self._setEnumEMaterialBehavioursProperty("MP_MATERIAL_BEHAVIOUR", value)
	def getFluidBulkModulus(self) -> float:
		return self._getDoubleProperty("MP_FLUID_BULK_MODULUS")
	def setFluidBulkModulus(self, value: float):
		return self._setDoubleProperty("MP_FLUID_BULK_MODULUS", value)
	def getUseBiotsCoefficientForCalculatingEffectiveStress(self) -> bool:
		return self._getBoolProperty("MP_USE_ALPHA_BIOT")
	def setUseBiotsCoefficientForCalculatingEffectiveStress(self, value: bool):
		return self._setBoolProperty("MP_USE_ALPHA_BIOT", value)
	def getAccountForWaterContentInCompressibility(self) -> bool:
		return self._getBoolProperty("MP_USE_WC_IN_COMP_COUPLED")
	def setAccountForWaterContentInCompressibility(self, value: bool):
		return self._setBoolProperty("MP_USE_WC_IN_COMP_COUPLED", value)
