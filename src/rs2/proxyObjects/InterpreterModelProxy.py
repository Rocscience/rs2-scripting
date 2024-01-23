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
	
	def ChangeModelStageReference(self, stageNumber: int):
		'''
		Change Model's stage by its stage number
		'''
		return self._callFunction('ChangeModelStageReference', [stageNumber])
	
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
	
	def GetMaterialQueryResults(self, stages: list[int]) -> dict[int, list[list[MaterialQueryResults]]]:
		"""
		Returns the results for all the material queries defined in the model.

		Returns:
			An object of type MaterialQueryResults. To extract the material-ID, x-coordinate, y-coordinate, distance, value or statistical analysis data from the result, 
			please call the any of the supported functions from the class:

			MaterialQueryResults.GetMaterialID(stage_number)
			MaterialQueryResults.GetXCoordinate(stage_number)
			MaterialQueryResults.GetYCoordinate(stage_number)
			MaterialQueryResults.GetDistance(stage_number)
			MaterialQueryResults.GetValue(stage_number)
			MaterialQueryResults.GetBaseStats(stage_number)
			MaterialQueryResults.GetMeanStats(stage_number)
			MaterialQueryResults.GetStandardDeviationStats(stage_number)
			MaterialQueryResults.GetCovarainceStats(stage_number)
				
		Typical Usage:
			results = model.GetMaterialQueryResults([1, 2])
			material_id = results.GetMaterialID(1)
			x_coordiante = results.GetXCoordinate(1)
			y_coordinate = results.GetYCoordinate(1)
			distance = results.GetDistance(1)
			value = results.GetValue(1)
		
		"""
		map_data = self._callFunction('GetMaterialQueryResults', [stages])
		map_material_query_data = {}
		for stage_number, list_stage_queries_data in map_data.items():
			list_stage_mat_queries = []
			for mat_query_data in list_stage_queries_data:
				# This list corresponds to the data at each vertex of material query for a given stage number in iteration
				list_all_node_query_data_as_classObjects = []
				for node_value_tuple in mat_query_data:
					mat_id = node_value_tuple[0]
					x, y, distance, value = node_value_tuple[1][0], node_value_tuple[1][1], node_value_tuple[1][2], node_value_tuple[1][3]
					statistical_data = node_value_tuple[2]
					list_all_node_query_data_as_classObjects.append(MaterialQueryResults(mat_id, x, y, distance, value, statistical_data))
				# Add this list of node results for the specific 'mat_query_data' in iteration
				list_stage_mat_queries.append(list_all_node_query_data_as_classObjects)
			
			map_material_query_data[stage_number] = list_stage_mat_queries
		
		return map_material_query_data

	
	