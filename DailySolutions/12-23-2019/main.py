import CoursePrerequisites

courses = {
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}

x = CoursePrerequisites.courses_to_take(courses)
print(x)