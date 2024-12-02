from rsmessages.requestFormat import functionRequest
from rs2._common.Client import Client
from rs2.modeler.Model import Model
from rs2.utilities.ApplicationManager import ApplicationManager
import winreg
import time

class RS2Modeler:
	"""
	:ref:`Modeler Example`
	"""
	def __init__(self, host='localhost', port=60054):
		self.client = Client(host, port)

	def openFile(self, fileName : str) -> Model:
		'''
		Takes in the absolute path to an rs2 file to be opened in the modeler.

		Examples:
			.. code-block:: python

				model = modeler.openFile('C:/simple_3_stage.fez')
		'''
		request = functionRequest('open_file', [fileName], keepReturnValueReference=True)
		modelObjectId = self.client.callFunction(request)
		model = Model(self.client, modelObjectId)
		return model

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

		rs2ModelerInstallLocation =  rf"{installationLocation}\RS2"

		return rs2ModelerInstallLocation
	
	def closeProgram(self, saveModels=True, timeout=30):
		'''
		Closes the modeler program. All unsaved models are saved by default.

		Examples:
			.. code-block:: python

				#saves all models before closing
				modeler.closeProgram(True)

				#closes the program without saving
				modeler.closeProgram(False)
		'''
		request = functionRequest('closeProgram', [saveModels])
		portUsed = self.client.callFunction(request)
		self.client.closeConnection()
		appManager = ApplicationManager()
		portIsAvailable = False
		startTime = time.time()
		while not portIsAvailable:
			if (time.time() - startTime) > timeout:
				raise TimeoutError("The application did not close within the given timeout time.")
			portIsAvailable = appManager._isPortAvailable(portUsed)