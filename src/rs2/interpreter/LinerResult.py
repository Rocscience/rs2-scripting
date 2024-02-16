from rs2.interpreter.UtilityResult import *

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

        self.axial_force = axial_force#8
        self.moment1 = moment1#9
        self.moment_mid = moment_mid#10
        self.moment2 = moment2#11
        self.shear_force = shear_force#12
        self.displacement_total = displacement_total#13
        self.displacement_x = displacement_x#14
        self.displacement_y = displacement_y#15
        self.axi_sym_force = axi_sym_force#16
        self.axi_sym_moment = axi_sym_moment#17
        self.beam_yield = bool(beam_yield)#18
        self.temperature = temperature#25
        ResetInvalid.validate(self)

class LinerResult:
    def __init__(self, entity_id, liner_element_results):
        self.entity_id = entity_id
        self.liner_element_results = liner_element_results