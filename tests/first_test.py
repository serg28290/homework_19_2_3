from scripts.skillfactory.homework_19_2_3.app.calculator import Calculator


class TestCalc(Calculator):
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(2, 2) == 4

    def test_division_calculate_correctly(self):
        assert self.calc.division(6, 3) == 2

    def test_multiply_subtraction_correctly(self):
        assert self.calc.subtraction(5, 4) == 1

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(8, 2) == 10
