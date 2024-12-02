from rs2._common.ProxyObject import ProxyObject
from rs2._common.documentProxy import DocumentProxy
from rs2.Units import Units
class BaseModel(ProxyObject):

	def __init__(self, client, ID):
		super().__init__(client, ID)
		self._documentProxy = self._getDocument()

	def _getDocument(self):
		documentObjectID = self._callFunction('getDocument', [], keepReturnValueReference=True)
		return DocumentProxy(self._client, documentObjectID)
	
	def _enforceFeaFezEnding(self, path: str):
		if not (path.endswith('.fea') or path.endswith('.fez')):
			raise ValueError('Path must end with .fea or .fez')
		
	def close(self):
		'''
		Closes the model
		
		Examples:
	
			.. code::
		
			   model.close()
		   
			See a full example in :ref:`Model Example`.
		
		'''
		return self._callFunction('close', [])
	
	def save(self):
		'''
		Saves the model
		
		Examples:
	
			.. code::
		
			   model.save()
		   
			See a full example in :ref:`Model Example`.

		'''
		return self._callFunction('save', [])
	
	def getUnits(self):
		'''
		
		Get Solid, Hydro and Thermal units for your model from RS2Modeler or RS2Interpreter.
		
		See Also:
			Each of solid units, hydro units and thermal units of your model can be accessed through `rs2.Units <rs2.Units.html>`_.
		
		Examples:
		
			.. code-block:: python
		
				modeler = RS2Modeler()			
				model = modeler.openFile(rf"{current_dir}\example_models\SupportStructuralResults.fez")
				# Get Solid, Hydro and Thermal units of your model
				modelerUnits = model.getUnits()
				print("\\nModeler Units")
				print("\\nSolid Units :")
				# Get solid units
				pprint(modelerUnits.solid_units)
				print("\\nHydro Units :")
				# Get hydro units
				pprint(modelerUnits.hydro_units)
				print("\\nThermal Units :")
				# Get thermal units
				pprint(modelerUnits.thermal_units)
			
			See a full example in :ref:`Get Model Units Example`


		'''
		NUM_UNITS = 3
		data = self._callFunction('getUnits', [])
		if (len (data) !=NUM_UNITS) :
			assert False, "Expected 3 units, got " + str(len(data))
		return Units(*data)
