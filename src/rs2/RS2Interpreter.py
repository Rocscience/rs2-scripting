from rsmessages.requestFormat import functionRequest
from .Client import Client
from rs2.ApplicationManager import ApplicationManager
from rs2.proxyObjects.InterpreterModelProxy import ModelProxy
import winreg

class RS2Interpreter:
	"""
	:ref:`Interpreter Example`
	"""
	def __init__(self, host = 'localhost', port=60055):
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
	
	def doNothing(self):
		request = functionRequest('doNothing', [])
		return self.client.callFunction(request)
	
	@classmethod
	def startApplication(cls, port : int, overridePathToExecutable : str = None, timeout : float = 30) -> None:
		"""Opens the most recently installed RS2 application. Starts the python server and binds it to the given port.

		Args:
			port (int): the port to bind the python server to. Use this same port when initializing RS2Modeler
			overridePathToExecutable (str, optional): full path to the desired executable to be opened. If not provided, the latest installation of rs2 is used
			timeout (float, optional): the maximum amount of time to wait for the application and server to start.
		
		Raises:
			ValueError: Port range must be between 49152 and 65535, otherwise ValueError is raised
			TimeoutError: if timeout is provided, raises TimeoutError if not able to connect to the server within that time.
		"""
		appManager = ApplicationManager()
		executablePath = overridePathToExecutable if overridePathToExecutable else cls._getApplicationPath()
		appManager.startApplication(executablePath, port, timeout)

	@staticmethod
	def _getApplicationPath() -> str:

		registry = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
		key = winreg.OpenKey(registry, r'SOFTWARE\Rocscience\RS2 11.0')
		installationLocation, type = winreg.QueryValueEx(key, "Install")

		rs2ModelerInstallLocation =  rf"{installationLocation}\Interpret"

		return rs2ModelerInstallLocation