import unittest
import Compress

class CompressTests(unittest.TestCase):

    def test_CompressReturnsEmptyArray_WhenEmptyArrayInputted(self):
        array = []
        result = Compress.compress(array)
        self.assertEqual(array, result)
    
    def test_CompressReturnsInputtedArray_WhenArrayHasNoDuplicates(self):
        array = ['a', 'b', 'c', 'd']
        result = Compress.compress(array)
        self.assertEqual(array, result)
    
    def test_CompressReturnsTwoElements_WhenArrayContainsOnlyOneCharacter(self):
        array = ['a', 'a', 'a', 'a']
        result = Compress.compress(array)
        self.assertEqual(['a', 4], result)
    
    def test_CompressReturnsCompressedArray_WhenArrayContainsDuplicates(self):
        array = ['a', 'a', 'b', 'c', 'c', 'c']
        result = Compress.compress(array)
        self.assertEqual(['a', 2, 'b', 'c', 3], result)