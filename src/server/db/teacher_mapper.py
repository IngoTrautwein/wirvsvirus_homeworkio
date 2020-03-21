from server.bo.teacher import Teacher
from server.db.mapper import Mapper


class TeacherMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from teacher")
        tuples = cursor.fetchall()

        for (id, first_name, surname) in tuples:
            teacher = Teacher()
            teacher.set_id(id)
            teacher.set_first_name(first_name)
            teacher.set_surname(surname)
            result.append(teacher)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_surname(self, name):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, first_name, surname FROM teachers WHERE surname LIKE '{}' ORDER BY surname".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, first_name, surname) in tuples:
            teacher = Teacher()
            teacher.set_id(id)
            teacher.set_first_name(first_name)
            teacher.set_surname(surname)
            result.append(teacher)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, first_name, surname FROM teachers WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, first_name, surname) = tuples[0]
            teacher = Teacher()
            teacher.set_id(id)
            teacher.set_first_name(first_name)
            teacher.set_surname(surname)
            result = teacher
        except IndexError:
            """tritt auf, wenn kein Tupel zurückgeliefert wurde"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, teacher):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM teachers ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            teacher.set_id(maxid[0]+1)

        command = "INSERT INTO teachers (id, first_name, surname) VALUES (%s,%s,%s)"
        data = (teacher.get_id(), teacher.get_first_name(), teacher.get_surname())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return teacher

    def update(self, teacher):
        cursor = self._cnx.cursor()

        command = "UPDATE teachers " + "SET first_name=%s, surname=%s WHERE id=%s"
        data = (teacher.get_first_name(), teacher.get_surname(), teacher.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, teacher):
        cursor = self._cnx.cursor()

        command = "DELETE FROM teachers WHERE id={}".format(teacher.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


if __name__ == "__main__":
    with TeacherMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)