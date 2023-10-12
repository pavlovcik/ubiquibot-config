import unittest
from src import new_business_logic

class TestNewBusinessLogic(unittest.TestCase):
    def test_calculate(self):
        # Test with positive numbers
        result = new_business_logic.calculate(5, 3)
        self.assertEqual(result, 8)

        # Test with negative numbers
        result = new_business_logic.calculate(-5, -3)
        self.assertEqual(result, -8)

        # Test with zero
        result = new_business_logic.calculate(0, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
