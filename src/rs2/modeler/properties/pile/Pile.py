from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.documentProxy import DocumentProxy
from rs2.modeler.properties.pile.Elastic import Elastic
from rs2.modeler.properties.pile.MohrCoulombPile import MohrCoulombPile
from rs2.modeler.properties.pile.Linear import Linear
from rs2.modeler.properties.pile.MultiLinear import MultiLinear
from rs2.modeler.properties.pile.MaterialDependentPile import MaterialDependentPile
from rs2.modeler.properties.pile.Beam import Beam
from rs2.modeler.properties.pile.ForceDisplacement import ForceDisplacement
class PileProperty(PropertyProxy):
	"""
	Attributes:
		Elastic (Elastic): Reference object for modifying property.
		MohrCoulombPile (MohrCoulombPile): Reference object for modifying property.
		Linear (Linear): Reference object for modifying property.
		MultiLinear (MultiLinear): Reference object for modifying property.
		MaterialDependentPile (MaterialDependentPile): Reference object for modifying property.
		Beam (Beam): Reference object for modifying property.
		ForceDisplacement (ForceDisplacement): Reference object for modifying property.

	Examples:
		:ref:`Pile Example`
	"""
	def __init__(self, client : Client, ID, documentProxyID):
		self.Elastic = Elastic(client, ID, documentProxyID)
		self.MohrCoulombPile = MohrCoulombPile(client, ID, documentProxyID)
		self.Linear = Linear(client, ID, documentProxyID)
		self.MultiLinear = MultiLinear(client, ID, documentProxyID)
		self.MaterialDependentPile = MaterialDependentPile(client, ID, documentProxyID)
		self.Beam = Beam(client, ID, documentProxyID)
		self.ForceDisplacement = ForceDisplacement(client, ID, documentProxyID)
		super().__init__(client, ID, documentProxyID)
	def getPileName(self) -> str:
		return self._getCStringProperty("PFP_NAME")
	def setPileName(self, value: str):
		return self._setCStringProperty("PFP_NAME", value)
	def getPileColor(self) -> int:
		return self._getUnsignedLongProperty("PFP_COLOR")
	def setPileColor(self, value: int):
		return self._setUnsignedLongProperty("PFP_COLOR", value)
	def getConnectionType(self) -> PileConnectionType:
		return PileConnectionType(self._getEnumEPileConnectionTypeProperty("PFP_TYPE"))
	def setConnectionType(self, value: PileConnectionType):
		return self._setEnumEPileConnectionTypeProperty("PFP_TYPE", value)
	def getSkinResistance(self) -> PileSkinResistanceType:
		return PileSkinResistanceType(self._getEnumEPileSkinResistanceTypeProperty("PFP_SKIN_RESISTANCE_METHOD"))
	def setSkinResistance(self, value: PileSkinResistanceType):
		return self._setEnumEPileSkinResistanceTypeProperty("PFP_SKIN_RESISTANCE_METHOD", value)
	def getMMax(self) -> float:
		return self._callFunction("__getattribute__", ["m_mmax"])
	def setMMax(self, MMax: float):
		return self._callFunction("setMMax", [MMax])
	def getOutOfPlaneSpacing(self) -> float:
		return self._callFunction("__getattribute__", ["m_plane_spacing"])
	def setOutOfPlaneSpacing(self, outOfPlaneSpacing: float):
		return self._callFunction("setOutOfPlaneSpacing", [outOfPlaneSpacing])
	def getLength(self) -> float:
		return self._callFunction("__getattribute__", ["m_length"])
	def setLength(self, Length: float):
		"""
		Resets the mesh if it exists.
		"""
		response = self._callFunction("setLength", [Length])
		DocumentProxy(self._client, self.documentProxyID).rebuildAndPostProcessPiles()
		return response
	def getStageForceDisplacement(self) -> bool:
		return self._callFunction("__getattribute__", ["apply_stage_factors"])
	def setStageForceDisplacement(self, stageForceDisplacement: bool):
		return self._callFunction("setApplyStageFactors", [stageForceDisplacement])
