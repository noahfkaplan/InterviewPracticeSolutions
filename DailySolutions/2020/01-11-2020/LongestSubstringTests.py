import unittest
import LongestSubstring

class LongestSubstringTests(unittest.TestCase):

    def test_returnsZero_WhenEmptySubstring(self):
        s = ''
        k = 1
        result = LongestSubstring.longest_substring_with_k_distinct_characters(s, k)
        self.assertEqual(result, 0)

    def test_returnsK_WhenSubstringHasNoDuplicateCharacters(self):
        s = 'abcdefghijk'
        k = 5
        result = LongestSubstring.longest_substring_with_k_distinct_characters(s, k)
        self.assertEqual(result, 5)

    def test_returnsLengthOfString_WhenKLargerThanString(self):
        s = 'abc'
        k = 4
        result = LongestSubstring.longest_substring_with_k_distinct_characters(s, k)
        self.assertEqual(result, 3)

    def test_returnsLongestSubstring_WhenKSmallerThanString(self):
        s = 'aabcdefff'
        k = 3
        result = LongestSubstring.longest_substring_with_k_distinct_characters(s, k)
        self.assertEqual(result, 5)

    def test_returnsLongestSubstring_WhenAlternatingRepeatingCharacters(self):
        s = 'jbcbdabababd'
        k = 3
        result = LongestSubstring.longest_substring_with_k_distinct_characters(s, k)
        self.assertEqual(result, 9)

    def test_containsCharacterReturnsNegativeOne_WhenArrayEmpty(self):
        array = []
        character = 'a'
        result = LongestSubstring.containsCharacter(array, character)
        self.assertEqual(result, -1)
    
    def test_containsCharacterReturnsNegativeOne_WhenValueNotInTuple(self):
        array = [('a', 1), ('b', 1), ('c', 1)]
        character = 'd'
        result = LongestSubstring.containsCharacter(array, character)
        self.assertEqual(result, -1)

    def test_containCharacterReturnsIndexOfValue_WhenValueInTuple(self):
        array = [('a', 1), ('b', 1), ('c', 1)]
        character = 'a'
        result = LongestSubstring.containsCharacter(array, character)
        self.assertEqual(result, 0)