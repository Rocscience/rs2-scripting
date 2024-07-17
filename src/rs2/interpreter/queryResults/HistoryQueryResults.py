class HistoryQueryResult:
    """
	Examples:
		:ref:`History Query Example`
	
	Attributes:
		horizontal_axis_result (double): Horizontal Axis Result for history query point.
        vertical_axis_result (double): Vertical Axis Result for history query point.
        location_x (double): X-Coordinate for history query point.
        location_y (double): Y-Coordinate for history query point.
	"""
    def __init__(self, x_location, y_location, horizontal_axis_result, vertical_axis_result):
        self.horizontal_axis_result = horizontal_axis_result
        self.vertical_axis_result = vertical_axis_result
        self.location_x = x_location
        self.location_y = y_location
    
    def GetXCoordinate(self):
        '''
        Returns the X-Coordinate of the point
        '''
        return self.location_x
    
    def GetYCoordinate(self):
        '''
        Returns the Y-Coordinate of the point
        '''
        return self.location_y

    def GetHorizontalAxisResult(self):
        '''
        Returns the horizontal axis result for the specific stage
        '''
        return self.horizontal_axis_result
    
    def GetVerticalAxisResult(self):
        '''
        Returns the vertical axis result for the specific stage
        '''
        return self.vertical_axis_result