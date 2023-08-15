from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class Tieback(PropertyProxy):
	def getOutofPlaneSpacing(self) -> float:
		return self._getDoubleProperty("BP_OUT_OF_PLANE_SPACING_BOLT")
	def setOutofPlaneSpacing(self, value: float):
		return self._validateAndSetDoubleProperty("BP_OUT_OF_PLANE_SPACING_BOLT", value)
	def getBoltDiameter(self) -> float:
		return self._getDoubleProperty("BP_BOLT_DIAMETER")
	def setBoltDiameter(self, value: float):
		return self._validateAndSetDoubleProperty("BP_BOLT_DIAMETER", value)
	def getBoltModulusE(self) -> float:
		return self._getDoubleProperty("BP_BOLT_MODULUS")
	def setBoltModulusE(self, value: float):
		return self._validateAndSetDoubleProperty("BP_BOLT_MODULUS", value)
	def getMaterialDependent(self) -> bool:
		return self._getBoolProperty("BP_MATERIAL_DEPENDENT")
	def setMaterialDependent(self, value: bool):
		return self._validateAndSetBoolProperty("BP_MATERIAL_DEPENDENT", value)
	def getBoltModel(self) -> BoltModels:
		return BoltModels(self._getEnumEBoltModelsProperty("BP_BOLT_MODEL"))
	def setBoltModel(self, value: BoltModels):
		return self._validateAndSetEnumEBoltModelsProperty("BP_BOLT_MODEL", value)
	def getTensileCapacity(self) -> float:
		return self._getDoubleProperty("BP_TENSILE_END")
	def setTensileCapacity(self, value: float):
		return self._validateAndSetDoubleProperty("BP_TENSILE_END", value)
	def getResidualTensileCapacity(self) -> float:
		return self._getDoubleProperty("BP_RES_TENSILE_END")
	def setResidualTensileCapacity(self, value: float):
		return self._validateAndSetDoubleProperty("BP_RES_TENSILE_END", value)
	def getBondStrengthCoefficient(self) -> float:
		return self._getDoubleProperty("BP_BOND_STRENGTH_COEFFICIENT")
	def setBondStrengthCoefficient(self, value: float):
		return self._validateAndSetDoubleProperty("BP_BOND_STRENGTH_COEFFICIENT", value)
	def getBondShearStiffnessCoefficient(self) -> float:
		return self._getDoubleProperty("BP_BOND_SHEAR_STIFF_COEFFICIENT")
	def setBondShearStiffnessCoefficient(self, value: float):
		return self._validateAndSetDoubleProperty("BP_BOND_SHEAR_STIFF_COEFFICIENT", value)
	def getBondShearStiffness(self) -> float:
		return self._getDoubleProperty("BP_BOND_SHEAR_STIFFNESS")
	def setBondShearStiffness(self, value: float):
		return self._validateAndSetDoubleProperty("BP_BOND_SHEAR_STIFFNESS", value)
	def getBondStrength(self) -> float:
		return self._getDoubleProperty("BP_BOND_STRENGTH")
	def setBondStrength(self, value: float):
		return self._validateAndSetDoubleProperty("BP_BOND_STRENGTH", value)
	def getJointShear(self) -> bool:
		return self._getBoolProperty("BP_USE_JOINT_SHEAR")
	def setJointShear(self, value: bool):
		return self._validateAndSetBoolProperty("BP_USE_JOINT_SHEAR", value)
	def getBoreholeDiameter(self) -> float:
		return self._getDoubleProperty("BP_BOREHOLE_DIAMETER_TIEBACK")
	def setBoreholeDiameter(self, value: float):
		return self._validateAndSetDoubleProperty("BP_BOREHOLE_DIAMETER_TIEBACK", value)
	def getPreTensioningForce(self) -> float:
		return self._getDoubleProperty("BP_PRETENSIONING")
	def setPreTensioningForce(self, value: float):
		return self._validateAndSetDoubleProperty("BP_PRETENSIONING", value)
	def getConstantPretensioningForceInInstallStage(self) -> bool:
		return self._getBoolProperty("BP_USE_CONSTANT_FORCE")
	def setConstantPretensioningForceInInstallStage(self, value: bool):
		return self._validateAndSetBoolProperty("BP_USE_CONSTANT_FORCE", value)
	def getFacePlates(self) -> bool:
		return self._getBoolProperty("BP_FACE_PLATES")
	def setFacePlates(self, value: bool):
		return self._validateAndSetBoolProperty("BP_FACE_PLATES", value)
	def getAddPullOutForce(self) -> bool:
		return self._getBoolProperty("BP_ADD_PULL_OUT_FORCE")
	def setAddPullOutForce(self, value: bool):
		return self._validateAndSetBoolProperty("BP_ADD_PULL_OUT_FORCE", value)
	def getPullOutForce(self) -> float:
		return self._getDoubleProperty("BP_PULL_OUT_FORCE")
	def setPullOutForce(self, value: float):
		return self._validateAndSetDoubleProperty("BP_PULL_OUT_FORCE", value)
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
	def getUseSecondaryBondLength(self) -> bool:
		return self._getBoolProperty("BP_ADD_SECONDARY_BOND_LENGTH")
	def setUseSecondaryBondLength(self, value: bool):
		return self._validateAndSetBoolProperty("BP_ADD_SECONDARY_BOND_LENGTH", value)
	def getSecondaryBondLengthType(self) -> SecondaryBondLengthType:
		return SecondaryBondLengthType(self._getEnumESecondaryBondLengthTypeProperty("BP_SECONDARY_BOND_LENGTH_TYPE"))
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
	def setProperties(self, OutofPlaneSpacing : float = None, BoltDiameter : float = None, BoltModulusE : float = None, MaterialDependent : bool = None, BoltModel : BoltModels = None, TensileCapacity : float = None, ResidualTensileCapacity : float = None, BondStrengthCoefficient : float = None, BondShearStiffnessCoefficient : float = None, BondShearStiffness : float = None, BondStrength : float = None, JointShear : bool = None, BoreholeDiameter : float = None, PreTensioningForce : float = None, ConstantPretensioningForceInInstallStage : bool = None, FacePlates : bool = None, AddPullOutForce : bool = None, PullOutForce : float = None, UseBondPercentageLength : bool = None, PercentageBondLength : int = None, BondLength : float = None, UseSecondaryBondLength : bool = None, SecondaryBondLengthType : SecondaryBondLengthType = None, PercentOfSecondaryBondLength : int = None, SecondaryBondLength : float = None, DelayInstallAfterBolt : int = None):
		if OutofPlaneSpacing:
			self._validateAndSetDoubleProperty("BP_OUT_OF_PLANE_SPACING_BOLT", OutofPlaneSpacing)
		if BoltDiameter:
			self._validateAndSetDoubleProperty("BP_BOLT_DIAMETER", BoltDiameter)
		if BoltModulusE:
			self._validateAndSetDoubleProperty("BP_BOLT_MODULUS", BoltModulusE)
		if MaterialDependent:
			self._validateAndSetBoolProperty("BP_MATERIAL_DEPENDENT", MaterialDependent)
		if BoltModel:
			self._validateAndSetEnumEBoltModelsProperty("BP_BOLT_MODEL", BoltModel)
		if TensileCapacity:
			self._validateAndSetDoubleProperty("BP_TENSILE_END", TensileCapacity)
		if ResidualTensileCapacity:
			self._validateAndSetDoubleProperty("BP_RES_TENSILE_END", ResidualTensileCapacity)
		if BondStrengthCoefficient:
			self._validateAndSetDoubleProperty("BP_BOND_STRENGTH_COEFFICIENT", BondStrengthCoefficient)
		if BondShearStiffnessCoefficient:
			self._validateAndSetDoubleProperty("BP_BOND_SHEAR_STIFF_COEFFICIENT", BondShearStiffnessCoefficient)
		if BondShearStiffness:
			self._validateAndSetDoubleProperty("BP_BOND_SHEAR_STIFFNESS", BondShearStiffness)
		if BondStrength:
			self._validateAndSetDoubleProperty("BP_BOND_STRENGTH", BondStrength)
		if JointShear:
			self._validateAndSetBoolProperty("BP_USE_JOINT_SHEAR", JointShear)
		if BoreholeDiameter:
			self._validateAndSetDoubleProperty("BP_BOREHOLE_DIAMETER_TIEBACK", BoreholeDiameter)
		if PreTensioningForce:
			self._validateAndSetDoubleProperty("BP_PRETENSIONING", PreTensioningForce)
		if ConstantPretensioningForceInInstallStage:
			self._validateAndSetBoolProperty("BP_USE_CONSTANT_FORCE", ConstantPretensioningForceInInstallStage)
		if FacePlates:
			self._validateAndSetBoolProperty("BP_FACE_PLATES", FacePlates)
		if AddPullOutForce:
			self._validateAndSetBoolProperty("BP_ADD_PULL_OUT_FORCE", AddPullOutForce)
		if PullOutForce:
			self._validateAndSetDoubleProperty("BP_PULL_OUT_FORCE", PullOutForce)
		if UseBondPercentageLength:
			self._validateAndSetBoolProperty("BP_USE_BOND_PERCENTAGE_LENGTH", UseBondPercentageLength)
		if PercentageBondLength:
			self._validateAndSetIntProperty("BP_BOND_PERCENTAGE_LENGTH", PercentageBondLength)
		if BondLength:
			self._validateAndSetDoubleProperty("BP_BOND_PHYSICAL_LENGTH", BondLength)
		if UseSecondaryBondLength:
			self._validateAndSetBoolProperty("BP_ADD_SECONDARY_BOND_LENGTH", UseSecondaryBondLength)
		if SecondaryBondLengthType:
			self._validateAndSetEnumESecondaryBondLengthTypeProperty("BP_SECONDARY_BOND_LENGTH_TYPE", SecondaryBondLengthType)
		if PercentOfSecondaryBondLength:
			self._validateAndSetIntProperty("BP_SECONDARY_BOND_LENGTH_PERCENT", PercentOfSecondaryBondLength)
		if SecondaryBondLength:
			self._validateAndSetDoubleProperty("BP_SECONDARY_BOND_LENGTH_PHYSICAL", SecondaryBondLength)
		if DelayInstallAfterBolt:
			self._validateAndSetIntProperty("BP_SECONDARY_BOND_DELAY", DelayInstallAfterBolt)