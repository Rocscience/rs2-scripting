Hydraulic Properties Script Examples
=========================================

Download the `StaticGroundwater.fez <https://github.com/Rocscience/rs2-scripting/blob/main/docs/example_code/example_models/StaticGroundwater.fez>`_ 
and `FEAGroundwater.fez <https://github.com/Rocscience/rs2-scripting/blob/main/docs/example_code/example_models/FEAGroundwater.fez>`_ for this example.

.. _hydraulic property example:
.. literalinclude:: ../../example_code/material_hydraulic_property_example.py
   :language: python
   :caption: Code Snippet: Manipulation of Hydraulic Properties

Output:

.. code::

	Piezo To Use = None

	Static Groundwater Properties

	Static Water Mode = StaticWaterModes.RU, RU Value = 4.0

	FEA Groundwater Properties

	K2/K1 = 2.0, K1 Definition = AnisotropyDefinitions.ANGLE, K1 Angle = 30.0

	Hydraulic Material Behaviour Stage Factor Value = MaterialBehaviours.UNDRAINED