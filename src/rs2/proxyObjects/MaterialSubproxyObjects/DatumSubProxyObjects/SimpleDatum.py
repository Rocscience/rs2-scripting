from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.PropertyEnums import *

from rs2.proxyObjects.MaterialSubproxyObjects.DatumSubProxyObjects.BaseDatum import BaseDatum

class SimpleDatum(BaseDatum):
    def setChange(self, change : float):
        self._callFunction("setChange", [change])
    def getChange(self) -> float:
        return self._callFunction("getChange")
    def setUseCutoff(self, useCutoff):
        self._callFunction("setUseCutoff", [useCutoff])
    def getUseCutoff(self) -> bool:
        return self._callFunction("getUseCutoff")
    def setCutoff(self, cutoff : float):
        self._callFunction("setCutoff", [cutoff])
    def getCutoff(self) -> float:
        return self._callFunction("getCutoff")
