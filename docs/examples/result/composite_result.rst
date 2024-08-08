Composite Result Script Examples
====================================

Download the `SupportResult.fez <https://github.com/Rocscience/rs2-scripting/blob/main/docs/example_code/example_models/SupportResults.fez>`_ for this example.

.. _Support Composite Results Example:
.. literalinclude:: ../../example_code/support_composite_example.py
   :language: python
   :caption: Code Snippet: Get Support Composite Results

Output:

.. code::

   Stage 1 Composite Results

        Composite Unique ID = External boundary0
        Joint Result for Composite with ID External boundary0:

                Joint Unique ID = External boundary0
                Joint Element Results:

                Start X-Coord = 11.949843172111, Start Y-Coord = 16.8602900357032, End X-Coord = 7.66165679261041, End Y-Coord = 16.0080637205343
                Distance = 2.186025624140804, Normal Stress = 4.0118, Shear Stress = 0.06408, Confining Stress = None
                Normal Displacement = 3.98454459388709e-05, Shear Displacement = 9.518369020371651e-07, Yielded = False

                Start X-Coord = 7.66165679261041, Start Y-Coord = 16.0080637205343, End X-Coord = 3.37347041310981, End Y-Coord = 15.1558374053654
                Distance = 6.558076872422411, Normal Stress = 5.5995, Shear Stress = -0.064085, Confining Stress = None
                Normal Displacement = 3.567238008880944e-05, Shear Displacement = -9.650382373340867e-07, Yielded = False

        Liner Result for Composite with ID External boundary0:

                Liner Unique ID = External boundary0
                Liner Element Results:

                Composite Layer = 1, Node Start = 55, Node End = 56
                Start X-Coord = 11.949843172111, Start Y-Coord = 16.8602900357032, End X-Coord = 7.66165679261041, End Y-Coord = 16.0080637205343
                Distance = 2.186025624140804, Axial Force = -21.786, Moment 1 = -44.105
                Moment-Mid = -125.36, Moment 2 = -206.62, Shear Force = -97.7
                Displacement Total = 0.003946398950942492, Displacement X = -0.0024462, Displacement Y = -0.0030968
                Axial Symmetry Force = None, Axial Symmetry Moment = None
                Beam Yield = False, Temperature = -18.0

                Composite Layer = 1, Node Start = 56, Node End = 57
                Start X-Coord = 7.66165679261041, Start Y-Coord = 16.0080637205343, End X-Coord = 3.37347041310981, End Y-Coord = 15.1558374053654
                Distance = 6.558076872422411, Axial Force = -129.95, Moment 1 = -195.16
                Moment-Mid = -113.91, Moment 2 = -32.647, Shear Force = -7.6313
                Displacement Total = 0.00421677623309561, Displacement X = -0.0023702, Displacement Y = -0.0034876
                Axial Symmetry Force = None, Axial Symmetry Moment = None
                Beam Yield = False, Temperature = -18.0

                Composite Layer = 2, Node Start = 55, Node End = 56
                Start X-Coord = 11.949843172111, Start Y-Coord = 16.8602900357032, End X-Coord = 7.66165679261041, End Y-Coord = 16.0080637205343
                Distance = 2.186025624140804, Axial Force = -21.786, Moment 1 = -44.105
                Moment-Mid = -125.36, Moment 2 = -206.62, Shear Force = -97.7
                Displacement Total = 0.003946398950942492, Displacement X = -0.0024462, Displacement Y = -0.0030968
                Axial Symmetry Force = None, Axial Symmetry Moment = None
                Beam Yield = False, Temperature = -18.0

                Composite Layer = 2, Node Start = 56, Node End = 57
                Start X-Coord = 7.66165679261041, Start Y-Coord = 16.0080637205343, End X-Coord = 3.37347041310981, End Y-Coord = 15.1558374053654
                Distance = 6.558076872422411, Axial Force = -129.95, Moment 1 = -195.16
                Moment-Mid = -113.91, Moment 2 = -32.647, Shear Force = -7.6313
                Displacement Total = 0.00421677623309561, Displacement X = -0.0023702, Displacement Y = -0.0034876
                Axial Symmetry Force = None, Axial Symmetry Moment = None
                Beam Yield = False, Temperature = -18.0

                Composite Layer = 3, Node Start = 55, Node End = 56
                Start X-Coord = 11.949843172111, Start Y-Coord = 16.8602900357032, End X-Coord = 7.66165679261041, End Y-Coord = 16.0080637205343
                Distance = 2.186025624140804, Axial Force = -0.01552, Moment 1 = -9.5518
                Moment-Mid = -82.658, Moment 2 = -155.76, Shear Force = -46.551
                Displacement Total = 0.004102127103101511, Displacement X = -0.0024026, Displacement Y = -0.0033249
                Axial Symmetry Force = None, Axial Symmetry Moment = None
                Beam Yield = False, Temperature = -18.0

                Composite Layer = 3, Node Start = 56, Node End = 57
                Start X-Coord = 7.66165679261041, Start Y-Coord = 16.0080637205343, End X-Coord = 3.37347041310981, End Y-Coord = 15.1558374053654
                Distance = 6.558076872422411, Axial Force = -0.16632, Moment 1 = -151.97
                Moment-Mid = -78.864, Moment 2 = -5.7581, Shear Force = 25.54
                Displacement Total = 0.004168850800880262, Displacement X = -0.0023836, Displacement Y = -0.0034202
                Axial Symmetry Force = None, Axial Symmetry Moment = None
                Beam Yield = False, Temperature = -18.0

                Composite Layer = 4, Node Start = 55, Node End = 56
                Start X-Coord = 11.949843172111, Start Y-Coord = 16.8602900357032, End X-Coord = 7.66165679261041, End Y-Coord = 16.0080637205343
                Distance = 2.186025624140804, Axial Force = -0.01552, Moment 1 = -9.5518
                Moment-Mid = -82.658, Moment 2 = -155.76, Shear Force = -46.551
                Displacement Total = 0.004102127103101511, Displacement X = -0.0024026, Displacement Y = -0.0033249
                Axial Symmetry Force = None, Axial Symmetry Moment = None
                Beam Yield = False, Temperature = -18.0

                Composite Layer = 4, Node Start = 56, Node End = 57
                Start X-Coord = 7.66165679261041, Start Y-Coord = 16.0080637205343, End X-Coord = 3.37347041310981, End Y-Coord = 15.1558374053654
                Distance = 6.558076872422411, Axial Force = -0.16632, Moment 1 = -151.97
                Moment-Mid = -78.864, Moment 2 = -5.7581, Shear Force = 25.54
                Displacement Total = 0.004168850800880262, Displacement X = -0.0023836, Displacement Y = -0.0034202
                Axial Symmetry Force = None, Axial Symmetry Moment = None
                Beam Yield = False, Temperature = -18.0

.. note::
    
    Since the element type for the model is 3-noded triangular, liner results are outputted at two nodes per liner element: 
    start node and end node. If the model uses quadratic element type, liner result are outputted at three nodes per element. 
    See the `Liner Results Overview <https://www.rocscience.com/help/rs2/documentation/rs2-interpret/liner-results/liner-results-overview>`_ topic for more information.
