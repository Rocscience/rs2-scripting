from rs2.interpreter._UtilityResult import *

class QueryResult:
    """

    Attributes:
        x_location (double): X-Coordinate for material query point.           
        y_location (double): Y-Coordinate for material query point.            
        distance (double): Distance for material query point.           
        value (double): Result type value for material query point.
    
    Examples:
    
		:ref:`Material Query Example`
        
	"""
    def __init__(self, x_location, y_location, distance, value):
        self.x_location = x_location
        self.y_location = y_location
        self.distance = distance
        self.value = value
        ResetInvalid.validate(self)
    
    def GetXCoordinate(self) -> float:
        '''
        Returns the X-Coordinate of the query
        '''
        return self.x_location
    
    def GetYCoordinate(self) -> float:
        '''
        Returns the Y-Coordinate of the query
        '''
        return self.y_location

    def GetDistance(self) -> float:
        '''
        Returns the distance of the query
        '''
        return self.distance
    
    def GetValue(self) -> float:
        '''
        Returns the value of the query based on model's current result type
        '''
        return self.value

class MaterialQueryResults:
    """
    Attributes:
        entity_ID (str): Unique Identifier for material query.
        material_id (int): Material Identifier for material query.
        query_values (list[QueryResult]): List of QueryResult point objects making up the material query.
     
        
    Examples:
    
		:ref:`Material Query Example`
	"""
    def __init__(self, entity_ID, material_id, query_values):
        self.entity_ID = entity_ID
        self.material_id = material_id
        # Construct QueryResult objects
        query_values_obj = []
        for value in query_values:
            query_values_obj.append(QueryResult(*value))
        self.query_values = query_values_obj
    
    def GetUniqueIdentifier(self) -> int:
        '''
        Returns the unique identifier for the material query
        '''
        return self.entity_ID
    
    def GetMaterialID(self) -> int:
        '''
        Returns the material ID of the query
        '''
        return self.material_id
    
    def GetAllValues(self) -> list[QueryResult]:
        '''
        |  Returns a list[QueryResult] representing result at all nodes of the material query
        |  To get the x-coordinate, y-coordinate, distance, or value, please call the supporting class methods:
        
        * QueryResult.GetXCoordinate()
        * QueryResult.GetYCoordinate()
        * QueryResult.GetDistance()
        * QueryResult.GetValue()
        '''
        return self.query_values