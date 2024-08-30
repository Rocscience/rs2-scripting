from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client

from distutils.dist import Distribution
from enum import Enum, auto
import warnings


class HydroDistribution(PropertyProxy):
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)

	def setHydroDistribution(self, variable: HydraulicVariableTypes, dist: HydraulicDistributionTypes, value):
		if(isinstance(value, str) and dist != HydraulicDistributionTypes.CONSTANT_DIST):
			return self._callFunction("setHydroDistribution", [variable.value, dist.value, value])
		elif(isinstance(value, float) and dist == HydraulicDistributionTypes.CONSTANT_DIST):
			return self._callFunction("setHydroDistribution", [variable.value, dist.value, value])
		else:
			warnings.warn(f"Please input a valid value for {dist}")

	def getHydroDistributionVal(self, variable: HydraulicVariableTypes) -> str:
		return self._callFunction("getHydroDistributionVal", [variable.value])
	def getHydroDistributionConstantVal(self, variable: HydraulicVariableTypes) -> float:
		return self._callFunction("getHydroDistributionConstantVal", [variable.value])


	def setNewHydroDistribution(self, variable:HydraulicVariableTypes, newDistribution: HydraulicDistributionTypes):
		return self._callFunction("setNewHydroDistribution", [variable, newDistribution])
	def getHydroDistribution(self, variable: HydraulicVariableTypes) -> HydraulicDistributionTypes:
		return self._callFunction("getHydroDistribution", [variable])
