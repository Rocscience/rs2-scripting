from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from rs2.modeler.properties.PropertyEnums import HydraulicDistributionTypes, HydraulicVariableTypes
from distutils.dist import Distribution
from enum import Enum, auto


class HydroDistribution(PropertyProxy):
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		pass
	def setSelectedHydroDistributionFunctionByName(self, variable:HydraulicVariableTypes, distribution: HydraulicDistributionTypes, name: str):
		pass
	def getSelectedHydroDistributionFunctionName(self, variable:HydraulicVariableTypes, distribution: HydraulicDistributionTypes) -> str:
		pass