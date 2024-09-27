from enum import Enum, auto
class HistoryQueryGraphEnums():
    """
    Set the history query graph.
    
    """


    class VerticalAxisTypes(Enum):
        HORIZONTAL_DISPLACEMENT = 4070
        VERTICAL_DISPLACEMENT = 4071
        HORIZONTAL_VELOCITY = 4072
        VERTICAL_VELOCITY = 4073
        HORIZONTAL_ACCELERATION = 4074
        VERTICAL_ACCELERATION = 4075
        EFFECTIVE_STRESS_XX = 4076
        EFFECTIVE_STRESS_YY = 4077
        EFFECTIVE_STRESS_XY = 4078
        EFFECTIVE_STRESS_Z = 4079
        STRAIN_XX = 4080
        STRAIN_YY = 4081
        STRAIN_XY = 4082
        # Water
        EXCESS_PORE_PRESSURE = 4083
        PORE_PRESSURE = 4084
        HORIZONTAL_HYDRAULIC_VELOCITY = 4085
        VERTICAL_HYDRAULIC_VELOCITY = 4086
        HORIZONTAL_HYDRAULIC_GRADIENT = 4087
        VERTICAL_HYDRAULIC_GRADIENT = 4088
        # Temperature
        TEMPERATURE = 4089
        HORIZONTAL_THERMAL_FLUX = 4090
        VERTICAL_THERMAL_FLUX = 4091
        HORIZONTAL_THERMAL_GRADIENT = 4092
        VERTICAL_THERMAL_GRADIENT = 4093
        
    class HorizontalAxisTypes(Enum):
        TIME = 9094
        STAGE_LOAD_PERCENTAGE = 9096

class TimeQueryGraphEnums():
    """
    Set the time query graph.
    
    """
    class VerticalAxisTypes(Enum):
        X_VELOCITY = 4041
        X_DISPLACEMENT = 4042
        X_ACCELERATION = 4043
        Y_VELOCITY = 4044
        Y_DISPLACEMENT = 4045
        Y_ACCELERATION = 4046
        PORE_PRESSURE = 4050
        STRAIN_XX = 4055
        STRAIN_YY = 4056
        STRAIN_XY = 4057
        TOTAL_STRESS_XX = 4058
        TOTAL_STRESS_YY = 4059
        TOTAL_STRESS_XY = 4060
        TOTAL_STRESS_ZZ = 4061
        EFFECTIVE_STRESS_XX = 4062
        EFFECTIVE_STRESS_YY = 4063
        EFFECTIVE_STRESS_XY = 4064
        EFFECTIVE_STRESS_ZZ = 4065
