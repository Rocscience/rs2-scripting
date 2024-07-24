Material Stiffness Properties Script Examples
===============================================================

Download the `ExampleModel.fez <https://github.com/Rocscience/rs2-scripting/blob/main/docs/example_code/example_models/ExampleModel.fez>`_ for this example.

.. _material property stiffness example:
.. literalinclude:: ../../example_code/material_stiffness_example.py
   :language: python
   :caption: Code Snippet: Manipulation of Stiffness Properties

Output:

.. code::

	Loading Custom Table = [(1.0, 2.0, 0.3), (4.0, 5.0, 0.4)]
	Unloading Condition = UnloadingConditions.DEVIATORIC_STRESS
	Unloading Custom Table = [(1.0, 2.0, 0.3), (4.0, 5.0, 0.4)]

	Isotropic Stage Factor Values
	Poisson Ratio Factor = 3.0, Res. Youngs Modulus Factor = 1.0, Shear Modulus Factor = 1.9

	NonLinear Hyperbolic Stage Factor Values
	Failure Ratio of RF = 1.0, Bulk Modulus ExpM = 2.0, Atmospheric Pressure = 3.3