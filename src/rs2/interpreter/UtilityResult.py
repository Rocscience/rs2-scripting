import sys

class ResetInvalid:
	# used by interpretor
    flt_max = 3.402823466e+38

    @staticmethod
    def validate(self):
        for key, value in vars(self).items():
            if isinstance(value, (int, float)) and value == sys.float_info.max:
                setattr(self, key, None)
        pass
    @staticmethod
    def validate_double(value):
        if isinstance(value, float) and (value >= ResetInvalid.flt_max):
            value = None
        return value



