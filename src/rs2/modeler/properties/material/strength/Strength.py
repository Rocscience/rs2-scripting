from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.material.strength.MohrCoulombStrength import MohrCoulombStrength
from rs2.modeler.properties.material.strength.HoekBrown import HoekBrown
from rs2.modeler.properties.material.strength.DruckerPrager import DruckerPrager
from rs2.modeler.properties.material.strength.GeneralizedHoekBrown import GeneralizedHoekBrown
from rs2.modeler.properties.material.strength.DiscreteFunction import DiscreteFunction
from rs2.modeler.properties.material.strength.CamClay import CamClay
from rs2.modeler.properties.material.strength.ModifiedCamClay import ModifiedCamClay
from rs2.modeler.properties.material.strength.MohrCoulombWithCap import MohrCoulombWithCap
from rs2.modeler.properties.material.strength.SofteningHardeningModel import SofteningHardeningModel
from rs2.modeler.properties.material.strength.BarcelonaBasic import BarcelonaBasic
from rs2.modeler.properties.material.strength.NorSandStrength import NorSandStrength
from rs2.modeler.properties.material.strength.BoundingSurfacePlasticity import BoundingSurfacePlasticity
from rs2.modeler.properties.material.strength.ManzariAndDafaliasStrength import ManzariAndDafaliasStrength
from rs2.modeler.properties.material.strength.PM4SandStrength import PM4SandStrength
from rs2.modeler.properties.material.strength.PM4SiltStrength import PM4SiltStrength
from rs2.modeler.properties.material.strength.Finn import Finn
from rs2.modeler.properties.material.strength.BartonBandisStrength import BartonBandisStrength
from rs2.modeler.properties.material.strength.Hyperbolic import Hyperbolic
from rs2.modeler.properties.material.strength.PowerCurve import PowerCurve
from rs2.modeler.properties.material.strength.ShearNormalFunction import ShearNormalFunction
from rs2.modeler.properties.material.strength.Shansep import Shansep
from rs2.modeler.properties.material.strength.VerticalStressRatio import VerticalStressRatio
from rs2.modeler.properties.material.strength.SnowdenModAnisotropicLinear import SnowdenModAnisotropicLinear
from rs2.modeler.properties.material.strength.AnisotropicLinear import AnisotropicLinear
from rs2.modeler.properties.material.strength.GeneralizedAnisotropic import GeneralizedAnisotropic
from rs2.modeler.properties.material.strength.JointedMohrCoulomb import JointedMohrCoulomb
from rs2.modeler.properties.material.strength.JointedGeneralizedHoekBrown import JointedGeneralizedHoekBrown
from rs2.modeler.properties.material.strength.ChSoilStrength import ChSoilStrength
from rs2.modeler.properties.material.strength.CySoilStrength import CySoilStrength
from rs2.modeler.properties.material.strength.DoubleYieldStrength import DoubleYieldStrength
from rs2.modeler.properties.material.strength.HardeningSoilStrength import HardeningSoilStrength
from rs2.modeler.properties.material.strength.HardeningSoilWithSmallStrainStiffness import HardeningSoilWithSmallStrainStiffness
from rs2.modeler.properties.material.strength.SoftSoilStrength import SoftSoilStrength
from rs2.modeler.properties.material.strength.SoftSoilCreepStrength import SoftSoilCreepStrength
from rs2.modeler.properties.material.strength.SwellingRockStrength import SwellingRockStrength
class Strength(PropertyProxy):
	"""
	:ref:`Material Property Strength Example`
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		self.MohrCoulombStrength = MohrCoulombStrength(client, ID, documentProxyID)
		self.HoekBrown = HoekBrown(client, ID, documentProxyID)
		self.DruckerPrager = DruckerPrager(client, ID, documentProxyID)
		self.GeneralizedHoekBrown = GeneralizedHoekBrown(client, ID, documentProxyID)
		self.DiscreteFunction = DiscreteFunction(client, ID, documentProxyID)
		self.CamClay = CamClay(client, ID, documentProxyID)
		self.ModifiedCamClay = ModifiedCamClay(client, ID, documentProxyID)
		self.MohrCoulombWithCap = MohrCoulombWithCap(client, ID, documentProxyID)
		self.SofteningHardeningModel = SofteningHardeningModel(client, ID, documentProxyID)
		self.BarcelonaBasic = BarcelonaBasic(client, ID, documentProxyID)
		self.NorSandStrength = NorSandStrength(client, ID, documentProxyID)
		self.BoundingSurfacePlasticity = BoundingSurfacePlasticity(client, ID, documentProxyID)
		self.ManzariAndDafaliasStrength = ManzariAndDafaliasStrength(client, ID, documentProxyID)
		self.PM4SandStrength = PM4SandStrength(client, ID, documentProxyID)
		self.PM4SiltStrength = PM4SiltStrength(client, ID, documentProxyID)
		self.Finn = Finn(client, ID, documentProxyID)
		self.BartonBandisStrength = BartonBandisStrength(client, ID, documentProxyID)
		self.Hyperbolic = Hyperbolic(client, ID, documentProxyID)
		self.PowerCurve = PowerCurve(client, ID, documentProxyID)
		self.ShearNormalFunction = ShearNormalFunction(client, ID, documentProxyID)
		self.Shansep = Shansep(client, ID, documentProxyID)
		self.VerticalStressRatio = VerticalStressRatio(client, ID, documentProxyID)
		self.SnowdenModAnisotropicLinear = SnowdenModAnisotropicLinear(client, ID, documentProxyID)
		self.AnisotropicLinear = AnisotropicLinear(client, ID, documentProxyID)
		self.GeneralizedAnisotropic = GeneralizedAnisotropic(client, ID, documentProxyID)
		self.JointedMohrCoulomb = JointedMohrCoulomb(client, ID, documentProxyID)
		self.JointedGeneralizedHoekBrown = JointedGeneralizedHoekBrown(client, ID, documentProxyID)
		self.ChSoilStrength = ChSoilStrength(client, ID, documentProxyID)
		self.CySoilStrength = CySoilStrength(client, ID, documentProxyID)
		self.DoubleYieldStrength = DoubleYieldStrength(client, ID, documentProxyID)
		self.HardeningSoilStrength = HardeningSoilStrength(client, ID, documentProxyID)
		self.HardeningSoilWithSmallStrainStiffness = HardeningSoilWithSmallStrainStiffness(client, ID, documentProxyID)
		self.SoftSoilStrength = SoftSoilStrength(client, ID, documentProxyID)
		self.SoftSoilCreepStrength = SoftSoilCreepStrength(client, ID, documentProxyID)
		self.SwellingRockStrength = SwellingRockStrength(client, ID, documentProxyID)
		super().__init__(client, ID, documentProxyID)
	def getFailureCriterion(self) -> StrengthCriteriaTypes:
		return StrengthCriteriaTypes(self._getEnumEStrengthCriteriaTypesProperty("MP_FAILURE_CRITERION"))
	def setFailureCriterion(self, value: StrengthCriteriaTypes):
		return self._setEnumEStrengthCriteriaTypesProperty("MP_FAILURE_CRITERION", value)
	def getUnsaturatedBehavior(self) -> UnsaturatedParameterType:
		return UnsaturatedParameterType(self._getEnumEUnsaturatedParameterTypeProperty("MP_UNSATURATED_PARAMETER_TYPE"))
	def setUnsaturatedBehavior(self, value: UnsaturatedParameterType):
		return self._setEnumEUnsaturatedParameterTypeProperty("MP_UNSATURATED_PARAMETER_TYPE", value)
	def getUnsaturatedShearStrengthType(self) -> UnsaturatedShearStrengthType:
		return UnsaturatedShearStrengthType(self._getEnumEUnsaturatedShearStrengthTypeProperty("MP_UNSATURATED_SHEAR_STRENGTH_TYPE"))
	def setUnsaturatedShearStrengthType(self, value: UnsaturatedShearStrengthType):
		return self._setEnumEUnsaturatedShearStrengthTypeProperty("MP_UNSATURATED_SHEAR_STRENGTH_TYPE", value)
	def getUnsaturatedShearStrengthAngle(self) -> float:
		return self._getDoubleProperty("MP_UNSATURATED_SHEAR_STRENGTH_ANGLE")
	def setUnsaturatedShearStrengthAngle(self, value: float):
		return self._setDoubleProperty("MP_UNSATURATED_SHEAR_STRENGTH_ANGLE", value)
	def getAirEntryValue(self) -> float:
		return self._getDoubleProperty("MP_UNSATURATED_AIR_ENTRY_VALUE")
	def setAirEntryValue(self, value: float):
		return self._setDoubleProperty("MP_UNSATURATED_AIR_ENTRY_VALUE", value)
	def getSingleEffectiveStressMethod(self) -> UnsaturatedSingleEffectiveStressMethod:
		return UnsaturatedSingleEffectiveStressMethod(self._getEnumEUnsaturatedSingleEffectiveStressMethodProperty("MP_UNSATURATED_SINGLE_EFFECTIVE_STRESS_METHOD"))
	def setSingleEffectiveStressMethod(self, value: UnsaturatedSingleEffectiveStressMethod):
		return self._setEnumEUnsaturatedSingleEffectiveStressMethodProperty("MP_UNSATURATED_SINGLE_EFFECTIVE_STRESS_METHOD", value)
	def getAlpha(self) -> float:
		return self._getDoubleProperty("MP_UNSATURATED_ALPHA")
	def setAlpha(self, value: float):
		return self._setDoubleProperty("MP_UNSATURATED_ALPHA", value)
	def getAirEntrySuction(self) -> float:
		return self._getDoubleProperty("MP_UNSATURATED_AIR_ENTRY_SUCTION")
	def setAirEntrySuction(self, value: float):
		return self._setDoubleProperty("MP_UNSATURATED_AIR_ENTRY_SUCTION", value)
	def getCriticalSuction(self) -> float:
		return self._getDoubleProperty("MP_UNSATURATED_CRITICAL_SUCTION")
	def setCriticalSuction(self, value: float):
		return self._setDoubleProperty("MP_UNSATURATED_CRITICAL_SUCTION", value)
	def getMaterialParameter(self) -> float:
		return self._getDoubleProperty("MP_UNSATURATED_MATERIAL_PARAMETER")
	def setMaterialParameter(self, value: float):
		return self._setDoubleProperty("MP_UNSATURATED_MATERIAL_PARAMETER", value)
	def getUseCutoff(self) -> bool:
		return self._getBoolProperty("MP_UNSATURATED_USE_CUTOFF")
	def setUseCutoff(self, value: bool):
		return self._setBoolProperty("MP_UNSATURATED_USE_CUTOFF", value)
	def getCutoffValue(self) -> float:
		return self._getDoubleProperty("MP_UNSATURATED_CUTOFF_VALUE")
	def setCutoffValue(self, value: float):
		return self._setDoubleProperty("MP_UNSATURATED_CUTOFF_VALUE", value)
	def getTabularValues(self) -> UnsaturatedTabularValueMethod:
		return UnsaturatedTabularValueMethod(self._getEnumEUnsaturatedTabularValueMethodProperty("MP_UNSATURATED_TABULAR_VALUE_METHOD"))
	def setTabularValues(self, value: UnsaturatedTabularValueMethod):
		return self._setEnumEUnsaturatedTabularValueMethodProperty("MP_UNSATURATED_TABULAR_VALUE_METHOD", value)
	def setUnsaturatedZoneTableWithRespectToSuction(self, coefficients: list[float], values: list[float]):
		"""
		Specify the coefficient and values with respect to suction.
		"""
		return self._callFunction("setUnsaturatedZoneTableWithRespectToSuction", [coefficients, values])
	def getUnsaturatedZoneTableWithRespectToSuction(self) -> tuple[list[float],list[float]]:
		"""
		Returns a tuple of lists where the first element is coefficients and the second is values with respect to suction.
		"""
		return self._callFunction("getUnsaturatedZoneTableWithRespectToSuction", [])
	def setUnsaturatedZoneTableWithRespectToDegreeOfSaturation(self, coefficients: list[float], values: list[float]):
		"""
		Specify the coefficient and values with respect to degree of saturation.
		"""
		return self._callFunction("setUnsaturatedZoneTableWithRespectToDegreeOfSaturation", [coefficients, values])
	def getUnsaturatedZoneTableWithRespectToDegreeOfSaturation(self) -> list[tuple[float,float]]:
		"""
		Returns a tuple of lists where the first element is coefficients and the second is values with respect to degree of saturation.
		"""
		return self._callFunction("getUnsaturatedZoneTableWithRespectToDegreeOfSaturation", [])
	def setUnsaturatedZoneTableWithRespectToEffectiveDegreeOfSaturation(self, coefficients: list[float], values: list[float]):
		"""
		Specify the coefficient and values with respect to effective degree of saturation.
		"""
		return self._callFunction("setUnsaturatedZoneTableWithRespectToEffectiveDegreeOfSaturation", [coefficients, values])
	def getUnsaturatedZoneTableWithRespectToEffectiveDegreeOfSaturation(self) -> list[tuple[float,float]]:
		"""
		Returns a tuple of lists where the first element is coefficients and the second is values with respect to effective degree of saturation.
		"""
		return self._callFunction("getUnsaturatedZoneTableWithRespectToEffectiveDegreeOfSaturation", [])