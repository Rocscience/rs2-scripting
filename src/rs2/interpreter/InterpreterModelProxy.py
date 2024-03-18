from rs2._common.ProxyObject import ProxyObject
from rs2._common.documentProxy import DocumentProxy
from rs2._common.Units import Units
from rs2.interpreter.InterpreterEnums import *
from rs2.interpreter.MeshResults import MeshResults
from rs2.interpreter.HistoryQueryResults import *
from rs2.interpreter.TimeQueryResults import *
from rs2.interpreter.InterpreterGraphEnums import *
from rs2.interpreter.JointResult import *
from rs2.interpreter.LinerResult import *
from rs2.interpreter.BoltResult import*
from rs2.interpreter.CompositeResult import*
from rs2.interpreter.MaterialQueryResults import *
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

	def saveCopyAs(self, fileName : str):
		'''
		Saves the model using the given file name.

		Example:

		.. code-block:: python
			
			model.saveCopyAs('C:/simple_3_stage.fez')
		'''
		formattedFileName = fileName.replace('/', '\\')
		return self._callFunction('saveAs', [formattedFileName])

	def save(self):
		'''
		Saves the model
		'''
		return self._callFunction('save', [])
	
	def SetActiveStage(self, stageNumber: int):
		'''
		Change model's active stage by its stage number
		'''
		return self._callFunction('SetActiveStage', [stageNumber])
	
	def SetResultType(self, resultType: ExportResultType) -> list[dict]:
		"""
		Sets the export result type for the model.

		Args:
			resultType (ExportResultType): Takes an enum of type ExportResultType representing the desired
			export option for mesh results.
		
		Raises:
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
				
		Example:

		.. code-block:: python

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
		
		Example:

		.. code-block:: python
		
			results = model.GetHistoryQueryResults(params)
			results_for_stage_1 = results[1]
			x_coordiante = results_for_stage_1[0].GetXCoordinate()
			y_coordinate = results_for_stage_1[0].GetYCoordinate()
			horizontal_result = results_for_stage_1[0].GetHorizontalResult()
			vertical_result = results_for_stage_1[0].GetVerticalResult()
		
		Raises:
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

		Please note points that are over an excavation at specific stages will not have data returned at those locations.

		Args:
			stages (list[int]): Takes the stages by their stage number for which results should be returned.
			vertical_axis (TimeQueryGraphEnums): Takes the vertical axis to generate results for.
		
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
		
		Raises:
			ValueError: vertical_axis must be an enum of type TimeQueryGraphEnums. Any other value will raise an error.
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

		Please note points that are over an excavation at specific stages will not have data returned at those locations.

		Args:
			stages (list[int]): Takes the stages by their stage number for which results should be returned.
			vertical_axis (TimeQueryGraphEnums): Takes the vertical axis to generate results for.
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
		
		Raises:
			ValueError: vertical_axis must be an enum of type TimeQueryGraphEnums. Any other value will raise an error.
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
	
	def GetMaterialQueryResults(self) -> list[MaterialQueryResults]:
		"""
		Returns the results for all the material queries defined in the model for active model stage and result type.
		To get results for a different stage, please call SetActiveStage(int stageNumber) before calling this function.
		To get results for a different result type, please call either before calling this function:
		- SetResultType(InterpreterGraphEnums resultType)
		- SetUserDefinedResultType("Your defined resultType name")

		Returns: 
			A list[MaterialQueryResults] of query results.
			To extract the Unique Identifier, Material ID for a specific material query object,
			please call any of the supported functions from the class:
			- MaterialQueryResults.GetUniqueIdentifier()
			- MaterialQueryResults.GetMaterialID()
			
			To get all the results for this query, please call:
			- MaterialQueryResults.GetAllValues()

			The above method returns list[QueryResult] for each result. 
			To get the x-coordiante, y-coordinate, distance or value, please call:
			- QueryResult.GetXCoordinate()
			- QueryResult.GetYCoordinate()
			- QueryResult.GetDistance()
			- QueryResult.GetValue()

		"""
		all_material_query_data = self._callFunction('GetMaterialQueryResults', [])
		all_mat_query_data_as_classObj = []
		for mat_query_data in all_material_query_data:
			# This list corresponds to the data at each vertex of material query in iteration
			entity_id, material_id, list_query_data = mat_query_data
			unpack_list_data = [entity_id, material_id, list_query_data]
			all_mat_query_data_as_classObj.append(MaterialQueryResults(*unpack_list_data))
		return all_mat_query_data_as_classObj

	
		

	def GetBoltResults (
		self, 
		stages: list[int]) -> dict[int, list[BoltResult]]:
		map_data = self._callFunction('GetBoltResults', [stages])
		structured_data = {}
		for stage_idx, stage_data in map_data.items():
			structured_data[stage_idx] = []
			for entity_name, entity_data in stage_data.items():
				yielding_results = []
				displacement_force_results = []
				# location # [start = [x,y],end = [x,y]]
				# yeilding
				# displacement force
				if len(entity_data) < 3 or len(entity_data[0]) <1 or len(entity_data[0][0]) < 4:
					continue

				for yeilding_vector in entity_data[1]:
					yielding = BoltYieldingResult(*yeilding_vector)
					yielding_results.append(yielding)

				for displacement_force_vector in entity_data[2]:
					displacement_force = BoltForceDisplacementResult(*displacement_force_vector)
					displacement_force_results.append(displacement_force)
				bolt_result = BoltResult(entity_name,entity_data,yielding_results, displacement_force_results)
				structured_data[stage_idx].append(bolt_result)
		return structured_data
		
	def process_joint_data(self, entity_data, entity_name):

		joint_element_results = []
		for joint_vector in entity_data[1]:
			#joint_vector[yeilded_indx] = bool(joint_vector[yeilded_indx])
			joint_element = JointElementResult(*joint_vector)
			joint_element_results.append(joint_element)
		joint_result = JointResult(entity_name, joint_element_results)
		return joint_result

	def process_liner_data(self, entity_data, entity_name):
		liner_element_results = []

		for liner_vector in entity_data[0]:
			liner_element = LinerElementResult(*liner_vector)
			liner_element_results.append(liner_element)
		liner_result = LinerResult(entity_name,liner_element_results)
		return liner_result

	def GetJointResults(
		self, 
		stages: list[int]) -> dict[int, list[JointResult]]:

		map_data = self._callFunction('GetJointResults', [stages])
		structured_data = {}
		for stage_idx, stage_data in map_data.items():

			structured_data[stage_idx] = []
			for entity_name, entity_data in stage_data.items():
				joint_result = self.process_joint_data(entity_data, entity_name)
				structured_data[stage_idx].append(joint_result)
		
		return structured_data
	
	def GetLinerResults(
		self, 
		stages: list[int]) -> dict[int, list[LinerResult]]:

		map_data = self._callFunction('GetLinerResults', [stages])
		structured_data = {}
		for stage_idx, stage_data in map_data.items():

			structured_data[stage_idx] = []
			for entity_name, entity_data in stage_data.items():
				liner_result = self.process_liner_data(entity_data, entity_name)
				structured_data[stage_idx].append(liner_result)
		
		return structured_data


	def GetPileResults(	
		self, 
		stages: list[int]) -> dict[int, list[PileResult]]:
		return self._get_composition_result('GetPileResults',PileResult, stages)

	def GetCompositeResults(	
		self, 
		stages: list[int]) -> dict[int, list[CompositeResult]]:
		return self._get_composition_result('GetCompositeResults',CompositeResult, stages)

	def GetStructuralResults(	
		self, 
		stages: list[int]) -> dict[int, list[PileResult]]:
		return self._get_composition_result('GetStructuralResults',StructuralResult, stages)


	def _get_composition_result(
	self,
	function_name: str,
	ResultType,
	stages: list[int]) -> dict[int, list[LinerResult]]:

		map_data = self._callFunction(function_name, [stages])
		structured_data = {}
		for stage_idx, stage_data in map_data.items():
			structured_data[stage_idx] = []
			for entity_name, entity_data in stage_data.items():
				liner_result = self.process_liner_data(entity_data, entity_name)
				joint_result = self.process_joint_data(entity_data, entity_name)
				composition_result = ResultType(entity_name,joint_result,liner_result)
				structured_data[stage_idx].append(composition_result)

		return structured_data

	def getUnits(self):
		'''
		Get Units
		'''
		NUM_UNITS = 3
		data = self._callFunction('getUnits', [])
		if len(data) != NUM_UNITS:
			assert False
			return Units()
		return Units(*data)

	def getCriticalSRF(self):
		'''
		Get Critical SRF
		'''
		return ResetInvalid.validate_double(self._callFunction('getCriticalSRF', []))