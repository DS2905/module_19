import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self): #позитивный тест на умножение
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_calculation_failed(self): #негативный тест на умножение
        assert self.calc.multiply(self, 2, 2) == 5

    def test_multiply_calculate_correctly(self): #позитивный тест на сложение
        assert self.calc.adding(self, 2, 3) == 5

    def test_multiply_calculate_correctly(self): #позитивный тест на вычитание
        assert self.calc.subtraction(self, 7, 6) == 1

    def test_multiply_calculate_correctly(self): #позитивнй тест на деление
        assert self.calc.division(self, 8, 4) == 2