from rs2.proxyObjects.propertyProxy import PropertyProxy
from rs2.PropertyEnums import *

class DatumType(Enum):
    DEPTH = 0,
    RADIAL = 1

class BaseDatum(PropertyProxy):
    def setType(self, type : DatumType):
        self._callFunction("setType", [type])
    def getType(self) -> DatumType:
        return self._callFunction("getType")
    def setDepth(self, depth : float):
        self._callFunction("setDepth", [depth])
    def getDepth(self) -> float:
        return self._callFunction("getDepth")
    def setCenter(self, x: float , y : float):
        self._callFunction("setCenter", [x,y])
    def getCenter(self)-> (float, float): 
        """
        Returns the Datum's center as a tuple (x,y)
        """
        return self._callFunction("getCenter")
    