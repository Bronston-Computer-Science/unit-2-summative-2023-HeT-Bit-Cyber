import unit_conversion

class TestConversion:
    
    @staticmethod
    def test_convert_length():
        assert unit_conversion.convert_length(10) == 32
        assert unit_conversion.convert_length(5) == 16
        assert unit_conversion.convert_length(43) == 137.6
    
    @staticmethod
    def test_convert_temperature():
        assert unit_conversion.convert_temperature(0) == 32
    
    @staticmethod
    def test_convert_weight():
        assert unit_conversion.convert_weight(10) == 22
        assert unit_conversion.convert_weight(5) == 11
        assert (unit_conversion.convert_weight(43) >= 94.6) & (unit_conversion.convert_weight(43) <= 94.7)