import unittest
import CoursePrerequisites

class CoursePrerequisitesTest(unittest.TestCase):

    def test_returnsEmptySet_WhenCourseListEmpty(self):
        courses = []
        result = CoursePrerequisites.courses_to_take(courses)
        self.assertEqual(result, [])

    def test_returnsEmptySet_WhenCourseIsItsOwnPrereq(self):
        courses = {
            'CSC100': ['CSC100'],
        }
        result = CoursePrerequisites.courses_to_take(courses)
        self.assertEqual(result, [])

    def test_returnsEmptySet_WhenCoursesHaveCircularPrerequisites(self):
        courses = {
            'CSC300': ['CSC200'], 
            'CSC200': ['CSC300'],
        }
        result = CoursePrerequisites.courses_to_take(courses)
        self.assertEqual(result, [])

    def test_returnsOrderedList_WhenMultipleCoursesWithPrereqsInputted(self):
        courses = {
            'CSC300': ['CSC100', 'CSC200'], 
            'CSC200': ['CSC100'], 
            'CSC100': []
        }
        result = CoursePrerequisites.courses_to_take(courses)
        self.assertEqual(result, ['CSC100', 'CSC200', 'CSC300'])