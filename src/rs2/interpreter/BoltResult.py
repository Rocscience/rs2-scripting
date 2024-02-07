class BoltYieldingResults:
    def __init__(self, start_x, start_y, end_x, end_y, yielding_flag):
        self.start_x = start_x #0
        self.start_y = start_y #1
        self.end_x = end_x #2
        self.end_y = end_y #3
        self.yielding_flag = yielding_flag #4

class BoltForceDisplacementResults:
    def __init__(self, location_x, location_y, distance, axial_force, axial_stress, shear_force, rock_displacement, bolt_displacement):
        self.location_x = location_x #0
        self.location_y = location_y #1
        self.distance = distance #2
        self.axial_force = axial_force #3
        self.axial_stress = axial_stress #4
        self.shear_force = shear_force #5
        self.rock_displacement = rock_displacement #6
        self.bolt_displacement = bolt_displacement #7
