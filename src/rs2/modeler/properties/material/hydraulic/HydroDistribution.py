from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from rs2._common.ProxyObject import ProxyObject
from distutils.dist import Distribution
from enum import Enum, auto
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
import warnings

class HydroDistributionFunctionStageFactor(ProxyObject):
	"""
	Set stage hydraulic distribution functions. 
	"""
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getHydroDistributionStagedFunction(self, variable: HydraulicVariableTypes) -> list[HydraulicDistributionTypes, str]:
		"""
		Return a list with HydraulicDistributionType and the assigned function name.
		"""
		distribution, funcName = self._callFunction("getHydroDistributionStagedFunction", [variable.value, self.propertyID], proxyArgumentIndices=[1])
		return [HydraulicDistributionTypes(distribution), funcName]

class HydroDistributionFunctionDefinedStageFactor(HydroDistributionFunctionStageFactor):
	"""
	Get stage hydraulic distribution functions. 
	"""
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setHydroDistributionStagedFunction(self, variable: HydraulicVariableTypes, dist: HydraulicDistributionTypes, value: str = None):
		"""
		Set the hydraulic distribution function for a specific stage.
		"""
		if value == None:
			return self._callFunction("setHydroDistributionStagedFunction", [variable.value, dist.value, self.propertyID], proxyArgumentIndices=[2])
		else:
			return self._callFunction("setHydroDistributionStagedFunction", [variable.value, dist.value, value, self.propertyID], proxyArgumentIndices=[3])

class HydroDistribution(PropertyProxy):
	"""
	Examples:
		:ref:`Hydraulic Distribution Function Example`
	
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[HydroDistributionFunctionDefinedStageFactor, HydroDistributionFunctionStageFactor]): Reference object for modifying stage factor property.
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[HydroDistributionFunctionDefinedStageFactor, HydroDistributionFunctionStageFactor](self._client, stageFactorInterfaceID, ID, HydroDistributionFunctionDefinedStageFactor, HydroDistributionFunctionStageFactor)

	def setHydroDistribution(self, variable: HydraulicVariableTypes, dist: HydraulicDistributionTypes, value):
		"""
		Set the given variable with selected non-constant hydraulic distribution with a defined hydraulic distribution function or with a constant hydraulic distribution with a constant value. 
		"""
		if(isinstance(value, str) and dist != HydraulicDistributionTypes.CONSTANT_DIST):
			return self._callFunction("setHydroDistribution", [variable.value, dist.value, value])
		elif(isinstance(value, float) and dist == HydraulicDistributionTypes.CONSTANT_DIST):
			return self._callFunction("setHydroDistribution", [variable.value, dist.value, value])
		else:
			warnings.warn(f"Please input a valid value for {dist}")

	def getHydroDistributionFunctionName(self, variable: HydraulicVariableTypes) -> str:
		"""
		Get the hydraulic distribution function name. See getHydroDistributionConstantVal to access constant value of constant distribution.
		"""
		return self._callFunction("getHydroDistributionFunctionName", [variable.value])
	def getHydroDistributionConstantVal(self, variable: HydraulicVariableTypes) -> float:
		"""
		Get the hydraulic distribution constant value. See getHydroDistributionFunctionName to access the function name of a non-constant distribution.
		"""
		return self._callFunction("getHydroDistributionConstantVal", [variable.value])
	def getHydroDistribution(self, variable: HydraulicVariableTypes) -> HydraulicDistributionTypes:
		"""
		Get the distribution function of the selected variable
		"""
		return HydraulicDistributionTypes(self._callFunction("getHydroDistribution", [variable.value]))
