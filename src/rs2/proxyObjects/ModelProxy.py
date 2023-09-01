from rs2.ProxyObject import ProxyObject
from rs2.proxyObjects.documentProxy import DocumentProxy
from rs2.proxyObjects.BoltPropertyProxy import BoltProperty
from rs2.proxyObjects.LinerPropertyProxy import LinerProperty
from rs2.proxyObjects.JointPropertyProxy import JointProperty

class ModelProxy(ProxyObject):
	"""
	:ref:`Model Example`
	"""
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
	
	def getJointPropertyByName(self, jointName : str) -> JointProperty:
		'''
		Returns a Joint Property object based on its name.
		'''
		jointObjectID = self._callFunction('getJointPropertyByName', [jointName], keepReturnValueReference=True)
		return JointProperty(self._client, jointObjectID, self._documentProxy._ID)
	
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
	
	def getAllJointProperties(self) -> list[JointProperty]:
		'''
		Returns a list of all Joint Property objects
		'''
		activeJointProperties = []
		jointObjectIDList = self._callFunction('getAllJointProperties', [], keepReturnValueReference=True)
		for jointObjectID in jointObjectIDList:
			activeJointProperties.append(JointProperty(self._client, jointObjectID, self._documentProxy._ID))
		return activeJointProperties
	
	def compute(self):
		'''
		Saves the file if modified and then runs compute. Replaces any existing results.
		'''
		return self._callFunction('compute', [False])

	def computeGroundWater(self):
		'''
		Saves the file if modified and then runs groundwater compute. Replaces any existing results.
		'''
		return self._callFunction('compute', [True])

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

