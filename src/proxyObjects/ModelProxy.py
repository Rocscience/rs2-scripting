from ProxyObject import ProxyObject
from proxyObjects.documentProxy import DocumentProxy
from proxyObjects.BoltPropertyProxy import BoltProperty

class ModelProxy(ProxyObject):

    def __init__(self, client, ID):
        super().__init__(client, ID)
        self._documentProxy = self._getDocument()

    def _getDocument(self):
        documentObjectID = self._callFunction('getDocument', [], keepReturnValueReference=True)
        return DocumentProxy(self._client, documentObjectID)

    def getFirstBolt(self) -> BoltProperty:
        boltObjectID = self._callFunction('getFirstBolt', [], keepReturnValueReference=True)
        return BoltProperty(self._client, boltObjectID, self._documentProxy._ID)
    
    def saveAndCompute(self, ignoreBernoulliLinerWarning = False, ignoreDynamicBCWarning = False):
        '''
        Saves the file and then Runs compute.

        ignoreBernoulliLinerWarning and ignoreDynamicBCWarning are optional flags to bypass warnings. Only use them if you know what you are doing!
        '''
        return self._callFunction('saveAndCompute', [False, ignoreBernoulliLinerWarning, ignoreDynamicBCWarning])

    def close(self):
        '''
        Closes the model
        '''
        return self._callFunction('close', [])

    def saveAs(self, fileName : str):
        '''
        Saves the model using the given file name.

        Typical usage example:
        model.saveAs('C:/simple_3_stage.fez')
        '''
        return self._callFunction('saveAs', [fileName])

    def save(self):
        '''
        Saves the model
        '''
        return self._callFunction('save', [])

