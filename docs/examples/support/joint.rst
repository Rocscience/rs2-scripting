Joint Script Examples
======================

Download the `ExampleModel.fez <https://github.com/Rocscience/rs2-scripting/blob/main/docs/example_code/example_models/ExampleModel.fez>`_ for this example.


.. _Joint Example:
.. literalinclude:: ../../example_code/joint_prop_example.py
   :language: python
   :caption: Code Snippet: Manipulation of Joint Properties

Output:

.. code::

	50.0
	150000.0
	True
	{'PeakCohesion': 155.0, 'PeakFriction': 26.8, 'ResCohesion': 76.0, 'ResFriction': 18.4, 'TensileStrength': 0.0, 'ResTensileStrength': 0.0, 'DeltaR': 0.1, 'InitialSlope': 20000.0, 'WorkSoftening': True, 'NormalStiffness': 100000.0, 'ShearStiffness': 15000.0, 'ApplyPorePressure': True, 'ApplyAdditionalPressureInsideJoint': False, 'AdditionalPressureType': <AdditionalPressureType.PRESSURE: 'JOINT_ADDITIONAL_PRESSURE_BY_VALUE'>, 'AdditionalPressureInsideJoint': 0.0, 'ApplyPressureToLinerSideOnly': False, 'ApplyStageFactors': True}
	{'NormalStiffness': 100000.0, 'ShearStiffness': 10000.0, 'ApplyPorePressure': True, 'ApplyAdditionalPressureInsideJoint': False, 'AdditionalPressureType': <AdditionalPressureType.PRESSURE: 'JOINT_ADDITIONAL_PRESSURE_BY_VALUE'>, 'AdditionalPressureInsideJoint': 5.0, 'ApplyPressureToLinerSideOnly': False, 'ApplyStageFactors': False}
	[[2.0, 8.0, 9.0, 12.0], [5.0, 6.0, 7.0, 8.0]]