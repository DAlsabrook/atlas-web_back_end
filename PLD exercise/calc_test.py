import unittest
from calc import Calculator


class Calc_test(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_add(self):
        value1 = 1.1
        value2 = 1.1
        sum = self.calculator.add(value1, value2)
        self.assertEqual(sum, 2.2)


if __name__ == '__main__':
    unittest.main()

