import unittest
import MergeOverlappingIntervals

class MergeOverlappingIntervalsTests(unittest.TestCase):

    def test_returnsEmptyArray_WhenNoInputtedIntervals(self):
        array = []
        result = MergeOverlappingIntervals.merge(array)
        self.assertEqual(array, result)
    
    def test_returnsInputtedArray_WhenInputContains1Interval(self):
        array = [(1, 10)]
        result = MergeOverlappingIntervals.merge(array)
        self.assertEqual(array, result)

    def test_mergesOverlappingIntervals_WhenInputContainsOverlappingIntervals(self):
        array = [(1, 3), (5, 8), (4, 10), (20, 25)]
        result = MergeOverlappingIntervals.merge(array)
        self.assertEqual(result, [(1, 3), (4, 10), (20, 25)])

    def test_mergesOverlappingIntervals_WhenInputNotSorted(self):
        array = [(5, 8), (4, 10), (20, 25), (1, 3)]
        result = MergeOverlappingIntervals.merge(array)
        self.assertEqual(result, [(1, 3), (4, 10), (20, 25)])

    def test_mergesOverlappingIntervals_When1IntervalContainsAllOthers(self):        
        array = [(5, 8), (4, 10), (20, 25), (1, 3), (0, 26)]
        result = MergeOverlappingIntervals.merge(array)
        self.assertEqual(result, [(0, 26)])
