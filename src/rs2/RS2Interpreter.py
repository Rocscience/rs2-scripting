from rsmessages.requestFormat import functionRequest
from .Client import Client

class RS2Interpreter:
	"""
	:ref:`Interpreter Example`
	"""
	def __init__(self, host = 'localhost', port=60055):
		self.client = Client(host, port)
	def doNothing(self):
		request = functionRequest('doNothing', [])
		return self.client.callFunction(request)