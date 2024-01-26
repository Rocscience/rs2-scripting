class BeamResult:
    def __init__(self, node_start, node_end, start_x, start_y, end_x, end_y, distance,axial_force, moment1, moment_mid, moment2, shear_force, displacement_total, displacement_x, displacement_y,
                 axi_sym_force, axi_sym_moment, comp_j_norm_stress, comp_j_shear_stress,
                 comp_j_norm_displace, comp_j_shear_displace,yielded, temperature):

        self.node_start = node_start
        self.node_end = node_end
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.distance = distance

        self.beam_axial_force = axial_force
        self.beam_moment1 = moment1
        self.beam_moment_mid = moment_mid
        self.beam_moment2 = moment2
        self.beam_shear_force = shear_force
        self.beam_displacement_total = displacement_total
        self.beam_displacement_x = displacement_x
        self.beam_displacement_y = displacement_y
        self.beam_axi_sym_force = axi_sym_force
        self.beam_axi_sym_moment = axi_sym_moment
        self.beam_comp_j_norm_stress = comp_j_norm_stress
        self.beam_comp_j_shear_stress = comp_j_shear_stress
        self.beam_comp_j_norm_displace = comp_j_norm_displace
        self.beam_comp_j_shear_displace = comp_j_shear_displace
        self.yielded = yielded

        self.beam_temperature = temperature


