from rs2.ProxyObject import ProxyObject

class DiscreteFunction(ProxyObject):
    def getName(self):
        return self._callFunction('getName', [])
    def setName(self, name : str):
        return self._callFunction('setName', [name])
    def setFunctionParameters(self, functionType : int, useModulus : bool, residualStrengthFactor : float, peakTensileStrength : float, residualTensileStrength : float, useModulusResidual : bool = False):
        return self._callFunction('setFunctionParameters', [functionType, useModulus, residualStrengthFactor, peakTensileStrength, residualTensileStrength, useModulusResidual])
    def getFunctionParameters(self):
        return self._callFunction('getFunctionParameters', [])
    def setInterpolationMethod(self, interpolationMethod : int):
        return self._callFunction('setInterpolationMethod', [interpolationMethod])
    def getInterpolationMethod(self):
        return self._callFunction('getInterpolationMethod', [])
    def setSymbolDrawing(self, symbol : int, exteriorColor : int, fillInterior : bool, interiorColor : int = 0):
        return self._callFunction('setSymbolDrawing', [symbol, exteriorColor, fillInterior, interiorColor])
    def getSymbolDrawing(self):
        return self._callFunction('getSymbolDrawing', [])
    def setPointLocations(self, locations : list[tuple[float, float]]):
        return self._callFunction('setPointLocations', [locations])
    def getPointLocations(self):
        return self._callFunction('getPointLocations', [])
    def setPointsC(self, c : list[float]):
        return self._callFunction('setPointsC', [c])
    def getPointsC(self):
        return self._callFunction('getPointsC', [])
    def setPointsPhi(self, phi : list[float]):
        return self._callFunction('setPointsPhi', [phi])
    def getPointsPhi(self):
        return self._callFunction('getPointsPhi', [])
    def setPointsModulus(self, modulus : list[float]):
        return self._callFunction('setPointsModulus', [modulus])
    def getPointsModulus(self):
        return self._callFunction('getPointsModulus', [])
    def setPointsModulusResidual(self, modulusResidual : list[float]):
        return self._callFunction('setPointsModulusResidual', [modulusResidual])
    def getPointsModulusResidual(self):
        return self._callFunction('getPointsModulusResidual', [])