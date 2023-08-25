import basic_math

class TestMath:
    
    @staticmethod
    def test_add():
        assert basic_math.add(1,2) == 3
        assert basic_math.add(5,2) == 7
        assert basic_math.add(25,28) == 53
    
    @staticmethod
    def test_subtract():
        assert basic_math.subtract(1,2) == -1
        assert basic_math.subtract(100,2) == 98
        assert basic_math.subtract(54,35) == 19
    
    @staticmethod
    def test_multiply():
        assert basic_math.multiply(1,2) == 2
        assert basic_math.multiply(20,2) == 40
        assert basic_math.multiply(100,15) == 1500
    
    @staticmethod
    def test_divide():
        assert basic_math.divide(1,1) == 1
        assert basic_math.divide(8,2) == 4
        assert basic_math.divide(25,5) == 5