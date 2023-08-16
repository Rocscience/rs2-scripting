from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.Client import Client
from enum import Enum, auto
from typing import List
from rs2.PropertyEnums import *
class PlainStrandCable(PropertyProxy):
	def getOutofPlaneSpacing(self) -> float:
		return self._getDoubleProperty("BP_OUT_OF_PLANE_SPACING_BOLT")
	def setOutofPlaneSpacing(self, value: float):
		return self._validateAndSetDoubleProperty("BP_OUT_OF_PLANE_SPACING_BOLT", value)
	def getFacePlates(self) -> bool:
		return self._getBoolProperty("BP_FACE_PLATES")
	def setFacePlates(self, value: bool):
		return self._validateAndSetBoolProperty("BP_FACE_PLATES", value)
	def getJointShear(self) -> bool:
		return self._getBoolProperty("BP_USE_JOINT_SHEAR")
	def setJointShear(self, value: bool):
		return self._validateAndSetBoolProperty("BP_USE_JOINT_SHEAR", value)
	def getBoreholeDiameter(self) -> float:
		return self._getDoubleProperty("BP_BOREHOLE_DIAMETER_CABLE")
	def setBoreholeDiameter(self, value: float):
		return self._validateAndSetDoubleProperty("BP_BOREHOLE_DIAMETER_CABLE", value)
	def getCableDiameter(self) -> float:
		return self._getDoubleProperty("BP_CABLE_DIAMETER")
	def setCableDiameter(self, value: float):
		return self._validateAndSetDoubleProperty("BP_CABLE_DIAMETER", value)
	def getCableModulusE(self) -> float:
		return self._getDoubleProperty("BP_CABLE_MODULUS")
	def setCableModulusE(self, value: float):
		return self._validateAndSetDoubleProperty("BP_CABLE_MODULUS", value)
	def getCablePeak(self) -> float:
		return self._getDoubleProperty("BP_CABLE_PEAK")
	def setCablePeak(self, value: float):
		return self._validateAndSetDoubleProperty("BP_CABLE_PEAK", value)
	def getWaterCementRatio(self) -> float:
		return self._getDoubleProperty("BP_WATER_CEMENT_RATIO")
	def setWaterCementRatio(self, value: float):
		return self._validateAndSetDoubleProperty("BP_WATER_CEMENT_RATIO", value)
	def getAddPullOutForce(self) -> bool:
		return self._getBoolProperty("BP_ADD_PULL_OUT_FORCE")
	def setAddPullOutForce(self, value: bool):
		return self._validateAndSetBoolProperty("BP_ADD_PULL_OUT_FORCE", value)
	def getPullOutForce(self) -> float:
		return self._getDoubleProperty("BP_PULL_OUT_FORCE")
	def setPullOutForce(self, value: float):
		return self._validateAndSetDoubleProperty("BP_PULL_OUT_FORCE", value)
	def getConstantShearStiffness(self) -> bool:
		return self._getBoolProperty("BP_ADD_CONSTANT_SHEAR_STIFFNESS")
	def setConstantShearStiffness(self, value: bool):
		return self._validateAndSetBoolProperty("BP_ADD_CONSTANT_SHEAR_STIFFNESS", value)
	def getStiffness(self) -> float:
		return self._getDoubleProperty("BP_CONSTANT_SHEAR_STIFFNESS")
	def setStiffness(self, value: float):
		return self._validateAndSetDoubleProperty("BP_CONSTANT_SHEAR_STIFFNESS", value)
	def getAddBulges(self) -> bool:
		return self._getBoolProperty("BP_ADD_BULGES")
	def setAddBulges(self, value: bool):
		return self._validateAndSetBoolProperty("BP_ADD_BULGES", value)
	def getBulgeType(self) -> BulgeTypes:
		return BulgeTypes(self._getEnumEBulgeTypesProperty("BP_BULGE_TYPE"))
	def setBulgeType(self, value: BulgeTypes):
		return self._validateAndSetEnumEBulgeTypesProperty("BP_BULGE_TYPE", value)
	def getBulgeLocations(self) -> List[float]:
		return self._callFunction("get_bulge_locations_ref", [])
	def setBulgeLocations(self, locations: List[float]):
		return self._callFunction("set_bulge_locations", [locations ])
	def setProperties(self, OutofPlaneSpacing : float = None, FacePlates : bool = None, JointShear : bool = None, BoreholeDiameter : float = None, CableDiameter : float = None, CableModulusE : float = None, CablePeak : float = None, WaterCementRatio : float = None, AddPullOutForce : bool = None, PullOutForce : float = None, ConstantShearStiffness : bool = None, Stiffness : float = None, AddBulges : bool = None, BulgeType : BulgeTypes = None):
		if OutofPlaneSpacing is not None:
			self._validateAndSetDoubleProperty("BP_OUT_OF_PLANE_SPACING_BOLT", OutofPlaneSpacing)
		if FacePlates is not None:
			self._validateAndSetBoolProperty("BP_FACE_PLATES", FacePlates)
		if JointShear is not None:
			self._validateAndSetBoolProperty("BP_USE_JOINT_SHEAR", JointShear)
		if BoreholeDiameter is not None:
			self._validateAndSetDoubleProperty("BP_BOREHOLE_DIAMETER_CABLE", BoreholeDiameter)
		if CableDiameter is not None:
			self._validateAndSetDoubleProperty("BP_CABLE_DIAMETER", CableDiameter)
		if CableModulusE is not None:
			self._validateAndSetDoubleProperty("BP_CABLE_MODULUS", CableModulusE)
		if CablePeak is not None:
			self._validateAndSetDoubleProperty("BP_CABLE_PEAK", CablePeak)
		if WaterCementRatio is not None:
			self._validateAndSetDoubleProperty("BP_WATER_CEMENT_RATIO", WaterCementRatio)
		if AddPullOutForce is not None:
			self._validateAndSetBoolProperty("BP_ADD_PULL_OUT_FORCE", AddPullOutForce)
		if PullOutForce is not None:
			self._validateAndSetDoubleProperty("BP_PULL_OUT_FORCE", PullOutForce)
		if ConstantShearStiffness is not None:
			self._validateAndSetBoolProperty("BP_ADD_CONSTANT_SHEAR_STIFFNESS", ConstantShearStiffness)
		if Stiffness is not None:
			self._validateAndSetDoubleProperty("BP_CONSTANT_SHEAR_STIFFNESS", Stiffness)
		if AddBulges is not None:
			self._validateAndSetBoolProperty("BP_ADD_BULGES", AddBulges)
		if BulgeType is not None:
			self._validateAndSetEnumEBulgeTypesProperty("BP_BULGE_TYPE", BulgeType)
	def getProperties(self):
		return {
		"OutofPlaneSpacing" : self.getOutofPlaneSpacing(), 
		"FacePlates" : self.getFacePlates(), 
		"JointShear" : self.getJointShear(), 
		"BoreholeDiameter" : self.getBoreholeDiameter(), 
		"CableDiameter" : self.getCableDiameter(), 
		"CableModulusE" : self.getCableModulusE(), 
		"CablePeak" : self.getCablePeak(), 
		"WaterCementRatio" : self.getWaterCementRatio(), 
		"AddPullOutForce" : self.getAddPullOutForce(), 
		"PullOutForce" : self.getPullOutForce(), 
		"ConstantShearStiffness" : self.getConstantShearStiffness(), 
		"Stiffness" : self.getStiffness(), 
		"AddBulges" : self.getAddBulges(), 
		"BulgeType" : self.getBulgeType(), 
		}
