
class Units:
	"""
	Attributes:
		solid_units (list[tuple[str]]): List of all solid units for your model.
		hydro_units (list[tuple[str]]): List of all hydraulic units for your model.
		thermal_units (list[tuple[str]]): List of all thermal units for your model.
		
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
			
		See a full example in :ref:`Get Model Units Example`.
		
		
	"""
	def __init__(self, solid_units=None, hydro_units=None, thermal_units=None):
		self.solid_units = solid_units
		self.hydro_units = hydro_units
		self.thermal_units = thermal_units
