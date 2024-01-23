class MaterialQueryResults:
    results = None
    def __init__(self, material_id, x_location, y_location, distance, value, statistical_data):
        self.material_id = material_id
        self.x_location = x_location
        self.y_location = y_location
        self.distance = distance
        self.value = value
        # Statistical Data is a list of [base_stats, mean_stats, standard_deviation_stats, covariance_stats] from the model
        self.statistical_data = statistical_data
    
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
    
    def GetBaseStats(self):
        '''
        Returns the base statistical value of the query based on model's current result type
        '''
        if self.statistical_data:
            return self.statistical_data[0]
    
    def GetMeanStats(self):
        '''
        Returns the mean statistical value of the query based on model's current result type
        '''
        if self.statistical_data:
            return self.statistical_data[1]
    
    def GetStandardDeviationStats(self):
        '''
        Returns the standard deviation statistical value of the query based on model's current result type
        '''
        if self.statistical_data:
            return self.statistical_data[2]
    
    def GetCovarianceStats(self):
        '''
        Returns the covariance statistical value of the query based on model's current result type
        '''
        if self.statistical_data:
            return self.statistical_data[3]