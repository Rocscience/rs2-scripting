from rsmessages.requestFormat import functionRequest
from .Client import Client
from rs2.proxyObjects.ModelProxy import ModelProxy

class RS2Modeler:
	def __init__(self):
		self.client = Client("RS2Modeler")

	def openFile(self, fileName : str) -> ModelProxy:
		'''
		Takes in the absolute path to an rs2 file to be opened in the modeler.

		Typical Usage example:
		model = modeler.openFile('C:/simple_3_stage.fez')
		'''
		request = functionRequest('open_file', [fileName], keepReturnValueReference=True)
		modelObjectId = self.client.callFunction(request)
		modelProxy = ModelProxy(self.client, modelObjectId)
		return modelProxy
