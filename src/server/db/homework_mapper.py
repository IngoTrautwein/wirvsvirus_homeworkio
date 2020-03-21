from server.bo.homework import Homework
from server.db.mapper import Mapper


class HomeworkMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from homework")
        tuples = cursor.fetchall()

        for (id, first_name, surname) in tuples:
            homework = Homework()
            homework.set_id(id)
            homework.set_first_name(first_name)
            homework.set_surname(surname)
            result.append(homework)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_surname(self, name):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, first_name, surname FROM homework WHERE surname LIKE '{}' ORDER BY surname".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, first_name, surname) in tuples:
            homework = Homework()
            homework.set_id(id)
            homework.set_first_name(first_name)
            homework.set_surname(surname)
            result.append(homework)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, first_name, surname FROM homework WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, first_name, surname) = tuples[0]
            homework = Homework()
            homework.set_id(id)
            homework.set_first_name(first_name)
            homework.set_surname(surname)
            result = homework
        except IndexError:
            """tritt auf, wenn kein Tupel zurückgeliefert wurde"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, homework):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM homework ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            homework.set_id(maxid[0]+1)

        command = "INSERT INTO homework (id, first_name, surname) VALUES (%s,%s,%s)"
        data = (homework.get_id(), homework.get_first_name(), homework.get_surname())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return homework

    def update(self, homework):
        cursor = self._cnx.cursor()

        command = "UPDATE homework " + "SET first_name=%s, surname=%s WHERE id=%s"
        data = (homework.get_first_name(), homework.get_surname(), homework.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, homework):
        cursor = self._cnx.cursor()

        command = "DELETE FROM homework WHERE id={}".format(homework.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


if __name__ == "__main__":
    with HomeworkMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)