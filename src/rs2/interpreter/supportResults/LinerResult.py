from rs2.interpreter._UtilityResult import *

class LinerElementResult:

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
        axial_force_mid,
        axial_force2,
        moment1,
        moment_mid,
        moment2,
        shear_force1,
        shear_force_mid,
        shear_force2,
        axi_sym_force1, 
        axi_sym_force_mid,  
        axi_sym_force2, 
        axi_sym_moment1,
        axi_sym_moment_mid,
        axi_sym_moment2,
        displacement_total1,
        displacement_total_mid,
        displacement_total2,
        displacement_x1,
        displacement_x_mid, 
        displacement_x2,  
        displacement_y1,  
        displacement_y_mid,  
        displacement_y2, 
        temperature1,
        temperature_mid,
        temperature2,
        curvature1,
        curvature_mid,
        curvature2,
        axial_strain1,
        axial_strain_mid,
        axial_strain2,
        hoop_curvature_strain1,
        hoop_curvature_strain_mid,
        hoop_curvature_strain2,
        hoop_axial_strain1,
        hoop_axial_strain_mid,
        hoop_axial_strain2,    
        beam_yield,
    ):

        self.composite_layer = int(composite_layer)
        self.node_start = int(node_start)
        self.node_end = int(node_end)
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.distance = distance

        self.axial_force1 = axial_force1
        self.axial_mid = axial_force_mid
        self.axial_force2 = axial_force2

        self.moment1 = moment1
        self.moment_mid = moment_mid
        self.moment2 = moment2

        self.shear_force1 = shear_force1
        self.shear_force_mid = shear_force_mid
        self.shear_force2 = shear_force2

        self.axi_sym_force1 = axi_sym_force1
        self.axi_sym_force_mid = axi_sym_force_mid
        self.axi_sym_force2 = axi_sym_force2

        self.axi_sym_moment1 = axi_sym_moment1
        self.axi_sym_moment_mid = axi_sym_moment_mid
        self.axi_sym_moment2 = axi_sym_moment2

        self.displacement_total1 = displacement_total1
        self.displacement_total_mid = displacement_total_mid
        self.displacement_total2 = displacement_total2

        self.displacement_x1 = displacement_x1
        self.displacement_x_mid = displacement_x_mid
        self.displacement_x2 = displacement_x2

        self.displacement_y1 = displacement_y1
        self.displacement_y_mid = displacement_y_mid
        self.displacement_y2 = displacement_y2

        self.temperature1 = temperature1
        self.temperature_mid = temperature_mid
        self.temperature2 = temperature2
        
        self.curvature1 = curvature1
        self.curvature_mid = curvature_mid
        self.curvature2 = curvature2

        self.axial_strain1      = axial_strain1
        self.axial_strain_mid   = axial_strain_mid
        self.axial_strain2      = axial_strain2

        self.hoop_curvature_strain1    = hoop_curvature_strain1
        self.hoop_curvature_strain_mid = hoop_curvature_strain_mid
        self.hoop_curvature_strain2    = hoop_curvature_strain2
        
        self.hoop_axial_strain1        = hoop_axial_strain1
        self.hoop_axial_strain_mid     = hoop_axial_strain_mid
        self.hoop_axial_strain2        = hoop_axial_strain2

        self.beam_yield = bool(beam_yield)

        ResetInvalid.validate(self)


class LinerResult:
    def __init__(self, entity_id, liner_element_results: LinerElementResult):
        self.entity_id = entity_id
        self.liner_element_results: LinerElementResult = liner_element_results
