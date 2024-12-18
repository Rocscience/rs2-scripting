from enum import Enum, auto
class ExportResultType(Enum):
	SOLID_TOTAL_STRESS_SIGMA_ONE = "INTERPRET_SIGMA_ONE"
	SOLID_TOTAL_STRESS_SIGMA_THREE = "INTERPRET_SIGMA_THREE"
	SOLID_TOTAL_STRESS_SIGMA_Z = "INTERPRET_SIGMA_ZED"
	STRENGTH_FACTOR = "INTERPRET_STRENGTH_FACTORS"
	SOLID_DISPLACEMENT_HORIZONTAL_DISPLACEMENT_ABS = "INTERPRET_X_DISP_ABS"
	SOLID_DISPLACEMENT_VERTICAL_DISPLACMENT_ABS = "INTERPRET_Y_DISP_ABS"
	SOLID_DISPLACEMENT_TOTAL_DISPLACEMENT = "INTERPRET_TOTAL_DISPLACE"
	STRENGTH_FACTOR_WITH_UBIQUITOUS_JOINTS = "INTERPRET_UBIQUITOUS"
	SOLID_EFFECTIVE_STRESS_EFFECTIVE_SIGMA_ONE = "INTERPRET_SIGMA_ONE_EFF"
	SOLID_EFFECTIVE_STRESS_EFFECTIVE_SIGMA_THREE = "INTERPRET_SIGMA_THREE_EFF"
	SOLID_EFFECTIVE_STRESS_EFFECTIVE_SIGMA_Z = "INTERPRET_SIGMA_Z_EFF"
	SEEPAGE_PORE_PRESSURE = "INTERPRET_PORE_PRESSURE"
	SEEPAGE_EXCESS_PORE_PRESSURE = "INTERPRET_EXCESS_PWP"
	SEEPAGE_DEGREE_OF_SATURATION = "INTERPRET_DEGREE_SATURATION"
	SEEPAGE_PRESSURE_HEAD = "INTERPRET_PRESSUREHEAD"
	SEEPAGE_TOTAL_HEAD = "INTERPRET_TOTAL_HEAD"
	SEEPAGE_HORIZONTAL_DISCHARGE_VELOCITY = "INTERPRET_X_FLUX_SIGNED"
	SEEPAGE_VERTICAL_DISCHARGE_VELOCITY = "INTERPRET_Y_FLUX_SIGNED"
	SEEPAGE_HORIZONTAL_DISCHARGE_VELOCITY_ABS = "INTERPRET_X_FLUX_ABS"
	SEEPAGE_VERTICAL_DISCHARGE_VELOCITY_ABS = "INTERPRET_Y_FLUX_ABS"
	SEEPAGE_TOTAL_DISCHARGE_VELOCITY = "INTERPRET_TOTAL_FLUX"
	SEEPAGE_HORIZONTAL_HYDRAULIC_GRADIENT_ABS = "INTERPRET_HYD_GRAD_X_ABS"
	SEEPAGE_VERTICAL_HYDARULIC_GRADIENT_ABS = "INTERPRET_HYD_GRAD_Y_ABS"
	SEEPAGE_HORIZONTAL_HYDRAULIC_GRADIENT = "INTERPRET_HYD_GRAD_X_SIGNED"
	SEEPAGE_VERTICAL_HYDARULIC_GRADIENT = "INTERPRET_HYD_GRAD_Y_SIGNED"
	SEEPAGE_TOTAL_HYDRAULIC_GRADIENT = "INTERPRET_HYD_GRAD_TOTAL"
	SEEPAGE_HORIZONTAL_PERMEABILITY = "INTERPRET_PERMEABILITY_X"
	SEEPAGE_VERTICAL_PERMEABILITY = "INTERPRET_PERMEABILITY_Y"
	SEEPAGE_SPATIAL_PERM = "INTERPRET_SPATIAL_PERM"
	SEEPAGE_SPATIAL_WC = "INTERPRET_SPATIAL_WC"
	SEEPAGE_SPATIAL_WC_RES = "INTERPRET_SPATIAL_WC_R"
	SEEPAGE_SPATIAL_CONDY = "INTERPRET_SPATIAL_CONDY"
	SEEPAGE_SPATIAL_ANGLE= "INTERPRET_SPATIAL_ANGLE"
	SEEPAGE_YIELDED_ELEMENTS = "INTERPRET_YIELDED_ELEMENTS"
	SOLID_STRAIN_VOLUMETRIC_STRAIN = "INTERPRET_STRAIN_VOLUMETRIC"
	SOLID_STRAIN_MAX_SHEAR_STRAIN = "INTERPRET_STRAIN_MAX_SHEAR"
	SOLID_DISPLACEMENT_HORIZONTAL_DISPLACEMENT = "INTERPRET_X_DISP_SIGNED"
	SOLID_DISPLACEMENT_VERTICAL_DISPLACEMENT = "INTERPRET_Y_DISP_SIGNED"
	SOLID_TOTAL_STRESS_MEAN_STRESS = "INTERPRET_STRESS_P"
	SOLID_TOTAL_STRESS_VON_MISES_STRESS = "INTERPRET_STRESS_Q"
	SOLID_EFFECTIVE_STRESS_EFFECTIVE_MEAN_STRESS = "INTERPRET_STRESS_P_EFF"
	SOLID_EFFECTIVE_STRESS_EFFECTIVE_VON_MISES_STRESS = "INTERPRET_STRESS_Q_EFF"
	SOLID_TOTAL_STRESS_SIGMA_XX = "INTERPRET_SIGMA_XX"
	SOLID_TOTAL_STRESS_SIGMA_YY = "INTERPRET_SIGMA_YY"
	SOLID_TOTAL_STRESS_SIGMA_XY = "INTERPRET_SIGMA_XY"
	SOLID_EFFECTIVE_STRESS_EFFECTIVE_SIGMA_XX = "INTERPRET_SIGMA_XX_EFF"
	SOLID_EFFECTIVE_STRESS_EFFECTIVE_SIGMA_YY = "INTERPRET_SIGMA_YY_EFF"
	SOLID_EFFECTIVE_STRESS_EFFECTIVE_SIGMA_XY = "INTERPRET_SIGMA_XY_EFF"
	SOLID_TOTAL_STRESS_DIFFERENTIAL_STRESS = "INTERPRET_STRESS_DIFFERENTIAL"
	SOLID_STRAIN_STRAIN_XX = "INTERPRET_STRAIN_XX"
	SOLID_STRAIN_STRAIN_YY = "INTERPRET_STRAIN_YY"
	SOLID_STRAIN_STRAIN_ZZ = "INTERPRET_STRAIN_ZZ"
	SOLID_STRAIN_STRAIN_XY = "INTERPRET_STRAIN_XY"
	SOLID_STRAIN_MAJOR_PRINCIPAL_STRAIN = "INTERPRET_STRAIN_P_MAJOR"
	SOLID_STRAIN_MEAN_PRINCIPAL_STRAIN = "INTERPRET_STRAIN_P_MEAN"
	SOLID_STRAIN_MINOR_PRINCIPAL_STRAIN = "INTERPRET_STRAIN_P_MINOR"
	PLASTIC_STRAIN_XX = "INTERPRET_PLASTIC_STRAIN_XX"
	PLASTIC_STRAIN_YY = "INTERPRET_PLASTIC_STRAIN_YY"
	PLASTIC_STRAIN_ZZ = "INTERPRET_PLASTIC_STRAIN_ZZ"
	PLASTIC_STRAIN_XY = "INTERPRET_PLASTIC_STRAIN_XY"
	PLASTIC_STRAIN_MAJOR_PRICIPAL_PLASTIC_STRAIN = "INTERPRET_PLASTIC_STRAIN_P_MAJOR"
	PLASTIC_STRAIN_MEAN_PRINCIPAL_PLASTIC_STRAIN = "INTERPRET_PLASTIC_STRAIN_P_MEAN"
	PLASTIC_STRAIN_MINOR_PRINCIPAL_PLASTIC_STRAIN = "INTERPRET_PLASTIC_STRAIN_P_MINOR"
	PLASTIC_STRAIN_VOLUMETRIC_PLASTIC_STRAIN = "INTERPRET_PLASTIC_STRAIN_VOLUMETRIC"
	PLASTIC_STRAIN_MAX_SHEAR_PLASTIC_STRAIN = "INTERPRET_PLASTIC_STRAIN_MAX_SHEAR"
	THERMAL_TEMPERATURE = "INTERPRET_TEMPERATURE"
	THERMAL_HORIZONTAL_FLUX = "INTERPRET_THERMO_X_FLUX_SIGNED"
	THERMAL_VERTICAL_FLUX = "INTERPRET_THERMO_Y_FLUX_SIGNED"
	THERMAL_TOTAL_FLUX = "INTERPRET_THERMO_TOTAL_FLUX"
	THERMAL_HORIZONTAL_GRADIENT = "INTERPRET_THERMO_GRAD_X_SIGNED"
	THERMAL_VERTICAL_GRADIENT = "INTERPRET_THERMO_GRAD_Y_SIGNED"
	THERMAL_TOTAL_GRADIENT = "INTERPRET_THERMO_GRAD_TOTAL"
	THERMAL_HORIZONTAL_CONDUCTIVITY = "INTERPRET_THERMO_CONDUCTIVITY_X_SIGNED"
	THERMAL_VERTICAL_CONDUCTIVITY = "INTERPRET_THERMO_CONDUCTIVITY_Y_SIGNED"
	THERMAL_TOTAL_CONDUCTIVITY = "INTERPRET_THERMO_CONDUCTIVITY_TOTAL"
	THERMAL_SPECIFIC_HEAT = "INTERPRET_SPECIFIC_HEAT"
	THERMAL_UNFROZEN_WATER_CONTENT = "INTERPRET_UNFROZEN_WATER_CONTENT"
	DYNAMIC_MINIMUM_X_DISPLACEMENT = "INTERPRET_DYN_MIN_DISPLACEMENT_X"
	DYNAMIC_MAXIMUM_X_DISPLACEMENT = "INTERPRET_DYN_MAX_DISPLACEMENT_X"
	DYNAMIC_MINIMUM_Y_DISPLACEMENT = "INTERPRET_DYN_MIN_DISPLACEMENT_Y"
	DYNAMIC_MAXIMUM_Y_DISPLACEMENT = "INTERPRET_DYN_MAX_DISPLACEMENT_Y"
	DYNAMIC_MINIMUM_X_VELOCITY = "INTERPRET_DYN_MIN_VELOCITY_X"
	DYNAMIC_MAXIMUM_X_VELOCITY = "INTERPRET_DYN_MAX_VELOCITY_X"
	DYNAMIC_MINIMUM_Y_VELOCITY = "INTERPRET_DYN_MIN_VELOCITY_Y"
	DYNAMIC_MAXIMUM_Y_VELOCITY = "INTERPRET_DYN_MAX_VELOCITY_Y"
	DYNAMIC_MINIMUM_X_ACCELERATION = "INTERPRET_DYN_MIN_ACCELERATION_X"
	DYNAMIC_MAXIMUM_X_ACCELERATION = "INTERPRET_DYN_MAX_ACCELERATION_X"
	DYNAMIC_MINIMUM_Y_ACCELERATION = "INTERPRET_DYN_MIN_ACCELERATION_Y"
	DYNAMIC_MAXIMUM_Y_ACCELERATION = "INTERPRET_DYN_MAX_ACCELERATION_Y"