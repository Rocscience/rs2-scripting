from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class MaterialDependent(PropertyProxy):
	def getNormalStiffness(self) -> float:
		return self._getDoubleProperty("JP_NORMAL_STIFFNESS")
	def setNormalStiffness(self, value: float):
		return self._setDoubleProperty("JP_NORMAL_STIFFNESS", value)
	def getInterfaceCoefficient(self) -> float:
		return self._getDoubleProperty("JP_INTERFACE_COEFFICIENT")
	def setInterfaceCoefficient(self, value: float):
		return self._setDoubleProperty("JP_INTERFACE_COEFFICIENT", value)
	def getShearStiffness(self) -> float:
		return self._getDoubleProperty("JP_SHEAR_STIFFNESS")
	def setShearStiffness(self, value: float):
		return self._setDoubleProperty("JP_SHEAR_STIFFNESS", value)
	def getDefineStiffness(self) -> DefineStiffness:
		return DefineStiffness(self._getEnumEJointStiffnessDefineProperty("JP_DEFINE_STIFFNESS"))
	def setDefineStiffness(self, value: DefineStiffness):
		return self._setEnumEJointStiffnessDefineProperty("JP_DEFINE_STIFFNESS", value)
	def getStiffnessCoefficient(self) -> float:
		return self._getDoubleProperty("JP_STIFFNESS_COEFFICIENT")
	def setStiffnessCoefficient(self, value: float):
		return self._setDoubleProperty("JP_STIFFNESS_COEFFICIENT", value)
	def getApplyPorePressure(self) -> bool:
		return self._getBoolProperty("JP_USE_GROUNDWATER_PORE_PRESSURE")
	def setApplyPorePressure(self, value: bool):
		return self._setBoolProperty("JP_USE_GROUNDWATER_PORE_PRESSURE", value)
	def getApplyAdditionalPressureInsideJoint(self) -> bool:
		return self._getBoolProperty("JP_USE_ADDITIONAL_PRESSURE")
	def setApplyAdditionalPressureInsideJoint(self, value: bool):
		return self._setBoolProperty("JP_USE_ADDITIONAL_PRESSURE", value)
	def getAdditionalPressureType(self) -> AdditionalPressureType:
		return AdditionalPressureType(self._getEnumEJointWaterPressureTypeProperty("JP_ADDITIONAL_TYPE"))
	def setAdditionalPressureType(self, value: AdditionalPressureType):
		return self._setEnumEJointWaterPressureTypeProperty("JP_ADDITIONAL_TYPE", value)
	def getAdditionalPressureInsideJoint(self) -> float:
		return self._getDoubleProperty("JP_ADDITIONAL_PRESSURE")
	def setAdditionalPressureInsideJoint(self, value: float):
		return self._setDoubleProperty("JP_ADDITIONAL_PRESSURE", value)
	def getPiezoID(self) -> int:
		return self._getIntProperty("JP_ADDITIONAL_PIEZO_ID")
	def setPiezoID(self, value: int):
		return self._setIntProperty("JP_ADDITIONAL_PIEZO_ID", value)
	def getApplyPressureToLinerSideOnly(self) -> bool:
		return self._getBoolProperty("JP_USE_PRESSURE_TO_LINER_SIDE_ONLY")
	def setApplyPressureToLinerSideOnly(self, value: bool):
		return self._setBoolProperty("JP_USE_PRESSURE_TO_LINER_SIDE_ONLY", value)
	def setMaterialDependentProperties(self, NormalStiffness : float = None, InterfaceCoefficient : float = None, ShearStiffness : float = None, DefineStiffness : DefineStiffness = None, StiffnessCoefficient : float = None, ApplyPorePressure : bool = None, ApplyAdditionalPressureInsideJoint : bool = None, AdditionalPressureType : AdditionalPressureType = None, AdditionalPressureInsideJoint : float = None, PiezoID : int = None, ApplyPressureToLinerSideOnly : bool = None):
		if(NormalStiffness):
			self._setDoubleProperty("JP_NORMAL_STIFFNESS", NormalStiffness)
		if(InterfaceCoefficient):
			self._setDoubleProperty("JP_INTERFACE_COEFFICIENT", InterfaceCoefficient)
		if(ShearStiffness):
			self._setDoubleProperty("JP_SHEAR_STIFFNESS", ShearStiffness)
		if(DefineStiffness):
			self._setEnumEJointStiffnessDefineProperty("JP_DEFINE_STIFFNESS", DefineStiffness)
		if(StiffnessCoefficient):
			self._setDoubleProperty("JP_STIFFNESS_COEFFICIENT", StiffnessCoefficient)
		if(ApplyPorePressure):
			self._setBoolProperty("JP_USE_GROUNDWATER_PORE_PRESSURE", ApplyPorePressure)
		if(ApplyAdditionalPressureInsideJoint):
			self._setBoolProperty("JP_USE_ADDITIONAL_PRESSURE", ApplyAdditionalPressureInsideJoint)
		if(AdditionalPressureType):
			self._setEnumEJointWaterPressureTypeProperty("JP_ADDITIONAL_TYPE", AdditionalPressureType)
		if(AdditionalPressureInsideJoint):
			self._setDoubleProperty("JP_ADDITIONAL_PRESSURE", AdditionalPressureInsideJoint)
		if(PiezoID):
			self._setIntProperty("JP_ADDITIONAL_PIEZO_ID", PiezoID)
		if(ApplyPressureToLinerSideOnly):
			self._setBoolProperty("JP_USE_PRESSURE_TO_LINER_SIDE_ONLY", ApplyPressureToLinerSideOnly)