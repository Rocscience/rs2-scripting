from . import Client
from rsmessages.requestFormat import functionRequest

class ProxyObject:
	def __init__(self, client : Client.Client, ID):
		self._client = client
		self._ID = ID

	def _callFunction(self, functionName, parameters = [], keepReturnValueReference = False, proxyArgumentIndices = []):
		request = functionRequest(functionName, parameters, self._ID, keepReturnValueReference, proxyArgumentIndices)
		return self._client.callFunction(request)

