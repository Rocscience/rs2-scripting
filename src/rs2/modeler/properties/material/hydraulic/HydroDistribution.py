
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from rs2._common.ProxyObject import ProxyObject

from enum import Enum, auto
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface

from dataclasses import dataclass
from typing import Optional

@dataclass
class HydroDistributionResult:
	distribution_type: HydraulicDistributionTypes
	function_name: Optional[str] = None

class HydroDistributionFunctionStageFactor(ProxyObject):
	"""
	Set stage hydraulic distribution functions. 
	"""
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getHydroDistributionStagedFunction(self, variable: HydraulicVariableTypes) -> HydroDistributionResult:
		"""
		Return a list with HydraulicDistributionType and the assigned function name.
		"""
		distribution_info = self._callFunction("getHydroDistributionStagedFunction", [variable.value, self.propertyID], proxyArgumentIndices=[1])
		
		if len(distribution_info) == 1:
			return HydroDistributionResult(distribution_type=HydraulicDistributionTypes(distribution_info[0]))
		elif len(distribution_info) == 2:
			return HydroDistributionResult(distribution_type=HydraulicDistributionTypes(distribution_info[0]), function_name=distribution_info[1])
		else:
			raise ValueError("Unexpected return length from 'getHydroDistributionStagedFunction'.")


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
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[HydroDistributionFunctionDefinedStageFactor, HydroDistributionFunctionStageFactor]): Reference object for modifying stage factor property.
	
	Examples:
		:ref:`Hydraulic Distribution Function Example`
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[HydroDistributionFunctionDefinedStageFactor, HydroDistributionFunctionStageFactor](self._client, stageFactorInterfaceID, ID, HydroDistributionFunctionDefinedStageFactor, HydroDistributionFunctionStageFactor)

	def setHydroDistribution(self, variable: HydraulicVariableTypes, dist: HydraulicDistributionTypes, value):
		"""
		Set the given variable with selected non-constant hydraulic distribution with a defined hydraulic distribution function or with a constant hydraulic distribution with a constant value. 
		"""
		if(isinstance(value, str) and dist != HydraulicDistributionTypes.CONSTANT_DISTRIBUTION):
			return self._callFunction("setHydroDistribution", [variable.value, dist.value, value])
		elif(isinstance(value, float) and dist == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION):
			return self._callFunction("setHydroDistribution", [variable.value, dist.value, value])
		else:
			raise ValueError(f"Please input a valid value for {dist}")
			

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
	
	def getApplicableHydroDistributionVariables(self) -> list[HydraulicVariableTypes]:
		applicationHydroDistributionVariables = []
		applicationHydroDistributionVariableNameList = self._callFunction("getApplicableHydroDistributionVariables", [])
		for variable in applicationHydroDistributionVariableNameList:
			if variable != "MP_DISTRIBUTION_WC_SLOPE_FUNCTION":
				applicationHydroDistributionVariables.append(HydraulicVariableTypes(variable))		
		return applicationHydroDistributionVariables

	def setProperties(self, 
				   KsDistribution : HydraulicDistributionTypes = None, Ks : float = None, KsFunction : str = None,
				   K2K1Distribution : HydraulicDistributionTypes = None, K2K1 : float = None, K2K1Function : str = None,
				   K1AngleDistribution : HydraulicDistributionTypes = None, K1Angle : float = None, K1AngleFunction : str = None,
				   WcSatDistribution : HydraulicDistributionTypes = None, WcSat : float = None, WcSatFunction : str = None,
				   WcResDistribution : HydraulicDistributionTypes = None, WcRes : float = None, WcResFunction : str = None,
				   DosSatDistribution : HydraulicDistributionTypes = None, DosSat : float = None, DosSatFunction : str = None,
				   DosResDistribution : HydraulicDistributionTypes = None, DosRes : float = None, DosResFunction : str = None,
				   RelativeKsDistribution : HydraulicDistributionTypes = None, RelativeKs : float = None, RelativeKsFunction : str = None,
				   RelativeWCDOSDistribution : HydraulicDistributionTypes = None, RelativeWCDOS : float = None, RelativeWCDOSFunction : str = None,
				   ):

		params = {
			HydraulicVariableTypes.KS_FUNCTION: (KsDistribution, Ks, KsFunction),
			HydraulicVariableTypes.K2K1_FUNCTION: (K2K1Distribution, K2K1, K2K1Function),
			HydraulicVariableTypes.K1_ANGLE_FUNCTION: (K1AngleDistribution, K1Angle, K1AngleFunction),
			HydraulicVariableTypes.WC_SAT_FUNCTION: (WcSatDistribution, WcSat, WcSatFunction),
			HydraulicVariableTypes.WC_RES_FUNCTION: (WcResDistribution, WcRes, WcResFunction),
			HydraulicVariableTypes.DOS_SAT_FUNCTION: (DosSatDistribution, DosSat, DosSatFunction),
			HydraulicVariableTypes.DOS_RES_FUNCTION: (DosResDistribution, DosRes, DosResFunction),
			HydraulicVariableTypes.RELATIVE_KS_FUNCTION: (RelativeKsDistribution, RelativeKs, RelativeKsFunction),
			HydraulicVariableTypes.RELATIVE_WC_DOS_FUNCTION: (RelativeWCDOSDistribution, RelativeWCDOS, RelativeWCDOSFunction)
		}
    
		for variable_type, (distribution, value, function) in params.items():
			if distribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION and value is not None:
				self.setHydroDistribution(variable_type, distribution, value)
			elif distribution != HydraulicDistributionTypes.CONSTANT_DISTRIBUTION and function is not None:
				self.setHydroDistribution(variable_type, distribution, function)

	def getProperties(self):
		properties = {}
		applicableVariables = self.getApplicableHydroDistributionVariables()
		
		hydraulic_distribution_property_map = {
			HydraulicVariableTypes.KS_FUNCTION: "Ks",
			HydraulicVariableTypes.K2K1_FUNCTION: "K2K1",
			HydraulicVariableTypes.K1_ANGLE_FUNCTION: "K1Angle",
			HydraulicVariableTypes.WC_SAT_FUNCTION: "WcSat",
			HydraulicVariableTypes.WC_RES_FUNCTION: "WcRes",
			HydraulicVariableTypes.DOS_SAT_FUNCTION: "DosSat",
			HydraulicVariableTypes.DOS_RES_FUNCTION: "DosRes",
			HydraulicVariableTypes.RELATIVE_KS_FUNCTION: "RelativeKs",
			HydraulicVariableTypes.RELATIVE_WC_DOS_FUNCTION: "RelativeWCDOS"
		}

		for applicableVariable in applicableVariables:
			hydroDistribution = self.getHydroDistribution(applicableVariable)
			hydroDistributionValue = (
				self.getHydroDistributionConstantVal(applicableVariable) 
				if hydroDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION 
				else self.getHydroDistributionFunctionName(applicableVariable)
			)

			hydraulic_distribution_property = hydraulic_distribution_property_map.get(applicableVariable)
			if hydraulic_distribution_property:
				properties[f"{hydraulic_distribution_property}Distribution"] = hydroDistribution
				if hydroDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION:
					properties[hydraulic_distribution_property] = hydroDistributionValue
				else:
					properties[f"{hydraulic_distribution_property}Function"] = hydroDistributionValue


		return properties