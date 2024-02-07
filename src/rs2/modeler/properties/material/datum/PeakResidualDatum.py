from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2.modeler.properties.PropertyEnums import *

from rs2.modeler.properties.material.datum.BaseDatum import BaseDatum
class PeakResidualDatum(BaseDatum):
    def setPeakChange(self, peakChange: float):
        self._callFunction("setChange1", [peakChange])
    def getPeakChange(self) -> float:
        return self._callFunction("getChange1")
    def setUsePeakCutoff(self, usePeakCutoff : bool):
        self._callFunction("setUsingCutoff1", [usePeakCutoff])
    def getUsePeakCutoff(self) -> bool:
        return bool(self._callFunction("getUsingCutoff1"))
    def setPeakCutoffValue(self, peakCutoffValue: float):
        self._callFunction("setCutoff1", [peakCutoffValue])
    def getPeakCutoffValue(self) -> float:
        return self._callFunction("getCutoff1")
    def setResidualChange(self, residualChange: float):
        self._callFunction("setChange2", [residualChange])
    def getResidualChange(self) -> float:
        return self._callFunction("getChange2")
    def setUseResidualCutoff(self, useResidualCutoff):
        self._callFunction("setUsingCutoff2", [useResidualCutoff])
    def getUseResidualCutoff(self) -> bool:
        return bool(self._callFunction("getUsingCutoff2"))
    def setResidualCutoffValue(self, residualCutoffValue: float):
        self._callFunction("setCutoff2", [residualCutoffValue])
    def getResidualCutoffValue(self) -> float:
        return self._callFunction("getCutoff2")
    
    
