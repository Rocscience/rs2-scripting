from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
class SwellingRockStrength(PropertyProxy):
	def getFrictionAngle(self) -> float:
		return self._getDoubleProperty("MP_SR_FRIC_ANGLE")
	def setFrictionAngle(self, value: float):
		return self._setDoubleProperty("MP_SR_FRIC_ANGLE", value)
	def getCohesion(self) -> float:
		return self._getDoubleProperty("MP_SR_COHESION")
	def setCohesion(self, value: float):
		return self._setDoubleProperty("MP_SR_COHESION", value)
	def getTensileStrength(self) -> float:
		return self._getDoubleProperty("MP_SR_TENSILE")
	def setTensileStrength(self, value: float):
		return self._setDoubleProperty("MP_SR_TENSILE", value)
	def getDilationAngle(self) -> float:
		return self._getDoubleProperty("MP_SR_DILATION_ANGLE")
	def setDilationAngle(self, value: float):
		return self._setDoubleProperty("MP_SR_DILATION_ANGLE", value)
	def getA0(self) -> float:
		return self._getDoubleProperty("MP_SR_A0")
	def setA0(self, value: float):
		return self._setDoubleProperty("MP_SR_A0", value)
	def getAElastic(self) -> float:
		return self._getDoubleProperty("MP_SR_A_ELASTIC")
	def setAElastic(self, value: float):
		return self._setDoubleProperty("MP_SR_A_ELASTIC", value)
	def getAPlastic(self) -> float:
		return self._getDoubleProperty("MP_SR_A_PLASTIC")
	def setAPlastic(self, value: float):
		return self._setDoubleProperty("MP_SR_A_PLASTIC", value)
	def getMaximumPlasticVolumetricStrainForAPlastic(self) -> float:
		return self._getDoubleProperty("MP_SR_MAX_PLASTIC_V_STRAIN")
	def setMaximumPlasticVolumetricStrainForAPlastic(self, value: float):
		return self._setDoubleProperty("MP_SR_MAX_PLASTIC_V_STRAIN", value)
	def getKSwellNormal(self) -> float:
		return self._getDoubleProperty("MP_SR_K_SWELL_NORMAL")
	def setKSwellNormal(self, value: float):
		return self._setDoubleProperty("MP_SR_K_SWELL_NORMAL", value)
	def getKSwellTangential(self) -> float:
		return self._getDoubleProperty("MP_SR_K_SWELL_TANGENT")
	def setKSwellTangential(self, value: float):
		return self._setDoubleProperty("MP_SR_K_SWELL_TANGENT", value)
	def getMaximumSwellingStressNormal(self) -> float:
		return self._getDoubleProperty("MP_SR_MAX_STRESS_NORMAL")
	def setMaximumSwellingStressNormal(self, value: float):
		return self._setDoubleProperty("MP_SR_MAX_STRESS_NORMAL", value)
	def getMaximumSwellingStressTangential(self) -> float:
		return self._getDoubleProperty("MP_SR_MAX_STRESS_TANGENT")
	def setMaximumSwellingStressTangential(self, value: float):
		return self._setDoubleProperty("MP_SR_MAX_STRESS_TANGENT", value)
	def getMinimumSwellingStress(self) -> float:
		return self._getDoubleProperty("MP_SR_MIN_STRESS")
	def setMinimumSwellingStress(self, value: float):
		return self._setDoubleProperty("MP_SR_MIN_STRESS", value)
	def getSwellingFormulation(self) -> SwellingForm:
		return SwellingForm(self._getEnumESwellingFormProperty("MP_SR_SWELLING_FORM"))
	def setSwellingFormulation(self, value: SwellingForm):
		return self._setEnumESwellingFormProperty("MP_SR_SWELLING_FORM", value)
	def getWaterCondition(self) -> WaterCondition:
		return WaterCondition(self._getEnumEWaterConditionProperty("MP_SR_WATER_CONDITION"))
	def setWaterCondition(self, value: WaterCondition):
		return self._setEnumEWaterConditionProperty("MP_SR_WATER_CONDITION", value)
	def getSigmaCoupling(self) -> float:
		return self._getDoubleProperty("MP_SR_SIGMA_COUPLING")
	def setSigmaCoupling(self, value: float):
		return self._setDoubleProperty("MP_SR_SIGMA_COUPLING", value)
	def setProperties(self, FrictionAngle : float = None, Cohesion : float = None, TensileStrength : float = None, DilationAngle : float = None, A0 : float = None, AElastic : float = None, APlastic : float = None, MaximumPlasticVolumetricStrainForAPlastic : float = None, KSwellNormal : float = None, KSwellTangential : float = None, MaximumSwellingStressNormal : float = None, MaximumSwellingStressTangential : float = None, MinimumSwellingStress : float = None, SwellingFormulation : SwellingForm = None, WaterCondition : WaterCondition = None, SigmaCoupling : float = None):
		if FrictionAngle is not None:
			self._setDoubleProperty("MP_SR_FRIC_ANGLE", FrictionAngle)
		if Cohesion is not None:
			self._setDoubleProperty("MP_SR_COHESION", Cohesion)
		if TensileStrength is not None:
			self._setDoubleProperty("MP_SR_TENSILE", TensileStrength)
		if DilationAngle is not None:
			self._setDoubleProperty("MP_SR_DILATION_ANGLE", DilationAngle)
		if A0 is not None:
			self._setDoubleProperty("MP_SR_A0", A0)
		if AElastic is not None:
			self._setDoubleProperty("MP_SR_A_ELASTIC", AElastic)
		if APlastic is not None:
			self._setDoubleProperty("MP_SR_A_PLASTIC", APlastic)
		if MaximumPlasticVolumetricStrainForAPlastic is not None:
			self._setDoubleProperty("MP_SR_MAX_PLASTIC_V_STRAIN", MaximumPlasticVolumetricStrainForAPlastic)
		if KSwellNormal is not None:
			self._setDoubleProperty("MP_SR_K_SWELL_NORMAL", KSwellNormal)
		if KSwellTangential is not None:
			self._setDoubleProperty("MP_SR_K_SWELL_TANGENT", KSwellTangential)
		if MaximumSwellingStressNormal is not None:
			self._setDoubleProperty("MP_SR_MAX_STRESS_NORMAL", MaximumSwellingStressNormal)
		if MaximumSwellingStressTangential is not None:
			self._setDoubleProperty("MP_SR_MAX_STRESS_TANGENT", MaximumSwellingStressTangential)
		if MinimumSwellingStress is not None:
			self._setDoubleProperty("MP_SR_MIN_STRESS", MinimumSwellingStress)
		if SwellingFormulation is not None:
			self._setEnumESwellingFormProperty("MP_SR_SWELLING_FORM", SwellingFormulation)
		if WaterCondition is not None:
			self._setEnumEWaterConditionProperty("MP_SR_WATER_CONDITION", WaterCondition)
		if SigmaCoupling is not None:
			self._setDoubleProperty("MP_SR_SIGMA_COUPLING", SigmaCoupling)
	def getProperties(self):
		return {
		"FrictionAngle" : self.getFrictionAngle(), 
		"Cohesion" : self.getCohesion(), 
		"TensileStrength" : self.getTensileStrength(), 
		"DilationAngle" : self.getDilationAngle(), 
		"A0" : self.getA0(), 
		"AElastic" : self.getAElastic(), 
		"APlastic" : self.getAPlastic(), 
		"MaximumPlasticVolumetricStrainForAPlastic" : self.getMaximumPlasticVolumetricStrainForAPlastic(), 
		"KSwellNormal" : self.getKSwellNormal(), 
		"KSwellTangential" : self.getKSwellTangential(), 
		"MaximumSwellingStressNormal" : self.getMaximumSwellingStressNormal(), 
		"MaximumSwellingStressTangential" : self.getMaximumSwellingStressTangential(), 
		"MinimumSwellingStress" : self.getMinimumSwellingStress(), 
		"SwellingFormulation" : self.getSwellingFormulation(), 
		"WaterCondition" : self.getWaterCondition(), 
		"SigmaCoupling" : self.getSigmaCoupling(), 
		}
