from rs2.ProxyObject import ProxyObject
from rs2.proxyObjects.documentProxy import DocumentProxy
from rs2.proxyObjects.BoltPropertyProxy import BoltProperty
from rs2.proxyObjects.LinerPropertyProxy import LinerProperty

class ModelProxy(ProxyObject):

	def __init__(self, client, ID):
		super().__init__(client, ID)
		self._documentProxy = self._getDocument()

	def _getDocument(self):
		documentObjectID = self._callFunction('getDocument', [], keepReturnValueReference=True)
		return DocumentProxy(self._client, documentObjectID)
    
	def getBoltPropertyByName(self, boltName : str) -> BoltProperty:

		'''
		Returns a Bolt Property object based on its name.
		'''

		boltObjectID = self._callFunction('getBoltPropertyByName', [boltName], keepReturnValueReference=True)
		return BoltProperty(self._client, boltObjectID, self._documentProxy._ID)
    
	def getLinerPropertyByName(self, linerName : str) -> LinerProperty:
		'''
		Returns a Liner Property object based on its name.
		'''
		linerObjectID = self._callFunction('getLinerPropertyByName', [linerName], keepReturnValueReference=True)
		return LinerProperty(self._client, linerObjectID, self._documentProxy._ID)
	
	def getAllBoltProperties(self) -> list[BoltProperty]:

		'''
		Returns a list of all Bolt Property objects
		'''
		activeBoltProperties = []
		boltObjectIDList = self._callFunction('getAllBoltProperties', [], keepReturnValueReference=True)
		for boltObjectID in boltObjectIDList:
			activeBoltProperties.append(BoltProperty(self._client, boltObjectID, self._documentProxy._ID))
		return activeBoltProperties

	def getAllLinerProperties(self) -> list[LinerProperty]:
		'''
		Returns a list of all Liner Property objects
		'''
		activeLinerProperties = []
		linerObjectIDList = self._callFunction('getAllLinerProperties', [], keepReturnValueReference=True)
		for linerObjectID in linerObjectIDList:
			activeLinerProperties.append(LinerProperty(self._client, linerObjectID, self._documentProxy._ID))
		return activeLinerProperties
	
	def saveAndCompute(self, ignoreBernoulliLinerWarning = False, ignoreDynamicBCWarning = False):
		'''
		Saves the file and then Runs compute.

		ignoreBernoulliLinerWarning and ignoreDynamicBCWarning are optional flags to bypass warnings. Only use them if you know what you are doing!
		'''
		return self._callFunction('saveAndCompute', [False, ignoreBernoulliLinerWarning, ignoreDynamicBCWarning])
	
	def saveAndComputeGroundWater(self, ignoreBernoulliLinerWarning = False, ignoreDynamicBCWarning = False):
		'''
		Saves the file and then Runs groundwater compute.

		ignoreBernoulliLinerWarning and ignoreDynamicBCWarning are optional flags to bypass warnings. Only use them if you know what you are doing!
		'''
		return self._callFunction('saveAndCompute', [True, ignoreBernoulliLinerWarning, ignoreDynamicBCWarning])

	def close(self):
		'''
		Closes the model
		'''
		return self._callFunction('close', [])

	def saveAs(self, fileName : str):
		'''
		Saves the model using the given file name.

		Typical usage example:
		model.saveAs('C:/simple_3_stage.fez')
		'''
		return self._callFunction('saveAs', [fileName])

	def save(self):
		'''
		Saves the model
		'''
		return self._callFunction('save', [])

