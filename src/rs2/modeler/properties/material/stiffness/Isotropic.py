from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
class IsotropicStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getPoissonsRatioFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_POISSONS_RATIO", self.propertyID], proxyArgumentIndices=[1])
	def getShearModulusFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_SHEAR_MODULUS", self.propertyID], proxyArgumentIndices=[1])
	def getYoungsModulusFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_YOUNGS_MODULUS", self.propertyID], proxyArgumentIndices=[1])
	def getResidualYoungsModulusFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_YOUNGS_MODULUS_RES", self.propertyID], proxyArgumentIndices=[1])
class IsotropicDefinedStageFactor(IsotropicStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setPoissonsRatioFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_POISSONS_RATIO", value, self.propertyID], proxyArgumentIndices=[2])
	def setShearModulusFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_SHEAR_MODULUS", value, self.propertyID], proxyArgumentIndices=[2])
	def setYoungsModulusFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_YOUNGS_MODULUS", value, self.propertyID], proxyArgumentIndices=[2])
	def setResidualYoungsModulusFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_YOUNGS_MODULUS_RES", value, self.propertyID], proxyArgumentIndices=[2])
class Isotropic(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[IsotropicDefinedStageFactor, IsotropicStageFactor]): Reference object for modifying stage factor property.

	Examples:
		:ref:`Material Property Stiffness Example`
	
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[IsotropicDefinedStageFactor, IsotropicStageFactor](self._client, stageFactorInterfaceID, ID, IsotropicDefinedStageFactor, IsotropicStageFactor)
	def getUseUnloadingCondition(self) -> bool:
		return self._getBoolProperty("MP_USE_UNLOADING_CONDITION")
	def setUseUnloadingCondition(self, value: bool):
		return self._setBoolProperty("MP_USE_UNLOADING_CONDITION", value)
	def getUnloadingCondition(self) -> UnloadingConditions:
		return UnloadingConditions(self._getEnumEUnloadingConditionsProperty("MP_UNLOADING_CONDITION"))
	def setUnloadingCondition(self, value: UnloadingConditions):
		return self._setEnumEUnloadingConditionsProperty("MP_UNLOADING_CONDITION", value)
	def getElasticParameters(self) -> ElasticParameters:
		return ElasticParameters(self._getEnumEElasticParametersProperty("MP_ELASTIC_PARAMETERS"))
	def setElasticParameters(self, value: ElasticParameters):
		return self._setEnumEElasticParametersProperty("MP_ELASTIC_PARAMETERS", value)
	def getShearModulus(self) -> float:
		return self._getDoubleProperty("MP_SHEAR_MODULUS")
	def setShearModulus(self, value: float):
		return self._setDoubleProperty("MP_SHEAR_MODULUS", value)
	def getPoissonsRatio(self) -> float:
		return self._getDoubleProperty("MP_POISSONS_RATIO")
	def setPoissonsRatio(self, value: float):
		return self._setDoubleProperty("MP_POISSONS_RATIO", value)
	def getYoungsModulus(self) -> float:
		return self._getDoubleProperty("MP_YOUNGS_MODULUS")
	def setYoungsModulus(self, value: float):
		return self._setDoubleProperty("MP_YOUNGS_MODULUS", value)
	def getUseResidualYoungsModulus(self) -> bool:
		return self._getBoolProperty("MP_USE_YOUNGS_MODULUS_RES")
	def setUseResidualYoungsModulus(self, value: bool):
		return self._setBoolProperty("MP_USE_YOUNGS_MODULUS_RES", value)
	def getResidualYoungsModulus(self) -> float:
		return self._getDoubleProperty("MP_YOUNGS_MODULUS_RES")
	def setResidualYoungsModulus(self, value: float):
		return self._setDoubleProperty("MP_YOUNGS_MODULUS_RES", value)
	def getUnloadingPoissonsRatio(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_POISSONS_RATIO")
	def setUnloadingPoissonsRatio(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_POISSONS_RATIO", value)
	def getUnloadingYoungsModulus(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS")
	def setUnloadingYoungsModulus(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS", value)
	def getUseUnloadingResidualYoungsModulus(self) -> bool:
		return self._getBoolProperty("MP_UNLOADING_USE_YOUNGS_MODULUS_RES")
	def setUseUnloadingResidualYoungsModulus(self, value: bool):
		return self._setBoolProperty("MP_UNLOADING_USE_YOUNGS_MODULUS_RES", value)
	def getUnloadingResidualYoungsModulus(self) -> float:
		return self._getDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_RES")
	def setUnloadingResidualYoungsModulus(self, value: float):
		return self._setDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_RES", value)
	def setProperties(self, UseUnloadingCondition : bool = None, UnloadingCondition : UnloadingConditions = None, ElasticParameters : ElasticParameters = None, ShearModulus : float = None, PoissonsRatio : float = None, YoungsModulus : float = None, UseResidualYoungsModulus : bool = None, ResidualYoungsModulus : float = None, UnloadingPoissonsRatio : float = None, UnloadingYoungsModulus : float = None, UseUnloadingResidualYoungsModulus : bool = None, UnloadingResidualYoungsModulus : float = None):
		if UseUnloadingCondition is not None:
			self._setBoolProperty("MP_USE_UNLOADING_CONDITION", UseUnloadingCondition)
		if UnloadingCondition is not None:
			self._setEnumEUnloadingConditionsProperty("MP_UNLOADING_CONDITION", UnloadingCondition)
		if ElasticParameters is not None:
			self._setEnumEElasticParametersProperty("MP_ELASTIC_PARAMETERS", ElasticParameters)
		if ShearModulus is not None:
			self._setDoubleProperty("MP_SHEAR_MODULUS", ShearModulus)
		if PoissonsRatio is not None:
			self._setDoubleProperty("MP_POISSONS_RATIO", PoissonsRatio)
		if YoungsModulus is not None:
			self._setDoubleProperty("MP_YOUNGS_MODULUS", YoungsModulus)
		if UseResidualYoungsModulus is not None:
			self._setBoolProperty("MP_USE_YOUNGS_MODULUS_RES", UseResidualYoungsModulus)
		if ResidualYoungsModulus is not None:
			self._setDoubleProperty("MP_YOUNGS_MODULUS_RES", ResidualYoungsModulus)
		if UnloadingPoissonsRatio is not None:
			self._setDoubleProperty("MP_UNLOADING_POISSONS_RATIO", UnloadingPoissonsRatio)
		if UnloadingYoungsModulus is not None:
			self._setDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS", UnloadingYoungsModulus)
		if UseUnloadingResidualYoungsModulus is not None:
			self._setBoolProperty("MP_UNLOADING_USE_YOUNGS_MODULUS_RES", UseUnloadingResidualYoungsModulus)
		if UnloadingResidualYoungsModulus is not None:
			self._setDoubleProperty("MP_UNLOADING_YOUNGS_MODULUS_RES", UnloadingResidualYoungsModulus)
	def getProperties(self):
		return {
		"UseUnloadingCondition" : self.getUseUnloadingCondition(), 
		"UnloadingCondition" : self.getUnloadingCondition(), 
		"ElasticParameters" : self.getElasticParameters(), 
		"ShearModulus" : self.getShearModulus(), 
		"PoissonsRatio" : self.getPoissonsRatio(), 
		"YoungsModulus" : self.getYoungsModulus(), 
		"UseResidualYoungsModulus" : self.getUseResidualYoungsModulus(), 
		"ResidualYoungsModulus" : self.getResidualYoungsModulus(), 
		"UnloadingPoissonsRatio" : self.getUnloadingPoissonsRatio(), 
		"UnloadingYoungsModulus" : self.getUnloadingYoungsModulus(), 
		"UseUnloadingResidualYoungsModulus" : self.getUseUnloadingResidualYoungsModulus(), 
		"UnloadingResidualYoungsModulus" : self.getUnloadingResidualYoungsModulus(), 
		}
