import unittest
import BuddyStrings

class BuddyStringsTests(unittest.TestCase):

    def test_returnsFalse_WhenBothStringsEmpty(self):
        A = ''
        B = ''
        result = BuddyStrings.buddyStrings(A, B)
        self.assertEqual(result, False)
        
    def test_returnsFalse_WhenStringsAreEqualAndContainNoDuplicateLetters(self):
        A = 'ab'
        B = 'ab'
        result = BuddyStrings.buddyStrings(A, B)
        self.assertEqual(result, False)

    def test_returnsFalse_WhenStringsDifferentLength(self):
        A = 'ab'
        B = 'abc'
        result = BuddyStrings.buddyStrings(A, B)
        self.assertEqual(result, False)

    def test_returnsTrue_WhenStringsAreEqualAndContainDuplicateLetters(self):
        A = 'aa'
        B = 'aa'
        result = BuddyStrings.buddyStrings(A, B)
        self.assertEqual(result, True)

    def test_returnsTrue_WhenCharactersToBeSwappedNextToEachother(self):
        A = 'ab'
        B = 'ba'
        result = BuddyStrings.buddyStrings(A, B)
        self.assertEqual(result, True)

    def test_returnsTrue_WhenCharactersToBeSwappedNotNextToEachother(self):
        A = 'aaaaabac'
        B = 'aaaaacab'
        result = BuddyStrings.buddyStrings(A, B)
        self.assertEqual(result, True)
