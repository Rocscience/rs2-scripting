class functionRequest:
    def __init__(self, functionName, parameters, objectID = None, keepReturnValueReference = False, proxyArgumentIndices = []):
        """
        functionName: Name of the function that should be called

        parameters: Arguments to pass to the function

        objectID (Optional): The identifier that indicates what object to call this function on. 
        If left as None, it is assumed the request is for a global function.

        keepReturnValueReference (optional): tells the program whether to keep a reference to the return value.
        this must be set to true for functions that return proxy objects so that the program keeps a 
        reference to the object on hand that the following requests can manipulate

        proxyArgumentIndices (optional): a list of indices into the 'parameters' argument that indicate which arguments are 
        Ids of proxy objects. This is used so that their corresponding objects can be retrieved on the other end before calling the function.
        """
        self.functionName = functionName
        self.parameters = parameters
        self.objectID = objectID
        self.keepReturnValueReference = keepReturnValueReference 
        self.ProxyArgumentIndices = proxyArgumentIndices
