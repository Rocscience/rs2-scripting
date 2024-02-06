from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.PropertyEnums import *

class SnowdenAnisotropicFunction(ProxyObject):
    def setFunctionType(self, functionType : SnowdenAnisotropicFunctionType):
        return self._callFunction("setFunctionType", [functionType.value])
    def getFunctionType(self) -> SnowdenAnisotropicFunctionType:
        return SnowdenAnisotropicFunctionType(self._callFunction("getFunctionType"))
    
    def setPeakTensileStrength(self, peakTensileStrength : float):
        return self._callFunction("setPeakTensileStrength", [peakTensileStrength])
    def getPeakTensileStrength(self) -> float:
        return float(self._callFunction("getPeakTensileStrength"))
    
    def setResidualTensileStrength(self, residualTensileStrength : float):
        return self._callFunction("setResidualTensileStrength", [residualTensileStrength])
    def getResidualTensileStrength(self) -> float:
        return float(self._callFunction("getResidualTensileStrength"))
    
    def setDilationRatio(self, dilationRatio : float):
        return self._callFunction("setDilationRatio", [dilationRatio])
    def getDilationRatio(self) -> float:
        return float(self._callFunction("getDilationRatio"))

    def setShearNormalFunction(self, normalStress : list[float], shearStress : list[float]):
        return self._callFunction("setShearNormalFunction", [normalStress, shearStress])

    def setShearNormalFunctionWithResidual(self, normalStress : list[float], shearStress : list[float], residualShearStress : list[float]):
        return self._callFunction("setShearNormalFunctionWithResidual", [normalStress, shearStress, residualShearStress])
    
    def setCohesionFrictionFunction(self, normalStress : list[float], cohesion : list[float], frictionAngle : list[float]):
        return self._callFunction("setCohesionFrictionFunction", [normalStress, cohesion, frictionAngle])
    
    def setCohesionFrictionFunctionWithResidual(self, normalStress : list[float], cohesion : list[float], frictionAngle : list[float], residualCohesion : list[float], residualFrictionAngle : list[float]):
        return self._callFunction("setCohesionFrictionFunctionWithResidual", [normalStress, cohesion, frictionAngle, residualCohesion, residualFrictionAngle])
    
    def getNormalStress(self) -> list[float]:
        return list(self._callFunction("getNormalStress"))
    
    def getShearStress(self) -> list[float]:
        return list(self._callFunction("getShearStress"))
    
    def getResidualShearStress(self) -> list[float]:
        return list(self._callFunction("getResidualShearStress"))
    
    def getCohesion(self) -> list[float]:
        return list(self._callFunction("getCohesion"))
    
    def getFrictionAngle(self) -> list[float]:
        return list(self._callFunction("getFrictionAngle"))
    
    def getResidualCohesion(self) -> list[float]:
        return list(self._callFunction("getResidualCohesion"))
    
    def getResidualFrictionAngle(self) -> list[float]:
        return list(self._callFunction("getResidualFrictionAngle"))