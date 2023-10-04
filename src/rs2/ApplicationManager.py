import subprocess
import time
from rs2.Client import Client

class ApplicationManager:
    minimumPort = 49152
    maximumPort = 65535
    def startApplication(self, pathToExecutable : str, port : int, timeout : float = None ):
        """
        Starts the application specified by pathToExecutable and starts the python server on the given port. 
        Returns when the server is ready to accept requests.
        Throws TimeoutError exception if the server is not ready within that time.

        Args:
            pathToExecutable: the full path to the executable of the application you want to start.
            port: the port number you want the python server to bind to.
            timeout: time in seconds before we stop trying to start the application
        
        Raises:
        	ValueError: Port range must be between 49152 and 65535, otherwise ValueError is raised
		    TimeoutError: if timeout is provided, raises TimeoutError if not able to connect to the server within that time.
        """
        if port < self.minimumPort | port > self.maximumPort:
            raise ValueError(f"port must be in the range {self.minimumPort} to {self.maximumPort}")
        
        p = subprocess.Popen([f"{pathToExecutable}", "-startpythonserver", f"{port}"], start_new_session = True, creationflags=subprocess.DETACHED_PROCESS)
        #continuously try to connect to the server and send a message. If it takes longer than timeout, throw a timeout exception
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
