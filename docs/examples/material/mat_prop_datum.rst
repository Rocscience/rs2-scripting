Material Properties Datum Script Examples
===============================================================

Download the `ExampleModel.fez <https://github.com/Rocscience/rs2-scripting/blob/main/docs/example_code/example_models/ExampleModel.fez>`_ for this example.

.. _material property datum example:
.. literalinclude:: ../../example_code/material_datum_example.py
   :language: python
   :caption: Code Snippet: Manipulation of Datum Properties

Output:

.. code::

	Youngs Modulus Datum Dependent Type:
	Datum Type = DatumType.DATUM_TYPE_RADIAL, Datum Value = 5.0, Center = (3.5, 2.0)
	Use Cutoff = True, Datum Change = 0.5, Cutoff = 0.8


	Friction Datum Dependent Type:
	Datum Type = DatumType.DATUM_TYPE_DEPTH, Datum Value = 5.0, Center = (5.0, 6.0)
	Use Peak Cutoff = True, Peak Change = 1.0, Peak Cutoff = 44.0
	Use Residual Cutoff = True, Residual Cutoff Value = 45.0


	Cohesion Datum Dependent Type:
	Datum Type = DatumType.DATUM_TYPE_RADIAL, Datum Value = 5.0, Center = (5.0, 6.0)
	Use Peak Cutoff = True, Peak Change = 1.0, Peak Cutoff = 44.0
	Use Residual Cutoff = True, Residual Cutoff Value = 45.0

	Change Factor = 0.2, Datum Factor Value= 3.0, Peak Cutoff Value Factor = 4.42