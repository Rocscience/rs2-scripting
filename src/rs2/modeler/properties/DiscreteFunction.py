from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.PropertyEnums import *
class DiscreteFunction(ProxyObject):
    def getName(self):
        return self._callFunction('getName', [])
    def setName(self, name : str):
        return self._callFunction('setName', [name])
    def setFunctionParameters(self, functionType : MaterialBehaviours, useModulus : bool, residualStrengthFactor : float, peakTensileStrength : float, residualTensileStrength : float, useModulusResidual : bool = False):
        return self._callFunction('setFunctionParameters', [functionType.value, useModulus, residualStrengthFactor, peakTensileStrength, residualTensileStrength, useModulusResidual])
    def getFunctionParameters(self):
        """
        Returns a tuple of (MaterialBehaviours, useModulus, residualStrengthFactor, peakTensileStrength, residualTensileStrength, useModulusResidual)
        """
        params = self._callFunction('getFunctionParameters', [])
        return (MaterialBehaviours(params[0]), params[1], params[2], params[3], params[4], params[5])
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