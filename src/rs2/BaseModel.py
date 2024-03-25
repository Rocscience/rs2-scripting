from rs2._common.ProxyObject import ProxyObject
from rs2._common.documentProxy import DocumentProxy
from rs2 import Units
class BaseModel(ProxyObject):

	def __init__(self, client, ID):
		super().__init__(client, ID)
		self._documentProxy = self._getDocument()

	def _getDocument(self):
		documentObjectID = self._callFunction('getDocument', [], keepReturnValueReference=True)
		return DocumentProxy(self._client, documentObjectID)
	
	def _enforceFeaFezEnding(self, path: str):
		if not (path.endswith('.fea') or path.endswith('.fez')):
			raise ValueError('Path must end with .fea or .fez')
		
	def close(self):
		'''
		:ref:`Model Example`

		|  Closes the model
		
		'''
		return self._callFunction('close', [])
	
	def save(self):
		'''
		:ref:`Model Example`

		|  Saves the model

		'''
		return self._callFunction('save', [])
	
	def getUnits(self):
		'''
		:ref:`Get Model Units Example`

		|  Get Solid, Hydro and Thermal units for your model
		'''
		NUM_UNITS = 3
		data = self._callFunction('getUnits', [])
		if (len (data) !=NUM_UNITS) :
			assert False, "Expected 3 units, got " + str(len(data))
		return Units(*data)
