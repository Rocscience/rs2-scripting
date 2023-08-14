from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class MohrCoulomb(PropertyProxy):
	def getTensileStrength(self) -> float:
		return self._getDoubleProperty("JP_TENSILE_STRENGTH")
	def setTensileStrength(self, value: float):
		return self._setDoubleProperty("JP_TENSILE_STRENGTH", value)
	def getPeakCohesion(self) -> float:
		return self._getDoubleProperty("JP_PEAK_COHESION")
	def setPeakCohesion(self, value: float):
		return self._setDoubleProperty("JP_PEAK_COHESION", value)
	def getPeakFrictionAngle(self) -> float:
		return self._getDoubleProperty("JP_PEAK_FRICTION_ANGLE")
	def setPeakFrictionAngle(self, value: float):
		return self._setDoubleProperty("JP_PEAK_FRICTION_ANGLE", value)
	def getDilationAngle(self) -> float:
		return self._getDoubleProperty("JP_DILATION_ANGLE")
	def setDilationAngle(self, value: float):
		return self._setDoubleProperty("JP_DILATION_ANGLE", value)
	def getDMin(self) -> float:
		return self._getDoubleProperty("JP_DMIN")
	def setDMin(self, value: float):
		return self._setDoubleProperty("JP_DMIN", value)
	def getDMax(self) -> float:
		return self._getDoubleProperty("JP_DMAX")
	def setDMax(self, value: float):
		return self._setDoubleProperty("JP_DMAX", value)
	def getDirectional(self) -> bool:
		return self._getBoolProperty("JP_DIRECTIONAL")
	def setDirectional(self, value: bool):
		return self._setBoolProperty("JP_DIRECTIONAL", value)
	def getResidualStrength(self) -> bool:
		return self._getBoolProperty("JP_USE_RES_STRENGTH")
	def setResidualStrength(self, value: bool):
		return self._setBoolProperty("JP_USE_RES_STRENGTH", value)
	def getResTensileStrength(self) -> float:
		return self._getDoubleProperty("JP_TENSILE_STRENGTH_RES")
	def setResTensileStrength(self, value: float):
		return self._setDoubleProperty("JP_TENSILE_STRENGTH_RES", value)
	def getResCohesion(self) -> float:
		return self._getDoubleProperty("JP_COHESION_RES")
	def setResCohesion(self, value: float):
		return self._setDoubleProperty("JP_COHESION_RES", value)
	def getResFrictionAngle(self) -> float:
		return self._getDoubleProperty("JP_FRICTION_ANGLE_RES")
	def setResFrictionAngle(self, value: float):
		return self._setDoubleProperty("JP_FRICTION_ANGLE_RES", value)
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
	def setMohrCoulombProperties(self, TensileStrength : float = None, PeakCohesion : float = None, PeakFrictionAngle : float = None, DilationAngle : float = None, DMin : float = None, DMax : float = None, Directional : bool = None, ResidualStrength : bool = None, ResTensileStrength : float = None, ResCohesion : float = None, ResFrictionAngle : float = None, NormalStiffness : float = None, ShearStiffness : float = None, ApplyPorePressure : bool = None, ApplyAdditionalPressureInsideJoint : bool = None, AdditionalPressureType : AdditionalPressureType = None, AdditionalPressureInsideJoint : float = None, PiezoID : int = None, ApplyPressureToLinerSideOnly : bool = None):
		if(TensileStrength):
			self._setDoubleProperty("JP_TENSILE_STRENGTH", TensileStrength)
		if(PeakCohesion):
			self._setDoubleProperty("JP_PEAK_COHESION", PeakCohesion)
		if(PeakFrictionAngle):
			self._setDoubleProperty("JP_PEAK_FRICTION_ANGLE", PeakFrictionAngle)
		if(DilationAngle):
			self._setDoubleProperty("JP_DILATION_ANGLE", DilationAngle)
		if(DMin):
			self._setDoubleProperty("JP_DMIN", DMin)
		if(DMax):
			self._setDoubleProperty("JP_DMAX", DMax)
		if(Directional):
			self._setBoolProperty("JP_DIRECTIONAL", Directional)
		if(ResidualStrength):
			self._setBoolProperty("JP_USE_RES_STRENGTH", ResidualStrength)
		if(ResTensileStrength):
			self._setDoubleProperty("JP_TENSILE_STRENGTH_RES", ResTensileStrength)
		if(ResCohesion):
			self._setDoubleProperty("JP_COHESION_RES", ResCohesion)
		if(ResFrictionAngle):
			self._setDoubleProperty("JP_FRICTION_ANGLE_RES", ResFrictionAngle)
		if(NormalStiffness):
			self._setDoubleProperty("JP_NORMAL_STIFFNESS", NormalStiffness)
		if(ShearStiffness):
			self._setDoubleProperty("JP_SHEAR_STIFFNESS", ShearStiffness)
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