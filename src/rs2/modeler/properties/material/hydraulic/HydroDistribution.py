from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client

from distutils.dist import Distribution
from enum import Enum, auto


class HydroDistribution(PropertyProxy):
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)

	def setHydroDistribution(self, variable:HydraulicVariableTypes, value: str):
		return self._callFunction("setHydroDistribution", [variable.value, value])
	def getHydroDistributionVal(self, variable:HydraulicVariableTypes) -> str:
		return self._callFunction("getHydroDistributionVal", [variable.value])

	def setHydroDistribution(self, variable:HydraulicVariableTypes, value: float):
		return self._setDoubleProperty(variable.value, value)
	def getHydroDistributionVal(self, variable:HydraulicVariableTypes) -> float:
		return self._getDoubleProperty(variable.value)

	def setNewHydroDistribution(self, variable:HydraulicVariableTypes, newDistribution: HydraulicDistributionTypes):
		return self._callFunction("setNewHydroDistribution", [variable, newDistribution])
	def getHydroDistribution(self, variable: HydraulicVariableTypes) -> HydraulicDistributionTypes:
		return self._callFunction("getHydroDistribution", [variable])
