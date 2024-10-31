from importlib.metadata import distribution
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from rs2._common.ProxyObject import ProxyObject
from distutils.dist import Distribution
from enum import Enum, auto
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
import warnings
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
		if (KsDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION) and (Ks is not None):
			self.setHydroDistribution(HydraulicVariableTypes.KS_FUNCTION, KsDistribution, Ks)
		if (KsDistribution != HydraulicDistributionTypes.CONSTANT_DISTRIBUTION) and (KsFunction is not None):
			self.setHydroDistribution(HydraulicVariableTypes.KS_FUNCTION, KsDistribution, KsFunction)

		if (K2K1Distribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION) and (K2K1 is not None):
			self.setHydroDistribution(HydraulicVariableTypes.K2K1_FUNCTION, K2K1Distribution, K2K1)
		if (K2K1Distribution != HydraulicDistributionTypes.CONSTANT_DISTRIBUTION) and (K2K1Function is not None):
			self.setHydroDistribution(HydraulicVariableTypes.K2K1_FUNCTION, K2K1Distribution, K2K1Function)

		if (K1AngleDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION) and (K1Angle is not None):
			self.setHydroDistribution(HydraulicVariableTypes.K1_ANGLE_FUNCTION, K1AngleDistribution, K1Angle)
		if (K1AngleDistribution != HydraulicDistributionTypes.CONSTANT_DISTRIBUTION) and (K1AngleFunction is not None):
			self.setHydroDistribution(HydraulicVariableTypes.K1_ANGLE_FUNCTION, K1AngleDistribution, K1AngleFunction)

		if (WcSatDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION) and (WcSat is not None):
			self.setHydroDistribution(HydraulicVariableTypes.WC_SAT_FUNCTION, WcSatDistribution, WcSat)
		if (WcSatDistribution != HydraulicDistributionTypes.CONSTANT_DISTRIBUTION) and (WcSatFunction is not None):
			self.setHydroDistribution(HydraulicVariableTypes.WC_SAT_FUNCTION, WcSatDistribution, WcSatFunction)

		if (WcResDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION) and (WcRes is not None):
			self.setHydroDistribution(HydraulicVariableTypes.WC_RES_FUNCTION, WcResDistribution, WcRes)
		if (WcResDistribution != HydraulicDistributionTypes.CONSTANT_DISTRIBUTION) and (WcResFunction is not None):
			self.setHydroDistribution(HydraulicVariableTypes.WC_RES_FUNCTION, WcResDistribution, WcResFunction)

		if (DosSatDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION) and (DosSat is not None):
			self.setHydroDistribution(HydraulicVariableTypes.DOS_SAT_FUNCTION, DosSatDistribution, DosSat)
		if (DosSatDistribution != HydraulicDistributionTypes.CONSTANT_DISTRIBUTION) and (DosSatFunction is not None):
			self.setHydroDistribution(HydraulicVariableTypes.DOS_SAT_FUNCTION, DosSatDistribution, DosSatFunction)

		if (DosResDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION) and (DosRes is not None):
			self.setHydroDistribution(HydraulicVariableTypes.DOS_RES_FUNCTION, DosResDistribution, DosRes)
		if (DosResDistribution != HydraulicDistributionTypes.CONSTANT_DISTRIBUTION) and (DosResFunction is not None):
			self.setHydroDistribution(HydraulicVariableTypes.DOS_RES_FUNCTION, DosResDistribution, DosResFunction)

		if (RelativeKsDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION) and (RelativeKs is not None):
			self.setHydroDistribution(HydraulicVariableTypes.RELATIVE_KS_FUNCTION, RelativeKsDistribution, RelativeKs)
		if (RelativeKsDistribution != HydraulicDistributionTypes.CONSTANT_DISTRIBUTION) and (RelativeKsFunction is not None):
			self.setHydroDistribution(HydraulicVariableTypes.RELATIVE_KS_FUNCTION, RelativeKsDistribution, RelativeKsFunction)

		if (RelativeWCDOSDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION) and (RelativeWCDOS is not None):
			self.setHydroDistribution(HydraulicVariableTypes.RELATIVE_WC_DOS_FUNCTION, RelativeWCDOSDistribution, RelativeWCDOS)
		if (RelativeWCDOSDistribution != HydraulicDistributionTypes.CONSTANT_DISTRIBUTION) and (RelativeWCDOSFunction is not None):
			self.setHydroDistribution(HydraulicVariableTypes.RELATIVE_WC_DOS_FUNCTION, RelativeWCDOSDistribution, RelativeWCDOSFunction)

	def getProperties(self):
		properties = {}
		applicableVariables = self.getApplicableHydroDistributionVariables()
		
		for applicableVariable in applicableVariables:
			hydroDistribution = self.getHydroDistribution(applicableVariable)
			if hydroDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION:
				hydroDistributionValue = self.getHydroDistributionConstantVal(applicableVariable)
			else:
				hydroDistributionValue = self.getHydroDistributionFunctionName(applicableVariable)

			if applicableVariable == HydraulicVariableTypes.KS_FUNCTION:
				properties["KsDistribution"] = hydroDistribution
				if hydroDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION:
					properties["Ks"] = hydroDistributionValue
				else:
					properties["KsFunction"] = hydroDistributionValue
			elif applicableVariable == HydraulicVariableTypes.K2K1_FUNCTION:
				properties["K2K1Distribution"] = hydroDistribution
				if hydroDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION:
					properties["K2K1"] = hydroDistributionValue
				else:
					properties["K2K1Function"] = hydroDistributionValue
			elif applicableVariable == HydraulicVariableTypes.K1_ANGLE_FUNCTION:
				properties["K1AngleDistribution"] = hydroDistribution
				if hydroDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION:
					properties["K1Angle"] = hydroDistributionValue
				else:
					properties["K1AngleFunction"] = hydroDistributionValue
			elif applicableVariable == HydraulicVariableTypes.WC_SAT_FUNCTION:
				properties["WcSatDistribution"] = hydroDistribution
				if hydroDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION:
					properties["K1Angle"] = hydroDistributionValue
				else:
					properties["K1AngleFunction"] = hydroDistributionValue
			elif applicableVariable == HydraulicVariableTypes.WC_RES_FUNCTION:
				properties["WcResDistribution"] = hydroDistribution
				if hydroDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION:
					properties["WcRes"] = hydroDistributionValue
				else:
					properties["WcResFunction"] = hydroDistributionValue
			elif applicableVariable == HydraulicVariableTypes.DOS_SAT_FUNCTION:
				properties["DosSatDistribution"] = hydroDistribution
				if hydroDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION:
					properties["DosSat"] = hydroDistributionValue
				else:
					properties["DosSatFunction"] = hydroDistributionValue
			elif applicableVariable == HydraulicVariableTypes.DOS_RES_FUNCTION:
				properties["DosResDistribution"] = hydroDistribution
				if hydroDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION:
					properties["DosRes"] = hydroDistributionValue
				else:
					properties["DosResFunction"] = hydroDistributionValue
			elif applicableVariable == HydraulicVariableTypes.RELATIVE_KS_FUNCTION:
				properties["RelativeKsDistribution"] = hydroDistribution
				if hydroDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION:
					properties["RelativeKs"] = hydroDistributionValue
				else:
					properties["RelativeKsFunction"] = hydroDistributionValue
			elif applicableVariable == HydraulicVariableTypes.RELATIVE_WC_DOS_FUNCTION:
				properties["RelativeWCDOSDistribution"] = hydroDistribution
				if hydroDistribution == HydraulicDistributionTypes.CONSTANT_DISTRIBUTION:
					properties["RelativeWCDOS"] = hydroDistributionValue
				else:
					properties["RelativeWCDOSFunction"] = hydroDistributionValue

		return properties