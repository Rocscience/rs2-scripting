from rs2.ProxyObject import ProxyObject
from enum import Enum
from rs2 import Client
class PropertyProxy(ProxyObject):
	def __init__(self, server : Client.Client, ID, documentProxyID) :
		self.documentProxyID = documentProxyID
		super().__init__(server, ID)
	def _getCStringProperty(self, propertyName: str):
		return self._callFunction("getCStringProperty", [propertyName])
	def _validateAndSetCStringProperty(self, propertyName: str, value):
		return self._callFunction("validateAndSetCStringProperty", [propertyName, value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEBoltTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumEBoltTypesProperty", [propertyName])
	def _validateAndSetEnumEBoltTypesProperty(self, propertyName: str, value):
		return self._callFunction("validateAndSetEnumEBoltTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getUnsignedLongProperty(self, propertyName: str):
		return self._callFunction("getUnsignedLongProperty", [propertyName])
	def _validateAndSetUnsignedLongProperty(self, propertyName: str, value):
		return self._callFunction("validateAndSetUnsignedLongProperty", [propertyName, value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getDoubleProperty(self, propertyName: str):
		return self._callFunction("getDoubleProperty", [propertyName])
	def _validateAndSetDoubleProperty(self, propertyName: str, value):
		return self._callFunction("validateAndSetDoubleProperty", [propertyName, value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getBoolProperty(self, propertyName: str):
		return self._callFunction("getBoolProperty", [propertyName])
	def _validateAndSetBoolProperty(self, propertyName: str, value):
		return self._callFunction("validateAndSetBoolProperty", [propertyName, value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEBoltModelsProperty(self, propertyName: str):
		return self._callFunction("getEnumEBoltModelsProperty", [propertyName])
	def _validateAndSetEnumEBoltModelsProperty(self, propertyName: str, value):
		return self._callFunction("validateAndSetEnumEBoltModelsProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEBulgeTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumEBulgeTypesProperty", [propertyName])
	def _validateAndSetEnumEBulgeTypesProperty(self, propertyName: str, value):
		return self._callFunction("validateAndSetEnumEBulgeTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getIntProperty(self, propertyName: str):
		return self._callFunction("getIntProperty", [propertyName])
	def _validateAndSetIntProperty(self, propertyName: str, value):
		return self._callFunction("validateAndSetIntProperty", [propertyName, value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumESecondaryBondLengthTypeProperty(self, propertyName: str):
		return self._callFunction("getEnumESecondaryBondLengthTypeProperty", [propertyName])
	def _validateAndSetEnumESecondaryBondLengthTypeProperty(self, propertyName: str, value):
		return self._callFunction("validateAndSetEnumESecondaryBondLengthTypeProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumELinerTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumELinerTypesProperty", [propertyName])
	def _validateAndSetEnumELinerTypesProperty(self, propertyName: str, value):
		return self._callFunction("validateAndSetEnumELinerTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEMaterialAnalysisTypesProperty(self, propertyName: str):
		return self._callFunction("getEnumEMaterialAnalysisTypesProperty", [propertyName])
	def _validateAndSetEnumEMaterialAnalysisTypesProperty(self, propertyName: str, value):
		return self._callFunction("validateAndSetEnumEMaterialAnalysisTypesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEGeometryChoiceProperty(self, propertyName: str):
		return self._callFunction("getEnumEGeometryChoiceProperty", [propertyName])
	def _validateAndSetEnumEGeometryChoiceProperty(self, propertyName: str, value):
		return self._callFunction("validateAndSetEnumEGeometryChoiceProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumELinerFormulationProperty(self, propertyName: str):
		return self._callFunction("getEnumELinerFormulationProperty", [propertyName])
	def _validateAndSetEnumELinerFormulationProperty(self, propertyName: str, value):
		return self._callFunction("validateAndSetEnumELinerFormulationProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumEStaticWaterModesProperty(self, propertyName: str):
		return self._callFunction("getEnumEStaticWaterModesProperty", [propertyName])
	def _validateAndSetEnumEStaticWaterModesProperty(self, propertyName: str, value):
		return self._callFunction("validateAndSetEnumEStaticWaterModesProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])