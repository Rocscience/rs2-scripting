from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2.modeler.properties.PropertyEnums import *

from rs2.modeler.properties.material.datum.BaseDatum import BaseDatum
class SimpleDatum(BaseDatum):
    def setChange(self, change : float):
        self._callFunction("setChange1", [change])
    def getChange(self) -> float:
        return self._callFunction("getChange1")
    def setUseCutoff(self, useCutoff):
        self._callFunction("setUsingCutoff1", [useCutoff])
    def getUseCutoff(self) -> bool:
        return bool(self._callFunction("getUsingCutoff1"))
    def setCutoff(self, cutoff : float):
        self._callFunction("setCutoff1", [cutoff])
    def getCutoff(self) -> float:
        return self._callFunction("getCutoff1")
