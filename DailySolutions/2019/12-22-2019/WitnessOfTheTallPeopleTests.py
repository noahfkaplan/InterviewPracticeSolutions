import unittest
import WitnessOfTheTallPeople

class WitnessOfTheTallPeopleTests(unittest.TestCase):

    def test_returns0_whenEmptyArray(self):
        array = []
        result = WitnessOfTheTallPeople.witnesses(array)
        self.assertEqual(result, len(array))

    def test_returns1_when1ElementInArray(self):
        array = [5]
        result = WitnessOfTheTallPeople.witnesses(array)
        self.assertEqual(result, len(array))

    def test_returnsN_whenArrayDecending(self):
        array = [5, 4, 3, 2, 1]
        result = WitnessOfTheTallPeople.witnesses(array)
        self.assertEqual(result, len(array))

    def test_returns1_whenArrayAscending(self):
        array = [1, 2, 3, 4, 5]
        result = WitnessOfTheTallPeople.witnesses(array)
        self.assertEqual(result, 1)

    def test_returnsCorrectNumber_whenMultiplePeopleCanSee(self):
        array = [3, 6, 3, 4, 1]
        result = WitnessOfTheTallPeople.witnesses(array)
        self.assertEqual(result, 3)