from rs2._common.ProxyObject import ProxyObject
from rs2._common.Client import Client
from rs2.modeler.properties.PropertyEnums import *

class StageFactors(ProxyObject):
	def __init__(self, client : Client, ID):
		super().__init__(client, ID)
	def setStageStrengthStiffnessStageFactors(self, value: bool):
		return self._callFunction("setApplyStrengthStiffnessStageFactors", [value])
	def getStageStrengthStiffnessStageFactors(self) -> bool:
		return self._callFunction("getApplyStrengthStiffnessStageFactors")
	def setStageThermalStageFactors(self, value: bool):
		return self._callFunction("setApplyThermalStageFactors", [value])
	def getStageThermalStageFactors(self) -> bool:
		return self._callFunction("getApplyThermalStageFactors")
	def setStageHydraulicStageFactor(self, value: bool):
		return self._callFunction("setApplyHydraulicStageFactor", [value])
	def getStageHydraulicStageFactor(self) -> bool:
		return self._callFunction("getApplyHydraulicStageFactor")
	def setStageDatumStageFactor(self, value: bool):
		return self._callFunction("setApplyDatumStageFactor", [value])
	def getStageDatumStageFactor(self) -> bool:
		return self._callFunction("getApplyDatumStageFactor")
	def setResetStress(self, value: bool):
		return self._callFunction("setResetStress", [value])
	def getResetStress(self) -> bool:
		return self._callFunction("getResetStress")