from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class BartonBandis(PropertyProxy):
	def getJCS(self) -> float:
		return self._getDoubleProperty("JP_JCS")
	def setJCS(self, value: float):
		return self._setDoubleProperty("JP_JCS", value)
	def getNormalStiffness(self) -> float:
		return self._getDoubleProperty("JP_NORMAL_STIFFNESS")
	def setNormalStiffness(self, value: float):
		return self._setDoubleProperty("JP_NORMAL_STIFFNESS", value)
	def getJRC(self) -> float:
		return self._getDoubleProperty("JP_JRC")
	def setJRC(self, value: float):
		return self._setDoubleProperty("JP_JRC", value)
	def getShearStiffness(self) -> float:
		return self._getDoubleProperty("JP_SHEAR_STIFFNESS")
	def setShearStiffness(self, value: float):
		return self._setDoubleProperty("JP_SHEAR_STIFFNESS", value)
	def getResidualFrictionAngle(self) -> float:
		return self._getDoubleProperty("JP_FRICTION_ANGLE_RES_BARTON")
	def setResidualFrictionAngle(self, value: float):
		return self._setDoubleProperty("JP_FRICTION_ANGLE_RES_BARTON", value)
	def getResidualStrength(self) -> bool:
		return self._getBoolProperty("JP_USE_RES_STRENGTH_BARTON")
	def setResidualStrength(self, value: bool):
		return self._setBoolProperty("JP_USE_RES_STRENGTH_BARTON", value)
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
	def setBartonBandisProperties(self, JCS : float = None, NormalStiffness : float = None, JRC : float = None, ShearStiffness : float = None, ResidualFrictionAngle : float = None, ResidualStrength : bool = None, ApplyPorePressure : bool = None, ApplyAdditionalPressureInsideJoint : bool = None, AdditionalPressureType : AdditionalPressureType = None, AdditionalPressureInsideJoint : float = None, PiezoID : int = None, ApplyPressureToLinerSideOnly : bool = None):
		if(JCS):
			self._setDoubleProperty("JP_JCS", JCS)
		if(NormalStiffness):
			self._setDoubleProperty("JP_NORMAL_STIFFNESS", NormalStiffness)
		if(JRC):
			self._setDoubleProperty("JP_JRC", JRC)
		if(ShearStiffness):
			self._setDoubleProperty("JP_SHEAR_STIFFNESS", ShearStiffness)
		if(ResidualFrictionAngle):
			self._setDoubleProperty("JP_FRICTION_ANGLE_RES_BARTON", ResidualFrictionAngle)
		if(ResidualStrength):
			self._setBoolProperty("JP_USE_RES_STRENGTH_BARTON", ResidualStrength)
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