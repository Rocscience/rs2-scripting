from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class MohrCoulombPile(PropertyProxy):
	def getShearStiffness(self) -> float:
		return self._getDoubleProperty("PFP_SHEAR_STIFFNESS")
	def setShearStiffness(self, value: float):
		return self._setDoubleProperty("PFP_SHEAR_STIFFNESS", value)
	def getNormalStiffness(self) -> float:
		return self._getDoubleProperty("PFP_NORMAL_STIFFNESS")
	def setNormalStiffness(self, value: float):
		return self._setDoubleProperty("PFP_NORMAL_STIFFNESS", value)
	def getFrictionAngle(self) -> float:
		return self._getDoubleProperty("PFP_FRICTION_ANGLE")
	def setFrictionAngle(self, value: float):
		return self._setDoubleProperty("PFP_FRICTION_ANGLE", value)
	def getResidualFrictionAngle(self) -> float:
		return self._getDoubleProperty("PFP_FRICTION_ANGLE_RES")
	def setResidualFrictionAngle(self, value: float):
		return self._setDoubleProperty("PFP_FRICTION_ANGLE_RES", value)
	def getCohesion(self) -> float:
		return self._getDoubleProperty("PFP_COHESION")
	def setCohesion(self, value: float):
		return self._setDoubleProperty("PFP_COHESION", value)
	def getResidualCohesion(self) -> float:
		return self._getDoubleProperty("PFP_RESIDUAL_COHESION")
	def setResidualCohesion(self, value: float):
		return self._setDoubleProperty("PFP_RESIDUAL_COHESION", value)
	def getUseShearResistanceCutoff(self) -> bool:
		return self._getBoolProperty("PFP_USE_SHEAR_RESISTANCE_CUTOFF")
	def setUseShearResistanceCutoff(self, value: bool):
		return self._setBoolProperty("PFP_USE_SHEAR_RESISTANCE_CUTOFF", value)
	def getShearResistanceCutoff(self) -> float:
		return self._getDoubleProperty("PFP_SHEAR_RESISTANCE_CUTOFF")
	def setShearResistanceCutoff(self, value: float):
		return self._setDoubleProperty("PFP_SHEAR_RESISTANCE_CUTOFF", value)
	def getPerimeter(self) -> float:
		return self._getDoubleProperty("PFP_PERIMETER")
	def setPerimeter(self, value: float):
		return self._setDoubleProperty("PFP_PERIMETER", value)
	def getUseBaseResistance(self) -> bool:
		return self._getBoolProperty("PFP_USE_BASE_RESISTANCE")
	def setUseBaseResistance(self, value: bool):
		return self._setBoolProperty("PFP_USE_BASE_RESISTANCE", value)
	def getBaseNormalStiffness(self) -> float:
		return self._getDoubleProperty("PFP_BASE_NORMAL_STIFFNESS")
	def setBaseNormalStiffness(self, value: float):
		return self._setDoubleProperty("PFP_BASE_NORMAL_STIFFNESS", value)
	def getBaseForceResistance(self) -> float:
		return self._getDoubleProperty("PFP_BASE_FORCE_RESISTANCE")
	def setBaseForceResistance(self, value: float):
		return self._setDoubleProperty("PFP_BASE_FORCE_RESISTANCE", value)
	def setProperties(self, ShearStiffness : float = None, NormalStiffness : float = None, FrictionAngle : float = None, ResidualFrictionAngle : float = None, Cohesion : float = None, ResidualCohesion : float = None, UseShearResistanceCutoff : bool = None, ShearResistanceCutoff : float = None, Perimeter : float = None, UseBaseResistance : bool = None, BaseNormalStiffness : float = None, BaseForceResistance : float = None):
		if ShearStiffness is not None:
			self._setDoubleProperty("PFP_SHEAR_STIFFNESS", ShearStiffness)
		if NormalStiffness is not None:
			self._setDoubleProperty("PFP_NORMAL_STIFFNESS", NormalStiffness)
		if FrictionAngle is not None:
			self._setDoubleProperty("PFP_FRICTION_ANGLE", FrictionAngle)
		if ResidualFrictionAngle is not None:
			self._setDoubleProperty("PFP_FRICTION_ANGLE_RES", ResidualFrictionAngle)
		if Cohesion is not None:
			self._setDoubleProperty("PFP_COHESION", Cohesion)
		if ResidualCohesion is not None:
			self._setDoubleProperty("PFP_RESIDUAL_COHESION", ResidualCohesion)
		if UseShearResistanceCutoff is not None:
			self._setBoolProperty("PFP_USE_SHEAR_RESISTANCE_CUTOFF", UseShearResistanceCutoff)
		if ShearResistanceCutoff is not None:
			self._setDoubleProperty("PFP_SHEAR_RESISTANCE_CUTOFF", ShearResistanceCutoff)
		if Perimeter is not None:
			self._setDoubleProperty("PFP_PERIMETER", Perimeter)
		if UseBaseResistance is not None:
			self._setBoolProperty("PFP_USE_BASE_RESISTANCE", UseBaseResistance)
		if BaseNormalStiffness is not None:
			self._setDoubleProperty("PFP_BASE_NORMAL_STIFFNESS", BaseNormalStiffness)
		if BaseForceResistance is not None:
			self._setDoubleProperty("PFP_BASE_FORCE_RESISTANCE", BaseForceResistance)
	def getProperties(self):
		return {
		"ShearStiffness" : self.getShearStiffness(), 
		"NormalStiffness" : self.getNormalStiffness(), 
		"FrictionAngle" : self.getFrictionAngle(), 
		"ResidualFrictionAngle" : self.getResidualFrictionAngle(), 
		"Cohesion" : self.getCohesion(), 
		"ResidualCohesion" : self.getResidualCohesion(), 
		"UseShearResistanceCutoff" : self.getUseShearResistanceCutoff(), 
		"ShearResistanceCutoff" : self.getShearResistanceCutoff(), 
		"Perimeter" : self.getPerimeter(), 
		"UseBaseResistance" : self.getUseBaseResistance(), 
		"BaseNormalStiffness" : self.getBaseNormalStiffness(), 
		"BaseForceResistance" : self.getBaseForceResistance(), 
		}
