class QueryResult:
    def __init__(self, x_location, y_location, distance, value):
        self.x_location = x_location
        self.y_location = y_location
        self.distance = distance
        self.value = value
    
    def GetXCoordinate(self):
        '''
        Returns the X-Coordinate of the query
        '''
        return self.x_location
    
    def GetYCoordinate(self):
        '''
        Returns the Y-Coordinate of the query
        '''
        return self.y_location

    def GetDistance(self):
        '''
        Returns the distance of the query
        '''
        return self.distance
    
    def GetValue(self):
        '''
        Returns the value of the query based on model's current result type
        '''
        return self.value

class MaterialQueryResults:
    def __init__(self, entity_ID, material_id, query_values):
        self.entity_ID = entity_ID
        self.material_id = material_id
        self.query_values = query_values
    
    def GetUniqueIdentifier(self):
        '''
        Returns the unique identifier for the material query
        '''
        return self.entity_ID
    
    def GetMaterialID(self):
        '''
        Returns the material ID of the query
        '''
        return self.material_id
    
    def GetAllValues(self):
        '''
        Returns a list[QueryResult] representing result at all nodes of the material query
        To get the x-coordinate, y-coordinate, distance, or value, please call the supporting class methods:
        - QueryResult.GetXCoordinate()
        - QueryResult.GetYCoordinate()
        - QueryResult.GetDistance()
        - QueryResult.GetValue()
        '''
        query_values = []
        for value in self.query_values:
            query_values.append(QueryResult(*value))
        return query_values