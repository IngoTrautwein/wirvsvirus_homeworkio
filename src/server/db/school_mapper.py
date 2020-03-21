from server.bo.school import School
from server.db.mapper import Mapper


class SchoolMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT id, name from school")
        tuples = cursor.fetchall()

        for (id, name) in tuples:
            school = School()
            school.set_id(id)
            school.set_name(name)
            result.append(school)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, name FROM school WHERE name LIKE '{}' ORDER BY name".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, name) in tuples:
            school = School()
            school.set_id(id)
            school.set_name(name)
            result.append(school)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name FROM school WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, name) = tuples[0]
            school = School()
            school.set_id(id)
            school.set_name(name)
            result = school
        except IndexError:
            """tritt auf, wenn kein Tupel zurückgeliefert wurde"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, school):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM school ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            school.set_id(maxid[0]+1)

        command = "INSERT INTO school (id, name) VALUES (%s,%s)"
        data = (school.get_id(), school.get_())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return school

    def update(self, school):
        cursor = self._cnx.cursor()

        command = "UPDATE school " + "SET name=%s WHERE id=%s"
        data = (school.get_name(), school.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, school):
        cursor = self._cnx.cursor()

        command = "DELETE FROM school WHERE id={}".format(school.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()

    def find_by_student_id(self, id):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name FROM school WHERE student_id={}".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, name) = tuples[0]
            school = School()
            school.set_id(id)
            school.set_name(name)
            result = school
        except IndexError:
            """tritt auf, wenn kein Tupel zurückgeliefert wurde"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result


if __name__ == "__main__":
    with SchoolMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)