from rs2._common.ProxyObject import ProxyObject

class DocumentProxy(ProxyObject):
	def rebuildAndPostProcessPiles(self):
		self._callFunction("rebuildAndPostProcessPiles", [])
