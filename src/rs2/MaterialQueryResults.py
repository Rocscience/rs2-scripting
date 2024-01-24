class MaterialQueryResults:
    results = None
    def __init__(self, material_id, x_location, y_location, distance, value):
        self.material_id = material_id
        self.x_location = x_location
        self.y_location = y_location
        self.distance = distance
        self.value = value
    
    def GetMaterialID(self):
        '''
        Returns the material ID of the query
        '''
        return self.material_id
    
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