from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2._common.Client import Client
from enum import Enum, auto
from typing import List
from rs2.modeler.properties.PropertyEnums import *
from rs2._common.documentProxy import DocumentProxy
class Beam(PropertyProxy):
	def getLinerProperty(self) -> str:
		return self._callFunction("getBeamLinerProperty", [])
	def setLinerProperty(self, linerName: str):
		"""
		Resets the mesh if it exists.
		"""
		response = self._callFunction("setBeamLinerProperty", [linerName])
		DocumentProxy(self._client, self.documentProxyID).rebuildAndPostProcessPiles()
		return response
	def getBeamSegment(self) -> tuple[list[float], list[str]]:
		return self._callFunction("getBeamSegment", [])
	def defineBeamSegment(self, Locations: list[float], Liners: list[str]):
		"""
		Resets the mesh if it exists.
		"""
		response = self._callFunction("defineBeamSegment", [Locations, Liners])
		DocumentProxy(self._client, self.documentProxyID).rebuildAndPostProcessPiles()
		return response
	def setApplication(self, method: PileApplicationType):
		"""
		Resets the mesh if it exists.
		"""
		response = self._callFunction("setBeamApplication", [method.value])
		DocumentProxy(self._client, self.documentProxyID).rebuildAndPostProcessPiles()
		return response
	def getApplication(self) -> PileApplicationType:
		return PileApplicationType(self._callFunction("getBeamApplication", []))
