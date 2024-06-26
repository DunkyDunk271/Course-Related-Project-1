class Professor:
    def __init__(self, prof_id, prof_name):
        self.Id = prof_id
        self.Name = prof_name
        self.CourseClasses = []

    def GetId(self):
        return self.Id
    
    def GetName(self):
        return self.Name
    
    def __hash__(self):
        return hash(self.Id)

    # Bind professor to course
    def add_prof_course(self, course_class):
        self.CourseClasses.append(course_class)

    def addCourseClass(self, course):
        self.CourseClasses.append(course)
    
    # Compares ID
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return hash(self) == hash(other)
    
    def __ne__(self, other):
        return not (self == other)
    