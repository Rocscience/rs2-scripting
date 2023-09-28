from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
from rs2.ProxyObject import ProxyObject
class MohrCoulombStageFactor(ProxyObject):
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
	def getTensileStrengthFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_TENSILE_STRENGTH", self.property._ID], proxyArgumentIndices=[1])
	def setTensileStrengthFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_TENSILE_STRENGTH", value, self.property._ID], proxyArgumentIndices=[2])
	def getPeakCohesionFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_PEAK_COHESION", self.property._ID], proxyArgumentIndices=[1])
	def setPeakCohesionFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_PEAK_COHESION", value, self.property._ID], proxyArgumentIndices=[2])
	def getPeakFrictionAngleFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_PEAK_FRICTION_ANGLE", self.property._ID], proxyArgumentIndices=[1])
	def setPeakFrictionAngleFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_PEAK_FRICTION_ANGLE", value, self.property._ID], proxyArgumentIndices=[2])
	def getResCohesionFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_COHESION_RES", self.property._ID], proxyArgumentIndices=[1])
	def setResCohesionFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_COHESION_RES", value, self.property._ID], proxyArgumentIndices=[2])
	def getResFrictionAngleFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_FRICTION_ANGLE_RES", self.property._ID], proxyArgumentIndices=[1])
	def setResFrictionAngleFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_FRICTION_ANGLE_RES", value, self.property._ID], proxyArgumentIndices=[2])
	def getResTensileStrengthFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_TENSILE_STRENGTH_RES", self.property._ID], proxyArgumentIndices=[1])
	def setResTensileStrengthFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_TENSILE_STRENGTH_RES", value, self.property._ID], proxyArgumentIndices=[2])
	def getAdditionalPressureInsideJointFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_ADDITIONAL_PRESSURE", self.property._ID], proxyArgumentIndices=[1])
	def setAdditionalPressureInsideJointFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_ADDITIONAL_PRESSURE", value, self.property._ID], proxyArgumentIndices=[2])
	def getGroundwaterPressureFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_GROUNDWATER_PRESSURE", self.property._ID], proxyArgumentIndices=[1])
	def setGroundwaterPressureFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_GROUNDWATER_PRESSURE", value, self.property._ID], proxyArgumentIndices=[2])
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
	def SetApplySSR(self, applySSR: bool):
		return self._callFunction("SetApplySSR", [applySSR])
	def GetApplySSR(self) -> bool:
		return self._callFunction("GetApplySSR", [])
	def SetPermeable(self, permeable: bool):
		return self._callFunction("SetPermeable", [permeable])
	def GetPermeable(self) -> bool:
		return self._callFunction("GetPermeable", [])
	def SetMeshConforming(self, meshConforming: bool):
		return self._callFunction("SetApplySSR", [meshConforming])
	def GetMeshConforming(self) -> bool:
		return self._callFunction("GetApplySSR", [])
	def getStageFactors(self) -> List[MohrCoulombStageFactor]:
		"""
		Returns the defined stage factors in a list, in order from stage 1 to n.
		"""
		stageFactorReferenceIds = self._callFunction('getStageFactors', [], keepReturnValueReference=True)
		stageFactors = []
		for stageFactorID in stageFactorReferenceIds :
			stageFactors.append(MohrCoulombStageFactor(self._client, stageFactorID, self))
		return stageFactors
	def setProperties(self, TensileStrength : float = None, PeakCohesion : float = None, PeakFrictionAngle : float = None, DilationAngle : float = None, DMin : float = None, DMax : float = None, Directional : bool = None, ResidualStrength : bool = None, ResTensileStrength : float = None, ResCohesion : float = None, ResFrictionAngle : float = None, NormalStiffness : float = None, ShearStiffness : float = None, ApplyPorePressure : bool = None, ApplyAdditionalPressureInsideJoint : bool = None, AdditionalPressureType : AdditionalPressureType = None, AdditionalPressureInsideJoint : float = None, PiezoID : int = None, ApplyPressureToLinerSideOnly : bool = None, ApplyStageFactors : bool = None):
		if TensileStrength is not None:
			self._setDoubleProperty("JP_TENSILE_STRENGTH", TensileStrength)
		if PeakCohesion is not None:
			self._setDoubleProperty("JP_PEAK_COHESION", PeakCohesion)
		if PeakFrictionAngle is not None:
			self._setDoubleProperty("JP_PEAK_FRICTION_ANGLE", PeakFrictionAngle)
		if DilationAngle is not None:
			self._setDoubleProperty("JP_DILATION_ANGLE", DilationAngle)
		if DMin is not None:
			self._setDoubleProperty("JP_DMIN", DMin)
		if DMax is not None:
			self._setDoubleProperty("JP_DMAX", DMax)
		if Directional is not None:
			self._setBoolProperty("JP_DIRECTIONAL", Directional)
		if ResidualStrength is not None:
			self._setBoolProperty("JP_USE_RES_STRENGTH", ResidualStrength)
		if ResTensileStrength is not None:
			self._setDoubleProperty("JP_TENSILE_STRENGTH_RES", ResTensileStrength)
		if ResCohesion is not None:
			self._setDoubleProperty("JP_COHESION_RES", ResCohesion)
		if ResFrictionAngle is not None:
			self._setDoubleProperty("JP_FRICTION_ANGLE_RES", ResFrictionAngle)
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
		"TensileStrength" : self.getTensileStrength(), 
		"PeakCohesion" : self.getPeakCohesion(), 
		"PeakFrictionAngle" : self.getPeakFrictionAngle(), 
		"DilationAngle" : self.getDilationAngle(), 
		"DMin" : self.getDMin(), 
		"DMax" : self.getDMax(), 
		"Directional" : self.getDirectional(), 
		"ResidualStrength" : self.getResidualStrength(), 
		"ResTensileStrength" : self.getResTensileStrength(), 
		"ResCohesion" : self.getResCohesion(), 
		"ResFrictionAngle" : self.getResFrictionAngle(), 
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
