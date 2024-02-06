from rs2.ProxyObject import ProxyObject
from rs2.proxyObjects.documentProxy import DocumentProxy
from rs2.InterpreterEnums import *
from rs2.MeshResults import MeshResults
from rs2.MaterialQueryResults import MaterialQueryResults
from rs2.HistoryQueryResults import HistoryQueryResult
from rs2.InterpreterGraphEnums import *
from rs2.JointResult import *
from rs2.BeamResult import *
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

	def AddMaterialQuery(self, points: list[list[float]]) -> str:
		"""
		Adds a material query point/line to your model using the specified coordinates in order.

		Returns:
			A unique identifier for the newly added material query point/line.
		
		"""
		return self._callFunction('AddMaterialQuery', [points])
	
	def RemoveMaterialQuery(self, IDs_toRemove: list[str]) -> str:
		"""
		Removes material query points or lines for provided list of IDs.
		
		"""
		return self._callFunction('RemoveMaterialQuery', [IDs_toRemove])
	
	def GetMaterialQueryResults(self) -> list[list[MaterialQueryResults]]:
		"""
		Returns the results for all the material queries defined in the model for active model stage and result type.
		To get results for a different stage, please call SetActiveStage(int stageNumber) before calling this function.
		To get results for a different result type, please call either before calling this function:
		- SetResultType(InterpreterGraphEnums resultType)
		- SetUserDefinedResultType("Your defined resultType name")

		Please note that results for points that fall outside the model mesh boundary are not returned.

		Returns: 
			A list[list[MaterialQueryResults]] of query results. The first inner list represents the results for all queries.
			The second inner list represents the data for points which make up a single material query.
			To extract the material-ID, x-coordinate, y-coordinate, distance, or value from the specific material query node object,
			please call any of the supported functions from the class:
			- MaterialQueryResults.GetUniqueIdentifier()
			- MaterialQueryResults.GetMaterialID()
			- MaterialQueryResults.GetXCoordinate()
			- MaterialQueryResults.GetYCoordinate()
			- MaterialQueryResults.GetDistance()
			- MaterialQueryResults.GetValue()

		"""
		all_material_query_data = self._callFunction('GetMaterialQueryResults', [])
		all_mat_query_data_as_classObj = []
		for mat_query_data in all_material_query_data:
			# This list corresponds to the data at each vertex of material query in iteration
			singleQueryValuesObject = []
			for node_value_tuple in mat_query_data:
				entity_id, material_id, list_query_data = node_value_tuple
				unpack_list_data = [entity_id, material_id, *list_query_data]
				singleQueryValuesObject.append(MaterialQueryResults(*unpack_list_data))
			# Add the data for this material query in final list
			all_mat_query_data_as_classObj.append(singleQueryValuesObject)
		
		return all_mat_query_data_as_classObj

	
	def GetHistoryQueryResults(self, hq_name: str, horizontal_axis: HistoryQueryGraphEnums.HorizontalAxisTypes, vertical_axis: HistoryQueryGraphEnums.VerticalAxisTypes, 
							stages: list[int]) -> dict[int, list[HistoryQueryResult]]:
		"""
		Returns the history query result for the provided query name with specified graph options and stages.

		Args:
			hq_name (str): Takes the name of the History Query Point.
			horizontal_axis (HistoryQueryGraphEnums): Takes the horizontal axis to generate results for.
			vertical_axis (HistoryQueryGraphEnums): Takes the vertical axis to generate results for.
			stages (int): Takes the stages by their stage number for which results should be returned.
		
		Returns:
			Returns a dictionary with key as stage number and value a List of HistoryQueryResult object.
			To extract the stage number, x-coordinate, y-coordinate, horizontal axis result and vertical axis result,
			please call the supported functions from the class:
			- HistoryQueryResult.GetXCoordinate()
			- HistoryQueryResult.GetYCoordinate()
			- HistoryQueryResult.GetHorizontalAxisResult()
			- HistoryQueryResult.GetVerticalAxisResult()
		
		Typical Usage:
			results = model.GetHistoryQueryResults(params)
			results_for_stage_1 = results[1]
			x_coordiante = results_for_stage_1[0].GetXCoordinate()
			y_coordinate = results_for_stage_1[0].GetYCoordinate()
			horizontal_result = results_for_stage_1[0].GetHorizontalResult()
			vertical_result = results_for_stage_1[0].GetVerticalResult()
		
		Exceptions:
			ValueError: horizontal_axis and vertical_axis must be an enum of type HistoryQueryGraphEnums.
						Any other value will raise an error.
		"""
		map_data = self._callFunction('GetHistoryQueryResults', [hq_name, horizontal_axis.value, vertical_axis.value, stages])
		structured_data = {}
		for stage_idx, stage_data in map_data.items():
			list_stage_data_as_classObj = []
			for result in stage_data:
				list_stage_data_as_classObj.append(HistoryQueryResult(result[0], result[1], result[2], result[3]))
			
			structured_data[stage_idx] = list_stage_data_as_classObj
		
		return structured_data
		
		
	
	def GetJointResults(
		self, 
		stages: list[int]) -> dict[int, list[JointResult]]:
		yeilded_indx = 10
		map_data = self._callFunction('GetJointResults', [stages])
		structured_data = {}
		for stage_idx, stage_data in map_data.items():
			list_stage_data_as_classObj = []
			for result in stage_data:
				result[yeilded_indx] = bool(result[yeilded_indx])
				list_stage_data_as_classObj.append(JointResult(*result))
			
			structured_data[stage_idx] = list_stage_data_as_classObj
		
		return structured_data

	def GetBeamResults(
		self, 
		stages: list[int]) -> dict[int, list[BeamResult]]:

		composite_layer_indx = 0
		node_id_start_indx = 1
		node_id_end_indx = 2
		liner_yeilded_indx = 18
		composite_level = 19
		composite_yeilded_indx = 24

		map_data = self._callFunction('GetBeamResults', [stages])
		structured_data = {}
		for stage_idx, stage_data in map_data.items():
			list_stage_data_as_classObj = []
			for result in stage_data:

				result[composite_layer_indx] = int(result[composite_layer_indx])
				result[node_id_start_indx] = int(result[node_id_start_indx])
				result[node_id_end_indx] = int(result[node_id_end_indx])
				result[composite_level] = int(result[composite_level])

				result[liner_yeilded_indx] = bool(result[liner_yeilded_indx])
				result[composite_yeilded_indx] = bool(result[composite_yeilded_indx])


				list_stage_data_as_classObj.append(BeamResult(*result))
			
			structured_data[stage_idx] = list_stage_data_as_classObj
		
		return structured_data