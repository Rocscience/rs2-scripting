from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.PropertyEnums import *

class HydroDistributionFunction(ProxyObject):
    def setPointsParameter(self, param : list[list[float]]):
        return self._callFunction('setPointsParameter', [param])
    def getPointsParameter(self) -> list[list[float]]:
        return self._callFunction('getPointsParameter', [])

