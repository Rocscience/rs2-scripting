from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.MohrCoulombStrength import MohrCoulombStrength
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.HoekBrown import HoekBrown
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.DruckerPrager import DruckerPrager
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.GeneralizedHoekBrown import GeneralizedHoekBrown
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.DiscreteFunction import DiscreteFunction
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.CamClay import CamClay
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.ModifiedCamClay import ModifiedCamClay
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.MohrCoulombWithCap import MohrCoulombWithCap
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.SofteningHardeningModel import SofteningHardeningModel
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.BarcelonaBasic import BarcelonaBasic
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.NorSandStrength import NorSandStrength
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.BoundingSurfacePlasticity import BoundingSurfacePlasticity
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.ManzariAndDafaliasStrength import ManzariAndDafaliasStrength
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.PM4SandStrength import PM4SandStrength
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.PM4SiltStrength import PM4SiltStrength
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.Finn import Finn
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.BartonBandisStrength import BartonBandisStrength
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.Hyperbolic import Hyperbolic
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.PowerCurve import PowerCurve
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.ShearNormalFunction import ShearNormalFunction
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.Shansep import Shansep
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.VerticalStressRatio import VerticalStressRatio
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.SnowdenModAnisotropicLinear import SnowdenModAnisotropicLinear
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.AnisotropicLinear import AnisotropicLinear
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.GeneralizedAnisotropic import GeneralizedAnisotropic
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.JointedMohrCoulomb import JointedMohrCoulomb
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.JointedGeneralizedHoekBrown import JointedGeneralizedHoekBrown
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.ChSoilStrength import ChSoilStrength
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.CySoilStrength import CySoilStrength
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.DoubleYieldStrength import DoubleYieldStrength
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.HardeningSoilStrength import HardeningSoilStrength
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.HardeningSoilWithSmallStrainStiffness import HardeningSoilWithSmallStrainStiffness
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.SoftSoilStrength import SoftSoilStrength
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.SoftSoilCreepStrength import SoftSoilCreepStrength
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.SwellingRockStrength import SwellingRockStrength
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
	def setUnsaturatedZoneTable(self, coefficients: list[float], values: list[float]):
		"""
		Depending on the type of tabular values selected, specify the coefficient and values with respect to suction, degree of saturation or effective degree of saturation.
		"""
		return self._callFunction("setUnsaturatedZoneTable", [coefficients, values])
	def getUnsaturatedZoneTable(self) -> list[tuple(float,float)]:
		"""
		Returns a list tuples where the first element is coefficients and the second is values with respect to suction, degree of saturation or effective degree of saturation.
		"""
		return self._callFunction("getUnsaturatedZoneTable", [])
