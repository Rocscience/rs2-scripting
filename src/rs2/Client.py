import logging
from rsmessages.requestFormat import functionRequest
from rsmessages.responseFormat import functionResponse, functionStatus
from multiprocessing.connection import Client as multiProcessingClient


logging.basicConfig(filename='python_client.log', filemode='w', format='%(process)d - %(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.level = logging.INFO


class Client:
	def __init__(self, pipeName):
		self.connection = self.establishConnection(pipeName)

	def establishConnection(self, pipeName):
		try:
			connection = multiProcessingClient(Rf'\\.\pipe\{pipeName}','AF_PIPE')
		except Exception as e:
			logger.error(f"Unable to create client. Full error: {e}")
			return
		return connection
	
	def send(self, request : functionRequest):
		if not self.connection:
			print('Unable to send request. Connection to the modeler was not established.')
			return
		try:
			self.connection.send(request)
		except ValueError as e:
			print(f'Unable to send request. Argument might be too large. Full error: {e}')

	def receive(self) -> functionResponse:
		try:
			response = self.connection.recv()
			return response
		except EOFError as e:
			print('Unable to receive request as there is nothing left to receive and the other end was closed.')
			return None

	def callFunction(self, functionRequest : functionRequest):
		self.send(functionRequest)
		response = self.receive()

		if response.status is not functionStatus.success:
			raise response.exception
		return response.value