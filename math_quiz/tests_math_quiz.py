import unittest
from mathQuiz import getRandomInteger, getRandomOperator, getMathProblem


class TestMathGame(unittest.TestCase):

    def test_getRandomInteger(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = getRandomInteger(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_getRandomOperator(self):
        # TODO
        pass

    def test_getMathProblem(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                ''' TODO add more test cases here '''
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                pass

if __name__ == "__main__":
    unittest.main()
