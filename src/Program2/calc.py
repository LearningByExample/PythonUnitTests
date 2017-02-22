class Calc(object):
    _last_result = None

    def operation(self, result):
        self._last_result = result
        return self._last_result

    def sum(self, a, b):
        return self.operation(a + b)

    def sub(self, a, b):
        return self.operation(a - b)

    def result(self):
        return self._last_result
