from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class Swellex(PropertyProxy):
	def getTensileCapacity(self) -> float:
		return self._getDoubleProperty("BP_TENSILE_END")
	def setTensileCapacity(self, value: float):
		return self._validateAndSetDoubleProperty("BP_TENSILE_END", value)
	def getResidualTensileCapacity(self) -> float:
		return self._getDoubleProperty("BP_RES_TENSILE_END")
	def setResidualTensileCapacity(self, value: float):
		return self._validateAndSetDoubleProperty("BP_RES_TENSILE_END", value)
	def getMaterialDependent(self) -> bool:
		return self._getBoolProperty("BP_MATERIAL_DEPENDENT")
	def setMaterialDependent(self, value: bool):
		return self._validateAndSetBoolProperty("BP_MATERIAL_DEPENDENT", value)
	def getTributaryArea(self) -> float:
		return self._getDoubleProperty("BP_TRIBUTARY_AREA")
	def setTributaryArea(self, value: float):
		return self._validateAndSetDoubleProperty("BP_TRIBUTARY_AREA", value)
	def getBoltModulusE(self) -> float:
		return self._getDoubleProperty("BP_BOLT_MODULUS")
	def setBoltModulusE(self, value: float):
		return self._validateAndSetDoubleProperty("BP_BOLT_MODULUS", value)
	def getOutofPlaneSpacing(self) -> float:
		return self._getDoubleProperty("BP_OUT_OF_PLANE_SPACING_BOLT")
	def setOutofPlaneSpacing(self, value: float):
		return self._validateAndSetDoubleProperty("BP_OUT_OF_PLANE_SPACING_BOLT", value)
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
	def getResidualBondStrength(self) -> float:
		return self._getDoubleProperty("BP_RES_BOND_STRENGTH")
	def setResidualBondStrength(self, value: float):
		return self._validateAndSetDoubleProperty("BP_RES_BOND_STRENGTH", value)
	def getBoltModel(self) -> BoltModels:
		return BoltModels(self._getEnumEBoltModelsProperty("BP_BOLT_MODEL"))
	def setBoltModel(self, value: BoltModels):
		return self._validateAndSetEnumEBoltModelsProperty("BP_BOLT_MODEL", value)
	def getJointShear(self) -> bool:
		return self._getBoolProperty("BP_USE_JOINT_SHEAR")
	def setJointShear(self, value: bool):
		return self._validateAndSetBoolProperty("BP_USE_JOINT_SHEAR", value)
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