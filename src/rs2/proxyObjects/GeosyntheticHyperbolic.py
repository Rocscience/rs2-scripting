from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class GeosyntheticHyperbolic(PropertyProxy):
	def getApplyAdditionalPressureInsideJoint(self) -> bool:
		return self._getBoolProperty("JP_USE_ADDITIONAL_PRESSURE")
	def setApplyAdditionalPressureInsideJoint(self, value: bool):
		return self._setBoolProperty("JP_USE_ADDITIONAL_PRESSURE", value)
	def getPeakAdhesionAtSigninf(self) -> float:
		return self._getDoubleProperty("JP_PEAK_ADHESION")
	def setPeakAdhesionAtSigninf(self, value: float):
		return self._setDoubleProperty("JP_PEAK_ADHESION", value)
	def getPeakFrictionAngleAtSign0(self) -> float:
		return self._getDoubleProperty("JP_PEAK_FRICTION_ANGLE_GEOSYN")
	def setPeakFrictionAngleAtSign0(self, value: float):
		return self._setDoubleProperty("JP_PEAK_FRICTION_ANGLE_GEOSYN", value)
	def getResAdhesionAtSigninf(self) -> float:
		return self._getDoubleProperty("JP_ADHESION_RES")
	def setResAdhesionAtSigninf(self, value: float):
		return self._setDoubleProperty("JP_ADHESION_RES", value)
	def getResFrictionAngleAtSign0(self) -> float:
		return self._getDoubleProperty("JP_FRICTION_ANGLE_RES_GEOSYN")
	def setResFrictionAngleAtSign0(self, value: float):
		return self._setDoubleProperty("JP_FRICTION_ANGLE_RES_GEOSYN", value)
	def getNormalStiffness(self) -> float:
		return self._getDoubleProperty("JP_NORMAL_STIFFNESS")
	def setNormalStiffness(self, value: float):
		return self._setDoubleProperty("JP_NORMAL_STIFFNESS", value)
	def getShearStiffness(self) -> float:
		return self._getDoubleProperty("JP_SHEAR_STIFFNESS")
	def setShearStiffness(self, value: float):
		return self._setDoubleProperty("JP_SHEAR_STIFFNESS", value)
	def getApplyPorePressure(self) -> bool:
		return self._getBoolProperty("JP_USE_GROUNDWATER_PORE_PRESSURE")
	def setApplyPorePressure(self, value: bool):
		return self._setBoolProperty("JP_USE_GROUNDWATER_PORE_PRESSURE", value)
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
	def setGeosyntheticHyperbolicProperties(self, ApplyAdditionalPressureInsideJoint : bool = None, PeakAdhesionAtSigninf : float = None, PeakFrictionAngleAtSign0 : float = None, ResAdhesionAtSigninf : float = None, ResFrictionAngleAtSign0 : float = None, NormalStiffness : float = None, ShearStiffness : float = None, ApplyPorePressure : bool = None, AdditionalPressureType : AdditionalPressureType = None, AdditionalPressureInsideJoint : float = None, PiezoID : int = None, ApplyPressureToLinerSideOnly : bool = None):
		if(ApplyAdditionalPressureInsideJoint):
			self._setBoolProperty("JP_USE_ADDITIONAL_PRESSURE", ApplyAdditionalPressureInsideJoint)
		if(PeakAdhesionAtSigninf):
			self._setDoubleProperty("JP_PEAK_ADHESION", PeakAdhesionAtSigninf)
		if(PeakFrictionAngleAtSign0):
			self._setDoubleProperty("JP_PEAK_FRICTION_ANGLE_GEOSYN", PeakFrictionAngleAtSign0)
		if(ResAdhesionAtSigninf):
			self._setDoubleProperty("JP_ADHESION_RES", ResAdhesionAtSigninf)
		if(ResFrictionAngleAtSign0):
			self._setDoubleProperty("JP_FRICTION_ANGLE_RES_GEOSYN", ResFrictionAngleAtSign0)
		if(NormalStiffness):
			self._setDoubleProperty("JP_NORMAL_STIFFNESS", NormalStiffness)
		if(ShearStiffness):
			self._setDoubleProperty("JP_SHEAR_STIFFNESS", ShearStiffness)
		if(ApplyPorePressure):
			self._setBoolProperty("JP_USE_GROUNDWATER_PORE_PRESSURE", ApplyPorePressure)
		if(AdditionalPressureType):
			self._setEnumEJointWaterPressureTypeProperty("JP_ADDITIONAL_TYPE", AdditionalPressureType)
		if(AdditionalPressureInsideJoint):
			self._setDoubleProperty("JP_ADDITIONAL_PRESSURE", AdditionalPressureInsideJoint)
		if(PiezoID):
			self._setIntProperty("JP_ADDITIONAL_PIEZO_ID", PiezoID)
		if(ApplyPressureToLinerSideOnly):
			self._setBoolProperty("JP_USE_PRESSURE_TO_LINER_SIDE_ONLY", ApplyPressureToLinerSideOnly)