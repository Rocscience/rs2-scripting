from rs2.ProxyObject import ProxyObject

class DocumentProxy(ProxyObject):
	def rebuildAndPostProcessPiles(self):
		self._callFunction("rebuildAndPostProcessPiles", [])
