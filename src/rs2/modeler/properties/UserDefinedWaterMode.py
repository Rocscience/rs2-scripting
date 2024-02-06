from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.PropertyEnums import WCInputType
class UserDefinedWaterMode(ProxyObject):
    def setWaterContentInputType(self, inputType : WCInputType):
        return self._callFunction('setWaterContentInputType', [inputType.value])
    def getWaterContentInputType(self) -> WCInputType:
        return WCInputType(self._callFunction('getWaterContentInputType'))
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
    
    