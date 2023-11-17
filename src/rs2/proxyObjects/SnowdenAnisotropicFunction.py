from rs2.ProxyObject import ProxyObject
from rs2.PropertyEnums import *

class SnowdenAnisotropicFunction(ProxyObject):
    def setFunctionType(self, functionType : SnowdenAnisotropicFunctionType):
        return self._callFunction("setFunctionType", [functionType.value])
    def getFunctionType(self) -> SnowdenAnisotropicFunctionType:
        return SnowdenAnisotropicFunctionType(self._callFunction("getFunctionType"))
    
    def setPeakTensileStrength(self, peakTensileStrength : float):
        return self._callFunction("setPeakTensileStrength", [peakTensileStrength])
    def getPeakTensileStrength(self) -> float:
        return float(self._callFunction("__getattribute__", ["dPeakTensileStrength"]))
    
    def setResidualTensileStrength(self, residualTensileStrength : float):
        return self._callFunction("setResidualTensileStrength", [residualTensileStrength])
    def getResidualTensileStrength(self) -> float:
        return float(self._callFunction("__getattribute__", ["dResidualTensileStrength"]))
    
    def setDilationRatio(self, dilationRatio : float):
        return self._callFunction("setDilationRatio", [dilationRatio])
    def getDilationRatio(self) -> float:
        return float(self._callFunction("__getattribute__", ["dDilationRatio"]))

    def setShearNormalFunction(self, normalStress : list[float], shearStress : list[float]):
        return self._callFunction("setShearNormalFunction", [normalStress, shearStress])

    def setShearNormalFunctionWithResidual(self, normalStress : list[float], shearStress : list[float], residualShearStress : list[float]):
        return self._callFunction("setShearNormalFunctionWithResidual", [normalStress, shearStress, residualShearStress])
    
    def setCohesionFrictionFunction(self, normalStress : list[float], cohesion : list[float], frictionAngle : list[float]):
        return self._callFunction("setCohesionFrictionFunction", [normalStress, cohesion, frictionAngle])
    
    def setCohesionFrictionFunctionWithResidual(self, normalStress : list[float], cohesion : list[float], frictionAngle : list[float], residualCohesion : list[float], residualFrictionAngle : list[float]):
        return self._callFunction("setCohesionFrictionFunctionWithResidual", [normalStress, cohesion, frictionAngle, residualCohesion, residualFrictionAngle])
    
    def getNormalStress(self) -> list[float]:
        return list(self._callFunction("__getattribute__", ["normalStress"]))
    
    def getShearStress(self) -> list[float]:
        return list(self._callFunction("__getattribute__", ["shearStress"]))
    
    def getResidualShearStress(self) -> list[float]:
        return list(self._callFunction("__getattribute__", ["residualShearStress"]))
    
    def getCohesion(self) -> list[float]:
        return list(self._callFunction("__getattribute__", ["cohesion"]))
    
    def getFrictionAngle(self) -> list[float]:
        return list(self._callFunction("__getattribute__", ["frictionAngle"]))
    
    def getResidualCohesion(self) -> list[float]:
        return list(self._callFunction("__getattribute__", ["residualCohesion"]))
    
    def getResidualFrictionAngle(self) -> list[float]:
        return list(self._callFunction("__getattribute__", ["residualFrictionAngle"]))