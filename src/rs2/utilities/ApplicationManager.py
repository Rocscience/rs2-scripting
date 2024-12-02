import subprocess
import time
from rs2._common.Client import Client
from multiprocessing.connection import Listener

class ApplicationManager:

    minimumPort = 49152
    maximumPort = 65535
    defaultTimeout = 30
    def startApplication(self, pathToExecutable : str, port : int, timeout : float = defaultTimeout ):
        """
        Starts the application specified by pathToExecutable and starts the python server on the given port. 
        Returns when the server is ready to accept requests.
        Throws TimeoutError exception if the server is not ready within that time.

        Parameters:
            pathToExecutable (str): the full path to the executable of the application you want to start.  
            port (int): the port number you want the python server to bind to.
                
                * minimumPort = 49152
                * maximumPort = 65535           
            timeout (int): time in seconds before we stop trying to start the application 
                
                * defaultTimeout = 30
        
        Raises:
        	ValueError: Port range must be between 49152 and 65535, otherwise ValueError is raised
		    TimeoutError: if timeout is provided, raises TimeoutError if not able to connect to the server within that time.
        """
        if port < self.minimumPort or port > self.maximumPort:
            raise ValueError(f"port must be in the range {self.minimumPort} to {self.maximumPort}")
        
        if not self._isPortAvailable(port):
            raise RuntimeError(f"port number {port} is occupied. Please choose another port.")

        subprocess.Popen([f"{pathToExecutable}", "-startpythonserver", f"{port}"], start_new_session = True, creationflags=subprocess.DETACHED_PROCESS)

        self._tryToConnectToServer(port, timeout)
       

    def _isPortAvailable(self, port):
        portAvailable = False
        listener = None
        try:
            listener = Listener(('localhost', port), 'AF_INET')
            portAvailable = True
        except Exception:
            portAvailable = False
        
        if listener:
            listener.close()

        return portAvailable

    def _tryToConnectToServer(self, port, timeout):

        startTime = time.time()
        serverIsRunning = False

        while not serverIsRunning:
            if timeout:
                if (time.time() - startTime) > timeout:
                    raise TimeoutError("The application did not start within the given timeout time.")
            try:
                client = Client("localhost", port)
                client.closeConnection()
            except Exception as e:
                continue
            serverIsRunning = True