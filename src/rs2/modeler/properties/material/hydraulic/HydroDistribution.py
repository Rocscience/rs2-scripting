from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client

from distutils.dist import Distribution
from enum import Enum, auto


class HydroDistribution(PropertyProxy):
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		pass
	def setHydroDistribution(self, variable:HydraulicVariableTypes, distribution: HydraulicDistributionTypes, value: str):
		pass
	def getSelectedHydroDistributionVal(self, variable:HydraulicVariableTypes, distribution: HydraulicDistributionTypes) -> str:
		pass
	def setHydroDistribution(self, variable:HydraulicVariableTypes, distribution: HydraulicDistributionTypes, value: float):
		pass
	def getSelectedHydroDistributionVal(self, variable:HydraulicVariableTypes, distribution: HydraulicDistributionTypes) -> float:
		pass
	def setNewHydroDistribution(self, variable:HydraulicVariableTypes, newDistribution: HydraulicDistributionTypes):
		pass
	def getHydroDistribution(self, variable: HydraulicVariableTypes) -> HydraulicDistributionTypes:
		pass