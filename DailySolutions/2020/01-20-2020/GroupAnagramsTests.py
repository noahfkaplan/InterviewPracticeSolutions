import unittest
import GroupAnagrams

class GroupAnagramsTests(unittest.TestCase):

    def test_returnsEmptyArray_WhenEmptyArrayInputted(self):
        strings = []
        result = GroupAnagrams.groupAnagramWords(strings)
        self.assertEqual(result, [])

    def test_returnsArrayWithOneSubArray_WhenOneStringInputted(self):
        strings = ['abc']
        result = GroupAnagrams.groupAnagramWords(strings)
        self.assertEqual(result, [['abc']])

    def test_returnsArrayWithOneSubArray_WhenAllStringsAnagrams(self):
        strings = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        result = GroupAnagrams.groupAnagramWords(strings)
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0]), len(strings))

    def test_returnsSubArrayForEachString_WhenNoStringsAnagrams(self):
        strings = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr']
        result = GroupAnagrams.groupAnagramWords(strings)
        self.assertEqual(len(result), 6)
        for subarray in result:
            self.assertEqual(len(subarray), 1)

    def test_returnsMultipleSubArrays_WhenMultipleAnagramSets(self):
        strings = ['abc', 'bcd', 'cba', 'cbd', 'efg']
        result = GroupAnagrams.groupAnagramWords(strings)
        self.assertEqual(len(result), 3)
    
    def test_returnsMultipleSubArrays_WhenSameCharacterAndDifferentLengths(self):
        strings = ['aaa', 'aaaa', 'bbb', 'bbbb']
        result = GroupAnagrams.groupAnagramWords(strings)
        self.assertEqual(len(result), 4)
        for subarray in result:
            self.assertEqual(len(subarray), 1)