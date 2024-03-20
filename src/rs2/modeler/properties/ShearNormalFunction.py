from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.PropertyEnums import *

class ShearNormalFunction(ProxyObject):
    def getName(self) -> str:
        return self._callFunction("Get_Name")
    def setMaterialType(self, materialType: MaterialType):
        return self._callFunction("setMaterialTypeByName", [materialType.value])
    def getMaterialType(self) -> str:
        return MaterialType(self._callFunction("getMaterialTypeName"))
    def setPeakTensileStrength(self, peakTensileStrength: float):
        return self._callFunction("setPeakTensileStrength", [peakTensileStrength])
    def getPeakTensileStrength(self) -> float:
        return self._callFunction("getPeakTensileStrength")
    def setResidualTensileStrength(self, residualTensileStrength: float):
        return self._callFunction("setResidualTensileStrength", [residualTensileStrength])
    def getResidualTensileStrength(self) -> float:
        return self._callFunction("getResidualTensileStrength")
    def setDilationRatio(self, dilationRatio: float):
        return self._callFunction("setDilationRatio", [dilationRatio])
    def getDilationRatio(self) -> float:
        return self._callFunction("getDilationRatio")
    def setUseCalculatedTensileStrength(self, useCalculatedTensileStrength: bool):
        return self._callFunction("setUseCalculatedTensileStrength", [useCalculatedTensileStrength])
    def getUseCalculatedTensileStrength(self) -> bool:
        return self._callFunction("getUseCalculatedTensileStrength")
    def setFunctionPoints(self, functionPoints: list[tuple[float,float,float]]):
        """set the function points. Each point has  (normal, shear, residual shear). Residual shear is ignored if the material type is not plastic.
        Function must not be concave. If a concave function is provided, it will transform the function into a convex function.

        Args:
            functionPoints: list of tuples of (normal, shear, residual shear)

        Returns:
            None
        """
        return self._callFunction("setFunctionPoints", [functionPoints])
    def getFunctionPoints(self) -> list[tuple[float,float,float]]:
        """returns the function points as a list of tuples of (normal, shear, residual shear). Residual shear is ignored if the material type is not plastic.

        Returns:
            list[tuple(float,float,float)]: list of tuples of (normal, shear, residual shear)
        """
        return self._callFunction("getFunctionPoints")
    