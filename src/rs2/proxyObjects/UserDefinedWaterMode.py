from rs2.ProxyObject import ProxyObject

class UserDefinedWaterMode(ProxyObject):
    def getWaterContentFunction(self) -> list[tuple[float, float]]:
        return self._callFunction('getWCFunction')
    def setWaterContentFunction(self, wcFunction : list[tuple[float, float]]):
        return self._callFunction('setWCFunction', [wcFunction])
    def getDegreeOfSaturationFunction(self) -> list[tuple[float, float]]:
        return self._callFunction('getDOSFunction')
    def setDegreeOfSaturationFunction(self, dosFunction : list[tuple[float, float]]):
        return self._callFunction('setDOSFunction', [dosFunction])
    def getPermeabilityFunction(self) -> list[tuple[float, float]]:
        return self._callFunction('getStrengthFunction')
    def setPermeabilityFunction(self, strengthFunction : list[tuple[float, float]]):
        return self._callFunction('setStrengthFunction', [strengthFunction])
    
    