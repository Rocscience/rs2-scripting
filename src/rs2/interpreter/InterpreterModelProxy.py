from rs2._common.ProxyObject import ProxyObject
from rs2._common.documentProxy import DocumentProxy
from rs2.interpreter.InterpreterEnums import *
from rs2.interpreter.MeshResults import MeshResults
from rs2.interpreter.HistoryQueryResults import *
from rs2.interpreter.TimeQueryResults import *
from rs2.interpreter.InterpreterGraphEnums import *
from rs2.interpreter.JointResult import *
from rs2.interpreter.BeamResult import *
from rs2.interpreter.BoltResult import*
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
	
	def GetAllTimeQueryPointResults(self, stages: list[int], 
							  vertical_axis: TimeQueryGraphEnums.VerticalAxisTypes
							  ) -> dict[int, list[TimeQueryPointResults]]:
		"""
		Returns the results for all the time query points defined in the model for given stages and graph axes type.

		Args:
			vertical_axis (TimeQueryGraphEnums): Takes the vertical axis to generate results for.
			stages (int): Takes the stages by their stage number for which results should be returned.
		
		Returns:
			Returns a dictionary with key as stage number and value a list[TimeQueryPointResults] object.
			To extract the unique identifier, x-coordinate, y-coordinate, horizontal axis result and vertical axis result,
			please call the supported functions from the class:
			- TimeQueryPointResults.GetUniqueIdentifier()
			
			To get all the results for this query, please call:
			- TimeQueryPointResults.GetAllValues()
		
		The above method returns list[QueryPointResult] for each node. 
			To get the x-coordiante, y-coordinate, dynamic stage time or value, please call:
			- QueryPointResult.GetXCoordinate()
			- QueryPointResult.GetYCoordinate()
			- QueryPointResult.GetStageTime()
			- QueryPointResult.GetValue()
		
		Exceptions:
			ValueError: horizontal_axis and vertical_axis must be an enum of type TimeQueryGraphEnums.
						Any other value will raise an error.
		"""
		map_data = self._callFunction('GetAllTimeQueryPointsResults', 
							 [stages, vertical_axis.value])
		structured_data = {}
		for stageNumber, stageData in map_data.items():
			list_stage_data_as_classObj = []
			for query_point_data in stageData:
				entity_id, list_node_result = query_point_data
				unpack_list_data = [entity_id, list_node_result]
				list_stage_data_as_classObj.append(TimeQueryPointResults(*unpack_list_data))
			
			structured_data[stageNumber] = list_stage_data_as_classObj
		
		return structured_data

	def GetAllTimeQueryLinesResults(self, stages: list[int], 
							  vertical_axis: TimeQueryGraphEnums.VerticalAxisTypes,
							  apply_post_process_scaling: bool
							  ) -> dict[int, list[TimeQueryLineResults]]:
		"""
		Returns the results for all the time query lines defined in the model for given stages and graph axes types.

		Please note midpoints that cross over excavations at specific stages will not have data returned at those locations.

		Args:
			horizontal_axis (TimeQueryGraphEnums): Takes the horizontal axis to generate results for.
			vertical_axis (TimeQueryGraphEnums): Takes the vertical axis to generate results for.
			stages (int): Takes the stages by their stage number for which results should be returned.
			apply_post_process_scaling (bool): Bool input taking whether post-process scaling should be applied or not
		
		Returns:
			Returns a dictionary with key as stage number and value a list[TimeQueryLineResults] object.
			To extract the unique identifier, or list[QueryLineResult] representing all node objects for this query line,
			please call the supported functions from the class:
			- TimeQueryLineResults.GetUniqueIdentifier()
			- TimeQueryLineResults.GetAllNodeObjects()
			
			To get list[QueryPointResult] denoting all the node objects at a specific node of time query line, please call:
			- QueryLineResult.GetNodeValues()
		
			The above method returns list[QueryPointResult] representing all the values at this node of the time query line. 
			To get the x-coordiante, y-coordinate, dynamic stage time or value, please call:
			- QueryPointResult.GetXCoordinate()
			- QueryPointResult.GetYCoordinate()
			- QueryPointResult.GetStageTime()
			- QueryPointResult.GetValue()
		
		Exceptions:
			ValueError: horizontal_axis and vertical_axis must be an enum of type TimeQueryGraphEnums.
						Any other value will raise an error.
		"""
		map_data =  self._callFunction('GetAllTimeQueryLinesResults', 
							 [stages, vertical_axis.value, apply_post_process_scaling])
		structured_data = {}
		for stageNumber, stageData in map_data.items():
			list_stage_data_as_classObj = []
			for line_data in stageData:
				entity_id, list_line_node_data = line_data
				unpack_list_data = [entity_id, list_line_node_data]
				list_stage_data_as_classObj.append(TimeQueryLineResults(*unpack_list_data))
			
			structured_data[stageNumber] = list_stage_data_as_classObj
		
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

	
	def GetBoltYieldingResults (
		self, 
		stages: list[int]) -> dict[int, list[BoltElementYieldStatus]]:
		yeilded_indx = 4
		map_data = self._callFunction('GetBoltYieldingResults', [stages])
		structured_data = {}
		for stage_idx, stage_data in map_data.items():
			list_stage_data_as_classObj = []
			for result in stage_data:
				result[yeilded_indx] = BoltElementYieldStatus(result[yeilded_indx])
				list_stage_data_as_classObj.append(BoltYieldingResult(*result))
			
			structured_data[stage_idx] = list_stage_data_as_classObj
		
		return structured_data
		
	def GetBoltForceDisplacementResults (
		self, 
		stages: list[int]) -> dict[int, list[BoltForceDisplacementResult]]:
		map_data = self._callFunction('GetBoltForceDisplacementResults', [stages])
		structured_data = {}
		for stage_idx, stage_data in map_data.items():
			list_stage_data_as_classObj = []
			for result in stage_data:
				list_stage_data_as_classObj.append(BoltForceDisplacementResult(*result))
			
			structured_data[stage_idx] = list_stage_data_as_classObj
		
		return structured_data	