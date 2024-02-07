from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.PropertyEnums import *
class DiscreteFunction(ProxyObject):
    def getName(self):
        return self._callFunction('getName', [])
    def setName(self, name : str):
        return self._callFunction('setName', [name])
    def setFunctionParameters(self, functionType : DiscreteDrainedMode, useModulus : bool, residualStrengthFactor : float, peakTensileStrength : float, residualTensileStrength : float, useModulusResidual : bool = False):
        return self._callFunction('setFunctionParameters', [functionType.value, useModulus, residualStrengthFactor, peakTensileStrength, residualTensileStrength, useModulusResidual])
    def getFunctionParameters(self):
        """
        Returns a tuple of (DiscreteDrainedMode, useModulus, residualStrengthFactor, peakTensileStrength, residualTensileStrength, useModulusResidual)
        """
        params = self._callFunction('getFunctionParameters', [])
        return (DiscreteDrainedMode(params[0]), params[1], params[2], params[3], params[4], params[5])
    def setInterpolationMethod(self, interpolationMethod : InterpolationMethod):
        return self._callFunction('setInterpolationMethod', [interpolationMethod.value])
    def getInterpolationMethod(self):
        return InterpolationMethod(self._callFunction('getInterpolationMethod', []))
    def setSymbolDrawing(self, symbol : SymbolTypes, exteriorColor : int, fillInterior : bool, interiorColor : int = 0):
        return self._callFunction('setSymbolDrawing', [symbol.value, exteriorColor, fillInterior, interiorColor])
    def getSymbolDrawing(self):
        """
        Returns a tuple of (SymbolTypes, exteriorColor, fillInterior, interiorColor)
        """
        symbolDrawing = self._callFunction('getSymbolDrawing', [])
        return (SymbolTypes(symbolDrawing[0]), symbolDrawing[1], symbolDrawing[2], symbolDrawing[3])
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