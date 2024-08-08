Pile Result Script Examples
==================================

Download the `SupportResult.fez <https://github.com/Rocscience/rs2-scripting/blob/main/docs/example_code/example_models/SupportResults.fez>`_ for this example.

.. _Support Pile Results Example:
.. literalinclude:: ../../example_code/support_pile_example.py
   :language: python
   :caption: Code Snippet: Get Support Pile Results

Output:

.. code::

   Stage 1 Pile Results

            Pile Unique ID = Pile0
            Joint Result for Pile with ID Pile0:

                    Joint Unique ID = Pile0
                    Joint Element Results:

                    Start X-Coord = 9.00086957359009, Start Y-Coord = 11.5846033227529, End X-Coord = 9.00086957359009, End Y-Coord = 7.79916982912479
                    Distance = 1.8927167468140547, Normal Stress = -0.92443, Shear Stress = 0.28125, Confining Stress = 1021.4
                    Normal Displacement = -4.6221e-05, Shear Displacement = 0.00010601666666666666, Yielded = False

            Liner Result for Pile with ID Pile0:

                    Liner Unique ID = Pile0
                    Liner Element Results:

                    Composite Layer = 2147483647, Node Start = 18, Node End = 6
                    Start X-Coord = 9.00086957359009, Start Y-Coord = 11.5846033227529, End X-Coord = 9.00086957359009, End Y-Coord = 7.79916982912479
                    Distance = 1.8927167468140547, Axial Force = 4.7223, Moment 1 = 2.2078
                    Moment-Mid = 2.2078, Moment 2 = 2.2078, Shear Force = -3.4994
                    Displacement Total = 0.0005066427731646825, Displacement X = 0.00027064, Displacement Y = -0.0004283
                    Axial Symmetry Force = None, Axial Symmetry Moment = None
                    Beam Yield = False, Temperature = 0.0

    Stage 2 Pile Results

            Pile Unique ID = Pile0
            Joint Result for Pile with ID Pile0:

                    Joint Unique ID = Pile0
                    Joint Element Results:

                    Start X-Coord = 9.00086957359009, Start Y-Coord = 11.5846033227529, End X-Coord = 9.00086957359009, End Y-Coord = 7.79916982912479
                    Distance = 1.8927167468140547, Normal Stress = -0.69699, Shear Stress = 0.12483, Confining Stress = 930.99
                    Normal Displacement = -3.484973333333334e-05, Shear Displacement = 6.241666666666667e-05, Yielded = False

            Liner Result for Pile with ID Pile0:

                    Liner Unique ID = Pile0
                    Liner Element Results:

                    Composite Layer = 2147483647, Node Start = 18, Node End = 6
                    Start X-Coord = 9.00086957359009, Start Y-Coord = 11.5846033227529, End X-Coord = 9.00086957359009, End Y-Coord = 7.79916982912479
                    Distance = 1.8927167468140547, Axial Force = -2.4216, Moment 1 = 1.6646
                    Moment-Mid = 1.6646, Moment 2 = 1.6646, Shear Force = -2.6384
                    Displacement Total = 0.0005836992266932003, Displacement X = -9.6168e-06, Displacement Y = 0.00058362
                    Axial Symmetry Force = None, Axial Symmetry Moment = None
                    Beam Yield = False, Temperature = 0.0