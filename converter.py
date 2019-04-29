class Converter:

    @staticmethod
    def convert_unit(value_in, unit_of_measurement_in='meters'):
        if unit_of_measurement_in.lower() != 'meters':
            new_value = (value_in / 1.0936132983)
            return new_value
        else:
            return value_in
