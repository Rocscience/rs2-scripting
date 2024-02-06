from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class SwellingRock(PropertyProxy):
	def getAngleToBeddingPlanes(self) -> float:
		return self._getDoubleProperty("MP_SR_V")
	def setAngleToBeddingPlanes(self, value: float):
		return self._setDoubleProperty("MP_SR_V", value)
	def getElasticModulusTangentialToBeddingPlane(self) -> float:
		return self._getDoubleProperty("MP_SR_MODULUS_TANGENT")
	def setElasticModulusTangentialToBeddingPlane(self, value: float):
		return self._setDoubleProperty("MP_SR_MODULUS_TANGENT", value)
	def getElasticModulusNormalToBeddingPlanes(self) -> float:
		return self._getDoubleProperty("MP_SR_MODULUS_NORMAL")
	def setElasticModulusNormalToBeddingPlanes(self, value: float):
		return self._setDoubleProperty("MP_SR_MODULUS_NORMAL", value)
	def getPoissonsRatioOutOfBeddingPlanes(self) -> float:
		return self._getDoubleProperty("MP_SR_POISSON_OUT_OF")
	def setPoissonsRatioOutOfBeddingPlanes(self, value: float):
		return self._setDoubleProperty("MP_SR_POISSON_OUT_OF", value)
	def getPoissonsRatioWithinBeddingPlanes(self) -> float:
		return self._getDoubleProperty("MP_SR_POISSON_WITHIN")
	def setPoissonsRatioWithinBeddingPlanes(self, value: float):
		return self._setDoubleProperty("MP_SR_POISSON_WITHIN", value)
	def getShearModulus(self) -> float:
		return self._getDoubleProperty("MP_SR_SHEAR_MODULUS")
	def setShearModulus(self, value: float):
		return self._setDoubleProperty("MP_SR_SHEAR_MODULUS", value)
	def setProperties(self, AngleToBeddingPlanes : float = None, ElasticModulusTangentialToBeddingPlane : float = None, ElasticModulusNormalToBeddingPlanes : float = None, PoissonsRatioOutOfBeddingPlanes : float = None, PoissonsRatioWithinBeddingPlanes : float = None, ShearModulus : float = None):
		if AngleToBeddingPlanes is not None:
			self._setDoubleProperty("MP_SR_V", AngleToBeddingPlanes)
		if ElasticModulusTangentialToBeddingPlane is not None:
			self._setDoubleProperty("MP_SR_MODULUS_TANGENT", ElasticModulusTangentialToBeddingPlane)
		if ElasticModulusNormalToBeddingPlanes is not None:
			self._setDoubleProperty("MP_SR_MODULUS_NORMAL", ElasticModulusNormalToBeddingPlanes)
		if PoissonsRatioOutOfBeddingPlanes is not None:
			self._setDoubleProperty("MP_SR_POISSON_OUT_OF", PoissonsRatioOutOfBeddingPlanes)
		if PoissonsRatioWithinBeddingPlanes is not None:
			self._setDoubleProperty("MP_SR_POISSON_WITHIN", PoissonsRatioWithinBeddingPlanes)
		if ShearModulus is not None:
			self._setDoubleProperty("MP_SR_SHEAR_MODULUS", ShearModulus)
	def getProperties(self):
		return {
		"AngleToBeddingPlanes" : self.getAngleToBeddingPlanes(), 
		"ElasticModulusTangentialToBeddingPlane" : self.getElasticModulusTangentialToBeddingPlane(), 
		"ElasticModulusNormalToBeddingPlanes" : self.getElasticModulusNormalToBeddingPlanes(), 
		"PoissonsRatioOutOfBeddingPlanes" : self.getPoissonsRatioOutOfBeddingPlanes(), 
		"PoissonsRatioWithinBeddingPlanes" : self.getPoissonsRatioWithinBeddingPlanes(), 
		"ShearModulus" : self.getShearModulus(), 
		}
