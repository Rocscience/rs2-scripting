from rs2.modeler.properties.propertyProxy import PropertyProxy
from rs2.modeler.properties.PropertyEnums import *
class BaseDatum(PropertyProxy):
    def setUsing(self, use : bool):
        self._callFunction("setUsing", [use])
    def getUsing(self) -> bool:
        return bool(self._callFunction("getUsing"))
    def setType(self, type : DatumType):
        self._callFunction("setType", [type.value])
    def getType(self) -> DatumType:
        return DatumType(self._callFunction("getType"))
    def setDatum(self, depth : float):
        self._callFunction("setDatum", [depth])
    def getDatum(self) -> float:
        return self._callFunction("getDatum")
    def setCenter(self, x: float , y : float):
        self._callFunction("setCenter", [x,y])
    def getCenter(self)-> (float, float): 
        """
        Returns the Datum's center as a tuple (x,y)
        """
        return self._callFunction("getCenter")
    