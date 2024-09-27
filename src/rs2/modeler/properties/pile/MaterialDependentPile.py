from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class MaterialDependentPile(PropertyProxy):
	def getInterfaceCoefficient(self) -> float:
		return self._getDoubleProperty("PFP_INTERFACE_COEFFICIENT")
	def setInterfaceCoefficient(self, value: float):
		return self._setDoubleProperty("PFP_INTERFACE_COEFFICIENT", value)
	def getUseStiffnessMaterialDependent(self) -> bool:
		return self._getBoolProperty("PFP_USE_MAT_DEPENDENT")
	def setUseStiffnessMaterialDependent(self, value: bool):
		return self._setBoolProperty("PFP_USE_MAT_DEPENDENT", value)
	def getStiffnessCoefficient(self) -> float:
		return self._getDoubleProperty("PFP_INTERFACE_STIFFNESS")
	def setStiffnessCoefficient(self, value: float):
		return self._setDoubleProperty("PFP_INTERFACE_STIFFNESS", value)
	def getShearStiffness(self) -> float:
		return self._getDoubleProperty("PFP_SHEAR_STIFFNESS")
	def setShearStiffness(self, value: float):
		return self._setDoubleProperty("PFP_SHEAR_STIFFNESS", value)
	def getNormalStiffness(self) -> float:
		return self._getDoubleProperty("PFP_NORMAL_STIFFNESS")
	def setNormalStiffness(self, value: float):
		return self._setDoubleProperty("PFP_NORMAL_STIFFNESS", value)
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
	def setProperties(self, InterfaceCoefficient : float = None, UseStiffnessMaterialDependent : bool = None, StiffnessCoefficient : float = None, ShearStiffness : float = None, NormalStiffness : float = None, UseShearResistanceCutoff : bool = None, ShearResistanceCutoff : float = None, Perimeter : float = None, UseBaseResistance : bool = None, BaseNormalStiffness : float = None, BaseForceResistance : float = None):
		if InterfaceCoefficient is not None:
			self._setDoubleProperty("PFP_INTERFACE_COEFFICIENT", InterfaceCoefficient)
		if UseStiffnessMaterialDependent is not None:
			self._setBoolProperty("PFP_USE_MAT_DEPENDENT", UseStiffnessMaterialDependent)
		if StiffnessCoefficient is not None:
			self._setDoubleProperty("PFP_INTERFACE_STIFFNESS", StiffnessCoefficient)
		if ShearStiffness is not None:
			self._setDoubleProperty("PFP_SHEAR_STIFFNESS", ShearStiffness)
		if NormalStiffness is not None:
			self._setDoubleProperty("PFP_NORMAL_STIFFNESS", NormalStiffness)
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
		"InterfaceCoefficient" : self.getInterfaceCoefficient(), 
		"UseStiffnessMaterialDependent" : self.getUseStiffnessMaterialDependent(), 
		"StiffnessCoefficient" : self.getStiffnessCoefficient(), 
		"ShearStiffness" : self.getShearStiffness(), 
		"NormalStiffness" : self.getNormalStiffness(), 
		"UseShearResistanceCutoff" : self.getUseShearResistanceCutoff(), 
		"ShearResistanceCutoff" : self.getShearResistanceCutoff(), 
		"Perimeter" : self.getPerimeter(), 
		"UseBaseResistance" : self.getUseBaseResistance(), 
		"BaseNormalStiffness" : self.getBaseNormalStiffness(), 
		"BaseForceResistance" : self.getBaseForceResistance(), 
		}
