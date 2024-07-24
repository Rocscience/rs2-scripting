Bolt Script Examples
======================

Download the `ExampleModel.fez <https://github.com/Rocscience/rs2-scripting/blob/main/docs/example_code/example_models/ExampleModel.fez>`_ for this example.

.. _Bolt Example:
.. literalinclude:: ../../example_code/bolt_prop_example.py
   :language: python
   :caption: Code Snippet: Manipulation of Bolt Properties

Output:

.. code::

	28.0
	True
	0.2
	{'BoltDiameter': 19.0, 'BoltModulusE': 250000.0, 'TensileCapacity': 0.2, 'ResidualTensileCapacity': 0.0, 'OutofPlaneSpacing': 1.2, 'PreTensioningForce': 0.0, 'ConstantPretensioningForceInInstallStage': True}
	{'BoreholeDiameter': 48.0, 'CableDiameter': 19.0, 'CableModulusE': 200000.0, 'CablePeak': 0.1, 'OutofPlaneSpacing': 1.0, 'WaterCementRatio': 0.35, 'JointShear': True, 'FacePlates': True, 'AddPullOutForce': True, 'PullOutForce': 1.0, 'ConstantShearStiffness': False, 'Stiffness': 100.0, 'AddBulges': True, 'BulgeType': <BulgeTypes.GARFORD_BULB_25MM: 'PHASE2_BULGE_GARFORD_25'>}
	[10.0, 20.0, 30.0]