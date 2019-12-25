def courses_to_take(course_to_prereqs):
    orderedCourses = []
    sorted = False
    while not sorted:
        solutionExists = False
        for course in course_to_prereqs:
            prereqsMet = True
            for prereq in course_to_prereqs[course]:
                if prereq not in orderedCourses:
                    prereqsMet = False

            if prereqsMet == True and course not in orderedCourses:
                orderedCourses.append(course)
                solutionExists = True
        if len(orderedCourses) == len(course_to_prereqs):
            sorted = True
        if not solutionExists:
            orderedCourses = []
            break
    return orderedCourses
            
