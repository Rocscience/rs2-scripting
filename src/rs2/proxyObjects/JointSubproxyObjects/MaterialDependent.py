from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class MaterialDependent(PropertyProxy):
	def getInterfaceCoefficient(self) -> float:
		return self._getDoubleProperty("JP_INTERFACE_COEFFICIENT")
	def setInterfaceCoefficient(self, value: float):
		return self._setDoubleProperty("JP_INTERFACE_COEFFICIENT", value)
	def getDefineStiffness(self) -> DefineStiffness:
		return DefineStiffness(self._getEnumEJointStiffnessDefineProperty("JP_DEFINE_STIFFNESS"))
	def setDefineStiffness(self, value: DefineStiffness):
		return self._setEnumEJointStiffnessDefineProperty("JP_DEFINE_STIFFNESS", value)
	def getNormalStiffness(self) -> float:
		return self._getDoubleProperty("JP_NORMAL_STIFFNESS")
	def setNormalStiffness(self, value: float):
		return self._setDoubleProperty("JP_NORMAL_STIFFNESS", value)
	def getShearStiffness(self) -> float:
		return self._getDoubleProperty("JP_SHEAR_STIFFNESS")
	def setShearStiffness(self, value: float):
		return self._setDoubleProperty("JP_SHEAR_STIFFNESS", value)
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
		return int(self._getIntProperty("JP_ADDITIONAL_PIEZO_ID"))
	def setPiezoID(self, value: int):
		return self._setIntProperty("JP_ADDITIONAL_PIEZO_ID", value)
	def getApplyPressureToLinerSideOnly(self) -> bool:
		return self._getBoolProperty("JP_USE_PRESSURE_TO_LINER_SIDE_ONLY")
	def setApplyPressureToLinerSideOnly(self, value: bool):
		return self._setBoolProperty("JP_USE_PRESSURE_TO_LINER_SIDE_ONLY", value)
	def getApplyStageFactors(self) -> bool:
		return self._getBoolProperty("JP_USE_STAGE_JOINT_PROPERTIES")
	def setApplyStageFactors(self, value: bool):
		return self._setBoolProperty("JP_USE_STAGE_JOINT_PROPERTIES", value)
	def setProperties(self, InterfaceCoefficient : float = None, DefineStiffness : DefineStiffness = None, NormalStiffness : float = None, ShearStiffness : float = None, StiffnessCoefficient : float = None, ApplyPorePressure : bool = None, ApplyAdditionalPressureInsideJoint : bool = None, AdditionalPressureType : AdditionalPressureType = None, AdditionalPressureInsideJoint : float = None, PiezoID : int = None, ApplyPressureToLinerSideOnly : bool = None, ApplyStageFactors : bool = None):
		if InterfaceCoefficient is not None:
			self._setDoubleProperty("JP_INTERFACE_COEFFICIENT", InterfaceCoefficient)
		if DefineStiffness is not None:
			self._setEnumEJointStiffnessDefineProperty("JP_DEFINE_STIFFNESS", DefineStiffness)
		if NormalStiffness is not None:
			self._setDoubleProperty("JP_NORMAL_STIFFNESS", NormalStiffness)
		if ShearStiffness is not None:
			self._setDoubleProperty("JP_SHEAR_STIFFNESS", ShearStiffness)
		if StiffnessCoefficient is not None:
			self._setDoubleProperty("JP_STIFFNESS_COEFFICIENT", StiffnessCoefficient)
		if ApplyPorePressure is not None:
			self._setBoolProperty("JP_USE_GROUNDWATER_PORE_PRESSURE", ApplyPorePressure)
		if ApplyAdditionalPressureInsideJoint is not None:
			self._setBoolProperty("JP_USE_ADDITIONAL_PRESSURE", ApplyAdditionalPressureInsideJoint)
		if AdditionalPressureType is not None:
			self._setEnumEJointWaterPressureTypeProperty("JP_ADDITIONAL_TYPE", AdditionalPressureType)
		if AdditionalPressureInsideJoint is not None:
			self._setDoubleProperty("JP_ADDITIONAL_PRESSURE", AdditionalPressureInsideJoint)
		if PiezoID is not None:
			self._setIntProperty("JP_ADDITIONAL_PIEZO_ID", PiezoID)
		if ApplyPressureToLinerSideOnly is not None:
			self._setBoolProperty("JP_USE_PRESSURE_TO_LINER_SIDE_ONLY", ApplyPressureToLinerSideOnly)
		if ApplyStageFactors is not None:
			self._setBoolProperty("JP_USE_STAGE_JOINT_PROPERTIES", ApplyStageFactors)
	def getProperties(self):
		return {
		"InterfaceCoefficient" : self.getInterfaceCoefficient(), 
		"DefineStiffness" : self.getDefineStiffness(), 
		"NormalStiffness" : self.getNormalStiffness(), 
		"ShearStiffness" : self.getShearStiffness(), 
		"StiffnessCoefficient" : self.getStiffnessCoefficient(), 
		"ApplyPorePressure" : self.getApplyPorePressure(), 
		"ApplyAdditionalPressureInsideJoint" : self.getApplyAdditionalPressureInsideJoint(), 
		"AdditionalPressureType" : self.getAdditionalPressureType(), 
		"AdditionalPressureInsideJoint" : self.getAdditionalPressureInsideJoint(), 
		"PiezoID" : self.getPiezoID(), 
		"ApplyPressureToLinerSideOnly" : self.getApplyPressureToLinerSideOnly(), 
		"ApplyStageFactors" : self.getApplyStageFactors(), 
		}