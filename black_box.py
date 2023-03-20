import unittest

# Test driven development

def sum(num_1, num_2):
    # return abs(num_1 + num_2) # error
    return num_1 + num_2

class BlackBoxTest(unittest.TestCase):
    def test_sum_two_positive_numbers(self):
        # Arrange
        num_1 = 10
        num_2 = 5

        result = sum(num_1, num_2)
        self.assertEqual(result, 15)

    def test_sum_two_negative_numbers(self):
        # Arrange
        num_1 = -10
        num_2 = -7

        result = sum(num_1, num_2)
        self.assertEqual(result, -17)

if __name__ == '__main__':
    unittest.main()