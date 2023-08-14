from rs2.ProxyObject import ProxyObject
from enum import Enum
from rs2.Client import Client
class PropertyProxy(ProxyObject):
	def __init__(self, server : Client, ID, documentProxyID) :
		self.documentProxyID = documentProxyID
		super().__init__(server, ID)
	def _getDoubleProperty(self, propertyName: str):
		return self._callFunction("getDoubleProperty", [propertyName])
	def _setDoubleProperty(self, propertyName: str, value):
		return self._callFunction("setDoubleProperty", [propertyName, value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getBoolProperty(self, propertyName: str):
		return self._callFunction("getBoolProperty", [propertyName])
	def _setBoolProperty(self, propertyName: str, value):
		return self._callFunction("setBoolProperty", [propertyName, value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEBulgeTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumEBulgeTypesProperty", [propertyName])
	def _setEnumEBulgeTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEBulgeTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEBoltModelsProperty(self, propertyName: str):
		return self._callFunction("getEnumEBoltModelsProperty", [propertyName])
	def _setEnumEBoltModelsProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEBoltModelsProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getIntProperty(self, propertyName: str):
		return self._callFunction("getIntProperty", [propertyName])
	def _setIntProperty(self, propertyName: str, value):
		return self._callFunction("setIntProperty", [propertyName, value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumESecondaryBondLengthTypeProperty(self, propertyName: str):
		return self._callFunction("getEnumESecondaryBondLengthTypeProperty", [propertyName])
	def _setEnumESecondaryBondLengthTypeProperty(self, propertyName: str, value):
		return self._callFunction("setEnumESecondaryBondLengthTypeProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getCStringProperty(self, propertyName: str):
		return self._callFunction("getCStringProperty", [propertyName])
	def _setCStringProperty(self, propertyName: str, value):
		return self._callFunction("setCStringProperty", [propertyName, value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getUnsignedLongProperty(self, propertyName: str):
		return self._callFunction("getUnsignedLongProperty", [propertyName])
	def _setUnsignedLongProperty(self, propertyName: str, value):
		return self._callFunction("setUnsignedLongProperty", [propertyName, value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEBoltTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumEBoltTypesProperty", [propertyName])
	def _setEnumEBoltTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEBoltTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEGeometryChoiceProperty(self, propertyName: str):
		return self._callFunction("getEnumEGeometryChoiceProperty", [propertyName])
	def _setEnumEGeometryChoiceProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEGeometryChoiceProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEMaterialAnalysisTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumEMaterialAnalysisTypesProperty", [propertyName])
	def _setEnumEMaterialAnalysisTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEMaterialAnalysisTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumELinerFormulationProperty(self, propertyName: str):
		return self._callFunction("getEnumELinerFormulationProperty", [propertyName])
	def _setEnumELinerFormulationProperty(self, propertyName: str, value):
		return self._callFunction("setEnumELinerFormulationProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEStaticWaterModesProperty(self, propertyName: str):
		return self._callFunction("getEnumEStaticWaterModesProperty", [propertyName])
	def _setEnumEStaticWaterModesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumEStaticWaterModesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumELinerTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumELinerTypesProperty", [propertyName])
	def _setEnumELinerTypesProperty(self, propertyName: str, value):
		return self._callFunction("setEnumELinerTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
