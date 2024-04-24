
class Units:
	"""
	Examples:
		:ref:`Get Model Units Example`
	
	Attributes:
        solid_units (list[tuple[str]]): List of all solid units for your model.
        hydro_units (list[tuple[str]]): List of all hydraulic units for your model.
        thermal_units (list[tuple[str]]): List of all thermal units for your model.
	"""
	def __init__(self, solid_units=None, hydro_units=None, thermal_units=None):
		self.solid_units = solid_units
		self.hydro_units = hydro_units
		self.thermal_units = thermal_units
