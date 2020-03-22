from server.bo.school_class import SchoolClass
from server.db.mapper import Mapper


class SchoolClassMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT id, name from school_class")
        tuples = cursor.fetchall()

        for (id, name) in tuples:
            school_class = self.__create_school_class(id, name)
            result.append(school_class)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, name FROM school_class WHERE name LIKE '{}' ORDER BY name".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, name) in tuples:
            school_class = self.__create_school_class(id, name)
            result.append(school_class)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name FROM school_class WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, name) = tuples[0]
            school_class = self.__create_school_class(id, name)
            result = school_class
        except IndexError:
            """tritt auf, wenn kein Tupel zurückgeliefert wurde"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def find_ids_of_subject_school_class(self, key):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT subject_school_class FROM subject_school_class WHERE school_class_id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id) in tuples:
            result.append(id)

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, school_class):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM school_class ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            school_class.set_id(maxid[0]+1)

        command = "INSERT INTO school_class (id, name) VALUES (%s,%s)"
        data = (school_class.get_id(), school_class.get_name())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return school_class

    def update(self, school_class):
        cursor = self._cnx.cursor()

        command = "UPDATE school_class " + "SET name=%s WHERE id=%s"
        data = (school_class.get_name(), school_class.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, school_class):
        cursor = self._cnx.cursor()

        command = "DELETE FROM school_class WHERE id={}".format(school_class.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def find_by_student_id(self, id):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name FROM school_class WHERE student_id={}".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, name) = tuples[0]
            school_class = self.__create_school_class(id, name)
            result = school_class
        except IndexError:
            """tritt auf, wenn kein Tupel zurückgeliefert wurde"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def __create_school_class(self, id, name):
        school_class = SchoolClass()
        school_class.set_id(id)
        school_class.set_name(name)
        return school_class

if __name__ == "__main__":
    with SchoolClassMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)