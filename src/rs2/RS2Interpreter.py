from rsmessages.requestFormat import functionRequest
from .Client import Client

class RS2Interpreter:
	def __init__(self):
		self.client = Client("RS2Interpreter")
	def doNothing(self):
		request = functionRequest('doNothing', [])
		return self.client.callFunction(request)