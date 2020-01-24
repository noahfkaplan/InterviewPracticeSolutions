import unittest
import reverseWords

class reverseWordsTests(unittest.TestCase):

    def test_ReturnsEmptyString_WhenEmptyStringInputted(self):
        string = ''
        result = reverseWords.reverse(string)
        self.assertEqual(result, '')

    def test_ReturnsReversedWord_WhenOneWordInputted(self):
        string = 'reverse'
        result = reverseWords.reverse(string)
        self.assertEqual(result, 'esrever')

    def test_ReturnsAllWordsReversed_WhenMultipleWordsInputted(self):
        string = 'reverse this sentence'
        result = reverseWords.reverse(string)
        self.assertEqual(result, 'esrever siht ecnetnes')