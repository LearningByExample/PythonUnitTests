from types import *


class Calc(object):
    _last_result = None
    _last_operation = None
    _sum = lambda self, a, b: a + b
    _sub = lambda self, a, b: a - b

    def operation(self, function, a, b):
        if not (type(a) is IntType):
            raise TypeError("a is not a number")
        if not (type(b) is IntType):
            raise TypeError("b is not a number")
        if not ((type(function) is MethodType) or (type(function) is FunctionType)):
            raise TypeError("function is not a function")

        self._last_result = function(a, b)
        self._last_operation = function

        return self._last_result

    def sum(self, a, b):
        return self.operation(self._sum, a, b)

    def sub(self, a, b):
        return self.operation(self._sub, a, b)

    def result(self):
        return self._last_result

    def repeat(self, a, b):
        return self.operation(self._last_operation, a, b)
