from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class Swellex(PropertyProxy):
	def getTensileCapacity(self) -> float:
		return self._getDoubleProperty("BP_TENSILE_END")
	def setTensileCapacity(self, value: float):
		return self._setDoubleProperty("BP_TENSILE_END", value)
	def getResidualTensileCapacity(self) -> float:
		return self._getDoubleProperty("BP_RES_TENSILE_END")
	def setResidualTensileCapacity(self, value: float):
		return self._setDoubleProperty("BP_RES_TENSILE_END", value)
	def getTributaryArea(self) -> float:
		return self._getDoubleProperty("BP_TRIBUTARY_AREA")
	def setTributaryArea(self, value: float):
		return self._setDoubleProperty("BP_TRIBUTARY_AREA", value)
	def getBoltModulusE(self) -> float:
		return self._getDoubleProperty("BP_BOLT_MODULUS")
	def setBoltModulusE(self, value: float):
		return self._setDoubleProperty("BP_BOLT_MODULUS", value)
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
	def getResidualBondStrength(self) -> float:
		return self._getDoubleProperty("BP_RES_BOND_STRENGTH")
	def setResidualBondStrength(self, value: float):
		return self._setDoubleProperty("BP_RES_BOND_STRENGTH", value)
	def getBoltModel(self) -> BoltModels:
		return BoltModels(self._getEnumEBoltModelsProperty("BP_BOLT_MODEL"))
	def setBoltModel(self, value: BoltModels):
		return self._setEnumEBoltModelsProperty("BP_BOLT_MODEL", value)
	def getJointShear(self) -> bool:
		return self._getBoolProperty("BP_USE_JOINT_SHEAR")
	def setJointShear(self, value: bool):
		return self._setBoolProperty("BP_USE_JOINT_SHEAR", value)
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
	def setProperties(self, TensileCapacity : float = None, ResidualTensileCapacity : float = None, TributaryArea : float = None, BoltModulusE : float = None, OutofPlaneSpacing : float = None, MaterialDependent : bool = None, BondStrengthCoefficient : float = None, BondShearStiffnessCoefficient : float = None, BondShearStiffness : float = None, BondStrength : float = None, ResidualBondStrength : float = None, BoltModel : BoltModels = None, JointShear : bool = None, PreTensioningForce : float = None, ConstantPretensioningForceInInstallStage : bool = None, FacePlates : bool = None, AddPullOutForce : bool = None, PullOutForce : float = None):
		if TensileCapacity is not None:
			self._setDoubleProperty("BP_TENSILE_END", TensileCapacity)
		if ResidualTensileCapacity is not None:
			self._setDoubleProperty("BP_RES_TENSILE_END", ResidualTensileCapacity)
		if TributaryArea is not None:
			self._setDoubleProperty("BP_TRIBUTARY_AREA", TributaryArea)
		if BoltModulusE is not None:
			self._setDoubleProperty("BP_BOLT_MODULUS", BoltModulusE)
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
		if ResidualBondStrength is not None:
			self._setDoubleProperty("BP_RES_BOND_STRENGTH", ResidualBondStrength)
		if BoltModel is not None:
			self._setEnumEBoltModelsProperty("BP_BOLT_MODEL", BoltModel)
		if JointShear is not None:
			self._setBoolProperty("BP_USE_JOINT_SHEAR", JointShear)
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
	def getProperties(self):
		return {
		"TensileCapacity" : self.getTensileCapacity(), 
		"ResidualTensileCapacity" : self.getResidualTensileCapacity(), 
		"TributaryArea" : self.getTributaryArea(), 
		"BoltModulusE" : self.getBoltModulusE(), 
		"OutofPlaneSpacing" : self.getOutofPlaneSpacing(), 
		"MaterialDependent" : self.getMaterialDependent(), 
		"BondStrengthCoefficient" : self.getBondStrengthCoefficient(), 
		"BondShearStiffnessCoefficient" : self.getBondShearStiffnessCoefficient(), 
		"BondShearStiffness" : self.getBondShearStiffness(), 
		"BondStrength" : self.getBondStrength(), 
		"ResidualBondStrength" : self.getResidualBondStrength(), 
		"BoltModel" : self.getBoltModel(), 
		"JointShear" : self.getJointShear(), 
		"PreTensioningForce" : self.getPreTensioningForce(), 
		"ConstantPretensioningForceInInstallStage" : self.getConstantPretensioningForceInInstallStage(), 
		"FacePlates" : self.getFacePlates(), 
		"AddPullOutForce" : self.getAddPullOutForce(), 
		"PullOutForce" : self.getPullOutForce(), 
		}
