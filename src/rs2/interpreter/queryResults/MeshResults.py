class MeshResults:
    """
	
    Attributes:
        results (list[list[double]]): Mesh results containing x-coordinate, y-coordinate and result type value for each node in your model.
        
        
    Examples:
    
		:ref:`Get Mesh Results Example`
        
	"""
    results = None

    def __init__(self, results):
        self.results = results

    def getXCoordinate(self, index):
        '''
        Returns the X-Coordinate of the mesh node for specified index
        '''
        return self.results[index][0]
    def getYCoordinate(self, index):
        '''
        Returns the Y-Coordinate of the mesh node for specified index
        '''
        return self.results[index][1]
    def getValue(self, index):
        '''
        Returns the value of the mesh node based on model's current result type and specified index
        '''
        return self.results[index][2]