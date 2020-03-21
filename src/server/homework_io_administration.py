from .bo.school import School
from .bo.school_class import SchoolClass
from .bo.student import Student
from .bo.teacher import Teacher

from .db.student_mapper import StudentMapper
from .db.teacher_mapper import TeacherMapper
from .db.school_class_mapper import SchoolClassMapper
from .db.school_mapper import SchoolMapper


class HomeworkIOAdministration:

    def __init__(self):
        pass

    """
    Student-spezifische Methoden
    """
    def create_student(self, first_name, surname):
        student = Student()
        student.set_first_name(first_name)
        student.set_surname(surname)
        student.set_id(1)

        with StudentMapper() as mapper:
            return mapper.insert(student)

    def get_student_by_surname(self, surname):
        with StudentMapper() as mapper:
            return mapper.find_by_surname(surname)

    def get_student_by_id(self, id):
        with StudentMapper() as mapper:
            return mapper.find_by_key(id)

    def get_all_students(self):
        with StudentMapper() as mapper:
            return mapper.find_all()

    def save_student(self, student):
        with StudentMapper() as mapper:
            mapper.update(student)

    def delete_student(self, student):
        with StudentMapper() as mapper:
            mapper.delete(student)

    """
    Teacher-spezifische Methoden
    """
    def create_teacher(self, first_name, surname):
        teacher = Teacher()
        teacher.set_first_name(first_name)
        teacher.set_surname(surname)
        teacher.set_id(1)

        with TeacherMapper() as mapper:
            return mapper.insert(teacher)

    def get_teacher_by_surname(self, surname):
        with TeacherMapper() as mapper:
            return mapper.find_by_surname(surname)

    def get_teacher_by_id(self, id):
        with TeacherMapper() as mapper:
            return mapper.find_by_key(id)

    def get_all_teachers(self):
        with TeacherMapper() as mapper:
            return mapper.find_all()

    def save_teacher(self, teacher):
        with TeacherMapper() as mapper:
            mapper.update(teacher)

    def delete_teacher(self, teacher):
        with TeacherMapper() as mapper:
            mapper.delete(teacher)

    """
    School-spezifische Methoden
    """
    def create_school(self, name):
        school = School()
        school.set_name(name)
        school.set_id(1)

        with SchoolMapper() as mapper:
            return mapper.insert(school)

    def get_all_schools(self):
        with SchoolMapper() as mapper:
            return mapper.find_all()

    def get_school_by_id(self, id):
        with SchoolMapper() as mapper:
            return mapper.find_by_key(id)

    def get_school_of_student(self, student):
        with SchoolMapper() as mapper:
            # keine Prüfung vorhanden
            return mapper.find_by_student_id(student.get_id())

    def delete_school(self, school):
        with SchoolMapper() as mapper:
            # Keine Prüfung ob Schüler, Lehrer etc. gelöscht wurden
            mapper.delete(school)

    def save_school(self, school):
        with SchoolMapper() as mapper:
            mapper.update(school)

    """
    School_Class-spezifische Methoden
    """
    def create_school_class(self, name):
        school_class = SchoolClass()
        school_class.set_name(name)
        school_class.set_id(1)

        with SchoolClassMapper() as mapper:
            return mapper.insert(school_class)

    def get_all_school_classes(self):
        with SchoolClassMapper() as mapper:
            return mapper.find_all()

    def get_school_class_by_id(self, id):
        with SchoolClassMapper() as mapper:
            return mapper.find_by_key(id)

    def get_school_class_of_student(self, student):
        with SchoolClassMapper() as mapper:
            # keine Prüfung vorhanden
            return mapper.find_by_student_id(student.get_id())

    def delete_school_class(self, school_class):
        with SchoolClassMapper() as mapper:
            # Keine Prüfung ob Schüler, Lehrer etc. gelöscht wurden
            mapper.delete(school_class)

    def save_school_class(self, school_class):
        with SchoolClassMapper() as mapper:
            mapper.update(school_class)