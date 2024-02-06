from rs2._common.ProxyObject import ProxyObject
from rs2.modeler.properties.PropertyEnums import *
from rs2.modeler.properties.MaterialJoint import MaterialJoint
class MaterialJointOptions(ProxyObject):
    def __init__(self, client, ID, documentProxyID):
        self.documentProxyID = documentProxyID
        super().__init__(client, ID)

    def setNumberOfJoints(self, value: int):
        return self._callFunction("setNumberOfJoints", [value])
    def getNumberOfJoints(self) -> int:
        return self._callFunction("getNumberOfJoints")
    def setUseTracePlane(self, jointIndex: int, value: bool):
        return self._callFunction("setUseTracePlane", [jointIndex, value])
    def getUseTracePlane(self, jointIndex: int) -> bool:
        return self._callFunction("getUseTracePlane", [jointIndex])
    def setTracePlaneProperties(self, jointIndex: int, tracePlaneDipDirection : float, dip : float, dipDirection : float):
        return self._callFunction("setTracePlaneProperties", [jointIndex, tracePlaneDipDirection, dip, dipDirection])
    def getTracePlaneProperties(self, jointIndex: int) -> tuple[float,float,float]:
        """ returns a tuple (traceplanedipdirection, dip, dipdirection) for the joint at the given index
        """
        return self._callFunction("getTracePlaneProperties", [jointIndex])
    def setInclination(self, jointIndex: int, value: float):
        return self._callFunction("setInclination", [jointIndex, value])
    def getInclination(self, jointIndex: int) -> float:
        return self._callFunction("getInclination", [jointIndex])
    def getJoint(self, jointIndex: int) -> MaterialJoint:
        return MaterialJoint(self._client, self._callFunction("getJoint", [jointIndex], keepReturnValueReference=True), self.documentProxyID)