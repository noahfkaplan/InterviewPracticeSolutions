import unittest
import RainWaterCapacity

class RainWaterCapacityTests(unittest.TestCase):

    def test_returnsZero_WhenEmptyArrayInputted(self):
        array = []        
        result = RainWaterCapacity.capacity(array)
        self.assertEqual(result, 0)

    def test_returnsZero_WhenLevelArrayInputted(self):
        array = [1,1,1,1,1]
        result = RainWaterCapacity.capacity(array)
        self.assertEqual(result, 0)

    def test_returnsZero_WhenDescendingArrayInputted(self):
        array = [0,1,2,3,4]
        result = RainWaterCapacity.capacity(array)
        self.assertEqual(result, 0)

    def test_returnsZero_WhenAscendingArrayInputted(self):
        array = [4,3,2,1,0]
        result = RainWaterCapacity.capacity(array)
        self.assertEqual(result, 0)

    def test_returnsPositiveNumber_WhenArrayDescendsThenAscends(self):
        array = [1,0,1]
        result = RainWaterCapacity.capacity(array)
        self.assertEqual(result, 1)
    
    def test_returnsCorrectCapacity_WhenValidArrayInputted(self):
        array = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        result = RainWaterCapacity.capacity(array)
        self.assertEqual(result, 6)