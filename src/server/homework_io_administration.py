from .bo.homework import Homework
from .bo.school import School
from .bo.school_class import SchoolClass
from .bo.student import Student
from .bo.subject import Subject
from .bo.teacher import Teacher
from .db.homework_mapper import HomeworkMapper

from .db.student_mapper import StudentMapper
from .db.subject_mapper import SubjectMapper
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

    def get_student_by_class(self, class_id):
        with StudentMapper() as mapper:
            return mapper.find_by_class(class_id)

    def get_student_by_school(self, school_id):
        with StudentMapper() as mapper:
            return mapper.find_by_school(school_id)

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

    def get_teachers_by_school(self, school):
        result = []
        with TeacherMapper() as mapper:
            ids = mapper.find_teachers_by_school(school)
            for id in ids:
                teacher = mapper.find_by_key(id)
                result.append(teacher)
            return result

    def get_teachers_by_school_class(self, school_class):
        result = []
        with TeacherMapper() as mapper:
            ids = mapper.find_teachers_by_school_class(school_class)
            for id in ids:
                teacher = mapper.find_by_key(id)
                result.append(teacher)
            return result

    def get_teachers_by_subject(self, subject):
        result = []
        with TeacherMapper() as mapper:
            ids = mapper.find_teachers_by_subject(subject)
            for id in ids:
                teacher = mapper.find_by_key(id)
                result.append(teacher)
            return result

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
    def create_school(self, name, address):
        school = School()
        school.set_name(name)
        school.set_id(1)
        school.set_address(address)

        with SchoolMapper() as mapper:
            return mapper.insert(school)

    def get_all_schools(self):
        with SchoolMapper() as mapper:
            return mapper.find_all()

    def get_school_by_id(self, id):
        with SchoolMapper() as mapper:
            return mapper.find_by_key(id)

    def delete_school(self, school):
        with SchoolMapper() as mapper:
            teachers = self.get_all_teachers()
            if not (teachers is None):
                for t in teachers:
                    self.delete_teacher(t)

            students = self.get_all_students()
            if not (students is None):
                for s in students:
                    self.delete_student(s)

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

    """
    Homework-spezifische Methoden
    """
    def create_homework(self,  description, file_path, start_event, end_event, school_class_id, subject_id):
        homework = Homework()
        homework.set_description(description)
        homework.set_file_path(file_path)
        homework.set_start_event(start_event)
        homework.set_end_event(end_event)
        homework.set_id(1)

        with HomeworkMapper() as mapper:
            sub_school_id = mapper.insert_subject_school_class(school_class_id, subject_id)
            homework.set_sub_school_id(sub_school_id)
            homework = mapper.insert(homework)

        return homework

    def get_all_homeworks(self):
        with HomeworkMapper() as mapper:
            return mapper.find_all()

    def get_homework_by_id(self, id):
        with HomeworkMapper() as mapper:
            return mapper.find_by_key(id)

    def get_school_of_student(self, student):
        with HomeworkMapper() as mapper:
            # keine Prüfung vorhanden
            return mapper.find_by_student_id(student.get_id())

    def delete_homework(self, homework):
        with HomeworkMapper() as mapper:
            # Prüfung fehlt
            mapper.delete(homework)

    def save_homework(self, homework):
        with HomeworkMapper() as mapper:
            mapper.update(homework)

    """
    Subject-spezifische Methoden
    """
    def create_subject(self, name):
        subject = Subject()
        subject.set_name(name)
        subject.set_id(1)

        with SubjectMapper() as mapper:
            return mapper.insert(subject)

    def get_all_subjects(self):
        with SubjectMapper() as mapper:
            return mapper.find_all()

    def get_subject_by_name(self, name):
        with SubjectMapper() as mapper:
            return mapper.find_by_name(name)

    def get_subject_by_id(self, id):
        with SubjectMapper() as mapper:
            return mapper.find_by_key(id)

    def delete_subject(self, subject):
        with SubjectMapper() as mapper:
            mapper.delete(subject)

    def save_subject(self, subject):
        with SubjectMapper() as mapper:
            mapper.update(subject)