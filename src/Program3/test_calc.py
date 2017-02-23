from unittest import TestCase
from hamcrest import *
from types import *

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
        assert_that(calc.result(), is_(3), is_(result))

    def test_operation(self):
        calc = Calc()

        mult = lambda a, b: a * b
        result = calc.operation(mult, 5, 5)

        assert_that(result, is_(25))
        assert_that(calc._last_operation, is_(mult), is_(type(LambdaType)))

    def test_repeat(self):
        calc = Calc()

        result = calc.sum(1, 2)
        assert_that(result, is_(calc.result()))

        result = calc.repeat(2, 2)
        assert_that(result, is_(4))
