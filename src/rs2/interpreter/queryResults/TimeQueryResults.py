class QueryPointResult:
    """
    Returns query point result.
    
    Attributes:
        x_location (double): X-Coordinate for time query point.
        y_location (double): Y-Coordinate for time query point.
        time (double): Dynamic stage time for time query point.
        value (double): Value for time query point.
    
        
    Examples:
    
		:ref:`Time Query Example`    
        
	"""
    def __init__(self, x_location, y_location, time, value):
        self.x_location = x_location
        self.y_location = y_location
        self.time = time
        self.value = value
    
    def GetXCoordinate(self) -> float:
        '''
        Returns the X-Coordinate of the query point
        '''
        return self.x_location

    def GetYCoordinate(self) -> float:
        '''
        Returns the Y-Coordinate of the query point
        '''
        return self.y_location

    def GetStageTime(self) -> float:
        '''
        Returns the dynamic stage time of the query point
        '''
        return self.time
    
    def GetValue(self) -> float:
        '''
        Returns the value of the time query point
        '''
        return self.value

class QueryLineResult:
    """
    Attributes:
        query_values (list[QueryPointResult]): List of QueryPointResult objects making up the result for the time query line.
    
    Examples:
		:ref:`Time Query Example`
	"""
    def __init__(self, list_node_values):
        list_node_value_obj = []
        for node_value in list_node_values:
            list_node_value_obj.append(QueryPointResult(*node_value))
        self.query_values = list_node_value_obj
    
    def GetNodeValues(self) -> list[QueryPointResult]:
        '''
        | Returns a list[QueryPointResult] representing result at this node part of the time query line
        | To get the x-coordinate, y-coordinate, dynamic stage time, or value, please call the supporting class methods:

        * QueryPointResult.GetXCoordinate()
        * QueryPointResult.GetYCoordinate()
        * QueryPointResult.GetStageTime()
        * QueryPointResult.GetValue()
        '''
        return self.query_values

class TimeQueryPointResults:
    """
    Attributes:
        entity_ID (str): Unique Identifier for time query point.
        query_values (list[QueryPointResult]): List of QueryPointResult object for time query point.
        
    Examples:
		:ref:`Time Query Example`
	"""
    # Stores all time query points result for specific stage
    def __init__(self, entity_ID, query_point_values):
        self.entity_ID = entity_ID
        # Construct QueryPointResult objects
        query_values_obj = []
        for value in query_point_values:
            query_values_obj.append(QueryPointResult(*value))
        self.query_values = query_values_obj
    
    def GetUniqueIdentifier(self) -> int:
        '''
        Returns the unique identifier for the time query point
        '''
        return self.entity_ID
    
    def GetAllValues(self) -> list[QueryPointResult]:
        '''
        | Returns a list[QueryPointResult] representing result at all nodes of the time query point
        | To get the x-coordinate, y-coordinate, dynamic stage time, or value, please call the supporting class methods:

        * QueryPointResult.GetXCoordinate()
        * QueryPointResult.GetYCoordinate()
        * QueryPointResult.GetStageTime()
        * QueryPointResult.GetValue()
        '''
        return self.query_values

class TimeQueryLineResults:
    """
    Attributes:
        entity_ID (str): Unique Identifier for time query line.
        line_data (list[QueryLineResult]): List of QueryLineResult object for time query line.
     
    Examples:
		:ref:`Time Query Example`
	"""
    # Stores all time query line result for specific stage
    def __init__(self, entity_ID, list_query_line_data):
        self.entity_ID = entity_ID
        # Construct QueryPointResult objects
        list_query_line_obj = []
        for list_line_node_data in list_query_line_data:
            list_query_line_obj.append(QueryLineResult(list_line_node_data))
        self.line_data = list_query_line_obj
    
    def GetUniqueIdentifier(self) -> int:
        '''
        Returns the unique identifier for the time query point
        '''
        return self.entity_ID
    
    def GetAllNodeObjects(self) -> list[QueryLineResult]:
        '''
        Returns a list[QueryLineResult] representing nodes making up the time query line

        To get list of node values associated with a specific node, please call the supported class method:

        * QueryLineResult.GetNodeValues()

        | The above returns a list[QueryPointResult] representing result at this node part of the time query line
        | To get the x-coordinate, y-coordinate, dynamic stage time, or value, please call the supporting class methods:
        
        * QueryPointResult.GetXCoordinate()
        * QueryPointResult.GetYCoordinate()
        * QueryPointResult.GetStageTime()
        * QueryPointResult.GetValue()
        '''
        return self.line_data