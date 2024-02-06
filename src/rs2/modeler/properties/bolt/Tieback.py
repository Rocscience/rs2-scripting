from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class Tieback(PropertyProxy):
	def getBoltDiameter(self) -> float:
		return self._getDoubleProperty("BP_BOLT_DIAMETER")
	def setBoltDiameter(self, value: float):
		return self._setDoubleProperty("BP_BOLT_DIAMETER", value)
	def getBoltModulusE(self) -> float:
		return self._getDoubleProperty("BP_BOLT_MODULUS")
	def setBoltModulusE(self, value: float):
		return self._setDoubleProperty("BP_BOLT_MODULUS", value)
	def getBoltModel(self) -> BoltModels:
		return BoltModels(self._getEnumEBoltModelsProperty("BP_BOLT_MODEL"))
	def setBoltModel(self, value: BoltModels):
		return self._setEnumEBoltModelsProperty("BP_BOLT_MODEL", value)
	def getTensileCapacity(self) -> float:
		return self._getDoubleProperty("BP_TENSILE_END")
	def setTensileCapacity(self, value: float):
		return self._setDoubleProperty("BP_TENSILE_END", value)
	def getResidualTensileCapacity(self) -> float:
		return self._getDoubleProperty("BP_RES_TENSILE_END")
	def setResidualTensileCapacity(self, value: float):
		return self._setDoubleProperty("BP_RES_TENSILE_END", value)
	def getOutofPlaneSpacing(self) -> float:
		return self._getDoubleProperty("BP_OUT_OF_PLANE_SPACING_BOLT")
	def setOutofPlaneSpacing(self, value: float):
		return self._setDoubleProperty("BP_OUT_OF_PLANE_SPACING_BOLT", value)
	def getMaterialDependent(self) -> bool:
		return self._getBoolProperty("BP_MATERIAL_DEPENDENT")
	def setMaterialDependent(self, value: bool):
		return self._setBoolProperty("BP_MATERIAL_DEPENDENT", value)
	def getBondStrengthCoefficient(self) -> float:
		return self._getDoubleProperty("BP_BOND_STRENGTH_COEFFICIENT")
	def setBondStrengthCoefficient(self, value: float):
		return self._setDoubleProperty("BP_BOND_STRENGTH_COEFFICIENT", value)
	def getBondShearStiffnessCoefficient(self) -> float:
		return self._getDoubleProperty("BP_BOND_SHEAR_STIFF_COEFFICIENT")
	def setBondShearStiffnessCoefficient(self, value: float):
		return self._setDoubleProperty("BP_BOND_SHEAR_STIFF_COEFFICIENT", value)
	def getBondShearStiffness(self) -> float:
		return self._getDoubleProperty("BP_BOND_SHEAR_STIFFNESS")
	def setBondShearStiffness(self, value: float):
		return self._setDoubleProperty("BP_BOND_SHEAR_STIFFNESS", value)
	def getBondStrength(self) -> float:
		return self._getDoubleProperty("BP_BOND_STRENGTH")
	def setBondStrength(self, value: float):
		return self._setDoubleProperty("BP_BOND_STRENGTH", value)
	def getJointShear(self) -> bool:
		return self._getBoolProperty("BP_USE_JOINT_SHEAR")
	def setJointShear(self, value: bool):
		return self._setBoolProperty("BP_USE_JOINT_SHEAR", value)
	def getBoreholeDiameter(self) -> float:
		return self._getDoubleProperty("BP_BOREHOLE_DIAMETER_TIEBACK")
	def setBoreholeDiameter(self, value: float):
		return self._setDoubleProperty("BP_BOREHOLE_DIAMETER_TIEBACK", value)
	def getPreTensioningForce(self) -> float:
		return self._getDoubleProperty("BP_PRETENSIONING")
	def setPreTensioningForce(self, value: float):
		return self._setDoubleProperty("BP_PRETENSIONING", value)
	def getConstantPretensioningForceInInstallStage(self) -> bool:
		return self._getBoolProperty("BP_USE_CONSTANT_FORCE")
	def setConstantPretensioningForceInInstallStage(self, value: bool):
		return self._setBoolProperty("BP_USE_CONSTANT_FORCE", value)
	def getFacePlates(self) -> bool:
		return self._getBoolProperty("BP_FACE_PLATES")
	def setFacePlates(self, value: bool):
		return self._setBoolProperty("BP_FACE_PLATES", value)
	def getAddPullOutForce(self) -> bool:
		return self._getBoolProperty("BP_ADD_PULL_OUT_FORCE")
	def setAddPullOutForce(self, value: bool):
		return self._setBoolProperty("BP_ADD_PULL_OUT_FORCE", value)
	def getPullOutForce(self) -> float:
		return self._getDoubleProperty("BP_PULL_OUT_FORCE")
	def setPullOutForce(self, value: float):
		return self._setDoubleProperty("BP_PULL_OUT_FORCE", value)
	def getUseBondPercentageLength(self) -> bool:
		return self._getBoolProperty("BP_USE_BOND_PERCENTAGE_LENGTH")
	def setUseBondPercentageLength(self, value: bool):
		return self._setBoolProperty("BP_USE_BOND_PERCENTAGE_LENGTH", value)
	def getPercentageBondLength(self) -> int:
		return self._getIntProperty("BP_BOND_PERCENTAGE_LENGTH")
	def setPercentageBondLength(self, value: int):
		return self._setIntProperty("BP_BOND_PERCENTAGE_LENGTH", value)
	def getBondLength(self) -> float:
		return self._getDoubleProperty("BP_BOND_PHYSICAL_LENGTH")
	def setBondLength(self, value: float):
		return self._setDoubleProperty("BP_BOND_PHYSICAL_LENGTH", value)
	def getUseSecondaryBondLength(self) -> bool:
		return self._getBoolProperty("BP_ADD_SECONDARY_BOND_LENGTH")
	def setUseSecondaryBondLength(self, value: bool):
		return self._setBoolProperty("BP_ADD_SECONDARY_BOND_LENGTH", value)
	def getSecondaryBondLengthType(self) -> SecondaryBondLengthType:
		return SecondaryBondLengthType(self._getEnumESecondaryBondLengthTypeProperty("BP_SECONDARY_BOND_LENGTH_TYPE"))
	def setSecondaryBondLengthType(self, value: SecondaryBondLengthType):
		return self._setEnumESecondaryBondLengthTypeProperty("BP_SECONDARY_BOND_LENGTH_TYPE", value)
	def getPercentOfSecondaryBondLength(self) -> int:
		return self._getIntProperty("BP_SECONDARY_BOND_LENGTH_PERCENT")
	def setPercentOfSecondaryBondLength(self, value: int):
		return self._setIntProperty("BP_SECONDARY_BOND_LENGTH_PERCENT", value)
	def getSecondaryBondLength(self) -> float:
		return self._getDoubleProperty("BP_SECONDARY_BOND_LENGTH_PHYSICAL")
	def setSecondaryBondLength(self, value: float):
		return self._setDoubleProperty("BP_SECONDARY_BOND_LENGTH_PHYSICAL", value)
	def getDelayInstallAfterBolt(self) -> int:
		return self._getIntProperty("BP_SECONDARY_BOND_DELAY")
	def setDelayInstallAfterBolt(self, value: int):
		return self._setIntProperty("BP_SECONDARY_BOND_DELAY", value)
	def setProperties(self, BoltDiameter : float = None, BoltModulusE : float = None, BoltModel : BoltModels = None, TensileCapacity : float = None, ResidualTensileCapacity : float = None, OutofPlaneSpacing : float = None, MaterialDependent : bool = None, BondStrengthCoefficient : float = None, BondShearStiffnessCoefficient : float = None, BondShearStiffness : float = None, BondStrength : float = None, JointShear : bool = None, BoreholeDiameter : float = None, PreTensioningForce : float = None, ConstantPretensioningForceInInstallStage : bool = None, FacePlates : bool = None, AddPullOutForce : bool = None, PullOutForce : float = None, UseBondPercentageLength : bool = None, PercentageBondLength : int = None, BondLength : float = None, UseSecondaryBondLength : bool = None, SecondaryBondLengthType : SecondaryBondLengthType = None, PercentOfSecondaryBondLength : int = None, SecondaryBondLength : float = None, DelayInstallAfterBolt : int = None):
		if BoltDiameter is not None:
			self._setDoubleProperty("BP_BOLT_DIAMETER", BoltDiameter)
		if BoltModulusE is not None:
			self._setDoubleProperty("BP_BOLT_MODULUS", BoltModulusE)
		if BoltModel is not None:
			self._setEnumEBoltModelsProperty("BP_BOLT_MODEL", BoltModel)
		if TensileCapacity is not None:
			self._setDoubleProperty("BP_TENSILE_END", TensileCapacity)
		if ResidualTensileCapacity is not None:
			self._setDoubleProperty("BP_RES_TENSILE_END", ResidualTensileCapacity)
		if OutofPlaneSpacing is not None:
			self._setDoubleProperty("BP_OUT_OF_PLANE_SPACING_BOLT", OutofPlaneSpacing)
		if MaterialDependent is not None:
			self._setBoolProperty("BP_MATERIAL_DEPENDENT", MaterialDependent)
		if BondStrengthCoefficient is not None:
			self._setDoubleProperty("BP_BOND_STRENGTH_COEFFICIENT", BondStrengthCoefficient)
		if BondShearStiffnessCoefficient is not None:
			self._setDoubleProperty("BP_BOND_SHEAR_STIFF_COEFFICIENT", BondShearStiffnessCoefficient)
		if BondShearStiffness is not None:
			self._setDoubleProperty("BP_BOND_SHEAR_STIFFNESS", BondShearStiffness)
		if BondStrength is not None:
			self._setDoubleProperty("BP_BOND_STRENGTH", BondStrength)
		if JointShear is not None:
			self._setBoolProperty("BP_USE_JOINT_SHEAR", JointShear)
		if BoreholeDiameter is not None:
			self._setDoubleProperty("BP_BOREHOLE_DIAMETER_TIEBACK", BoreholeDiameter)
		if PreTensioningForce is not None:
			self._setDoubleProperty("BP_PRETENSIONING", PreTensioningForce)
		if ConstantPretensioningForceInInstallStage is not None:
			self._setBoolProperty("BP_USE_CONSTANT_FORCE", ConstantPretensioningForceInInstallStage)
		if FacePlates is not None:
			self._setBoolProperty("BP_FACE_PLATES", FacePlates)
		if AddPullOutForce is not None:
			self._setBoolProperty("BP_ADD_PULL_OUT_FORCE", AddPullOutForce)
		if PullOutForce is not None:
			self._setDoubleProperty("BP_PULL_OUT_FORCE", PullOutForce)
		if UseBondPercentageLength is not None:
			self._setBoolProperty("BP_USE_BOND_PERCENTAGE_LENGTH", UseBondPercentageLength)
		if PercentageBondLength is not None:
			self._setIntProperty("BP_BOND_PERCENTAGE_LENGTH", PercentageBondLength)
		if BondLength is not None:
			self._setDoubleProperty("BP_BOND_PHYSICAL_LENGTH", BondLength)
		if UseSecondaryBondLength is not None:
			self._setBoolProperty("BP_ADD_SECONDARY_BOND_LENGTH", UseSecondaryBondLength)
		if SecondaryBondLengthType is not None:
			self._setEnumESecondaryBondLengthTypeProperty("BP_SECONDARY_BOND_LENGTH_TYPE", SecondaryBondLengthType)
		if PercentOfSecondaryBondLength is not None:
			self._setIntProperty("BP_SECONDARY_BOND_LENGTH_PERCENT", PercentOfSecondaryBondLength)
		if SecondaryBondLength is not None:
			self._setDoubleProperty("BP_SECONDARY_BOND_LENGTH_PHYSICAL", SecondaryBondLength)
		if DelayInstallAfterBolt is not None:
			self._setIntProperty("BP_SECONDARY_BOND_DELAY", DelayInstallAfterBolt)
	def getProperties(self):
		return {
		"BoltDiameter" : self.getBoltDiameter(), 
		"BoltModulusE" : self.getBoltModulusE(), 
		"BoltModel" : self.getBoltModel(), 
		"TensileCapacity" : self.getTensileCapacity(), 
		"ResidualTensileCapacity" : self.getResidualTensileCapacity(), 
		"OutofPlaneSpacing" : self.getOutofPlaneSpacing(), 
		"MaterialDependent" : self.getMaterialDependent(), 
		"BondStrengthCoefficient" : self.getBondStrengthCoefficient(), 
		"BondShearStiffnessCoefficient" : self.getBondShearStiffnessCoefficient(), 
		"BondShearStiffness" : self.getBondShearStiffness(), 
		"BondStrength" : self.getBondStrength(), 
		"JointShear" : self.getJointShear(), 
		"BoreholeDiameter" : self.getBoreholeDiameter(), 
		"PreTensioningForce" : self.getPreTensioningForce(), 
		"ConstantPretensioningForceInInstallStage" : self.getConstantPretensioningForceInInstallStage(), 
		"FacePlates" : self.getFacePlates(), 
		"AddPullOutForce" : self.getAddPullOutForce(), 
		"PullOutForce" : self.getPullOutForce(), 
		"UseBondPercentageLength" : self.getUseBondPercentageLength(), 
		"PercentageBondLength" : self.getPercentageBondLength(), 
		"BondLength" : self.getBondLength(), 
		"UseSecondaryBondLength" : self.getUseSecondaryBondLength(), 
		"SecondaryBondLengthType" : self.getSecondaryBondLengthType(), 
		"PercentOfSecondaryBondLength" : self.getPercentOfSecondaryBondLength(), 
		"SecondaryBondLength" : self.getSecondaryBondLength(), 
		"DelayInstallAfterBolt" : self.getDelayInstallAfterBolt(), 
		}
