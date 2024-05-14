from rs2.interpreter._UtilityResult import *

class LinerElementResult:
    def __init__(self,composite_layer, node_start, node_end, start_x, start_y, end_x, end_y, distance,axial_force, moment1, moment_mid, moment2, shear_force, displacement_total, displacement_x, displacement_y,
                 axi_sym_force, axi_sym_moment,beam_yield,temperature):

        self.composite_layer = int(composite_layer) #0
        self.node_start = int(node_start) #1
        self.node_end = int(node_end)#2
        self.start_x = start_x#3
        self.start_y = start_y#4
        self.end_x = end_x#5
        self.end_y = end_y#6
        self.distance = distance#7

        self.axial_force1 = axial_force#8
        self.moment1 = moment1#9
        self.moment_mid = moment_mid#10
        self.moment2 = moment2#11
        self.shear_force1 = shear_force#12
        self.displacement_total1 = displacement_total#13
        self.displacement_x1 = displacement_x#14
        self.displacement_y1 = displacement_y#15
        self.axi_sym_force1 = axi_sym_force#16
        self.axi_sym_moment1 = axi_sym_moment#17
        self.beam_yield1 = bool(beam_yield)#18
        self.temperature1 = temperature#25

        self.axial_force2    = axial_force
        self.axial_mid      = axial_force

        self.shear_force2          = shear_force
        self.shear_force_mid       = shear_force

        self.displacement_total2          = displacement_total
        self.displacement_total_mid       = displacement_total

        self.displacement_x2          = displacement_x
        self.displacement_x_mid       = displacement_x

        self.displacement_y2          = displacement_y
        self.displacement_y_mid       = displacement_y

        self.axi_sym_force2          = axi_sym_force
        self.axi_sym_force_mid       = axi_sym_force

        self.axi_sym_moment2          = axi_sym_moment
        self.axi_sym_moment_mid       = axi_sym_moment

        self.beam_yield2          = beam_yield
        self.beam_yield_mid       = beam_yield

        self.temperature2          = temperature
        self.temperature_mid       = temperature
        ResetInvalid.validate(self)


    def __init__(
        self,
        composite_layer, 
        node_start, 
        node_end, 
        start_x, 
        start_y, 
        end_x, 
        end_y, 
        distance,
        axial_force1, 
        moment1, 
        moment_mid, 
        moment2, 
        shear_force1, 
        displacement_total1, 
        displacement_x1, 
        displacement_y1,
        axi_sym_force1, 
        axi_sym_moment1,
        beam_yield1,
        temperature1,
        axial_mid,
        axial_force2,
        shear_force_mid,
        shear_force2,
        displacement_total_mid,
        displacement_total2,
        displacement_x_mid,
        displacement_x2,
        displacement_y_mid,
        displacement_y2,
        axi_sym_force_mid,
        axi_sym_force2,
        axi_sym_moment_mid,
        axi_sym_moment2,
        beam_yield_mid,
        beam_yield2,
        temperature_mid,
        temperature2):

        self.composite_layer = int(composite_layer) #0
        self.node_start = int(node_start) #1
        self.node_end = int(node_end)#2
        self.start_x = start_x#3
        self.start_y = start_y#4
        self.end_x = end_x#5
        self.end_y = end_y#6
        self.distance = distance#7

        self.axial_force1 = axial_force1#8
        self.moment1 = moment1#9
        self.moment_mid = moment_mid#10
        self.moment2 = moment2#11
        self.shear_force1 = shear_force1#12
        self.displacement_total = displacement_total1#13
        self.displacement_x = displacement_x1#14
        self.displacement_y = displacement_y1#15
        self.axi_sym_force = axi_sym_force1#16
        self.axi_sym_moment = axi_sym_moment1#17
        self.beam_yield = bool(beam_yield1)#18
        self.temperature = temperature1#25

        self.axial_mid      = axial_force_mid
        self.axial_force2    = axial_force2

        self.shear_force_mid       = shear_force_mid
        self.shear_force2          = shear_force2

        self.displacement_total_mid       = displacement_total_mid
        self.displacement_total2          = displacement_total2

        self.displacement_x_mid       = displacement_x_mid
        self.displacement_x2          = displacement_x2

        self.displacement_y_mid       = displacement_y_mid
        self.displacement_y2          = displacement_y2

        self.axi_sym_force_mid       = axi_sym_force_mid
        self.axi_sym_force2          = axi_sym_force2

        self.axi_sym_moment_mid       = axi_sym_moment_mid
        self.axi_sym_moment2          = axi_sym_moment2

        self.beam_yield_mid       = beam_yield_mid
        self.beam_yield2          = beam_yield2

        self.temperature_mid       = temperature_mid
        self.temperature2          = temperature2

        ResetInvalid.validate(self)

class LinerResult:
    def __init__(self, entity_id, liner_element_results: LinerElementResult):
        self.entity_id = entity_id
        self.liner_element_results: LinerElementResult = liner_element_results