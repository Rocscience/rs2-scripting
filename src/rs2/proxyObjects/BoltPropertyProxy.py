from proxyObjects.propertyProxy import PropertyProxy
from enum import Enum, auto
from typing import List
class BoltProperty(PropertyProxy):
	class BoltTypes(Enum):
		END_ANCHORED = "END_ANCHORED"
		FULLY_BONDED = "FULLY_BONDED"
		QUEENS_CABLE = "QUEENS_CABLE"
		SHEAR_BOLT = "SHEAR_BOLT"
		TIEBACK_BOLT = "TIEBACK_BOLT"
	class BulgeTypes(Enum):
		PHASE2_BULGE_GARFORD_25 = "PHASE2_BULGE_GARFORD_25"
		PHASE2_BULGE_NUTCASE_21 = "PHASE2_BULGE_NUTCASE_21"
	class SecondaryBondLengthType(Enum):
		P2_BOLT_TIEBACK_SECONDARY_PERCENT = "P2_BOLT_TIEBACK_SECONDARY_PERCENT"
		P2_BOLT_TIEBACK_SECONDARY_PHYSICAL = "P2_BOLT_TIEBACK_SECONDARY_PHYSICAL"
		P2_BOLT_TIEBACK_SECONDARY_FULLY = "P2_BOLT_TIEBACK_SECONDARY_FULLY"
		NUM_TIEBACK_SECONDARY_TYPE = "NUM_TIEBACK_SECONDARY_TYPE"
	class BoltModels(Enum):
		P2_BOLT_PLASTIC = "P2_BOLT_PLASTIC"
		P2_BOLT_ELASTIC = "P2_BOLT_ELASTIC"
		NUM_BOLT_MODELS = "NUM_BOLT_MODELS"
	def getBoltName(self) -> str:
		return self._getCStringProperty("BP_NAME")
	def setBoltName(self, value: str):
		return self._validateAndSetCStringProperty("BP_NAME", value)
	def getBoltType(self) -> BoltTypes:
		return self.BoltTypes(self._getEnumEBoltTypesProperty("BP_TYPE"))
	def setBoltType(self, value: BoltTypes):
		return self._validateAndSetEnumEBoltTypesProperty("BP_TYPE", value)
	def getBoltColor(self) -> int:
		return self._getUnsignedLongProperty("BP_COLOR")
	def setBoltColor(self, value: int):
		return self._validateAndSetUnsignedLongProperty("BP_COLOR", value)
	def getBoltDiameter(self) -> float:
		return self._getDoubleProperty("BP_BOLT_DIAMETER")
	def setBoltDiameter(self, value: float):
		return self._validateAndSetDoubleProperty("BP_BOLT_DIAMETER", value)
	def getBoltModulusE(self) -> float:
		return self._getDoubleProperty("BP_BOLT_MODULUS")
	def setBoltModulusE(self, value: float):
		return self._validateAndSetDoubleProperty("BP_BOLT_MODULUS", value)
	def getTensileCapacity(self) -> float:
		return self._getDoubleProperty("BP_TENSILE_END")
	def setTensileCapacity(self, value: float):
		return self._validateAndSetDoubleProperty("BP_TENSILE_END", value)
	def getResidualTensileCapacity(self) -> float:
		return self._getDoubleProperty("BP_RES_TENSILE_END")
	def setResidualTensileCapacity(self, value: float):
		return self._validateAndSetDoubleProperty("BP_RES_TENSILE_END", value)
	def getTributaryArea(self) -> float:
		return self._getDoubleProperty("BP_TRIBUTARY_AREA")
	def setTributaryArea(self, value: float):
		return self._validateAndSetDoubleProperty("BP_TRIBUTARY_AREA", value)
	def getBondStrength(self) -> float:
		return self._getDoubleProperty("BP_BOND_STRENGTH")
	def setBondStrength(self, value: float):
		return self._validateAndSetDoubleProperty("BP_BOND_STRENGTH", value)
	def getResidualBondStrength(self) -> float:
		return self._getDoubleProperty("BP_RES_BOND_STRENGTH")
	def setResidualBondStrength(self, value: float):
		return self._validateAndSetDoubleProperty("BP_RES_BOND_STRENGTH", value)
	def getBondShearStiffness(self) -> float:
		return self._getDoubleProperty("BP_BOND_SHEAR_STIFFNESS")
	def setBondShearStiffness(self, value: float):
		return self._validateAndSetDoubleProperty("BP_BOND_SHEAR_STIFFNESS", value)
	def getOutofPlaneSpacing(self) -> float:
		return self._getDoubleProperty("BP_OUT_OF_PLANE_SPACING_BOLT")
	def setOutofPlaneSpacing(self, value: float):
		return self._validateAndSetDoubleProperty("BP_OUT_OF_PLANE_SPACING_BOLT", value)
	def getFacePlates(self) -> bool:
		return self._getBoolProperty("BP_FACE_PLATES")
	def setFacePlates(self, value: bool):
		return self._validateAndSetBoolProperty("BP_FACE_PLATES", value)
	def getPreTensioningForce(self) -> float:
		return self._getDoubleProperty("BP_PRETENSIONING")
	def setPreTensioningForce(self, value: float):
		return self._validateAndSetDoubleProperty("BP_PRETENSIONING", value)
	def getConstantPretensioningForceInInstallStage(self) -> bool:
		return self._getBoolProperty("BP_USE_CONSTANT_FORCE")
	def setConstantPretensioningForceInInstallStage(self, value: bool):
		return self._validateAndSetBoolProperty("BP_USE_CONSTANT_FORCE", value)
	def getBoltModel(self) -> BoltModels:
		return self.BoltModels(self._getEnumEBoltModelsProperty("BP_BOLT_MODEL"))
	def setBoltModel(self, value: BoltModels):
		return self._validateAndSetEnumEBoltModelsProperty("BP_BOLT_MODEL", value)
	def getJointShear(self) -> bool:
		return self._getBoolProperty("BP_USE_JOINT_SHEAR")
	def setJointShear(self, value: bool):
		return self._validateAndSetBoolProperty("BP_USE_JOINT_SHEAR", value)
	def getBoreholeDiameter(self) -> float:
		return self._getDoubleProperty("BP_BOREHOLE_DIAMETER_CABLE")
	def setBoreholeDiameter(self, value: float):
		return self._validateAndSetDoubleProperty("BP_BOREHOLE_DIAMETER_CABLE", value)
	def getCableDiameter(self) -> float:
		return self._getDoubleProperty("BP_CABLE_DIAMETER")
	def setCableDiameter(self, value: float):
		return self._validateAndSetDoubleProperty("BP_CABLE_DIAMETER", value)
	def getCableModulusE(self) -> float:
		return self._getDoubleProperty("BP_CABLE_MODULUS")
	def setCableModulusE(self, value: float):
		return self._validateAndSetDoubleProperty("BP_CABLE_MODULUS", value)
	def getCablePeak(self) -> float:
		return self._getDoubleProperty("BP_CABLE_PEAK")
	def setCablePeak(self, value: float):
		return self._validateAndSetDoubleProperty("BP_CABLE_PEAK", value)
	def getWaterCementRatio(self) -> float:
		return self._getDoubleProperty("BP_WATER_CEMENT_RATIO")
	def setWaterCementRatio(self, value: float):
		return self._validateAndSetDoubleProperty("BP_WATER_CEMENT_RATIO", value)
	def getAddPullOutForce(self) -> bool:
		return self._getBoolProperty("BP_ADD_PULL_OUT_FORCE")
	def setAddPullOutForce(self, value: bool):
		return self._validateAndSetBoolProperty("BP_ADD_PULL_OUT_FORCE", value)
	def getPullOutForce(self) -> float:
		return self._getDoubleProperty("BP_PULL_OUT_FORCE")
	def setPullOutForce(self, value: float):
		return self._validateAndSetDoubleProperty("BP_PULL_OUT_FORCE", value)
	def getConstantShearStiffness(self) -> bool:
		return self._getBoolProperty("BP_ADD_CONSTANT_SHEAR_STIFFNESS")
	def setConstantShearStiffness(self, value: bool):
		return self._validateAndSetBoolProperty("BP_ADD_CONSTANT_SHEAR_STIFFNESS", value)
	def getStiffness(self) -> float:
		return self._getDoubleProperty("BP_CONSTANT_SHEAR_STIFFNESS")
	def setStiffness(self, value: float):
		return self._validateAndSetDoubleProperty("BP_CONSTANT_SHEAR_STIFFNESS", value)
	def getAddBulges(self) -> bool:
		return self._getBoolProperty("BP_ADD_BULGES")
	def setAddBulges(self, value: bool):
		return self._validateAndSetBoolProperty("BP_ADD_BULGES", value)
	def getBulgeType(self) -> BulgeTypes:
		return self.BulgeTypes(self._getEnumEBulgeTypeProperty("BP_BULGE_TYPE"))
	def setBulgeType(self, value: BulgeTypes):
		return self._validateAndSetEnumEBulgeTypeProperty("BP_BULGE_TYPE", value)
	def getUseBondPercentageLength(self) -> bool:
		return self._getBoolProperty("BP_USE_BOND_PERCENTAGE_LENGTH")
	def setUseBondPercentageLength(self, value: bool):
		return self._validateAndSetBoolProperty("BP_USE_BOND_PERCENTAGE_LENGTH", value)
	def getPercentageBondLength(self) -> int:
		return self._getIntProperty("BP_BOND_PERCENTAGE_LENGTH")
	def setPercentageBondLength(self, value: int):
		return self._validateAndSetIntProperty("BP_BOND_PERCENTAGE_LENGTH", value)
	def getBondLength(self) -> float:
		return self._getDoubleProperty("BP_BOND_PHYSICAL_LENGTH")
	def setBondLength(self, value: float):
		return self._validateAndSetDoubleProperty("BP_BOND_PHYSICAL_LENGTH", value)
	def getSecondaryBondLength(self) -> bool:
		return self._getBoolProperty("BP_ADD_SECONDARY_BOND_LENGTH")
	def setSecondaryBondLength(self, value: bool):
		return self._validateAndSetBoolProperty("BP_ADD_SECONDARY_BOND_LENGTH", value)
	def getSecondaryBondLengthType(self) -> SecondaryBondLengthType:
		return self.SecondaryBondLengthType(self._getEnumESecondaryBondLengthTypeProperty("BP_SECONDARY_BOND_LENGTH_TYPE"))
	def setSecondaryBondLengthType(self, value: SecondaryBondLengthType):
		return self._validateAndSetEnumESecondaryBondLengthTypeProperty("BP_SECONDARY_BOND_LENGTH_TYPE", value)
	def getPercentOfSecondaryBondLength(self) -> int:
		return self._getIntProperty("BP_SECONDARY_BOND_LENGTH_PERCENT")
	def setPercentOfSecondaryBondLength(self, value: int):
		return self._validateAndSetIntProperty("BP_SECONDARY_BOND_LENGTH_PERCENT", value)
	def getSecondaryBondLength(self) -> float:
		return self._getDoubleProperty("BP_SECONDARY_BOND_LENGTH_PHYSICAL")
	def setSecondaryBondLength(self, value: float):
		return self._validateAndSetDoubleProperty("BP_SECONDARY_BOND_LENGTH_PHYSICAL", value)
	def getDelayInstallAfterBolt(self) -> int:
		return self._getIntProperty("BP_SECONDARY_BOND_DELAY")
	def setDelayInstallAfterBolt(self, value: int):
		return self._validateAndSetIntProperty("BP_SECONDARY_BOND_DELAY", value)
	def getMaterialDependent(self) -> bool:
		return self._getBoolProperty("BP_MATERIAL_DEPENDENT")
	def setMaterialDependent(self, value: bool):
		return self._validateAndSetBoolProperty("BP_MATERIAL_DEPENDENT", value)
	def getBondStrengthCoefficient(self) -> float:
		return self._getDoubleProperty("BP_BOND_STRENGTH_COEFFICIENT")
	def setBondStrengthCoefficient(self, value: float):
		return self._validateAndSetDoubleProperty("BP_BOND_STRENGTH_COEFFICIENT", value)
	def getBondShearStiffnessCoefficient(self) -> float:
		return self._getDoubleProperty("BP_BOND_SHEAR_STIFF_COEFFICIENT")
	def setBondShearStiffnessCoefficient(self, value: float):
		return self._validateAndSetDoubleProperty("BP_BOND_SHEAR_STIFF_COEFFICIENT", value)
