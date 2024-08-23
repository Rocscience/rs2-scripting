from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client

from distutils.dist import Distribution
from enum import Enum, auto


class HydroDistribution(PropertyProxy):
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)

	def setHydroDistribution(self, variable:HydraulicVariableTypes, distribution: HydraulicDistributionTypes, value: str):
		return self._callFunction("setHydroDistribution", [variable, distribution, value])
	def getSelectedHydroDistributionVal(self, variable:HydraulicVariableTypes, distribution: HydraulicDistributionTypes) -> str:
		return self._callFunction("getSelectedHydroDistributionVal", [variable, distribution])
	def setHydroDistribution(self, variable:HydraulicVariableTypes, distribution: HydraulicDistributionTypes, value: float):
		return self._callFunction("setHydroDistribution", [variable, distribution, value])
	def getSelectedHydroDistributionVal(self, variable:HydraulicVariableTypes, distribution: HydraulicDistributionTypes) -> float:
		return self._callFunction("getSelectedHydroDistributionVal", [variable, distribution])
	def setNewHydroDistribution(self, variable:HydraulicVariableTypes, newDistribution: HydraulicDistributionTypes):
		return self._callFunction("setNewHydroDistribution", [variable, newDistribution])
	def getHydroDistribution(self, variable: HydraulicVariableTypes) -> HydraulicDistributionTypes:
		return self._callFunction("getHydroDistribution", [variable])
