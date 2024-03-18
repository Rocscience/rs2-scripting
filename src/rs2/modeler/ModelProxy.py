from rs2._common.ProxyObject import ProxyObject
from rs2._common.documentProxy import DocumentProxy
from rs2._common.Units import Units
from rs2.modeler.properties.bolt.Bolt import BoltProperty
from rs2.modeler.properties.liner.Liner import LinerProperty
from rs2.modeler.properties.joint.Joint import JointProperty
from rs2.modeler.properties.pile.Pile import PileProperty
from rs2.modeler.properties.StructuralInterface import StructuralInterfaceProperty
from rs2.modeler.properties.CompositeProperty import CompositeProperty

from rs2.modeler.properties.material.MaterialPropertyProxy import MaterialProperty
from rs2.modeler.properties.ShearNormalFunctionProxy import ShearNormalFunction
from rs2.modeler.properties.UserDefinedWaterMode import UserDefinedWaterMode
from rs2.modeler.properties.DiscreteFunction import DiscreteFunction

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
    
	def getBoltPropertyByName(self, boltName : str) -> BoltProperty:

		'''
		Returns a Bolt Property object based on its name.
		'''

		boltObjectID = self._callFunction('getBoltPropertyByName', [boltName], keepReturnValueReference=True)
		return BoltProperty(self._client, boltObjectID, self._documentProxy._ID)
    
	def getLinerPropertyByName(self, linerName : str) -> LinerProperty:
		'''
		Returns a Liner Property object based on its name.
		'''
		linerObjectID = self._callFunction('getLinerPropertyByName', [linerName], keepReturnValueReference=True)
		return LinerProperty(self._client, linerObjectID, self._documentProxy._ID)
	
	def getJointPropertyByName(self, jointName : str) -> JointProperty:
		'''
		Returns a Joint Property object based on its name.
		'''
		jointObjectID = self._callFunction('getJointPropertyByName', [jointName], keepReturnValueReference=True)
		return JointProperty(self._client, jointObjectID, self._documentProxy._ID)
	
	def getPilePropertyByName(self, pileName : str) -> PileProperty:
		'''
		Returns a Pile Property object based on its name.
		'''
		pileObjectID = self._callFunction('getPilePropertyByName', [pileName], keepReturnValueReference=True)
		return PileProperty(self._client, pileObjectID, self._documentProxy._ID)

	def getStructuralInterfacePropertyByName(self, structuralName : str) -> StructuralInterfaceProperty:
		'''
		Returns a Structural Interface Property object based on its name.
		'''
		structuralInterfaceObjectID = self._callFunction('getStructuralPropertyByName', [structuralName], keepReturnValueReference=True)
		return StructuralInterfaceProperty(self._client, structuralInterfaceObjectID, self._documentProxy._ID)
	
	def getCompositeLinerPropertyByName(self, compositeName : str) -> CompositeProperty:
		'''
		Returns a Composite Liner Property object based on its name.
		'''
		compositeLinerObjectID = self._callFunction('getCompositePropertyByName', [compositeName], keepReturnValueReference=True)
		return CompositeProperty(self._client, compositeLinerObjectID, self._documentProxy._ID)
	
	

	def getMaterialPropertyByName(self, materialName : str) -> MaterialProperty:
		'''
		Returns a Material Property object based on its name.
		'''
		materialObjectID = self._callFunction('getMaterialPropertyByName', [materialName], keepReturnValueReference=True)
		return MaterialProperty(self._client, materialObjectID, self._documentProxy._ID)

	def getAllBoltProperties(self) -> list[BoltProperty]:

		'''
		Returns a list of all Bolt Property objects
		'''
		activeBoltProperties = []
		boltObjectIDList = self._callFunction('getAllBoltProperties', [], keepReturnValueReference=True)
		for boltObjectID in boltObjectIDList:
			activeBoltProperties.append(BoltProperty(self._client, boltObjectID, self._documentProxy._ID))
		return activeBoltProperties

	def getAllLinerProperties(self) -> list[LinerProperty]:
		'''
		Returns a list of all Liner Property objects
		'''
		activeLinerProperties = []
		linerObjectIDList = self._callFunction('getAllLinerProperties', [], keepReturnValueReference=True)
		for linerObjectID in linerObjectIDList:
			activeLinerProperties.append(LinerProperty(self._client, linerObjectID, self._documentProxy._ID))
		return activeLinerProperties
	
	def getAllJointProperties(self) -> list[JointProperty]:
		'''
		Returns a list of all Joint Property objects
		'''
		activeJointProperties = []
		jointObjectIDList = self._callFunction('getAllJointProperties', [], keepReturnValueReference=True)
		for jointObjectID in jointObjectIDList:
			activeJointProperties.append(JointProperty(self._client, jointObjectID, self._documentProxy._ID))
		return activeJointProperties
	
	def getAllPileProperties(self) -> list[PileProperty]:
		'''
		Returns a list of all Pile Property objects
		'''
		activePileProperties = []
		pileObjectIDList = self._callFunction('getAllPileProperties', [], keepReturnValueReference=True)
		for pileObjectID in pileObjectIDList:
			activePileProperties.append(PileProperty(self._client, pileObjectID, self._documentProxy._ID))
		return activePileProperties
	
	def getAllStructuralInterfaceProperties(self) -> list[StructuralInterfaceProperty]:
		'''
		Returns a list of all Structural Interface Property objects
		'''
		activeStructuralProperties = []
		structuralObjectIDList = self._callFunction('getAllStructuralProperties', [], keepReturnValueReference=True)
		for structuralObjectID in structuralObjectIDList:
			activeStructuralProperties.append(StructuralInterfaceProperty(self._client, structuralObjectID, self._documentProxy._ID))
		return activeStructuralProperties
	
	def getAllCompositeLinerProperties(self) -> list[CompositeProperty]:
		'''
		Returns a list of all Composite Liner Property objects
		'''
		activeCompositeProperties = []
		compositeObjectIDList = self._callFunction('getAllCompositeProperties', [], keepReturnValueReference=True)
		for compositeObjectID in compositeObjectIDList:
			activeCompositeProperties.append(CompositeProperty(self._client, compositeObjectID, self._documentProxy._ID))
		return activeCompositeProperties
	
	def getAllMaterialProperties(self) -> list[MaterialProperty]:
		'''
		Returns a list of all Material Property objects
		'''
		activeMaterialProperties = []
		materialObjectIDList = self._callFunction('getAllMaterialProperties', [], keepReturnValueReference=True)
		for materialObjectID in materialObjectIDList:
			activeMaterialProperties.append(MaterialProperty(self._client, materialObjectID, self._documentProxy._ID))
		return activeMaterialProperties
	
	def getShearNormalFunctions(self) -> list[ShearNormalFunction]:
		'''
		Returns a list of all shear normal functions
		'''
		activeShearNormalFunctionProperties = []
		shearNormalFunctionIDList = self._callFunction('getShearNormalFunctions', [], keepReturnValueReference=True)
		for shearNormalFunctionObjectID in shearNormalFunctionIDList:
			activeShearNormalFunctionProperties.append(ShearNormalFunction(self._client, shearNormalFunctionObjectID))
		return activeShearNormalFunctionProperties
	
	def getShearNormalFunctionByName(self, shearNormalFunctionName : str) -> ShearNormalFunction:
		'''
		Returns a shear normal function object based on its name.
		'''
		shearNormalFunctionObjectID = self._callFunction('getShearNormalFunctionByName', [shearNormalFunctionName], keepReturnValueReference=True)
		return ShearNormalFunction(self._client, shearNormalFunctionObjectID)
	
	def createNewShearNormalFunction(self, functionName):
		'''
		Creates a new shear normal function with the given name
		'''
		return self._callFunction('createNewShearNormalFunction', [functionName])
	
	def deleteShearNormalFunction(self, functionName):
		'''
		Deletes a shear normal function with the given name
		'''
		return self._callFunction('deleteShearNormalFunction', [functionName])
	
	def renameShearNormalFunction(self, oldName, newName):
		'''
		Renames a shear normal function with the given name
		'''
		return self._callFunction('renameShearNormalFunction', [oldName, newName])
	
	def getUserDefinedPermeabilityAndWaterContentMode(self, name : str) -> UserDefinedWaterMode:
		'''
		Returns a User Defined Water Mode object based on its name.
		'''
		userDefinedWaterModeObjectID = self._callFunction('getUserDefinedWaterMode', [name], keepReturnValueReference=True)
		return UserDefinedWaterMode(self._client, userDefinedWaterModeObjectID)
	
	def createUserDefinedPermeabilityAndWaterContentMode(self, name : str) -> UserDefinedWaterMode:
		'''
		Creates a User Defined Water Mode object with the given name.
		'''
		userDefinedWaterModeObjectID = self._callFunction('createUserDefinedWaterMode', [name], keepReturnValueReference=True)
		return UserDefinedWaterMode(self._client, userDefinedWaterModeObjectID)

	def deleteUserDefinedPermeabilityAndWaterContentMode(self, name : str):
		'''
		Deletes a User Defined Water Mode object with the given name.
		'''
		return self._callFunction('deleteUserDefinedWaterMode', [name])
	
	def renameUserDefinedPermeabilityAndWaterContentMode(self, oldName : str, newName : str):
		'''
		Renames a User Defined Water Mode object with the given name.
		'''
		return self._callFunction('renameUserDefinedWaterMode', [oldName, newName])
	
	def AddHistoryQueryPoint(self, x: float, y: float, history_query_name: str):
		'''
		Add a new History Query point to your model with the specified coordinates and label name

		Args:
			x (float): The x-coordinate value for the query point.
			y (float): The y-coordinate value for the query point.
			history_query_name (str): The label name for your query point.

		'''
		return self._callFunction('AddHistoryQueryPoint', [x, y, history_query_name])
	

	def RemoveHistoryQueryPoint(self, history_query_name: str):
		'''
		Remove a History Query point from your model by label name.

		Args:
			history_query_name (str): The label name for your query point.

		'''
		return self._callFunction('RemoveHistoryQueryPoint', [history_query_name])

	def AddTimeQueryLine(self, points: list[list[float]], points_on_line: int) -> str:
		'''
		Add a new Time Query Line to your model with the specified coordinates

		Args:
			points (list[list[float]]) : List of points making the time query line.
			points_on_line (int) : Number of segments to evenly divide time query line
		
		Warning:
			points_on_line must be between 1 and 10 inclusive.

		'''
		return self._callFunction('AddTimeQueryLine', [points, points_on_line])
	
	def RemoveTimeQueryLine(self, IDs_toRemove: list[str]):
		'''
		Removes Time Query Line(s) from your model using provided list of IDs.

		Args:
			IDs_toRemove (list[str]): List of unique identifier for time query line(s) to remove.

		'''
		return self._callFunction('RemoveTimeQueryLine', [IDs_toRemove])
	
	def AddTimeQueryPoint(self, x: float, y: float) -> str:
		'''
		Add a new Time Query Point to your model with the specified x and y coordinates

		Args:
			x (float) : x-coordinate of the time query line.
			y (float) : y-coordinate of the time query line.

		'''
		return self._callFunction('AddTimeQueryPoint', [x, y])
	
	def RemoveTimeQueryPoint(self, IDs_toRemove: list[str]):
		'''
		Removes Time Query Point(s) from your model using provided list of IDs.

		Args:
			IDs_toRemove (list[str]): List of unique identifier for time query points(s) to remove.

		'''
		return self._callFunction('RemoveTimeQueryPoint', [IDs_toRemove])
	
	def compute(self):
		'''
		Saves the file if modified and then runs compute. Replaces any existing results.

		Warning:
			All objects retrieved from the interpreter for this file will be invalidated after this call.
			If you have an interpreter model open, you should close, compute, and then re-open the model.

			.. code-block:: python

				interpreterModel.close()
				model.compute()
				interpreterModel = modeler.openFile('C:/previouslyOpened.fez')
				
		'''
		return self._callFunction('compute', [False])

	def computeGroundWater(self):
		'''
		Saves the file if modified and then runs groundwater compute. Replaces any existing results.

		Warning:
			All objects retrieved from the interpreter for this file will be invalidated after this call.
			If you have an interpreter model open, you should close, compute, and then re-open the model.

			.. code-block:: python

				interpreterModel.close()
				model.compute()
				interpreterModel = modeler.openFile('C:/previouslyOpened.fez')
		'''
		return self._callFunction('compute', [True])

	def close(self):
		'''
		Closes the model
		'''
		return self._callFunction('close', [])

	def saveAs(self, fileName : str):
		'''
		Saves the model using the given file name.

		Example:

		.. code-block:: python

			model.saveAs('C:/simple_3_stage.fez')
		'''
		formattedFileName = fileName.replace('/', '\\')
		return self._callFunction('saveAs', [formattedFileName])

	def save(self):
		'''
		Saves the model
		'''
		return self._callFunction('save', [])

	def getDiscreteFunctions(self) -> list[DiscreteFunction]:
		'''
		Returns a list of all discrete functions
		'''
		activeDiscreteFunctionProperties = []
		discreteFunctionIDList = self._callFunction('getDiscreteFunctions', [], keepReturnValueReference=True)
		for discreteFunctionObjectID in discreteFunctionIDList:
			activeDiscreteFunctionProperties.append(DiscreteFunction(self._client, discreteFunctionObjectID))
		return activeDiscreteFunctionProperties
	
	def getDiscreteFunctionByName(self, discreteFunctionName : str) -> DiscreteFunction:
		'''
		Returns a discrete function object based on its name.
		'''
		discreteFunctionObjectID = self._callFunction('getDiscreteFunctionByName', [discreteFunctionName], keepReturnValueReference=True)
		return DiscreteFunction(self._client, discreteFunctionObjectID)
	
	def createNewDiscreteFunction(self, functionName):
		'''
		Creates a new discrete function with the given name
		'''
		return self._callFunction('createNewDiscreteFunction', [functionName])
	
	def deleteDiscreteFunction(self, functionName):
		'''
		Deletes a discrete function with the given name
		'''
		return self._callFunction('deleteDiscreteFunction', [functionName])
	
	def renameDiscreteFunction(self, oldName, newName):
		'''
		Renames a discrete function with the given name
		'''
		return self._callFunction('renameDiscreteFunction', [oldName, newName])	
	def getUnits(self):
		'''
		Get Units
		'''
		NUM_UNITS = 3
		data = self._callFunction('getUnits', [])
		if (len (data) !=NUM_UNITS) :
			assert False
			return Units()
		return Units(*data)

	def ResetProperties(self):
		'''
		Reset All Properties
		'''
		return self._callFunction('ResetProperties', [])
	
