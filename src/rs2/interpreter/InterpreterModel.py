from rs2.interpreter.InterpreterEnums import *
from rs2.interpreter.queryResults.MeshResults import MeshResults
from rs2.interpreter.queryResults.HistoryQueryResults import *
from rs2.interpreter.queryResults.TimeQueryResults import *
from rs2.interpreter.InterpreterGraphEnums import *
from rs2.interpreter.supportResults.JointResult import *
from rs2.interpreter.supportResults.LinerResult import *
from rs2.interpreter.supportResults.BoltResult import*
from rs2.interpreter.supportResults.CompositeResult import*
from rs2.interpreter.queryResults.MaterialQueryResults import *
from rs2.BaseModel import BaseModel

class Model(BaseModel):
	"""
	:ref:`Model Example`
	"""
	def saveCopyAs(self, fileName : str):
		'''
		Saves the model using the given file name.

		Examples:
			.. code-block:: python
			
				model.saveCopyAs('C:/simple_3_stage.fez')
		'''
		formattedFileName = fileName.replace('/', '\\')
		self._enforceFeaFezEnding(formattedFileName)
		return self._callFunction('saveAs', [formattedFileName])


	
	def SetActiveStage(self, stageNumber: int):
		'''
		:ref:`Material Query Example`

		|  Change model's active stage by its stage number
		'''
		return self._callFunction('SetActiveStage', [stageNumber])
	
	def SetResultType(self, resultType: ExportResultType) -> list[dict]:
		"""
		:ref:`Get Mesh Results Example`

		|  Sets the export result type for your model.
		
		Raises:
			ValueError: resultType must be an enum of type ExportResultType. Any other value will raise an error
		
		"""
		return self._callFunction('SetResultType', [resultType.value])
	
	def SetUserDefinedResultType(self, resultName: str) -> list[dict]:
		"""
		|  Sets the export result type to the user defined result type name.
		
		"""
		return self._callFunction('SetUserDefinedResultType', [resultName])
	
	def GetMeshResults(self) -> MeshResults:
		"""
		:ref:`Get Mesh Results Example`

		|  Returns the mesh results at all nodes for your model.
		
		"""
		results = self._callFunction('GetMeshResults', [])
		return MeshResults(results)

	def GetHistoryQueryResults(self, hq_name: str, horizontal_axis: HistoryQueryGraphEnums.HorizontalAxisTypes, vertical_axis: HistoryQueryGraphEnums.VerticalAxisTypes, 
							stages: list[int]) -> dict[int, list[HistoryQueryResult]]:
		"""
		:ref:`History Query Example`

		|   Returns a map of HistoryQueryResult for all input stages and history queries in your model.
		
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
		:ref:`Time Query Example`

		|  Returns a map of TimeQueryPointResults for all input stages and time query points in your model.

		|  Please note points that are over an excavation at specific stages will not have data returned at those locations.
		
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
		:ref:`Time Query Example`

		|  Returns a map of TimeQueryLineResults for all input stages and time query lines in your model.

		|  Please note points that are over an excavation at specific stages will not have data returned at those locations.
		
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
		:ref:`Material Query Example`

		|  Adds a material query point/line to your model using the specified coordinates in order.

		|  Returns a unique identifier for the newly added material query point/line.
		
		"""
		return self._callFunction('AddMaterialQuery', [points])
	
	def RemoveMaterialQuery(self, IDs_toRemove: list[str]) -> str:
		"""
		:ref:`Material Query Example`

		|  Removes material query points or lines for provided list of IDs.

		"""
		return self._callFunction('RemoveMaterialQuery', [IDs_toRemove])
	
	def GetMaterialQueryResults(self) -> list[MaterialQueryResults]:
		"""
		:ref:`Material Query Example`
		
		|  Returns the results for all the material queries defined in your model for active model stage and result type.
		|  To get results for a different stage, please call SetActiveStage(int stageNumber) before calling this function.
		|  To get results for a different result type, please call either before calling this function:

		* SetResultType(InterpreterGraphEnums resultType)
		* SetUserDefinedResultType("Your defined resultType name")

		"""
		all_material_query_data = self._callFunction('GetMaterialQueryResults', [])
		all_mat_query_data_as_classObj = []
		for mat_query_data in all_material_query_data:
			# This list corresponds to the data at each vertex of material query in iteration
			entity_id, material_id, list_query_data = mat_query_data
			unpack_list_data = [entity_id, material_id, list_query_data]
			all_mat_query_data_as_classObj.append(MaterialQueryResults(*unpack_list_data))
		return all_mat_query_data_as_classObj

	def GetBoltResults (self, stages: list[int]) -> dict[int, list[BoltResult]]:
		"""
		:ref:`Support Bolt Results Example`
		
		|  Returns a map of BoltResult for all input stages and support bolt defined in your model.

		"""
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
				if len(entity_data[1]) < 1 or len(entity_data[2]) < 1:
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
		
	def _process_joint_data(self, entity_data, entity_name):

		joint_element_results = []
		for joint_vector in entity_data[1]:
			#joint_vector[yeilded_indx] = bool(joint_vector[yeilded_indx])
			joint_element = JointElementResult(*joint_vector)
			joint_element_results.append(joint_element)
		joint_result = JointResult(entity_name, joint_element_results)
		return joint_result

	def _process_liner_data(self, entity_data, entity_name):
		liner_element_results = []

		for liner_vector in entity_data[0]:
			liner_element = LinerElementResult(*liner_vector)
			liner_element_results.append(liner_element)
		liner_result = LinerResult(entity_name,liner_element_results)
		return liner_result

	def GetJointResults(self, stages: list[int]) -> dict[int, list[JointResult]]:
		"""
		:ref:`Support Joint Results Example`
		
		|  Returns a map of JointResult for all input stages and support joint defined in your model.

		"""
		map_data = self._callFunction('GetJointResults', [stages])
		structured_data = {}
		for stage_idx, stage_data in map_data.items():

			structured_data[stage_idx] = []
			for entity_name, entity_data in stage_data.items():
				joint_result = self._process_joint_data(entity_data, entity_name)
				structured_data[stage_idx].append(joint_result)
		
		return structured_data
	
	def GetLinerResults(self, stages: list[int]) -> dict[int, list[LinerResult]]:
		"""
		:ref:`Support Liner Results Example`
		
		|  Returns a map of LinerResult for all input stages and support liner defined in your model.

		"""
		map_data = self._callFunction('GetLinerResults', [stages])
		structured_data = {}
		for stage_idx, stage_data in map_data.items():

			structured_data[stage_idx] = []
			for entity_name, entity_data in stage_data.items():
				liner_result = self._process_liner_data(entity_data, entity_name)
				structured_data[stage_idx].append(liner_result)
		
		return structured_data

	def GetPileResults(self, stages: list[int]) -> dict[int, list[PileResult]]:
		"""
		:ref:`Support Pile Results Example`
		
		|  Returns a map of PileResult for all input stages and support pile defined in your model.

		"""
		return self._get_composition_result('GetPileResults',PileResult, stages)

	def GetCompositeResults(self, stages: list[int]) -> dict[int, list[CompositeResult]]:
		"""
		:ref:`Support Composite Results Example`
		
		|  Returns a map of CompositeResult for all input stages and support composite defined in your model.

		"""
		return self._get_composition_result('GetCompositeResults',CompositeResult, stages)

	def GetStructuralResults(self, stages: list[int]) -> dict[int, list[StructuralResult]]:
		"""
		:ref:`Support Structural Results Example`
		
		|  Returns a map of StructuralResult for all input stages and support structural defined in your model.

		"""
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
				liner_result = self._process_liner_data(entity_data, entity_name)
				joint_result = self._process_joint_data(entity_data, entity_name)
				composition_result = ResultType(entity_name,joint_result,liner_result)
				structured_data[stage_idx].append(composition_result)

		return structured_data


	def getCriticalSRF(self):
		'''
		|  Get Critical SRF
		'''
		return ResetInvalid.validate_double(self._callFunction('getCriticalSRF', []))