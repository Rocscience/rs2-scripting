from rs2.ProxyObject import ProxyObject
from rs2.proxyObjects.documentProxy import DocumentProxy
from rs2.InterpreterEnums import *
from rs2.MeshResults import MeshResults
from rs2.MaterialQueryResults import MaterialQueryResults

class ModelProxy(ProxyObject):
	"""
	:ref:`Model Example`
	"""
	def __init__(self, client, ID):
		super().__init__(client, ID)
		self._documentProxy = self._getDocument()

	def _getDocument(self):
		documentObjectID = self._callFunction('getDocument', [], keepReturnValueReference=True)
		return DocumentProxy(self._client, documentObjectID)

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
	
	def SetActiveStage(self, stageNumber: int):
		'''
		Change Model's stage by its stage number
		'''
		return self._callFunction('SetActiveStage', [stageNumber])
	
	def SetResultType(self, resultType: ExportResultType) -> list[dict]:
		"""
		Sets the export result type for the model.

		Args:
			resultType (ExportResultType): Takes an enum of type ExportResultType representing the desired
			export option for mesh results.
		
		Exceptions:
			ValueError: resultType must be an enum of type ExportResultType. Any other value will raise an error
		
		"""
		return self._callFunction('SetResultType', [resultType.value])
	
	def SetUserDefinedResultType(self, resultName: str) -> list[dict]:
		"""
		Sets the export result type to the user defined result type name.

		Args:
			resultName (str): Takes the name of the user defined export option to generate mesh results for.
		
		"""
		return self._callFunction('SetUserDefinedResultType', [resultName])
	
	def GetMeshResults(self) -> MeshResults:
		"""
		Returns the mesh results at all nodes of the model.

		Returns:
			An object of type MeshResults. To extract the x-coordinate, y-coordinate or value from the returned data, 
			please call the supported functions from the class:
			MeshResults.GetXCoordinate(index)
			MeshResults.GetYCoordinate(index)
			MeshResults.GetValue(index)
				
		Typical Usage:
			results = model.GetMeshResults()
			x_coordiante = results.GetXCoordinate(0)
			y_coordinate = results.GetYCoordinate(0)
			value = results.GetValue(0)
		
		"""
		results = self._callFunction('GetMeshResults', [])
		return MeshResults(results)

	def AddMaterialQueryPoint(self, x: float, y: float) -> str:
		"""
		Adds a material query point to your model at the specified coordinates.

		Returns:
			A unique identifier for the newly added material query point.
		
		"""
		return self._callFunction('AddMaterialQueryPoint', [x, y])

	def AddMaterialQueryLine(self, points: list[list[float]]) -> str:
		"""
		Adds a material query line to your model using the specified coordinates in order.

		Returns:
			A unique identifier for the newly added material query line.
		
		"""
		return self._callFunction('AddMaterialQueryLine', [points])
	
	def RemoveMaterialQuery(self, guid: str) -> str:
		"""
		Removes a material query point or line from your model by ID.
		
		"""
		return self._callFunction('RemoveMaterialQuery', [guid])
	
	def GetMaterialQueryResults(self) -> list[list[MaterialQueryResults]]:
		"""
		Returns the results for all the material queries defined in the model for active model stage and result type.
		To get results for a different stage of your model, please call SetActiveStage(int stageNumber) first.
		To get results for a different result type, please call either of before getting results:
			- SetResultType(InterpreterGraphEnums)
			- SetUserDefinedResultType("Your custom resultType name")
		
		Please note that results for points that fall outside the model mesh boundary is not returned.

		Returns:
			A list[list[MaterialQueryResults]] of query results. The first inner list represents to results for all queries. 
			The second inner list represents the data for points which make up a single material query.
			To extract the material-ID, x-coordinate, y-coordinate, distance, or value from the specific material query node object, 
			please call the any of the supported functions from the class:

			MaterialQueryResults.GetMaterialID()
			MaterialQueryResults.GetXCoordinate()
			MaterialQueryResults.GetYCoordinate()
			MaterialQueryResults.GetDistance()
			MaterialQueryResults.GetValue()
		
		"""
		all_material_query_data = self._callFunction('GetMaterialQueryResults', [])
		all_mat_query_data_as_classObj = []
		for mat_query_data in all_material_query_data:
			# This list corresponds to the data at each vertex of material query in iteration
			singleQueryValuesObject = []
			for node_value_tuple in mat_query_data:
				material_id, list_query_data = node_value_tuple
				unpack_list_data = [material_id, *list_query_data]
				singleQueryValuesObject.append(MaterialQueryResults(*unpack_list_data))
			# Add the data for this material query in final list
			all_mat_query_data_as_classObj.append(singleQueryValuesObject)
		
		return all_mat_query_data_as_classObj

	
	