import unittest
import SortedAlphabetically

class SortedAlphabeticallyTests(unittest.TestCase):
    
    def test_isSortedReturnsFalse_WhenEmptyArrayInputted(self):
        strings = []
        sortOrder = 'zyxwvutsrqponmlkjihgfedcba'
        result = SortedAlphabetically.isSorted(strings, sortOrder)
        self.assertFalse(result)

    def test_isSortedReturnsTrue_WhenSingleElementInputted(self):
        strings = ['abcd']
        sortOrder = 'zyxwvutsrqponmlkjihgfedcba'
        result = SortedAlphabetically.isSorted(strings, sortOrder)
        self.assertTrue(result)

    def test_isSortedReturnsTrue_WhenAllElementsAreEqual(self):
        strings = ['abcd', 'abcd']
        sortOrder = 'zyxwvutsrqponmlkjihgfedcba'
        result = SortedAlphabetically.isSorted(strings, sortOrder)
        self.assertTrue(result)

    def test_isSortedReturnsTrue_WhenTwoElementsAreSorted(self):
        strings = ['zbc', 'abcd']
        sortOrder = 'zyxwvutsrqponmlkjihgfedcba'
        result = SortedAlphabetically.isSorted(strings, sortOrder)
        self.assertTrue(result)

    def test_isSortedReturnsTrue_WhenMoreThanTwoElementsAreSorted(self):
        strings = ['zzbc', 'zbc', 'abcd']
        sortOrder = 'zyxwvutsrqponmlkjihgfedcba'
        result = SortedAlphabetically.isSorted(strings, sortOrder)
        self.assertTrue(result)

    def test_isSortedReturnsFalse_WhenTwoElementsNotSorted(self):
        strings = ['abcd', 'zbc']
        sortOrder = 'zyxwvutsrqponmlkjihgfedcba'
        result = SortedAlphabetically.isSorted(strings, sortOrder)
        self.assertFalse(result)

    def test_isSortedReturnsFalse_WhenMoreThanTwoElementsNotSorted(self):
        strings = ['abcd', 'zzbc', 'zbc']
        sortOrder = 'zyxwvutsrqponmlkjihgfedcba'
        result = SortedAlphabetically.isSorted(strings, sortOrder)
        self.assertFalse(result)

    def test_isSortedReturnsTrue_WhenLaterWordsBeginWithPreviousWords(self):
        strings = ['he', 'heat', 'heater']
        sortOrder = 'zyxwvutsrqponmlkjihgfedcba'
        result = SortedAlphabetically.isSorted(strings, sortOrder)
        self.assertTrue(result)
    
    def test_isSortedReturnsFalse_WhenPreviousWordsBeginWithLaterWords(self):
        strings = ['heater', 'heat', 'he']
        sortOrder = 'zyxwvutsrqponmlkjihgfedcba'
        result = SortedAlphabetically.isSorted(strings, sortOrder)
        self.assertFalse(result)

    def test_isSortedReturnsTrue_WhenMoreThanTwoWordsSortedUsingRandomSortOrder(self):
        strings = ['wtyu', 'wygq', 'fghj']
        sortOrder = 'qwertyuiopasdfghjklzxcvbnm'
        result = SortedAlphabetically.isSorted(strings, sortOrder)
        self.assertTrue(result)
        
    def test_isSortedReturnsFalse_WhenMoreThanTwoWordsSortedUsingRandomSortOrder(self):
        strings = ['wtyu', 'fghj', 'wygq']
        sortOrder = 'qwertyuiopasdfghjklzxcvbnm'
        result = SortedAlphabetically.isSorted(strings, sortOrder)
        self.assertFalse(result)