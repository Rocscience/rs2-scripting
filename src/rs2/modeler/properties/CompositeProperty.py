from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class CompositeProperty(PropertyProxy):
	"""
	Examples:
		:ref:`Composite Liner Example`
	"""
	def getCompositeName(self) -> str:
		return self._getCStringProperty("CLP_NAME")
	def setCompositeName(self, value: str):
		return self._setCStringProperty("CLP_NAME", value)
	def getCompositeColor(self) -> int:
		return self._getUnsignedLongProperty("CLP_COLOR")
	def setCompositeColor(self, value: int):
		return self._setUnsignedLongProperty("CLP_COLOR", value)
	def getJointPlacement(self) -> CompositeJointPlacementTypes:
		return CompositeJointPlacementTypes(self._getEnumECompositeJointPlacementProperty("CLP_JOINT_PLACEMENT"))
	def setJointPlacement(self, value: CompositeJointPlacementTypes):
		return self._setEnumECompositeJointPlacementProperty("CLP_JOINT_PLACEMENT", value)
	def getCompositeJointPropertyName(self) -> str:
		"""
		Returns the applied joint name
		"""
		return self._callFunction("getCompositeJointPropertyName", [])
	def setCompositeJointPropertyByName(self, jointName: str):
		"""
		Set joint by name
		"""
		return self._callFunction("setCompositeJointPropertyByName", [jointName])
	def getCompositeLinerPropertyName(self, layerNumber: int) -> str:
		"""
		Returns the liner name for specified layer number
		"""
		return self._callFunction("getCompositeLinerPropertyName", [layerNumber])
	def setCompositeLinerPropertyByName(self, layerNumber: int, linerName: str):
		"""
		Set liner by name for specified layer number
		"""
		return self._callFunction("setCompositeLinerPropertyByName", [layerNumber, linerName])
	def getNumberOfLayers(self) -> int:
		"""
		Returns number of layers
		"""
		return self._callFunction("getNumberOfLayers", [])
	def setNumberOfLayers(self, num_layers: int):
		"""
		Set number of layers
		"""
		return self._callFunction("setNumberOfLayers", [num_layers])
	def getJointApplied(self) -> bool:
		"""
		Returns boolean indicating whether joint interface is applied or not
		"""
		return self._callFunction("getJointApplied", [])
	def setJointApplied(self, joint_applied: bool):
		"""
		Set joint interface as boolean
		"""
		return self._callFunction("setJointApplied", [joint_applied])
	def getInstallDelay(self, layerNumber: int) -> int:
		"""
		Returns install delay as integer for specified layer number
		"""
		return self._callFunction("getInstallDelay", [layerNumber])
	def setInstallDelay(self, layerNumber: int, stagesBelow: int):
		"""
		Set install delay for specified layer number. Please note that install delay cannot be set for first layer.
		"""
		return self._callFunction("setInstallDelay", [layerNumber, stagesBelow])
	def getRemovedStage(self, layerNumber: int) -> int:
		"""
		Returns removed stages as integer for specified layer number
		"""
		return self._callFunction("getRemovedStage", [layerNumber])
	def setRemovedStage(self, layerNumber: int, stagesBelow: int):
		"""
		Set removed stages for specified layer number. To set the removed stages to "Never", please set stagesBelow to -1
		"""
		return self._callFunction("setRemovedStage", [layerNumber, stagesBelow])
