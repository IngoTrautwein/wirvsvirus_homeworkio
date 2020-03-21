from server.bo.student import Student
from server.db.mapper import Mapper


class StudentMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from student")
        tuples = cursor.fetchall()

        for (id, first_name, surname) in tuples:
            student = Student()
            student.set_id(id)
            student.set_first_name(first_name)
            student.set_surname(surname)
            result.append(student)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_surname(self, name):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, first_name, surname FROM Students WHERE surname LIKE '{}' ORDER BY surname".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, first_name, surname) in tuples:
            student = Student()
            student.set_id(id)
            student.set_first_name(first_name)
            student.set_surname(surname)
            result.append(student)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, first_name, surname FROM Students WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, first_name, surname) = tuples[0]
            student = Student()
            student.set_id(id)
            student.set_first_name(first_name)
            student.set_surname(surname)
            result = student
        except IndexError:
            """tritt auf, wenn kein Tupel zurückgeliefert wurde"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, student):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM Students ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            student.set_id(maxid[0]+1)

        command = "INSERT INTO Students (id, first_name, surname) VALUES (%s,%s,%s)"
        data = (student.get_id(), student.get_first_name(), student.get_surname())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return student

    def update(self, student):
        cursor = self._cnx.cursor()

        command = "UPDATE Students " + "SET first_name=%s, surname=%s WHERE id=%s"
        data = (student.get_first_name(), student.get_surname(), student.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, student):
        cursor = self._cnx.cursor()

        command = "DELETE FROM Students WHERE id={}".format(student.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


if __name__ == "__main__":
    with StudentMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)