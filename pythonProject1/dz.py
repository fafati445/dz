from itertools import count


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {midle_grade(self)}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {midle_grade(self)}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_homework(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

def midle_grade(self):
    count = 0
    for i in self.grades.values():
        for e in i:
            count+=1
    max = 0
    for i in self.grades.values():
        for e in i:
            max+=e
    return max/count

def midle_grade_po_kursu_studentov(list_members,course):
    grades_list =[]
    for i in list_members:
        if course in i.courses_in_progress:
            grades_list += i.grades[course]
    return f'среднее значение по курсу у студентов: {sum(grades_list)/len(grades_list)}'

def midle_grade_po_kursu_lectorov(list_members,course):
    grades_list =[]
    for i in list_members:
        if course in i.courses_attached:
            grades_list += i.grades[course]
    return f'среднее значение по курсу у лекторов: {sum(grades_list)/len(grades_list)}'

def __eq__(self,other):
    if midle_grade(self) == midle_grade(other):
        return f'они равны'
    elif midle_grade(self) > midle_grade(other):
        return f'1-й объект больше второго'
    else:
        return f'2-ой объект больше первого'




student1 = Student('vasya','bobov','m')
student1.courses_in_progress += ['python','go']
student2 = Student('misha','bobol','m')
student2.courses_in_progress += ['python','go']

lecture1 = Lecturer('Katya','popova')
lecture1.courses_attached += ['python','go']
lecture2 = Lecturer('masha','popola')
lecture2.courses_attached += ['python','go']

student1.rate_lecturer(lecture1,'python',10)
student1.rate_lecturer(lecture1,'go',9)
student2.rate_lecturer(lecture2,'python',5)
student2.rate_lecturer(lecture2,'go',7)

student1.finished_courses += ['введение в программирование']
reviewer = Reviewer('pasha','imbicilov')
reviewer.courses_attached += ['python','go']

reviewer.rate_homework(student1,'python',8)
reviewer.rate_homework(student1,'go',7)
reviewer.rate_homework(student2,'python',9)
reviewer.rate_homework(student2,'go',6)

print(midle_grade(student1))
print(midle_grade(student2))
print(midle_grade(lecture2))
print(midle_grade(lecture1))
print()
print(reviewer)
print()
print(lecture1)
print()
print(student1)
print()
print(__eq__(lecture2,lecture1))
print(__eq__(lecture1,lecture1))
print(__eq__(student1,lecture2))
print(__eq__(student1,student2))
print()
students = [student1, student2]
lecturer = [lecture1,lecture2]
print(midle_grade_po_kursu_studentov(students,'go'))
print(midle_grade_po_kursu_lectorov(lecturer,'python'))