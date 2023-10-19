from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.PropertyEnums import *

from rs2.proxyObjects.MaterialSubproxyObjects.DatumSubProxyObjects.BaseDatum import BaseDatum

class PeakResidualDatum(PropertyProxy):
    def setPeakChange(self, peakChange: float):
        self._callFunction("setPeakChange", [peakChange])
    def getPeakChange(self) -> float:
        return self._callFunction("getPeakChange")
    def setUsePeakCutoff(self, usePeakCutoff : bool):
        self._callFunction("setUsePeakCutoff", [usePeakCutoff])
    def getUsePeakCutoff(self) -> bool:
        return self._callFunction("getUsePeakCutoff")
    def setPeakCutoffValue(self, peakCutoffValue: float):
        self._callFunction("setPeakCutoffValue", [peakCutoffValue])
    def getPeakCutoffValue(self) -> float:
        return self._callFunction("getPeakCutoffValue")
    def setResidualChange(self, residualChange: float):
        self._callFunction("setResidualChange", [residualChange])
    def getResidualChange(self) -> float:
        return self._callFunction("getResidualChange")
    def setUseResidualCutoff(self, useResidualCutoff):
        self._callFunction("setUseResidualCutoff", [useResidualCutoff])
    def getUseResidualCutoff(self) -> bool:
        return self._callFunction("getUseResidualCutoff")
    def setResidualCutoffValue(self, residualCutoffValue: float):
        self._callFunction("setResidualCutoffValue", [residualCutoffValue])
    def getResidualCutoffValue(self) -> float:
        return self._callFunction("getResidualCutoffValue")
    
    
