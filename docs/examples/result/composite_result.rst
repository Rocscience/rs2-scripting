Composite Result Script Examples
====================================

Download the `SupportResult.fez <https://github.com/Rocscience/rs2-scripting/blob/main/docs/example_code/example_models/SupportResults.fez>`_ for this example.

.. _Support Composite Results Example:
.. literalinclude:: ../../example_code/support_composite_example.py
   :language: python
   :caption: Code Snippet: Get Support Composite Results

Output
------------------
.. literalinclude:: ../../example_code/support_composite_example_result.txt
   :language: python

.. note::
    
    Since the element type for the model is 3-noded triangular, liner results are outputted at two nodes per liner element: 
    start node and end node. If the model uses quadratic element type, liner result are outputted at three nodes per element. 
    See the `Liner Results Overview <https://www.rocscience.com/help/rs2/documentation/rs2-interpret/liner-results/liner-results-overview>`_ topic for more information.
