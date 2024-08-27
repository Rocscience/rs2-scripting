from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client

from distutils.dist import Distribution
from enum import Enum, auto


class HydroDistribution(PropertyProxy):
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)

	def setSelectedHydroDistributionFunctionByName(self, variable:HydraulicVariableTypes, value: str):
		return self._callFunction("setSelectedHydroDistributionFunctionByName", [0, value])
	def getSelectedHydroDistributionFunctionByName(self, variable:HydraulicVariableTypes) -> str:
		return self._callFunction("getSelectedHydroDistributionFunctionByName", [variable.value])
	def setSelectedHydroDistributionFunctionByName(self, variable:HydraulicVariableTypes, value: float):
		return self._callFunction("setSelectedHydroDistributionFunctionByName", [variable, value])
	def getSelectedHydroDistributionFunctionByName(self, variable:HydraulicVariableTypes) -> float:
		return self._callFunction("getSelectedHydroDistributionFunctionByName", [variable])
	def setNewHydroDistribution(self, variable:HydraulicVariableTypes, newDistribution: HydraulicDistributionTypes):
		return self._callFunction("setNewHydroDistribution", [variable, newDistribution])
	def getHydroDistribution(self, variable: HydraulicVariableTypes) -> HydraulicDistributionTypes:
		return self._callFunction("getHydroDistribution", [variable])
