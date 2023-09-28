from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.ProxyObject import ProxyObject
class GeosyntheticHyperbolicStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, property : PropertyProxy):
		super().__init__(client, ID)
		self.property = property
	def getNormalStiffnessFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_NORMAL_STIFFNESS", self.property._ID], proxyArgumentIndices=[1])
	def setNormalStiffnessFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_NORMAL_STIFFNESS", value, self.property._ID], proxyArgumentIndices=[2])
	def getShearStiffnessFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_SHEAR_STIFFNESS", self.property._ID], proxyArgumentIndices=[1])
	def setShearStiffnessFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_SHEAR_STIFFNESS", value, self.property._ID], proxyArgumentIndices=[2])
	def getPeakAdhesionAtSigninfFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_PEAK_ADHESION", self.property._ID], proxyArgumentIndices=[1])
	def setPeakAdhesionAtSigninfFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_PEAK_ADHESION", value, self.property._ID], proxyArgumentIndices=[2])
	def getPeakFrictionAngleAtSign0Factor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_PEAK_FRICTION_ANGLE_GEOSYN", self.property._ID], proxyArgumentIndices=[1])
	def setPeakFrictionAngleAtSign0Factor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_PEAK_FRICTION_ANGLE_GEOSYN", value, self.property._ID], proxyArgumentIndices=[2])
	def getResAdhesionAtSigninfFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_ADHESION_RES", self.property._ID], proxyArgumentIndices=[1])
	def setResAdhesionAtSigninfFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_ADHESION_RES", value, self.property._ID], proxyArgumentIndices=[2])
	def getResFrictionAngleAtSign0Factor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_FRICTION_ANGLE_RES_GEOSYN", self.property._ID], proxyArgumentIndices=[1])
	def setResFrictionAngleAtSign0Factor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_FRICTION_ANGLE_RES_GEOSYN", value, self.property._ID], proxyArgumentIndices=[2])
	def getAdditionalPressureInsideJointFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_ADDITIONAL_PRESSURE", self.property._ID], proxyArgumentIndices=[1])
	def setAdditionalPressureInsideJointFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_ADDITIONAL_PRESSURE", value, self.property._ID], proxyArgumentIndices=[2])
	def getGroundwaterPressureFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_GROUNDWATER_PRESSURE", self.property._ID], proxyArgumentIndices=[1])
	def setGroundwaterPressureFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_GROUNDWATER_PRESSURE", value, self.property._ID], proxyArgumentIndices=[2])
class GeosyntheticHyperbolic(PropertyProxy):
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
	def getStageFactors(self) -> List[GeosyntheticHyperbolicStageFactor]:
		"""
		Returns the defined stage factors in a list, in order from stage 1 to n.
		"""
		stageFactorReferenceIds = self._callFunction('getStageFactors', [], keepReturnValueReference=True)
		stageFactors = []
		for stageFactorID in stageFactorReferenceIds :
			stageFactors.append(GeosyntheticHyperbolicStageFactor(self._client, stageFactorID, self))
		return stageFactors
	def setProperties(self, PeakAdhesionAtSigninf : float = None, PeakFrictionAngleAtSign0 : float = None, ResAdhesionAtSigninf : float = None, ResFrictionAngleAtSign0 : float = None, NormalStiffness : float = None, ShearStiffness : float = None, ApplyPorePressure : bool = None, ApplyAdditionalPressureInsideJoint : bool = None, AdditionalPressureType : AdditionalPressureType = None, AdditionalPressureInsideJoint : float = None, PiezoID : int = None, ApplyPressureToLinerSideOnly : bool = None, ApplyStageFactors : bool = None):
		if PeakAdhesionAtSigninf is not None:
			self._setDoubleProperty("JP_PEAK_ADHESION", PeakAdhesionAtSigninf)
		if PeakFrictionAngleAtSign0 is not None:
			self._setDoubleProperty("JP_PEAK_FRICTION_ANGLE_GEOSYN", PeakFrictionAngleAtSign0)
		if ResAdhesionAtSigninf is not None:
			self._setDoubleProperty("JP_ADHESION_RES", ResAdhesionAtSigninf)
		if ResFrictionAngleAtSign0 is not None:
			self._setDoubleProperty("JP_FRICTION_ANGLE_RES_GEOSYN", ResFrictionAngleAtSign0)
		if NormalStiffness is not None:
			self._setDoubleProperty("JP_NORMAL_STIFFNESS", NormalStiffness)
		if ShearStiffness is not None:
			self._setDoubleProperty("JP_SHEAR_STIFFNESS", ShearStiffness)
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
		"PeakAdhesionAtSigninf" : self.getPeakAdhesionAtSigninf(), 
		"PeakFrictionAngleAtSign0" : self.getPeakFrictionAngleAtSign0(), 
		"ResAdhesionAtSigninf" : self.getResAdhesionAtSigninf(), 
		"ResFrictionAngleAtSign0" : self.getResFrictionAngleAtSign0(), 
		"NormalStiffness" : self.getNormalStiffness(), 
		"ShearStiffness" : self.getShearStiffness(), 
		"ApplyPorePressure" : self.getApplyPorePressure(), 
		"ApplyAdditionalPressureInsideJoint" : self.getApplyAdditionalPressureInsideJoint(), 
		"AdditionalPressureType" : self.getAdditionalPressureType(), 
		"AdditionalPressureInsideJoint" : self.getAdditionalPressureInsideJoint(), 
		"PiezoID" : self.getPiezoID(), 
		"ApplyPressureToLinerSideOnly" : self.getApplyPressureToLinerSideOnly(), 
		"ApplyStageFactors" : self.getApplyStageFactors(), 
		}
