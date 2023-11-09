from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.MohrCoulomb import MohrCoulomb
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.HoekBrown import HoekBrown
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.DruckerPrager import DruckerPrager
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.GeneralizedHoekBrown import GeneralizedHoekBrown
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.DiscreteFunction import DiscreteFunction
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.CamClay import CamClay
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.ModifiedCamClay import ModifiedCamClay
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.MohrCoulombWithCap import MohrCoulombWithCap
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.SofteningHardeningModel import SofteningHardeningModel
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.BarcelonaBasic import BarcelonaBasic
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.NorSand import NorSand
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.BoundingSurfacePlasticity import BoundingSurfacePlasticity
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.ManzariAndDafalias import ManzariAndDafalias
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.PM4Sand import PM4Sand
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.PM4Silt import PM4Silt
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.Finn import Finn
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.BartonBandis import BartonBandis
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
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.ChSoil import ChSoil
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.CySoil import CySoil
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.DoubleYield import DoubleYield
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.HardeningSoil import HardeningSoil
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.HardeningSoilWithSmallStrainStiffness import HardeningSoilWithSmallStrainStiffness
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.SoftSoil import SoftSoil
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.SoftSoilCreep import SoftSoilCreep
from rs2.proxyObjects.MaterialSubproxyObjects.StrengthSubProxyObjects.SwellingRock import SwellingRock
class Strength(PropertyProxy):
	"""
	:ref:`Material Property Strength Example`
	"""
	def __init__(self, server : Client, ID, documentProxyID):
		self.MohrCoulomb = MohrCoulomb(server, ID, documentProxyID)
		self.HoekBrown = HoekBrown(server, ID, documentProxyID)
		self.DruckerPrager = DruckerPrager(server, ID, documentProxyID)
		self.GeneralizedHoekBrown = GeneralizedHoekBrown(server, ID, documentProxyID)
		self.DiscreteFunction = DiscreteFunction(server, ID, documentProxyID)
		self.CamClay = CamClay(server, ID, documentProxyID)
		self.ModifiedCamClay = ModifiedCamClay(server, ID, documentProxyID)
		self.MohrCoulombWithCap = MohrCoulombWithCap(server, ID, documentProxyID)
		self.SofteningHardeningModel = SofteningHardeningModel(server, ID, documentProxyID)
		self.BarcelonaBasic = BarcelonaBasic(server, ID, documentProxyID)
		self.NorSand = NorSand(server, ID, documentProxyID)
		self.BoundingSurfacePlasticity = BoundingSurfacePlasticity(server, ID, documentProxyID)
		self.ManzariAndDafalias = ManzariAndDafalias(server, ID, documentProxyID)
		self.PM4Sand = PM4Sand(server, ID, documentProxyID)
		self.PM4Silt = PM4Silt(server, ID, documentProxyID)
		self.Finn = Finn(server, ID, documentProxyID)
		self.BartonBandis = BartonBandis(server, ID, documentProxyID)
		self.Hyperbolic = Hyperbolic(server, ID, documentProxyID)
		self.PowerCurve = PowerCurve(server, ID, documentProxyID)
		self.ShearNormalFunction = ShearNormalFunction(server, ID, documentProxyID)
		self.Shansep = Shansep(server, ID, documentProxyID)
		self.VerticalStressRatio = VerticalStressRatio(server, ID, documentProxyID)
		self.SnowdenModAnisotropicLinear = SnowdenModAnisotropicLinear(server, ID, documentProxyID)
		self.AnisotropicLinear = AnisotropicLinear(server, ID, documentProxyID)
		self.GeneralizedAnisotropic = GeneralizedAnisotropic(server, ID, documentProxyID)
		self.JointedMohrCoulomb = JointedMohrCoulomb(server, ID, documentProxyID)
		self.JointedGeneralizedHoekBrown = JointedGeneralizedHoekBrown(server, ID, documentProxyID)
		self.ChSoil = ChSoil(server, ID, documentProxyID)
		self.CySoil = CySoil(server, ID, documentProxyID)
		self.DoubleYield = DoubleYield(server, ID, documentProxyID)
		self.HardeningSoil = HardeningSoil(server, ID, documentProxyID)
		self.HardeningSoilWithSmallStrainStiffness = HardeningSoilWithSmallStrainStiffness(server, ID, documentProxyID)
		self.SoftSoil = SoftSoil(server, ID, documentProxyID)
		self.SoftSoilCreep = SoftSoilCreep(server, ID, documentProxyID)
		self.SwellingRock = SwellingRock(server, ID, documentProxyID)
		super().__init__(server, ID, documentProxyID)
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
