from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.material.hydraulic.FEAGroundwater.Simple import Simple
from rs2.modeler.properties.material.hydraulic.FEAGroundwater.Fredlund import Fredlund
from rs2.modeler.properties.material.hydraulic.FEAGroundwater.Genuchten import Genuchten
from rs2.modeler.properties.material.hydraulic.FEAGroundwater.Brooks import Brooks
from rs2.modeler.properties.material.hydraulic.FEAGroundwater.Gardner import Gardner
from rs2.modeler.properties.material.hydraulic.FEAGroundwater.Constant import Constant
from rs2.modeler.properties.material.hydraulic.FEAGroundwater.UserDefined import UserDefined
from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.AbsoluteStageFactorGettersInterface import AbsoluteStageFactorGettersInterface
class FEAGroundwaterStageFactor(ProxyObject):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID)
		self.propertyID = propertyID
	def getK1AngleFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_K1_ANGLE", self.propertyID], proxyArgumentIndices=[1])
	def getK2K1Factor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_K2_K1", self.propertyID], proxyArgumentIndices=[1])
	def getMvFactor(self) -> float:
		return self._callFunction("getDoubleFactor", ["MP_MV", self.propertyID], proxyArgumentIndices=[1])
	def getAnisotropicSurfaceFactor(self) -> str:
		return self._callFunction("getSurfaceFactor", [self.propertyID], proxyArgumentIndices=[0])
class FEAGroundwaterDefinedStageFactor(FEAGroundwaterStageFactor):
	def __init__(self, client : Client, ID, propertyID):
		super().__init__(client, ID, propertyID)
	def setK1AngleFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_K1_ANGLE", value, self.propertyID], proxyArgumentIndices=[2])
	def setK2K1Factor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_K2_K1", value, self.propertyID], proxyArgumentIndices=[2])
	def setMvFactor(self, value: float):
		return self._callFunction("setDoubleFactor", ["MP_MV", value, self.propertyID], proxyArgumentIndices=[2])
	def setAnisotropicSurfaceFactor(self, surfaceName: str):
		return self._callFunction("setSurfaceFactor", [surfaceName, self.propertyID], proxyArgumentIndices=[1])
class FEAGroundwater(PropertyProxy):
	"""
	Attributes:
		stageFactorInterface (AbsoluteStageFactorGettersInterface[FEAGroundwaterDefinedStageFactor, FEAGroundwaterStageFactor]): Reference object for modifying stage factor property.
		Simple (Simple): Reference object for modifying property.
		Fredlund (Fredlund): Reference object for modifying property.
		Genuchten (Genuchten): Reference object for modifying property.
		Brooks (Brooks): Reference object for modifying property.
		Gardner (Gardner): Reference object for modifying property.
		Constant (Constant): Reference object for modifying property.
		UserDefined (UserDefined): Reference object for modifying property.

	Examples:
		:ref:`Hydraulic Property FEAGroundwater Example`
	"""
	def __init__(self, client : Client, ID, documentProxyID, stageFactorInterfaceID):
		super().__init__(client, ID, documentProxyID)
		self.stageFactorInterface = AbsoluteStageFactorGettersInterface[FEAGroundwaterDefinedStageFactor, FEAGroundwaterStageFactor](self._client, stageFactorInterfaceID, ID, FEAGroundwaterDefinedStageFactor, FEAGroundwaterStageFactor)
		self.Simple = Simple(client, ID, documentProxyID, stageFactorInterfaceID)
		self.Fredlund = Fredlund(client, ID, documentProxyID, stageFactorInterfaceID)
		self.Genuchten = Genuchten(client, ID, documentProxyID, stageFactorInterfaceID)
		self.Brooks = Brooks(client, ID, documentProxyID, stageFactorInterfaceID)
		self.Gardner = Gardner(client, ID, documentProxyID, stageFactorInterfaceID)
		self.Constant = Constant(client, ID, documentProxyID, stageFactorInterfaceID)
		self.UserDefined = UserDefined(client, ID, documentProxyID)
	def getModel(self) -> GroundWaterModes:
		return GroundWaterModes(self._getEnumEGroundWaterModesProperty("MP_HYDRAULIC_MODEL"))
	def setModel(self, value: GroundWaterModes):
		return self._setEnumEGroundWaterModesProperty("MP_HYDRAULIC_MODEL", value)
	def getK2K1(self) -> float:
		return self._getDoubleProperty("MP_K2_K1")
	def setK2K1(self, value: float):
		return self._setDoubleProperty("MP_K2_K1", value)
	def getK1Definition(self) -> AnisotropyDefinitions:
		return AnisotropyDefinitions(self._getEnumEAnisotropyDefinitionsProperty("MP_K1_DEFINITION"))
	def setK1Definition(self, value: AnisotropyDefinitions):
		return self._setEnumEAnisotropyDefinitionsProperty("MP_K1_DEFINITION", value)
	def getK1Angle(self) -> float:
		return self._getDoubleProperty("MP_K1_ANGLE")
	def setK1Angle(self, value: float):
		return self._setDoubleProperty("MP_K1_ANGLE", value)
	def getMvModel(self) -> MVModel:
		return MVModel(self._getEnumEMVModelProperty("MP_MV_MODEL"))
	def setMvModel(self, value: MVModel):
		return self._setEnumEMVModelProperty("MP_MV_MODEL", value)
	def getMv(self) -> float:
		return self._getDoubleProperty("MP_MV")
	def setMv(self, value: float):
		return self._setDoubleProperty("MP_MV", value)
	def setK1SurfaceToUseByName(self, surfaceName: str):
		"""
		surfaceName is the name of the surface to be used. Surface must be present in the model.
		"""
		return self._callFunction("setK1SurfaceToUseByName", [surfaceName])
	def getK1SurfaceToUse(self) -> str:
		return self._callFunction("getK1SurfaceToUse", [])
