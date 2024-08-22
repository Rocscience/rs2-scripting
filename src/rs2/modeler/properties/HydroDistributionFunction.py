from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.material.hydraulic.HydroDistribution import *
class HydroDistributionFunction(ProxyObject):
    def setPointsDist(self, dist : list[float]):
        pass
    def getPointsDist(self):
        pass
    def setPointCoordinates(self, locations : list[tuple[float, float]]):
        pass
    def getPointCoordinates(self):
        pass
    def setPointsParameter(self, param : list[float]):
        pass
    def getPointsParameter(self):
        pass
    def redefineHydroDistributionFunction(self, variable: HydraulicVariableTypes, functionName: str, newDistribution: HydraulicDistributionTypes):
        pass

