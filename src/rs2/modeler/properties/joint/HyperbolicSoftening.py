from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorInterface import AbsoluteStageFactorInterface
class HyperbolicSofteningStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getNormalStiffnessFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_NORMAL_STIFFNESS", self.propertyID], proxyArgumentIndices=[1])
	def getShearStiffnessFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_SHEAR_STIFFNESS", self.propertyID], proxyArgumentIndices=[1])
	def getPeakCohesionFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_HYPERBOL_COHESION", self.propertyID], proxyArgumentIndices=[1])
	def getPeakFrictionFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_HYPERBOL_FRICTION", self.propertyID], proxyArgumentIndices=[1])
	def getResCohesionFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_HYPERBOL_COHESION_RES", self.propertyID], proxyArgumentIndices=[1])
	def getResFrictionFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_HYPERBOL_FRICTION_RES", self.propertyID], proxyArgumentIndices=[1])
	def getTensileStrengthFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_HYPERBOL_TENSILE_STRENGTH", self.propertyID], proxyArgumentIndices=[1])
	def getResTensileStrengthFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_HYPERBOL_TENSILE_STRENGTH_RES", self.propertyID], proxyArgumentIndices=[1])
	def getDeltaRFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_HYPERBOL_DELTAP_R", self.propertyID], proxyArgumentIndices=[1])
	def getInitialSlopeFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_HYPERBOL_INITIAL_SLOPE", self.propertyID], proxyArgumentIndices=[1])
	def getWorkSofteningFactor(self) -> bool:
		return self._callFunction("getBoolFactor", ["JP_WORK_SOFTENING", self.propertyID], proxyArgumentIndices=[1])
	def getAdditionalPressureInsideJointFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["JP_ADDITIONAL_PRESSURE", self.propertyID], proxyArgumentIndices=[1])
	def getGroundwaterPressureFactor(self) -> float:
		return self._callFunction("__getattribute__", ["m_groundwater_pressure_factor"])
	def getJointPermeableFactor(self) -> bool:
		return self._callFunction("__getattribute__", ["m_joint_permeable_factor"])
class HyperbolicSofteningDefinedStageFactor(HyperbolicSofteningStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setNormalStiffnessFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_NORMAL_STIFFNESS", value, self.propertyID], proxyArgumentIndices=[2])
	def setShearStiffnessFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_SHEAR_STIFFNESS", value, self.propertyID], proxyArgumentIndices=[2])
	def setPeakCohesionFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_HYPERBOL_COHESION", value, self.propertyID], proxyArgumentIndices=[2])
	def setPeakFrictionFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_HYPERBOL_FRICTION", value, self.propertyID], proxyArgumentIndices=[2])
	def setResCohesionFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_HYPERBOL_COHESION_RES", value, self.propertyID], proxyArgumentIndices=[2])
	def setResFrictionFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_HYPERBOL_FRICTION_RES", value, self.propertyID], proxyArgumentIndices=[2])
	def setTensileStrengthFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_HYPERBOL_TENSILE_STRENGTH", value, self.propertyID], proxyArgumentIndices=[2])
	def setResTensileStrengthFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_HYPERBOL_TENSILE_STRENGTH_RES", value, self.propertyID], proxyArgumentIndices=[2])
	def setDeltaRFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_HYPERBOL_DELTAP_R", value, self.propertyID], proxyArgumentIndices=[2])
	def setInitialSlopeFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_HYPERBOL_INITIAL_SLOPE", value, self.propertyID], proxyArgumentIndices=[2])
	def setWorkSofteningFactor(self, value: bool):
		return self._callFunction("setBoolFactor", ["JP_WORK_SOFTENING", value, self.propertyID], proxyArgumentIndices=[2])
	def setAdditionalPressureInsideJointFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["JP_ADDITIONAL_PRESSURE", value, self.propertyID], proxyArgumentIndices=[2])
	def setGroundwaterPressureFactor(self, GroundWaterPressure: float):
		return self._callFunction("setGroundwaterPressureFactor", [GroundWaterPressure])
	def setJointPermeableFactor(self, Permeable: bool):
		return self._callFunction("setJointPermeableFactor", [Permeable])
class HyperbolicSoftening(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorInterface[HyperbolicSofteningDefinedStageFactor, HyperbolicSofteningStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Joint Stage Factor Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		super().__init__(client, ID, documentProxyID)
		stageFactorInterfaceID = self._callFunction("getStageFactorInterface", [], keepReturnValueReference=True)
		self.stageFactorInterface = AbsoluteStageFactorInterface[HyperbolicSofteningDefinedStageFactor, HyperbolicSofteningStageFactor](self._client, stageFactorInterfaceID, ID, HyperbolicSofteningDefinedStageFactor, HyperbolicSofteningStageFactor)
	def getPeakCohesion(self) -> float:
		return self._getDoubleProperty("JP_HYPERBOL_COHESION")
	def setPeakCohesion(self, value: float):
		return self._setDoubleProperty("JP_HYPERBOL_COHESION", value)
	def getPeakFriction(self) -> float:
		return self._getDoubleProperty("JP_HYPERBOL_FRICTION")
	def setPeakFriction(self, value: float):
		return self._setDoubleProperty("JP_HYPERBOL_FRICTION", value)
	def getResCohesion(self) -> float:
		return self._getDoubleProperty("JP_HYPERBOL_COHESION_RES")
	def setResCohesion(self, value: float):
		return self._setDoubleProperty("JP_HYPERBOL_COHESION_RES", value)
	def getResFriction(self) -> float:
		return self._getDoubleProperty("JP_HYPERBOL_FRICTION_RES")
	def setResFriction(self, value: float):
		return self._setDoubleProperty("JP_HYPERBOL_FRICTION_RES", value)
	def getTensileStrength(self) -> float:
		return self._getDoubleProperty("JP_HYPERBOL_TENSILE_STRENGTH")
	def setTensileStrength(self, value: float):
		return self._setDoubleProperty("JP_HYPERBOL_TENSILE_STRENGTH", value)
	def getResTensileStrength(self) -> float:
		return self._getDoubleProperty("JP_HYPERBOL_TENSILE_STRENGTH_RES")
	def setResTensileStrength(self, value: float):
		return self._setDoubleProperty("JP_HYPERBOL_TENSILE_STRENGTH_RES", value)
	def getDeltaR(self) -> float:
		return self._getDoubleProperty("JP_HYPERBOL_DELTAP_R")
	def setDeltaR(self, value: float):
		return self._setDoubleProperty("JP_HYPERBOL_DELTAP_R", value)
	def getInitialSlope(self) -> float:
		return self._getDoubleProperty("JP_HYPERBOL_INITIAL_SLOPE")
	def setInitialSlope(self, value: float):
		return self._setDoubleProperty("JP_HYPERBOL_INITIAL_SLOPE", value)
	def getWorkSoftening(self) -> bool:
		return self._getBoolProperty("JP_WORK_SOFTENING")
	def setWorkSoftening(self, value: bool):
		return self._setBoolProperty("JP_WORK_SOFTENING", value)
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
	def getApplyPressureToLinerSideOnly(self) -> bool:
		return self._getBoolProperty("JP_USE_PRESSURE_TO_LINER_SIDE_ONLY")
	def setApplyPressureToLinerSideOnly(self, value: bool):
		return self._setBoolProperty("JP_USE_PRESSURE_TO_LINER_SIDE_ONLY", value)
	def getApplyStageFactors(self) -> bool:
		return self._getBoolProperty("JP_USE_STAGE_JOINT_PROPERTIES")
	def setApplyStageFactors(self, value: bool):
		return self._setBoolProperty("JP_USE_STAGE_JOINT_PROPERTIES", value)
	def setPiezoID(self, piezoName: str):
		return self._callFunction("python_setPiezoPressureID", [piezoName])
	def getPiezoID(self):
		return self._callFunction("python_getPiezoPressureID", [])
	def setProperties(self, PeakCohesion : float = None, PeakFriction : float = None, ResCohesion : float = None, ResFriction : float = None, TensileStrength : float = None, ResTensileStrength : float = None, DeltaR : float = None, InitialSlope : float = None, WorkSoftening : bool = None, NormalStiffness : float = None, ShearStiffness : float = None, ApplyPorePressure : bool = None, ApplyAdditionalPressureInsideJoint : bool = None, AdditionalPressureType : AdditionalPressureType = None, AdditionalPressureInsideJoint : float = None, ApplyPressureToLinerSideOnly : bool = None, ApplyStageFactors : bool = None):
		if PeakCohesion is not None:
			self._setDoubleProperty("JP_HYPERBOL_COHESION", PeakCohesion)
		if PeakFriction is not None:
			self._setDoubleProperty("JP_HYPERBOL_FRICTION", PeakFriction)
		if ResCohesion is not None:
			self._setDoubleProperty("JP_HYPERBOL_COHESION_RES", ResCohesion)
		if ResFriction is not None:
			self._setDoubleProperty("JP_HYPERBOL_FRICTION_RES", ResFriction)
		if TensileStrength is not None:
			self._setDoubleProperty("JP_HYPERBOL_TENSILE_STRENGTH", TensileStrength)
		if ResTensileStrength is not None:
			self._setDoubleProperty("JP_HYPERBOL_TENSILE_STRENGTH_RES", ResTensileStrength)
		if DeltaR is not None:
			self._setDoubleProperty("JP_HYPERBOL_DELTAP_R", DeltaR)
		if InitialSlope is not None:
			self._setDoubleProperty("JP_HYPERBOL_INITIAL_SLOPE", InitialSlope)
		if WorkSoftening is not None:
			self._setBoolProperty("JP_WORK_SOFTENING", WorkSoftening)
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
		if ApplyPressureToLinerSideOnly is not None:
			self._setBoolProperty("JP_USE_PRESSURE_TO_LINER_SIDE_ONLY", ApplyPressureToLinerSideOnly)
		if ApplyStageFactors is not None:
			self._setBoolProperty("JP_USE_STAGE_JOINT_PROPERTIES", ApplyStageFactors)
	def getProperties(self):
		return {
		"PeakCohesion" : self.getPeakCohesion(), 
		"PeakFriction" : self.getPeakFriction(), 
		"ResCohesion" : self.getResCohesion(), 
		"ResFriction" : self.getResFriction(), 
		"TensileStrength" : self.getTensileStrength(), 
		"ResTensileStrength" : self.getResTensileStrength(), 
		"DeltaR" : self.getDeltaR(), 
		"InitialSlope" : self.getInitialSlope(), 
		"WorkSoftening" : self.getWorkSoftening(), 
		"NormalStiffness" : self.getNormalStiffness(), 
		"ShearStiffness" : self.getShearStiffness(), 
		"ApplyPorePressure" : self.getApplyPorePressure(), 
		"ApplyAdditionalPressureInsideJoint" : self.getApplyAdditionalPressureInsideJoint(), 
		"AdditionalPressureType" : self.getAdditionalPressureType(), 
		"AdditionalPressureInsideJoint" : self.getAdditionalPressureInsideJoint(), 
		"ApplyPressureToLinerSideOnly" : self.getApplyPressureToLinerSideOnly(), 
		"ApplyStageFactors" : self.getApplyStageFactors(), 
		}
