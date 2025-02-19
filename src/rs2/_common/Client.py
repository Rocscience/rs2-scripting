import warnings
from rsmessages.requestFormat import functionRequest
from rsmessages.responseFormat import functionResponse, functionStatus
from multiprocessing.connection import Client as multiProcessingClient

class Client:
	def __init__(self, host, port):
		self.compatibleProgramVersion = "11.026"
		self.connection = self.establishConnection(host, port)
		if self.connection == None:
			raise RuntimeError("Could not establish connection with the server. Make sure the server is started on the application.")
		
		versionCompatible = self.callFunction(functionRequest("checkVersion", [self.compatibleProgramVersion]))
		if not versionCompatible:
			self.connection.close()
			raise RuntimeError(f"""
					  Library version is not compatible with the program version. 
					  Please ensure the versions match by installing the correct version of the library or program. 
					  Library version: {self.compatibleProgramVersion} Program version: find in help->about.
					  """
					  )
 
	def establishConnection(self, host, port):
		try:
			connection = multiProcessingClient((host, port) ,'AF_INET')
		except Exception as e:
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

		if response.warnings:
			for warning in response.warnings:
				minimumUserStackDepth = 3 #assumes user will not call the client directly.
				warnings.warn(warning, UserWarning, stacklevel=minimumUserStackDepth)

		if response.status is not functionStatus.success:
			raise response.exception
		
		return response.value
	
	def closeConnection(self):
		if self.connection:
			self.connection.close()
			self.connection = None

	def __del__(self):
		self.closeConnection()