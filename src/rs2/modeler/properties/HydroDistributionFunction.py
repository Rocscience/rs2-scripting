from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.PropertyEnums import *

class HydroDistributionFunction(ProxyObject):
    """
    This class corresponding to the Define Hydraulic Distribution Function window.
    """
    def setPointsParameter(self, param : list[list[float]]):
        """
        Set data points of hydraulic distribution function through a list.
        """
        return self._callFunction('setPointsParameter', [param])
    def getPointsParameter(self) -> list[list[float]]:
        """
        Return a list of data points from the selected hydraulic distribution function.
        """
        return self._callFunction('getPointsParameter', [])

