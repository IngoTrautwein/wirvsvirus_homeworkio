from server.bo.class import Class
from server.db.mapper import Mapper


class ClassMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from class")
        tuples = cursor.fetchall()

        for (id, first_name, surname) in tuples:
            class = Class()
            class.set_id(id)
            class.set_first_name(first_name)
            class.set_surname(surname)
            result.append(class)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_surname(self, name):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, first_name, surname FROM classs WHERE surname LIKE '{}' ORDER BY surname".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, first_name, surname) in tuples:
            class = Class()
            class.set_id(id)
            class.set_first_name(first_name)
            class.set_surname(surname)
            result.append(class)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, first_name, surname FROM classs WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, first_name, surname) = tuples[0]
            class = Class()
            class.set_id(id)
            class.set_first_name(first_name)
            class.set_surname(surname)
            result = class
        except IndexError:
            """tritt auf, wenn kein Tupel zurückgeliefert wurde"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, class):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM classs ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            class.set_id(maxid[0]+1)

        command = "INSERT INTO classs (id, first_name, surname) VALUES (%s,%s,%s)"
        data = (class.get_id(), class.get_first_name(), class.get_surname())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return class

    def update(self, class):
        cursor = self._cnx.cursor()

        command = "UPDATE classs " + "SET first_name=%s, surname=%s WHERE id=%s"
        data = (class.get_first_name(), class.get_surname(), class.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, class):
        cursor = self._cnx.cursor()

        command = "DELETE FROM classs WHERE id={}".format(class.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


if __name__ == "__main__":
    with ClassMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)