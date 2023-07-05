from ProxyObject import ProxyObject
from enum import Enum
import Client
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
	def _getEnumEBulgeTypeProperty(self, propertyName: str):
		return self._callFunction("getEnumEBulgeTypeProperty", [propertyName])
	def _validateAndSetEnumEBulgeTypeProperty(self, propertyName: str, value):
		return self._callFunction("validateAndSetEnumEBulgeTypeProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getIntProperty(self, propertyName: str):
		return self._callFunction("getIntProperty", [propertyName])
	def _validateAndSetIntProperty(self, propertyName: str, value):
		return self._callFunction("validateAndSetIntProperty", [propertyName, value, self.documentProxyID], proxyArgumentIndices=[2])
	def _getEnumESecondaryBondLengthTypeProperty(self, propertyName: str):
		return self._callFunction("getEnumESecondaryBondLengthTypeProperty", [propertyName])
	def _validateAndSetEnumESecondaryBondLengthTypeProperty(self, propertyName: str, value):
		return self._callFunction("validateAndSetEnumESecondaryBondLengthTypeProperty", [propertyName, value.value, self.documentProxyID], proxyArgumentIndices=[2])
