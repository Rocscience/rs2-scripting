class BeamResult:
    def __init__(self,composite_layer, node_start, node_end, start_x, start_y, end_x, end_y, distance,axial_force, moment1, moment_mid, moment2, shear_force, displacement_total, displacement_x, displacement_y,
                 axi_sym_force, axi_sym_moment,beam_yield,comp_layer, comp_j_norm_stress, comp_j_shear_stress,
                 comp_j_norm_displace, comp_j_shear_displace,joint_yielded, temperature):

        self.composite_layer = composite_layer #0
        self.node_start = node_start #1
        self.node_end = node_end#2
        self.start_x = start_x#3
        self.start_y = start_y#4
        self.end_x = end_x#5
        self.end_y = end_y#6
        self.distance = distance#7

        self.beam_axial_force = axial_force#8
        self.beam_moment1 = moment1#9
        self.beam_moment_mid = moment_mid#10
        self.beam_moment2 = moment2#11
        self.beam_shear_force = shear_force#12
        self.beam_displacement_total = displacement_total#13
        self.beam_displacement_x = displacement_x#14
        self.beam_displacement_y = displacement_y#15
        self.beam_axi_sym_force = axi_sym_force#16
        self.beam_axi_sym_moment = axi_sym_moment#17
        self.beam_yield = beam_yield#18
        self.comp_layer = comp_layer#19
        self.beam_comp_j_norm_stress = comp_j_norm_stress#20
        self.beam_comp_j_shear_stress = comp_j_shear_stress#21
        self.beam_comp_j_norm_displace = comp_j_norm_displace#22
        self.beam_comp_j_shear_displace = comp_j_shear_displace#23
        self.joint_yielded = joint_yielded #24

        self.beam_temperature = temperature#25


