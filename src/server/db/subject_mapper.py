from server.bo.subject import Subject
from server.db.mapper import Mapper


class SubjectMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from subject")
        tuples = cursor.fetchall()

        for (id, first_name, surname) in tuples:
            subject = Subject()
            subject.set_id(id)
            subject.set_first_name(first_name)
            subject.set_surname(surname)
            result.append(subject)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_surname(self, name):
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT id, first_name, surname FROM subject WHERE surname LIKE '{}' ORDER BY surname".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, first_name, surname) in tuples:
            subject = Subject()
            subject.set_id(id)
            subject.set_first_name(first_name)
            subject.set_surname(surname)
            result.append(subject)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_key(self, key):
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, first_name, surname FROM subject WHERE id={}".format(key)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, first_name, surname) = tuples[0]
            subject = Subject()
            subject.set_id(id)
            subject.set_first_name(first_name)
            subject.set_surname(surname)
            result = subject
        except IndexError:
            """tritt auf, wenn kein Tupel zurückgeliefert wurde"""
            result = None

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, subject):
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM subject ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            subject.set_id(maxid[0]+1)

        command = "INSERT INTO subject (id, first_name, surname) VALUES (%s,%s,%s)"
        data = (subject.get_id(), subject.get_first_name(), subject.get_surname())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return subject

    def update(self, subject):
        cursor = self._cnx.cursor()

        command = "UPDATE subject " + "SET first_name=%s, surname=%s WHERE id=%s"
        data = (subject.get_first_name(), subject.get_surname(), subject.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, subject):
        cursor = self._cnx.cursor()

        command = "DELETE FROM subject WHERE id={}".format(subject.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()


if __name__ == "__main__":
    with SubjectMapper() as mapper:
        result = mapper.find_all()
        for p in result:
            print(p)