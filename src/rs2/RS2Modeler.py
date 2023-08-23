from rsmessages.requestFormat import functionRequest
from .Client import Client
from rs2.proxyObjects.ModelProxy import ModelProxy

class RS2Modeler:
	def __init__(self, host='localhost', port=60054):
		self.client = Client(host, port)

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
