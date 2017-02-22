from unittest import TestCase
from hamcrest import *
from calc import Calc


class TestCal(TestCase):
    def test_sum(self):
        calculator = Calc()
        result = calculator.sum(1, 2)
        assert_that(result, is_(3))

    def test_sub(self):
        calculator = Calc()
        result = calculator.sub(1, 2)
        assert_that(result, is_(-1))

    def test_result(self):
        calc = Calc()
        result = calc.sum(1, 2)
        assert_that(result, is_(3), is_(result))
