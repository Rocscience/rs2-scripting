from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class StructuralInterfaceProperty(PropertyProxy):
	"""
	Examples:
		:ref:`Structural Interface Example`
	"""
	def getStructuralInterfaceName(self) -> str:
		"""
		Returns the structural interface name
		"""
		return self._callFunction("getStructuralInterfaceName", [])
	def setStructuralInterfaceName(self, name: str):
		"""
		Sets structural interface name
		"""
		return self._callFunction("setStructuralInterfaceName", [name])
	def getColor(self) -> int:
		"""
		Returns the structural interface color
		"""
		return self._callFunction("getColor", [])
	def setColor(self, color: int):
		"""
		Sets structural interface color
		"""
		return self._callFunction("setColor", [color])
	def getPositiveJointPropertyName(self) -> str:
		"""
		Returns the positive side joint property name
		"""
		return self._callFunction("getPositiveJointPropertyName", [])
	def setPositiveJointPropertyByName(self, jointName: str):
		"""
		Set positive side joint property by name
		"""
		return self._callFunction("setPositiveJointPropertyByName", [jointName])
	def getNegativeJointPropertyName(self) -> str:
		"""
		Returns the negative side joint property name
		"""
		return self._callFunction("getNegativeJointPropertyName", [])
	def setNegativeJointPropertyByName(self, jointName: str):
		"""
		Set negative side joint property by name
		"""
		return self._callFunction("setNegativeJointPropertyByName", [jointName])
	def getLinerPropertyName(self) -> str:
		"""
		Returns the liner property name
		"""
		return self._callFunction("getLinerPropertyName", [])
	def setLinerPropertyByName(self, linerName: str):
		"""
		Set liner property by name
		"""
		return self._callFunction("setLinerPropertyByName", [linerName])
