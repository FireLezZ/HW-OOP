class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = [] 
        self.grades = {}
    
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def average_grade(self):
        total_grades = 0
        total_count = 0
        for grades_list in self.grades.values():
            total_grades += sum(grades_list)
            total_count += len(grades_list)
        if total_count > 0:
            return round(total_grades / total_count, 1)
        else:
            return 0
    def __str__(self):
        return (f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}")
        
    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}   
    
    def average_grade(self):
        total_grades = 0
        total_count = 0
        for grades_list in self.grades.values():
            total_grades += sum(grades_list)
            total_count += len(grades_list)
        if total_count > 0:
            return round(total_grades / total_count, 1)
        else:
            return 0
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}"
    
    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
     
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"   
  
first_student = Student('Ruoy', 'Eman', 'your_gender')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Git']
first_student.finished_courses += ['Введение в програмирование']
 
first_mentor = Mentor('Some', 'Buddy')                 
first_mentor.courses_attached += ['Python']

first_reviewer = Reviewer("Ivan", "Ivanov")   
first_reviewer.courses_attached += ['Python'] 
 
first_lecturer = Lecturer('Semen', 'Semenov') 
first_lecturer.courses_attached += ['Python'] 

first_reviewer.rate_hw(first_student, 'Python', 10) 
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 10) 
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'Python', 9)
 
 


first_student.rate_lecturer(first_lecturer, 'Python', 10)
first_student.rate_lecturer(first_lecturer, 'Python', 10)
first_student.rate_lecturer(first_lecturer, 'Python', 10)
first_student.rate_lecturer(first_lecturer, 'Python', 10)
first_student.rate_lecturer(first_lecturer, 'Python', 10)
first_student.rate_lecturer(first_lecturer, 'Python', 10)
first_student.rate_lecturer(first_lecturer, 'Python', 9)



print(first_reviewer)

print(first_lecturer)
print(first_student)

print(first_lecturer == first_student)