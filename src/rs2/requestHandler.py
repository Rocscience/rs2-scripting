from Server import requestQueue, responseQueue, objectStore
from responseFormat import functionResponse, functionStatus
from requestFormat import functionRequest
import logging

logging.basicConfig(filename='request_handler.log', filemode='w', format='%(process)d - %(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.level = logging.INFO

def handleRequest(interface_module):
    request = requestQueue.get()
    try:
        returnValue = callDesiredFunction(request, interface_module)
        response = createResponse(returnValue, request.keepReturnValueReference)                
        responseQueue.put(response)

    except AttributeError as e:
        logger.error(f"The function requested to be called does not exist. Full error: {e}")
        response = functionResponse(functionStatus.notFound, None, e)
        responseQueue.put(response)
    except Exception as e:
        logger.error(f"There was an exception thrown when trying to call the requested fucntion. Full error: {e}")
        response = functionResponse(functionStatus.failure, None, e)
        responseQueue.put(response)

def callDesiredFunction(request: functionRequest, interface_module):
    desiredFunction = None
    if request.objectID is None:
        desiredFunction = getattr(interface_module, request.functionName)
    else:
        desiredObject = objectStore[request.objectID]
        desiredFunction = getattr(desiredObject, request.functionName)

    for index in request.ProxyArgumentIndices:
        request.parameters[index] = objectStore[request.parameters[index]]

    return desiredFunction(*request.parameters)

def createResponse(returnValue, keepReturnValueReference):
    if keepReturnValueReference:
        objectID = id(returnValue)
        objectStore[objectID] = returnValue
        return functionResponse(functionStatus.success, objectID)
    else:
        return functionResponse(functionStatus.success, returnValue)
    